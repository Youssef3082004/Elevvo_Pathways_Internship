import re
import pandas as pd
import pymupdf
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import spacy


class Employer():

    @staticmethod
    def _setup_skill_extractor(knowsSkills:list[str]):
        nlp = spacy.load("en_core_web_sm")    
        ruler = nlp.add_pipe("entity_ruler", before="ner")
        patterns = [{"label": "SKILL", "pattern": [{"LOWER": skill.lower()} for skill in s.split()]} for s in knowsSkills]    
        ruler.add_patterns(patterns)
        return nlp
    
    @staticmethod
    def extract_skills(text:str,knowsSkills:list[str]) -> list[str]:
        doc = Employer._setup_skill_extractor(knowsSkills)(text)
        found_skills = set(ent.text for ent in doc.ents if ent.label_ == "SKILL")
        return list(found_skills) if len(list(found_skills)) > 1 else ["No Matched Skill"]

    def __init__(self):
        pass
        
    
    def _SimilarityCVwithJobs(self,Employer_Desc:str,Qualifications:str,Work_type:str,Gender:str) -> tuple[np.ndarray,pd.DataFrame,pd.DataFrame]:
        self.Jobs = pd.read_csv("Dataset/Jobs.csv")
        self.Companies = pd.read_csv("Dataset/Companies.csv")
        model = SentenceTransformer(model_name_or_path="all-MiniLM-L6-v2")
        filterd_Jobs = self.Jobs[(self.Jobs["Qualifications"] == Qualifications) & (self.Jobs["Work Type"] == Work_type) & ((self.Jobs["Preference"] == Gender) | (self.Jobs["Preference"] == "Both")) ]
        filterd_companies = self.Companies[self.Companies["Job Id"].isin(filterd_Jobs["Job Id"].to_list())]

        jd_embedding = model.encode([Employer_Desc])
        resume_embeddings = model.encode(filterd_Jobs["Job Description"].to_list())
        
        return cosine_similarity(jd_embedding, resume_embeddings)[0] , filterd_Jobs , filterd_companies
    
    def GetTopJobs(self,Employer_Desc:str,Qualifications:str,Work_type:str,Gender:str) -> pd.DataFrame:
        Similarity_Scores , Filterd_Jobs , Filterd_Companies = self._SimilarityCVwithJobs(Employer_Desc=Employer_Desc,Qualifications=Qualifications,Work_type=Work_type,Gender=Gender)
        results = []
        for i, score in enumerate(Similarity_Scores):
            job_data = Filterd_Jobs.iloc[i]
            company_data = Filterd_Companies.iloc[i]

            results.append({
                "Job Description": job_data["Job Description"],
                "Salary Range":job_data['Salary Range'],
                "Contact Person":company_data['Contact Person'],
                "Contact":company_data['Contact'],
                "skills":job_data['skills'],
                "Job Title":job_data["Job Title"],


                "Company" :company_data["Company"],
                "Company Size" :company_data["Company Size"],
                "location" :company_data["location"],
                "Country" :company_data["Country"],
                "latitude" :company_data["latitude"],
                "longitude" :company_data["longitude"],
                "Match_Score": round(score * 100, 2), 
            })
        
        return pd.DataFrame(results).sort_values(by="Match_Score", ascending=False).iloc[:101,:]
    
    def Get_Qualifications(self) -> list:
        return ['B.Com', 'B.Tech', 'BA', 'BBA', 'BCA', 'M.Com', 'M.Tech', 'MBA', 'MCA', 'PhD']
    
    def Get_WorkTypes(self) -> list:
        return ['Contract', 'Full-Time', 'Intern', 'Part-Time', 'Temporary']
    

    def Read_CV(seld,path:str):
        cv_text = []
        doc = pymupdf.open(f"{path}") 
        for i,page in enumerate(doc): 
            cv_text.append(page.get_text())
        cv_text = " ".join(cv_text).lower()
        cv_text = re.sub(pattern=r"[^a-z\n]",string=cv_text,repl=" ")
        cv_text = re.sub(pattern=r"\b[a-zA-Z]{1}\b",string=cv_text,repl=" ")
        cv_text = re.sub(pattern=r"\s+",string=cv_text,repl=" ")
        return cv_text
