from abc import ABC, abstractmethod
from pandas import DataFrame
from typing import Union
class Abstr_DataFrameControler(ABC):
    def __init__(self, logDF:DataFrame):
        self.logDF = logDF

    @abstractmethod
    def process_method(self) -> Union[DataFrame,list]: 
        pass