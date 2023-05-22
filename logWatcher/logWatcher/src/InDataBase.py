import pandas as pd
import re

TYPE_LIST = ['Debug:', 'Auth:', 'Error:']

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
        
        grouped_data = pd.DataFrame(self.log_list, columns=["date", "type", "value", "section"]).groupby("section")
        grouped_list = [grouped_data.get_group(group_name) for group_name in grouped_data.groups]
        
        return grouped_list

def extract_number(string):
    pattern = r'^\(\d+\)'  

    match = re.match(pattern, string)
    if match:
        number = int(match.group(0)[1:-1]) 
        return number
    else:
        return False