from abc import ABC, abstractmethod
from pandas import DataFrame
from typing import Union

# Class README: _AbstrOuputControler
# 추상 클래스, 수집/가공된 로그데이터에 대한 출력 방식을 구현하기 위한 추상 클래스
# 설정 파일의 값에 따라 기능을 새로운 클래스를 만들어가며 확장할 수 있도록 추상 클래스 구현
# 해당 클래스를 상속하여 사용함으로써 확장에 용이

class _AbstrOuputControler(ABC):
    def __init__(self, logDF:DataFrame):
        self.logDF = logDF

    @abstractmethod
    def process_method(self) -> Union[DataFrame,list]: 
        pass