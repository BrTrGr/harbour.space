"""Problem 03: GET request for HTML content.

Task:
1. Send GET to https://example.com
2. Print:
   - status code
   - Content-Type header
   - HTML body (response.text)
3. Verify content type contains text/html
4. Add raise_for_status()
"""

import requests

URL = "https://example.com"


def main() -> None:
    response = requests.get(URL)
    response.raise_for_status()
    
    print(f"Status code: {response.status_code}")
    print(f"Content-Type: {response.headers.get('Content-type')}")
    print(f"HTML body: {response.text}")
    
    if "text/html"  in response.headers.get('Content-type'):
        print("Verified, content type contains: text/html")


if __name__ == "__main__":
    main()