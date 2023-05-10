#!/usr/bin/python3
"""
nction that queries the Reddit API and returns a list
containing the titles of all hot articles for a given subreddit.
"""
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    base_url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    hearders = {"User-Agent":
                "lenux.0x16-api_advanced:v1.0.0(by /u/sbusiso_Mdlalose_)"}
    params = {
        "after": after,
        "count": 100,
        "limit": 10
    }
    response = requests.get(base_url, headers=hearders, params=params,
                            allow_redirects=False)
    if response.status_code != 200:
        return None

    result = response.json().get("data")
    after = result("after")
    count = count + result.get("dist")
    for i in result.append(i.get("children")):
        hot_list.append(i.get("data").get("title"))
