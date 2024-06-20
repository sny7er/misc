# reads a list of urls, urls.txt (be sure to proceed each with http:// ) 
# performs a GET request on each, returns a response
# waits for a time-out if there is no response, dies with an error


import requests
from requests.exceptions import RequestException, Timeout

def read_urls_from_file(file_name):
    with open(file_name, 'r') as file:
        urls = file.readlines()
    # Strip whitespace characters like '\n' at the end of each line
    urls = [url.strip() for url in urls if url.strip()]
    return urls

def check_urls(urls):
    timeout = 3  # Timeout in seconds
    for url in urls:
        try:
            response = requests.get(url, timeout=timeout)
            print(f"URL: {url}, Status Code: {response.status_code}")
        except Timeout:
            print(f"URL: {url}, Error: Timeout - Request timed out")
        except RequestException as e:
            print(f"URL: {url}, Error: {e}")

if __name__ == "__main__":
    file_name = 'urls.txt'  # Specify your file name here
    urls = read_urls_from_file(file_name)
    check_urls(urls)
