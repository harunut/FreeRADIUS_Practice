import pandas as pd
import re

TYPE_LIST = ['Debug:', 'Auth:']

class InDataBase:
    def __init__(self, log_data):
        self.log_data = log_data
        self.log_list = []
    
    def process_logs(self):
        for log in self.log_data:
            for log_type in TYPE_LIST:
                if log_type in log:
                    index = log.index(log_type)
                    date = log[:index]
                    type_value = log[index:]
                    section = extract_number(type_value[type_value.find(":") + 2:])
                    
                    if section is not False:
                        self.log_list.append(
                            [date[:-3], 
                             type_value[:type_value.find(":")], 
                             type_value[type_value.find(":") + 4 + len(str(section)):], 
                             section
                             ])
                        break
                    else:
                        break
        
        if len(self.log_list) > 1 and type(pd.DataFrame(self.log_list)) is not None:
            return pd.DataFrame(self.log_list, columns=["date", "type", "value", "section"])

def extract_number(string):
    pattern = r'^\(\d+\)'  # (숫자) 패턴을 나타내는 정규표현식

    match = re.match(pattern, string)
    if match:
        number = int(match.group(0)[1:-1])  # 괄호를 제외한 숫자만 추출
        return number
    else:
        return False