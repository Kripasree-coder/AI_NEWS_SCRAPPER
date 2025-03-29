import requests
from bs4 import BeautifulSoup
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import time

nltk.download('punkt')
nltk.download('stopwords')

def fetch_headlines(url="https://www.bbc.com/news/topics/cdl8n2edg0gt/artificial-intelligence"):  
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'lxml')
        headlines = soup.find_all('h3', class_='entry-title')[:10]  # Get top 10 headlines
        return [headline.get_text().strip() for headline in headlines]
    
    return ["Failed to fetch news. Please try again later."]

def summarize_text(text):
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(text.lower())
    filtered_words = [word for word in words if word not in stop_words]
    return " ".join(filtered_words[:5])  # Simple summary
