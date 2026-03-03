import pandas as pd

class JobsDataTransmiter:

    results =  None
    cv = None

    @staticmethod
    def set_Results(Results:pd.DataFrame):
        JobsDataTransmiter.results = Results
    
    def Get_Results() -> pd.DataFrame:
        return JobsDataTransmiter.results
    
    @staticmethod
    def set_CVText(cv:str):
        JobsDataTransmiter.cv = cv

    def Get_CVText() -> str:
        return JobsDataTransmiter.cv

class EmployersDataTransmiter:

    results = None
    path = None

    @staticmethod 
    def set_Results(Results:list[tuple[str,float]]):
        EmployersDataTransmiter.results = Results
    
    @staticmethod 
    def Get_Results() -> list[tuple[str,float]]:
        return EmployersDataTransmiter.results 
    
    @staticmethod
    def set_Path(path:str):
        EmployersDataTransmiter.path = path
    
    def Get_Path() -> str:
        return EmployersDataTransmiter.path