import sys
import os
import signal
import json
import time
from scanner import scan_directory
from monitor import start_monitor_background, stop_monitor

PID_FILE = ".beaconshield.pid"

def main():
    if len(sys.argv) < 2:
        print("Usage:\n\tbeaconshield scan <directory>\n\tbeaconshield monitor start <directory>\n\tbeaconshield monitor stop")
        sys.exit(1)

    command = sys.argv[1]
    
    if command == "scan":
        target_dir = sys.argv[2] if len(sys.argv) > 2 else "."
        summary = scan_directory(target_dir)
        print("\n✅ Scan Complete:")
        print(json.dumps(summary, indent=2))

    elif command == "monitor":
        subcommand = sys.argv[2] if len(sys.argv) > 2 else ""
        
        if subcommand == "start":
            target_dir = sys.argv[3] if len(sys.argv) > 3 else "."
            
            if os.path.exists(PID_FILE):
                print("[!] Already running. Stop first.")
                sys.exit(1)
                
            pid = start_monitor_background(target_dir)
            with open(PID_FILE, 'w') as f:
                f.write(str(pid))
            print(f"🔍 Monitoring started (PID: {pid}).")

        elif subcommand == "stop":
            stop_monitor(PID_FILE)
        else:
            print("Unknown monitor subcommand:", subcommand)
            sys.exit(1)
    else:
        print("Unknown command:", command)
        sys.exit(1)


if __name__ == "__main__":
    main()