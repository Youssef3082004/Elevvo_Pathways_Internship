import pandas as pd


class column:

    def __init__(self,Column_name:str,Dataset:pd.DataFrame):
        self.Column_name = Column_name
        self.Dataset = Dataset
    

    def Update(self,func):
        self.Dataset[self.Column_name] = self.Dataset[self.Column_name].apply(func=func)
        
        
