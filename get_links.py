import requests
from bs4 import BeautifulSoup

def get_links(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')

            links = soup.find_all('a')
            url_links = [link.get('href') for link in links]

            return url_links
        else:
            raise requests.exceptions.RequestError(f"Error: {response.status_code}")
    except requests.exceptions.RequestException as error:
        raise requests.exceptions.RequestException(f"Error: {str(error)}")

if __name__ == "__main__":
    url = "https://tryhackme.com"
    links = get_links(url)
    print(f"Links found on {url}")
    for link in links:
        print(link)
