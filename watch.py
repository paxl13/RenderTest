#!/usr/bin/env python3
"""
File watcher for development - automatically restarts Flask app when files change.
"""
import os
import sys
import subprocess
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class RestartHandler(FileSystemEventHandler):
    def __init__(self):
        self.process = None
        self.start_app()
    
    def start_app(self):
        """Start or restart the Flask application."""
        if self.process:
            print("Stopping Flask app...")
            self.process.terminate()
            self.process.wait()
        
        print("Starting Flask app...")
        self.process = subprocess.Popen([
            sys.executable, "main.py"
        ], env=dict(os.environ, FLASK_DEBUG="1"))
    
    def on_modified(self, event):
        """Handle file modification events."""
        if event.is_directory:
            return
        
        # Only restart on Python file changes or template changes
        if event.src_path.endswith(('.py', '.html', '.css', '.js')):
            print(f"File changed: {event.src_path}")
            print("Restarting Flask app...")
            self.start_app()

def main():
    """Run the file watcher."""
    print("Starting file watcher for Flask development...")
    print("Watching: *.py, *.html, *.css, *.js files")
    print("Press Ctrl+C to stop")
    
    event_handler = RestartHandler()
    observer = Observer()
    
    # Watch current directory and templates directory
    observer.schedule(event_handler, ".", recursive=True)
    observer.start()
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nStopping file watcher...")
        if event_handler.process:
            event_handler.process.terminate()
        observer.stop()
    
    observer.join()

if __name__ == "__main__":
    main()