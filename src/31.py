import requests
from bs4 import BeautifulSoup

def fetch_webpage(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
        return None

# Example usage
url = "https://www.example.com"
webpage = fetch_webpage(url)
if webpage:
    with open("example.html", "w") as f:
        f.write(webpage.text)
