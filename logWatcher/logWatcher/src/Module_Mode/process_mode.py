from pandas import DataFrame
from src.Abstr._AbstrModeControler import _AbstrModeControler
import utils.ReaderLogWatcherConf as conf
from AAAlog import AAA
import json, datetime
import pandas as pd


class Mode_print(_AbstrModeControler):
    def __init__(self, logDF: DataFrame):
        super().__init__(logDF)
        
    def process_method(self) -> None:
        instance_AAA = AAA(self.logDF[~self.logDF['value'].str.strip().str.startswith('modsingle')])
        
        result = dict()
        result["pre_AUTH"] = instance_AAA.UserInfo()
        result["AUTH"] = instance_AAA.AuthInfo()
        result["post_AUTH"] = instance_AAA.PostInfo()
        print(json.dumps(result, indent=4))
        input()

class Mode_toJson(_AbstrModeControler):
    def __init__(self, logDF: DataFrame):
        super().__init__(logDF)
        
    def process_method(self) -> pd.DataFrame:
        instance_AAA = AAA(self.logDF[~self.logDF['value'].str.strip().str.startswith('modsingle')])
        
        section = self.logDF.iloc[0]['section']
        date = datetime.date.today().strftime("%d%m%y")
        
        result = dict()
        result["pre_AUTH"] = instance_AAA.UserInfo()
        result["AUTH"] = instance_AAA.AuthInfo()
        result["post_AUTH"] = instance_AAA.PostInfo()
        
        json_data = json.dumps(result, indent=4)
        json_path = f"{conf.folder_path}/json/{date}_{section}.json"
        with open(json_path, "w") as file:
            file.write(json_data)
        







