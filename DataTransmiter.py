import pandas as pd

class DataTransmiter:

    results =  None
    cv = None

    @staticmethod
    def set_Results(Results:pd.DataFrame):
        DataTransmiter.results = Results
    
    def Get_Results() -> pd.DataFrame:
        return DataTransmiter.results
    
    @staticmethod
    def set_CVText(cv:str):
        DataTransmiter.cv = cv
    

    def Get_CVText() -> str:
        return DataTransmiter.cv
