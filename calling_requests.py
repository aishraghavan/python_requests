"""
Pre req: pip install requests.
"""

import requests

class CallingRequests(object):
    def call_google(self):
        url = "https://www.google.com/"
        response = requests.get(url)
        print response.status_code

    def call_query(self, query):
        query = query.replace(" ", "+")
        url = "https://www.google.com/#q="
        url += query
        response = requests.get(url)
        print response.status_code

if __name__ == "__main__":
    test_requests = CallingRequests()
    test_requests.call_google()
    test_requests.call_query("target near me")
