import pandas as pd
import nltk
nltk.download('vader_lexicon')
import pyodbc
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Define a function to map the sentiment scores to positive, negative, or neutral
def get_sentiment_category(score):
    if score > 0:
        return 'Positive'
    elif score < 0:
        return 'Negative'
    else:
        return 'Neutral'

# Load the CSV file into a pandas DataFrame
df = pd.read_csv('Reviews_Data/H&M_reviews.csv')

# Create an instance of the SentimentIntensityAnalyzer class from NLTK
sia = SentimentIntensityAnalyzer()

# Create an empty list to store the sentiment scores
sentiment_scores = []

# Loop through each review in the DataFrame, calculate its sentiment score, and append it to the sentiment_scores list
for review in df['H&M_Review']:
    sentiment_scores.append(sia.polarity_scores(review)['compound'])

# Map the sentiment scores to categories using the get_sentiment_category function
sentiment_categories = [get_sentiment_category(score) for score in sentiment_scores]

# Create a new column in the DataFrame to store the sentiment categories
df['Sentiment Category'] = sentiment_categories

# Save the updated DataFrame to a new CSV file
df.to_csv('sentiment_categories.csv', index=False)





# import pandas as pd
# from textblob import TextBlob

# # Define a function to map the polarity scores to positive, negative, or neutral
# def get_sentiment_category(score):
#     if score > 0:
#         return 'Positive'
#     elif score < 0:
#         return 'Negative'
#     else:
#         return 'Neutral'

# # Load the CSV file into a pandas DataFrame
# df = pd.read_csv('Reviews_Data/H&M_reviews.csv')

# # Create an empty list to store the polarity scores
# polarity_scores = []

# # Loop through each review in the DataFrame, calculate its polarity score, and append it to the polarity_scores list
# for review in df['H&M_Review']:
#     blob = TextBlob(review)
#     polarity_scores.append(blob.sentiment.polarity)

# # Map the polarity scores to categories using the get_sentiment_category function
# sentiment_categories = [get_sentiment_category(score) for score in polarity_scores]

# # Create a new column in the DataFrame to store the sentiment categories
# df['Sentiment Category'] = sentiment_categories

# # Save the updated DataFrame to a new CSV file
# df.to_csv('sentiment_categories.csv', index=False)