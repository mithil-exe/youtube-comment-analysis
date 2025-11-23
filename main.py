from dataLoder import load_comments
from cleaning import clean_dataframe
from analysis import (
    word_frequency,
    plot_word_frequency,
    sentiment_analysis,
    plot_sentiment_counts
)

# Step 1: Load dataset
df = load_comments("youtube_comments.csv")
print("Dataset Loaded Successfully!")
print("Total Comments:", len(df))

# Step 2: Clean text
df = clean_dataframe(df)
print("Text Cleaning Completed!")
print(df.head())

# Step 3: Word frequency + graph
print("\nTop 20 Words:")
print(word_frequency(df))
plot_word_frequency(df)

# Step 4: Sentiment analysis + graph
df = sentiment_analysis(df)
print("\nSentiment Counts:")
print(df['Sentiment'].value_counts())
plot_sentiment_counts(df)

print("\nAll Analysis Completed Successfully!")
