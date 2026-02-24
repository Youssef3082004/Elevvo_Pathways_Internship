# Question Answering System (SQuAD Evaluation)
<div align="center">

[![Python](https://img.shields.io/badge/Python-3.13+-3776AB?style=for-the-badge&logo=python&logoColor=3776AB)](https://python.org)
[![huggingface](https://img.shields.io/badge/huggingface-5.2.0-ffd21e?style=for-the-badge&logo=huggingface&logoColor=ffd21e)](https://huggingface.co/)
[![PYTorch](https://img.shields.io/badge/PYtorch-2.7.0-orange?style=for-the-badge&logo=pytorch&logoColor=orange)](https://pytorch.org/)
[![Pandas](https://img.shields.io/badge/Pandas-2.2.3-purple?style=for-the-badge&logo=pandas&logoColor=purple)](https://pandas.pydata.org/)
[![NumPy](https://img.shields.io/badge/NumPy-2.2.6-013243?style=for-the-badge&logo=numpy&logoColor=white)](https://numpy.org)


</div>

# 📑 Description
This repository contains tools for processing Question Answering datasets and evaluating the **DistilBERT** model on the [**SQuAD (Stanford Question Answering Dataset)**](https://www.kaggle.com/datasets/stanfordu/stanford-question-answering-dataset) task.

## 📂 Project Structure
```
├── Dataset
│   ├── dev.json
│   ├── train.json
│   └── train.csv
├── .gitignore
├── Json_Converter.ipynb
├── Model.ipynb
└── Readme.md
```

## 🚀 Getting Started

### Prerequisites

* Ensure you have the following libraries installed:

```bash
pip install torch pandas transformers datasets tqdm

```

### Model Information

* The project utilizes the `distilbert-base-cased-distilled-squad` model from Hugging Face. This model is a smaller, faster, and cheaper version of BERT, specifically fine-tuned for extractive question answering.

### Evaluation Metrics

The system evaluates the predicted answers against ground truth using:

* **Exact Match (EM):** Measures the percentage of predictions that match the ground truth answers exactly.
* **F1 Score:** Measures the average overlap between the prediction and the ground truth tokens.

## 🚩 Model Performance Metrics
* **F1 Score: 84.81%**
* **Exact Match (EM): 72.0%**

**Evaluation Setup**

* **Model:** `distilbert-base-cased-distilled-squad`
* **Dataset:** SQuAD (Stanford Question Answering Dataset)
* **Sample Size:** The metrics above were derived from evaluating 100 samples from the dataset.

## 🛠️ Usage

1. **Data Preparation**: Use `Json_Converter.ipynb` to parse your raw SQuAD-style JSON files into a structured tabular format.
2. **Inference**: Run `Model.ipynb` to load the model and tokenizer. Use the `get_answer(question, context)` function to extract answers from text.
3. **Evaluation**: The notebook provides a pipeline to iterate through the dataset and calculate the overall accuracy of the model.

## 📊 Sample Data Format

The processed dataset includes the following fields:

* `Title`: The topic of the context.
* `Context`: The background text.
* `Question`: The query to be answered.
* `Answer_Text`: The ground truth answer.
* `Answer_Start`: The character index where the answer begins.

---
<h3 align="center">Developed as part of the Elevvo Pathways Internship - Level 3</h3>