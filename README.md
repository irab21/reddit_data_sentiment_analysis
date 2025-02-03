# Stock Sentiment Analysis from Reddit

This Streamlit application fetches stock-related discussions from the **WallStreetBets** subreddit and performs sentiment analysis using the **VADER** sentiment analyzer. It helps gauge the overall sentiment towards a stock based on Reddit discussions and provides a simple prediction of potential stock movement.

## Features
- Fetches recent discussions from the **WallStreetBets** subreddit based on a stock symbol.
- Analyzes sentiment using the **VADER SentimentIntensityAnalyzer**.
- Displays sentiment scores, post details, and a sentiment distribution chart.
- Provides a simple stock movement prediction based on average sentiment scores.

## Installation & Setup
### Prerequisites
Ensure you have Python installed along with the following dependencies:
- `praw`
- `pandas`
- `streamlit`
- `vaderSentiment`

You can install them using:
```bash
pip install praw pandas streamlit vaderSentiment
```

### Setting Up Reddit API Credentials
To use this application, you need Reddit API credentials. Create an application on [Reddit API](https://www.reddit.com/prefs/apps) and obtain:
- `client_id`
- `client_secret`
- `user_agent`

Replace these values in the script:
```python
reddit = praw.Reddit(client_id='your_client_id',
                     client_secret='your_client_secret',
                     user_agent='your_user_agent')
```

## How to Run the App
Run the Streamlit application using:
```bash
streamlit run app.py
```
Replace `app.py` with the filename of your script.

## Usage
1. Enter the stock symbol (e.g., AAPL for Apple).
2. Select the number of posts to analyze using the slider.
3. Click the "Fetch Data" button to retrieve and analyze discussions.
4. View sentiment scores, post details, and sentiment distribution.
5. Get a simple prediction on stock movement.

## Interpretation of Sentiment Scores
- **Positive Sentiment ( > 0.1 )** → Stock is likely to go **up**.
- **Negative Sentiment ( < -0.1 )** → Stock is likely to go **down**.
- **Neutral Sentiment (between -0.1 and 0.1)** → Stock movement is **uncertain**.

## Limitations & Future Improvements
- The model relies on Reddit sentiment, which may not always correlate with actual stock performance.
- More advanced ML models can improve prediction accuracy.
- Expand subreddit sources for a broader sentiment analysis.

## License
This project is for educational and research purposes only.

---
**Author:** Ira Bajpai 
**GitHub:** irab21
**Contact:** bajpaiira21@gmail.com

