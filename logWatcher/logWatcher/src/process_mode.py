from Abstr_DataFrameControler import Abstr_DataFrameControler
from typing import Union
import pandas as pd

class CheckRunModule(Abstr_DataFrameControler):
    def process_method(self) -> pd.DataFrame:
        step1_df = self.logDF[~self.logDF['value'].str.strip().str.startswith('modsingle')].copy()
        
        Result_df = step1_df[step1_df['value'].str.strip().str[0] == '#'].copy()
        return step1_df
        
    