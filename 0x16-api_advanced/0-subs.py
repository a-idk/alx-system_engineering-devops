#!/usr/bin/python3
"""
Title: Return Subscribers from API
Description: Write a function that queries the Reddit API and returns the
        number of subscribers (not active users, total subscribers) for a
        given subreddit. If an invalid subreddit is given, the function
        should return 0.
Author: @a_idk scripting
"""

import requests


def number_of_subscribers(subreddit):
    """
    Method that returns the total number of subscribers in subreddit
    Args:
        subreddit: Name of the subreddit
    """
    # check if subreddit contain str
    if (type(subreddit) is not str):
        print(0)
        return

    api_url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "0x16.api.advanced.project by ALX"}
    resp = requests.get(api_url, headers=headers, allow_redirects=False)

    # Checking the response status code
    if resp.status_code is not 200:
        print(0)
    else:
        print(resp.json().get("data").get("subscribers"))
