# BBC News Topic Modeling

<div align="center">

[![Python](https://img.shields.io/badge/Python-3.13+-3776AB?style=for-the-badge&logo=python&logoColor=3776AB)](https://python.org)
[![Pandas](https://img.shields.io/badge/Pandas-2.2.3+-3776AB?style=for-the-badge&logo=pandas&logoColor=white)](https://python.org)
[![NumPy](https://img.shields.io/badge/NumPy-1.26+-013243?style=for-the-badge&logo=numpy&logoColor=white)](https://numpy.org)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.4+-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-3.9+-11557C?style=for-the-badge&logo=matplotlib&logoColor=white)](https://matplotlib.org)
[![Seaborn](https://img.shields.io/badge/Seaborn-0.13+-4C72B0?style=for-the-badge&logo=python&logoColor=white)](https://seaborn.pydata.org)
[![Seaborn](https://img.shields.io/badge/nltk-3.9.0+-472B0?style=for-the-badge&logo=python&logoColor=white)](https://seaborn.pydata.org)
</div>

## 🚀 Overview

This repository contains a Jupyter Notebook (`Model.ipynb`) that demonstrates how to perform Topic Modeling on a BBC News dataset using Natural Language Processing (NLP) techniques and Machine Learning pipelines.



## ⚙️ Methodology

The notebook covers the entire pipeline from raw text to topic extraction:

1. **Data Loading & Consolidation:** - Reads [**The BBC News dataset**](https://www.kaggle.com/datasets/gpreda/bbc-news/data) and creates a unified `text` feature by combining the article `title` and `description`.
   - Cleans missing values and duplicate rows.
   
2. **Text Cleaning & Preprocessing (via Custom `Column` class):** 
   - Lowercasing all text.
   - Removing single-letter words and all punctuation using Regular Expressions.
   - Tokenization.
   - Stopwords removal using NLTK (`stopwords.words("english")`).
   - Lemmatization using `WordNetLemmatizer`.

3. **Modeling:**
   - Evaluates word frequencies using **TF-IDF Vectorization** (`TfidfVectorizer`).
   - Builds two separate Scikit-Learn `Pipeline`s to discover 20 underlying topics:
     - **Latent Dirichlet Allocation (LDA)**
     - **Non-Negative Matrix Factorization (NMF)**

4. **Visualization & Analysis:**
   - Extracts and displays the top 10 contributing words for each topic.
   - Classifies individual news rows into their dominant topics.
   - Provides an interactive HTML visualization of the LDA model using `pyLDAvis`.

## 🛠️ Technologies Used
* **Data Manipulation:** `pandas`, `numpy`, `re`
* **NLP:** `nltk` (corpus, tokenize, stem)
* **Machine Learning:** `scikit-learn` (Pipelines, TfidfVectorizer, LatentDirichletAllocation, NMF)
* **Visualization:** `pyLDAvis`, `matplotlib`, `wordcloud`


## 📁 Project Structure
```
|── Dataset         # Dataset Folder
├── assets
│   ├── words.png
│   └── words2.png
├── .gitignore
├── Column.py       # A helper Python script
├── Model.ipynb     # The main Jupyter Notebook
└── Readme.md
```



## 📍 Visualize the most frequent Words in **LDA** Topics
![Demo Image](assets/words.png) 

## 📍 Visualize the most frequent Words in **NMF** Topics
![Demo Image](assets/words2.png)

---
<h3 align="center">Developed as part of the Elevvo Pathways Internship - Level 2</h3>