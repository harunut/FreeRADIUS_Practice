import sys
sys.path.append("/etc/raddb/logWatcher/logWatcher")

from LogClass import LogWatcher

if __name__ == "__main__":
    log_watcher = LogWatcher()
    log_watcher.watch_start()