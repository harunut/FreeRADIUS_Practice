from abc import ABC, abstractmethod
from pandas import DataFrame
from typing import Union

# Class README: _AbstrModeControler
# 추상 클래스, 수집한 로그 데이터를 처리하는 기법을 구현하기 위한 추상 클래스
# 확장성을 목적으로 작성되었으며, 새로운 처리 기법을 구현하기 위해서 상속하여 사용

class _AbstrModeControler(ABC):
    def __init__(self, logDF:DataFrame):
        self.logDF = logDF

    @abstractmethod
    def process_method(self) -> Union[DataFrame,list]: 
        pass