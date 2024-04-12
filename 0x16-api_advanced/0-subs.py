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
        return(0)
    """
    if not isinstance(subreddit, str):
        return(0)
    """

    api_url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "linus:0x16.api.advanced.project:v1.0.0 (by ALX)"}
    resp = requests.get(api_url, headers=headers, allow_redirects=False)

    # Checking the response status code
    if resp.status_code is not 200:
        return(0)
    return(resp.json().get("data").get("subscribers"))
