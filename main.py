import sys
import re
import requests
import json

def read_input():
    """Reads a series of strings separated by \n and returns a list.
    """
    output = []
    for line in sys.stdin:
        if line.strip() == '':
            break
        output.append(line.strip())
    return output

def is_valid_url(url: str) -> bool:
    return re.match(r"http(s?):\/\/[A-Za-z0-9\-\.\_\~\:\/\?\#\[\]\@\!\$\&\'\(\)\*\+\,\;\%\=]+", url) is not None 

def main():
    urls = read_input()
    for url in urls:
        if is_valid_url(url):
            try:
                response = requests.get(url, timeout=10)
                print(json.dumps({
                    "Status_code": response.status_code,
                    "Url": url,
                    "Content_length": response.headers.get("Content-Length", "unknown"),
                    "Date": response.headers.get("Date", "unknown")
                }, indent = 4))
            except requests.exceptions.RequestException:
                print(json.dumps({
                    "Url": url,
                    "Error": "RequestException"
                }, indent = 4), file=sys.stderr)
        else:
            print(json.dumps({
                "Url": url,
                "Error": "invalid url"
            }, indent = 4), file=sys.stderr)               

if __name__ == '__main__':
    main()