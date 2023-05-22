import pandas as pd
import re
from utils.ReaderLogWatcherConf import *

# Class README: AAA
# Radius 인증의 3단계 과정[pre_auth, auth, post_auth]의 로그들을 구별하여 관리하기 위한 클래스
# 이 클래스는 각 단계의 로그들을 그룹화하여 관리할 수 있으며 기능 추가가 필요할 경우 추가적인 메소드 작성으로
# 간편하게 원하는 기능을 구현할 수 있다.
class AAA:
    def __init__(self, ReturnedDataModuleResult:pd.DataFrame):
        preIndexStart, preIndexEnd = find_range(ReturnedDataModuleResult['value'], 'Received', '# Executing section authorize')
        authIndexStart, authIndexEnd = find_range(ReturnedDataModuleResult['value'], '# Executing section authorize', '# Executing group from')
        postIndexStart, postIndexEnd = find_range(ReturnedDataModuleResult['value'], '# Executing group from')
        
        self.pre_authorize:pd.DataFrame = ReturnedDataModuleResult.iloc[preIndexStart:preIndexEnd, :].copy()
        self.auth:pd.DataFrame = ReturnedDataModuleResult.iloc[authIndexStart:authIndexEnd, :].copy()
        self.post_authorize:pd.DataFrame = ReturnedDataModuleResult.iloc[postIndexStart:postIndexEnd, :].copy()
          
    def UserInfo(self):
        authDict = dict()
        for element in self.pre_authorize.iloc[2:,:-1]['value']:
            if "=" in element:
                key, value = element.split('=')
                key = key.strip()
                value = value.strip()
                authDict[key] = value
                
        userInfo:dict = {
            'userName': self.pre_authorize.iloc[1,:]['value'][self.pre_authorize.iloc[1,:]['value'].find("=") + 3:-1],
            'AuthInfo': authDict
        }
        
        return userInfo
    
    def AuthInfo(self):
        authInfo = dict()
        for element in self.auth.iloc[2:,:-1]['value']:
            if re.match(r"^\[[^\]]+\]", element.strip()):
                if "=" in element:
                    key, value = element.split('=')
                    key = key.strip()
                    value = value.strip()
                    if value != "noop":
                        authInfo[key] = value
        
        return authInfo
    
    def PostInfo(self):
        
        postInfo = dict()
        for element in self.post_authorize['value']:
            if re.match(r"^\[[^\]]+\]", element.strip()):
                if "=" in element:
                    key, value = element.split('=')
                    key = key.strip()
                    value = value.strip()
                    if value != "noop":
                        postInfo[key] = value
                    
                    
        for index, row in self.post_authorize.iterrows():
            if 'Auth' in row['type']:
                postInfo['Auth'] = row['value'].strip()
                break
        
        return postInfo

def find_range(lst, start_str, end_str="DEFAULT_VALUE"):
    start_index = None
    end_index = None

    for i, item in enumerate(lst):
        if item.find(start_str) != -1: 
            start_index = i
        elif item.find(end_str) != -1: 
            end_index = i
            break
    if end_str == "DEFAULT_VALUE":
        return start_index, -1
    
    elif start_index is not None and end_index is not None:
        return start_index, end_index
    
    else:
        return None