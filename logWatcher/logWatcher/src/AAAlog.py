import pandas as pd

# Class README: AAA
# Radius 인증의 3단계 과정[pre_auth, auth, post_auth]의 로그들을 구별하여 관리하기 위한 클래스
# 이 클래스는 각 단계의 로그들을 그룹화하여 관리할 수 있으며 기능 추가가 필요할 경우 추가적인 메소드 작성으로
# 간편하게 원하는 기능을 구현할 수 있다.

class AAA:
    def __init__(self, ReturnedDataModuleResult:pd.DataFrame):
        self.pre_authorize:list = list()
        self.auth:list = list()
        self.post_authorize:list = list()
        
        for element in ReturnedDataModuleResult['value']:
            if element.strip() and element.strip()[0] == '#':
                print(element)

        
        #print(ReturnedDataModuleResult['value'])