#!/usr/bin/python3
"""
function that queries the Reddit API and returns a list
containing the titles of all hot articles for a given subreddit
"""
import requests


def recurse(subreddit, hot_list=[]):
    base_url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    hearders = {"User-Agent":
                "lenux.0x16-api_advanced:v1.0.0(by /u/sbusiso_Mdlalose_)"}
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    response = requests.get(base_url, headers=hearders, params=params,
                            allow_redirects=False)
    if response.status_code == 400:
        return None

    results = response.json().get("data")
    after = results.get("after")
    count += results.get("dist")
    for i in results.get("children"):
        hot_list.append(i.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
