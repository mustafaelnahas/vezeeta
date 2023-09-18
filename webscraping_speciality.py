
# installing & importing libraries
# !pip install requests
# !pip install beautifulsoup4
import requests
from bs4 import BeautifulSoup

# Generating a request for vezeeta.com
url = 'https://www.vezeeta.com/ar/%D8%AF%D9%83%D8%AA%D9%88%D8%B1/%D8%B9%D8%B8%D8%A7%D9%85/%D9%85%D8%B5%D8%B1'
response = requests.get(url)
print(response.text)