import re
import pandas as pd
import pymupdf
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np



class Employer():

    def __init__(self):
        pass
        
    
    def _SimilarityCVwithJobs(self,Employer_Desc:str,Job_Title:str,Work_type:str,Gender:str) -> tuple[np.ndarray,pd.DataFrame,pd.DataFrame]:
        self.Jobs = pd.read_csv("Dataset/Jobs.csv")
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
                "Contact Person":company_data['Contact Person'],
                "Contact":company_data['Contact'],

                "Company" :company_data["Company"],
                "Company Size" :company_data["Company Size"],
                "location" :company_data["location"],
                "Country" :company_data["Country"],
                "latitude" :company_data["latitude"],
                "longitude" :company_data["longitude"],
                "Match_Score": round(score * 100, 2), 
            })
        
        return pd.DataFrame(results).sort_values(by="Match_Score", ascending=False)
    
    def Get_Jobs(self) -> list:
        return ['Account Director','Account Executive','Account Manager','Accountant','Administrative Assistant','Aerospace Engineer','Architect','Architectural Designer','Art Director',
                'Art Teacher','Back-End Developer','Brand Ambassador','Brand Manager','Business Analyst','Business Development Manager','Chemical Analyst','Chemical Engineer','Civil Engineer',
                'Content Writer','Copywriter','Customer Service Manager','Customer Service Representative','Customer Success Manager','Customer Support Specialist','Data Analyst',
                'Data Engineer','Data Entry Clerk','Data Scientist','Database Administrator','Database Developer','Dental Hygienist','Digital Marketing Specialist',
                'Electrical Designer','Electrical Engineer','Email Marketing Specialist','Environmental Consultant','Environmental Engineer','Event Coordinator','Event Manager',
                'Event Planner','Executive Assistant','Family Lawyer','Family Nurse Practitioner','Finance Manager','Financial Advisor','Financial Analyst','Financial Controller','Financial Planner',
                'Front-End Developer','Front-End Engineer','Graphic Designer','HR Coordinator','HR Generalist','HR Manager','Human Resources Manager','IT Administrator',
                'IT Manager','IT Support Specialist','Interior Designer','Inventory Analyst','Investment Advisor','Investment Analyst','Investment Banker',
                'Java Developer','Key Account Manager','Landscape Architect','Landscape Designer','Legal Advisor','Legal Assistant','Legal Counsel','Legal Secretary',
                'Litigation Attorney','Market Analyst','Market Research Analyst','Marketing Analyst','Marketing Coordinator','Marketing Director','Marketing Manager',
                'Marketing Specialist','Mechanical Designer','Mechanical Engineer','Network Administrator','Network Analyst','Network Engineer','Network Security Specialist','Network Technician',
                'Nurse Manager','Nurse Practitioner','Occupational Therapist','Office Manager','Operations Manager','Paralegal','Pediatrician','Personal Assistant',
                'Pharmaceutical Sales Representative','Physical Therapist','Physician Assistant','Process Engineer','Procurement Coordinator','Procurement Manager','Procurement Specialist',
                'Product Designer','Product Manager','Project Coordinator','Project Manager','Psychologist','Public Relations Specialist','Purchasing Agent','QA Analyst',
                'QA Engineer','Quality Assurance Analyst','Registered Nurse','Research Analyst','Research Scientist','SEM Specialist','SEO Analyst','SEO Specialist','Sales Associate','Sales Consultant',
                'Sales Manager','Sales Representative','Social Media Coordinator','Social Media Manager','Social Worker','Software Architect',
                'Software Developer','Software Engineer','Software Tester','Speech Therapist','Structural Engineer','Substance Abuse Counselor','Supply Chain Analyst','Supply Chain Manager','Systems Administrator',
                'Systems Analyst','Systems Engineer','Tax Consultant','Teacher','Technical Writer','UI Developer','UX Researcher','UX/UI Designer','Urban Planner',
                'Veterinarian','Web Designer','Web Developer','Wedding Planner']
    
    def Get_WorkTypes(self) -> list:
        return ['Contract', 'Full-Time', 'Intern', 'Part-Time', 'Temporary']
    

    def Read_CV(seld,path:str):
        cv_text = []
        doc = pymupdf.open(f"{path}") 
        for i,page in enumerate(doc): 
            cv_text.append(page.get_text())
        cv_text = " ".join(cv_text).lower()
        cv_text = re.sub(pattern=r"[^a-z\n]",string=cv_text,repl=" ")
        cv_text = re.sub(pattern=r"\s+",string=cv_text,repl=" ")
        
        return cv_text
