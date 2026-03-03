from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import pymupdf
import os 

class Employers:

    @staticmethod
    def _Read_CVS(path:str) -> tuple[list[str],list[str]]:
        cvs = os.listdir(rf"{path}")
        files = []
        for cv in cvs:
            doc = pymupdf.open(filename=fr"{path}/{cv}")
            file_content = []

            for page in doc:

                file_content.append(page.get_text())
            files.append(" ".join( file_content))
        return files ,cvs
    
    @staticmethod
    def GetTopCVs(job_description:str,path:str) -> list[tuple[str,float]]:
        CVFiles ,cvs_names = Employers._Read_CVS(path=path)
        model = SentenceTransformer(model_name_or_path="all-MiniLM-L6-v2")
        cvs_embedding = model.encode(CVFiles)
        job_description_embedding = model.encode([job_description])
        similarities = cosine_similarity(job_description_embedding,cvs_embedding)[0]

        scores = {}
        for file,score in zip(cvs_names,similarities):
            scores[file] = round(score *100 ,2)
        return sorted(scores.items(),key=lambda x:x[1],reverse=True)