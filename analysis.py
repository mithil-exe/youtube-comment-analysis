from collections import Counter
import matplotlib.pyplot as plt
from textblob import TextBlob

def word_frequency(df):
    all_words = " ".join(df['cleaned']).split()
    return Counter(all_words).most_common(20)

def plot_word_frequency(df):
    freq = word_frequency(df)
    words = [item[0] for item in freq]
    counts = [item[1] for item in freq]

    plt.figure(figsize=(10, 5))
    plt.bar(words, counts)
    plt.xlabel("Words")
    plt.ylabel("Frequency")
    plt.title("Top 20 Most Frequent Words")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def sentiment_analysis(df):
    sentiments = []

    for text in df['cleaned']:
        polarity = TextBlob(text).sentiment.polarity

        if polarity > 0:
            sentiments.append("Positive")
        elif polarity < 0:
            sentiments.append("Negative")
        else:
            sentiments.append("Neutral")

    df["Sentiment"] = sentiments
    return df

def plot_sentiment_counts(df):
    counts = df['Sentiment'].value_counts()

    plt.figure(figsize=(6,4))
    plt.bar(counts.index, counts.values)
    plt.xlabel("Sentiment")
    plt.ylabel("Count")
    plt.title("Sentiment Distribution")
    plt.show()
