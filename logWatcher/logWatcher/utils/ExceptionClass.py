import sys
class ExceptionTryControl(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
    
    def handle_exception(self):
        if self.message == "Error : configure 0":
            # 특정한 에러 메시지에 대한 처리
            print("\033[91mError:\033[0m Invalid mode configuration. Please check the 'mode' value in the logWatcher.conf file.")
            sys.exit()
            
        # elif self.message == "Another Error Message":
        #     # 다른 에러 메시지에 대한 처리
        #     print("Handling another error message")
            
        else:
            # 그 외의 에러 메시지에 대한 처리
            print("Handling generic error message")