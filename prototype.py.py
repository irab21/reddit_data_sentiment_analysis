import praw
import pandas as pd
import streamlit as st
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Initialize PRAW with your credentials
reddit = praw.Reddit(client_id='_F3fW259iDGlYd5KfBa9QQ', 
                     client_secret='oBWmCvJXctLCffEP-83tL1mfLUvXgg', 
                     user_agent='my_stock_analysis_app by /u/NoTrash7060')

# Function to fetch Reddit discussions for a specific stock
def fetch_reddit_data(stock_symbol, limit=100):
    subreddit = reddit.subreddit('wallstreetbets')  # WallStreetBets is popular for stock discussions
    posts = subreddit.search(stock_symbol, sort='new', limit=limit)
    
    data = []
    for post in posts:
        data.append([post.title, post.selftext, post.score, post.url, post.created_utc])
    
    df = pd.DataFrame(data, columns=['Title', 'Content', 'Score', 'URL', 'Created UTC'])
    return df

# Function to perform sentiment analysis using VADER
def analyze_sentiment(df):
    analyzer = SentimentIntensityAnalyzer()
    sentiments = []
    for text in df['Title'] + ' ' + df['Content']:
        sentiment_score = analyzer.polarity_scores(text)
        sentiments.append(sentiment_score['compound'])  # compound score represents overall sentiment
    df['Sentiment'] = sentiments
    return df

# Streamlit UI
def main():
    st.title('Stock Sentiment Analysis from Reddit')
    
    stock_symbol = st.text_input('Enter Stock Symbol', 'AAPL')  # Default: AAPL (Apple)
    limit = st.slider('Number of Posts', 10, 100, 50)  # Limit the number of posts fetched
    
    if st.button('Fetch Data'):
        st.write('Fetching data for', stock_symbol)
        
        # Fetch Reddit data
        df = fetch_reddit_data(stock_symbol, limit)
        
        # Perform sentiment analysis
        df = analyze_sentiment(df)
        
        # Display the data
        st.write(df[['Title', 'Sentiment', 'Score', 'URL']].head(20))
        
        # Plot sentiment distribution
        st.subheader('Sentiment Distribution')
        st.bar_chart(df['Sentiment'].value_counts())
        
        # Simple prediction model (e.g., based on average sentiment)
        avg_sentiment = df['Sentiment'].mean()
        
        avg_sentiment = round(df['Sentiment'].mean(), 2)
        

        st.write(f"Average Sentiment Score is: {avg_sentiment}")
        if avg_sentiment > 0.1:
            st.write('Prediction: Stock is likely to go up')
        elif avg_sentiment < -0.1:
            st.write('Prediction: Stock is likely to go down')
        else:
            st.write('Prediction: Stock movement is uncertain')

if __name__ == '__main__':
    main()
