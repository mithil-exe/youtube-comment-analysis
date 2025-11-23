# YouTube Comment Analysis – NLP Mini Project

This repository contains the dataset and Python scripts used to collect, clean, analyze, and visualize YouTube comments from the video:

**"2025’s Most Important Career Podcast – Make Money Using AI | The Ranveer Show"**  
Video Link: https://youtu.be/YG1sW00jwLY

---

## 📂 Dataset

The dataset was extracted using the YouTube Data API and then cleaned using Python.
After preprocessing, the final cleaned dataset file is:

- `youtube_comments.csv`
- `youtube_comments_cleaned.csv` (after text cleaning)

---

## 🛠️ Python Scripts Used

This project uses **five Python files**, each handling a different stage of the NLP workflow.

### **1. `comments.py` – YouTube Comment Scraper**
- Uses YouTube Data API (`googleapiclient`)
- Fetches all top-level comments from the video
- Stores them into `youtube_comments.csv`

### **2. `dataLoader.py` – Dataset Loader**
- Loads the CSV file
- Renames columns properly for consistent processing

### **3. `cleaning.py` – Text Preprocessing**
- Converts text to lowercase  
- Removes punctuation  
- Tokenizes words  
- Removes English stopwords  
- Creates a new column `cleaned` in the DataFrame

### **4. `analysis.py` – NLP + Visualization**
Contains:
- **Word Frequency Calculation**
- **Bar Plot of Top 20 Words**
- **Sentiment Analysis using TextBlob**
- **Sentiment Distribution Graph**

### **5. `main.py` – Project Pipeline**
Runs the entire workflow:
1. Load dataset  
2. Clean text  
3. Show word frequencies  
4. Plot frequency graph  
5. Perform sentiment analysis  
6. Plot sentiment graph  

---

## 📁 Repository Structure

