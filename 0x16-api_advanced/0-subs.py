#!/usr/bin/python3
"""
Script to query the Reddit API for the number of subcribers.
"""
import requests


def number_of_subscribers(subreddit):
    base_url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    hearders = {
        "User-Agent": "lenux.0x16-api_advanced:v1.0.0 (by /u/sbusiso_Mdlaose_)"}
    if not subreddit or type(subreddit) is not str:
        return 0
    response = requests.get(base_url).format(subreddit), hearders.json()
    result = response.get("data", {}).get("subcribers", 0)
    return result
