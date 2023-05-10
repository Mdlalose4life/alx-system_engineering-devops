#!/usr/bin/python3
"""
Script to query the Reddit API for the number of subcribers.
"""
import requests


def number_of_subscribers(subreddit):
    base_url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    hearders = {"User-Agent":
                "lenux.0x16-api_advanced:v1.0.0(by /u/sbusiso_Mdlalose_)"}
    response = requests.get(base_url, headers=hearders, allow_redirects=False)
    if response.status_code == 404:
        return 0
    result = response.json().get("data")
    return result.get("subcribers")
