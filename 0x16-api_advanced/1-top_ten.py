#!/usr/bin/python3
"""
Title: TOP ten titles
Description: Write a function that queries the Reddit API and prints the
        titles of the first 10 hot posts listed for a given subreddit.
Author: @a_idk scripting
"""

import requests


def top_ten(subreddit):
    """
    Method that returns top ten titles of first 10 hot posts
    Args:
        subreddit: Name of the subreddit
    """
    api_url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    headers = {"User-Agent": "0x16.api.advanced.project by ALX/C:17"}
    lm = {"limit": 10}

    resp = requests.get(
            api_url, headers=headers, params=lm, allow_redirects=False
            )

    # Checking the response status code
    if resp.status_code == 404:
        print('None')
        return
    # parsing the json response, printing the task requirements
    output = resp.json().get("data")
    for x in output.get("children"):
        print(x.get("data").get("title"))
