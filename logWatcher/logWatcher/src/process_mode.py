from pandas import DataFrame
from Abstr_DataFrameControler import Abstr_DataFrameControler
from utils.ReaderLogWatcherConf import *
from AAAlog import AAA
import json
import pandas as pd

class CheckRunModule(Abstr_DataFrameControler):
    
    def process_method(self) -> pd.DataFrame:
        instance_AAA = AAA(self.logDF[~self.logDF['value'].str.strip().str.startswith('modsingle')])
        
        result = dict()
        
        
        result["pre_AUTH"] = instance_AAA.UserInfo()
        result["AUTH"] = instance_AAA.AuthInfo()
        result["post_AUTH"] = instance_AAA.PostInfo()
        
        
        
        print(json.dumps(result, indent=4))
        
        
        # print(json.dumps(instance_AAA.UserInfo(), indent=4))
        # print(json.dumps(instance_AAA.AuthInfo(), indent=4))
        # print(json.dumps(instance_AAA.PostInfo(), indent=4))
        
        print("*" * 60)
        
