"""
REQUESTS — Third-Party Library

Requests is the most popular HTTP library 5.1 - For:
- GET requests
- POST requests
- APIs
- JSON responses
"""

import requests

# ---------------------------------------------------------
# BASIC GET REQUEST
# ---------------------------------------------------------

response = requests.get("https://api.github.com")
print(response.status_code)
print(response.headers["content-type"])

# ---------------------------------------------------------
# JSON RESPONSE
# ---------------------------------------------------------

data = response.json()
print(data)

# ---------------------------------------------------------
# GET WITH PARAMETERS
# ---------------------------------------------------------

params = {"q": "python"}
r = requests.get("https://api.github.com/search/repositories", params=params)
print(r.json()["total_count"])
