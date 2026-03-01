import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np



class Employer():

    def __init__(self):
        self.Jobs = pd.read_csv("Dataset/Jobs.csv")
    
    def _SimilarityCVwithJobs(self,Employer_Desc:str,Job_Title:str,Work_type:str,Gender:str) -> tuple[np.ndarray,pd.DataFrame,pd.DataFrame]:
        self.Companies = pd.read_csv("Dataset/Companies.csv")
        model = SentenceTransformer(model_name_or_path="all-MiniLM-L6-v2")
        filterd_Jobs = self.Jobs[(self.Jobs["Job Title"] == Job_Title) & (self.Jobs["Work Type"] == Work_type) & ((self.Jobs["Preference"] == Gender) | (self.Jobs["Preference"] == "Both")) ]
        filterd_companies = self.Companies[self.Companies["Job Id"].isin(filterd_Jobs["Job Id"].to_list())]

        jd_embedding = model.encode([Employer_Desc])
        resume_embeddings = model.encode(filterd_Jobs["Job Description"].to_list())
        
        return cosine_similarity(jd_embedding, resume_embeddings)[0] , filterd_Jobs , filterd_companies
    
    def GetTopJobs(self,Employer_Desc:str,Job_Title:str,Work_type:str,Gender:str) -> pd.DataFrame:
        Similarity_Scores , Filterd_Jobs , Filterd_Companies = self._SimilarityCVwithJobs(Employer_Desc=Employer_Desc,Job_Title=Job_Title,Work_type=Work_type,Gender=Gender)
        results = []
        for i, score in enumerate(Similarity_Scores):
            job_data = Filterd_Jobs.iloc[i]
            company_data = Filterd_Companies.iloc[i]

            results.append({
                "Job Description": job_data["Job Description"],
                "Salary Range":job_data['Salary Range'],
                "Benefits":job_data['Benefits'],
                "skills":job_data['skills'],
                "Contact Person":company_data['Contact Person'],
                "Contact":company_data['Contact'],
                "Responsibilities":job_data['Responsibilities'],

                "Company" :company_data["Company"],
                "Company Profile" :company_data["Company Profile"],
                "Company Size" :company_data["Company Size"],
                "location" :company_data["location"],
                "Country" :company_data["Country"],
                "latitude" :company_data["latitude"],
                "longitude" :company_data["longitude"],
                "Date":job_data['Date'],
                "Match_Score": round(score * 100, 2), 
            })
        
        return pd.DataFrame(results).sort_values(by="Match_Score", ascending=False)
    
    def Get_Jobs(self) -> list:
        return np.unique(self.Jobs["Job Title"]).tolist()
    
    def Get_WorkTypes(self) -> list:
        return np.unique(self.Jobs["Work Type"]).tolist()
