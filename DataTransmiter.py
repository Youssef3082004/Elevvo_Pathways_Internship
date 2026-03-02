import pandas as pd

class DataTransmiter:

    results =  None

    @staticmethod
    def set_Results(Results:pd.DataFrame):
        DataTransmiter.results = Results
    
    def Get_Results() -> pd.DataFrame:
        return DataTransmiter.results
