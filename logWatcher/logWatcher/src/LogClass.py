from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from utils.ReaderLogWatcherConf import *
from InDataBase import InDataBase
from process_mode import CheckRunModule
from AAAlog import AAA
import json
import time
import pandas as pd

class LogHandler(FileSystemEventHandler):
    def __init__(self):
        self.last_position = 0
        self.count = 0
        
    def on_modified(self, event):
        if not event.is_directory:
            with open(event.src_path) as f:
                # 파일의 끝으로 이동
                f.seek(0, 2)
                file_size = f.tell()

                # 이전 위치부터 파일의 끝까지 읽기
                f.seek(self.last_position)
                new_content = f.read(file_size - self.last_position)
                content_list = new_content.split("\n")

     
                # 'Received Access-Request'를 포함한 첫번째 항목 찾기
                while content_list:
                    if 'Received Access-Request' in content_list[0]:
                        break
                    else:
                        content_list.pop(0)

                # 리스트를 전부 탐색했는데도 'Received Access-Request'를 찾지 못한 경우 함수 종료
                if not content_list:
                    return

                logDB = InDataBase(content_list).process_logs()
                for element in logDB:
                    if type(element) != pd.DataFrame or element.empty: 
                        return -1
                    elif processMode == "stdout":
                        CheckRunModule(element).process_method()
      
                # 현재 위치 저장
                self.last_position = file_size

class LogWatcher:
    def __init__(self):
        self.observer = Observer()
        self.logHandler = LogHandler()

    def watch_start(self):
        self.observer.schedule(self.logHandler, path=log_file, recursive=True)
        self.observer.start()

        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            # 프로그램 종료 시 Observer 중지
            self.observer.stop()

        # Observer 종료 대기
        self.observer.join()