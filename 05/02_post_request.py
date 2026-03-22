"""Problem 02: POST request to JSONPlaceholder.

Task:
1. Send POST to https://jsonplaceholder.typicode.com/posts
2. Send JSON payload with fields: title, body, userId
3. Print:
   - status code
   - raw body
   - parsed JSON
4. Confirm response includes your data + id

Note: JSONPlaceholder simulates writes; data is not truly persisted.
"""

import requests

URL = "https://jsonplaceholder.typicode.com/posts"

def main() -> None:
    payload = {
        "title": "API Testing",
        "body": "Sending a POST request",
        "userID": 1
    }
    response = requests.post(URL, json=payload)
    
    print(f"Satus code: {response.status_code}")
    print(f"Raw body: {response.text}")
    parsed_json = response.json()
    print(f"Parsed JSON: {parsed_json}")
    
    if all(i in parsed_json for i in payload) and "id" in parsed_json:
        print("\nConfirmed: Response includes original data + new ID.")


if __name__ == "__main__":
    main()
