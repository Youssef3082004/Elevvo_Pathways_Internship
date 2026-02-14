# Amazon Product Review Sentiment Analysis
<div align="center">

[![Python](https://img.shields.io/badge/Python-3.13+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Pandas](https://img.shields.io/badge/Pandas-2.2.3+-3776AB?style=for-the-badge&logo=pandas&logoColor=white)](https://python.org)
[![NumPy](https://img.shields.io/badge/NumPy-1.26+-013243?style=for-the-badge&logo=numpy&logoColor=white)](https://numpy.org)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.4+-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-3.9+-11557C?style=for-the-badge&logo=matplotlib&logoColor=white)](https://matplotlib.org)
[![Seaborn](https://img.shields.io/badge/Seaborn-0.13+-4C72B0?style=for-the-badge&logo=python&logoColor=white)](https://seaborn.pydata.org)
[![Seaborn](https://img.shields.io/badge/nltk-3.9.0+-472B0?style=for-the-badge&logo=python&logoColor=white)](https://seaborn.pydata.org)

</div>

## 📑 Description
This project is part of the **Elevvo Pathways Internship (Task 1)**. It focuses on building a Machine Learning model to classify Amazon product reviews as either **Positive (1)** or **Negative (0)** using Natural Language Processing (NLP) techniques.

## 📂 Project Structure

```
|── Dataset         # Dataset Folder
├── assets
│   ├── acc.png
│   └── words.png
├── .gitignore
├── Column.py       # A helper Python script
├── Model.ipynb     # The main Jupyter Notebook
└── Readme.md
```

## 🛠️ Features & Workflow

### 1. Data Preprocessing
The text data undergoes a rigorous cleaning pipeline to ensure high-quality input for the models:
- **Lowercasing**: Converting all text to lowercase for consistency.
- **Noise Removal**: Removing single characters and special characters using Regex.
- **Tokenization**: Splitting sentences into individual words using NLTK.
- **Stopword Removal**: Filtering out common English stopwords (excluding negation words like "not", "don't" to preserve sentiment context).
- **Lemmatization**: Converting words to their base root form (e.g., "running" → "run") using `WordNetLemmatizer`.

### 2. Feature Engineering
- **TF-IDF Vectorization**: Converting cleaned text data into numerical vectors to reflect word importance.

### 3. Model Building
The project implements and compares multiple algorithms:
- **Logistic Regression**: A robust baseline for binary classification.
- **Naive Bayes (MultinomialNB)**: Suitable for high-dimensional text data.
- 

## 🧩 Helper Class (`Column.py`)

The `column` class is a custom utility designed to apply functions to pandas DataFrame columns efficiently without Reapeating Code.

```python
# Example Usage
from Column import column
text_col = column(Dataset=df, Column_name="CleanedText")
text_col.Update(func=lambda x: x.lower())

```

## 📊 Results

* **Logistic Regression Accuracy**: 90.85%
* **Weighted Logistic Regression Accuracy**: 90.60%
* **Naive Bayes Accuracy**: 80.05%

## ✅ Models Accuracy Matrix

![Demo Image](assets/acc.png)

## 📍 Most frequent **Positive** and **Negative** words

![Demo Image](assets/words.png)


## 🚀 Getting Started

### Prerequisites
Make sure you have Python installed along with the following libraries:

```bash
pip install pandas numpy seaborn matplotlib nltk scikit-learn