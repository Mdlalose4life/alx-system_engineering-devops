#!/usr/bin/python3
""" Function that queries the Reddit API and
    print the titles of the first 10 hot posts
"""
import requests


def top_ten(subreddit):
    base_url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    hearders = {"User-Agent":
                "lenux.0x16-api_advanced:v1.0.0(by /u/sbusiso_Mdlalose_)"}
    params = {
        "limit": 10
    }
    response = requests.get(base_url, headers=hearders, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        print(None)
        return
    results = response.json().get("data")
    [print(c.get("data").get("title")) for c in results.get("children")]
