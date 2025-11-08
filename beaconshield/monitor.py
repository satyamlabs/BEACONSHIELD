import multiprocessing
import os
import signal
import time
from scanner import scan_file_for_keywords
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class BeaconShieldHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if not event.is_directory:
            print(f"[MONITOR] File changed: {event.src_path}")
            scan_file_for_keywords(event.src_path)

def monitor_worker(path_to_watch, event_flag):
    event_handler = BeaconShieldHandler()
    observer = Observer()
    observer.schedule(event_handler, path_to_watch, recursive=True)
    observer.start()

    try:
        while not event_flag.value:
            time.sleep(1)
    except KeyboardInterrupt:
        pass
    finally:
        observer.stop()
        observer.join()

def start_monitor_background(path_to_watch):
    event_flag = multiprocessing.Value('b', False)  # Shared boolean flag
    process = multiprocessing.Process(target=monitor_worker, args=(path_to_watch, event_flag))
    process.start()
    return process.pid

def stop_monitor(pid_file):
    if not os.path.exists(pid_file):
        print("[!] Not running or already stopped.")
        return
    
    try:
        with open(pid_file, 'r') as f:
            pid = int(f.read())
        os.kill(pid, signal.SIGTERM)
        os.remove(pid_file)
        print("🛑 Monitoring stopped.")
    except ValueError:
        print("[!] Invalid PID file")
    except ProcessLookupError:
        print("[!] Process not found – removing stale PID file")
        os.remove(pid_file)
    except Exception as e:
        print(f"[ERROR] Failed to stop monitor: {e}")