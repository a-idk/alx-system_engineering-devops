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
    api_url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    headers = {"User-Agent": "0x16.api.advanced.project by ALX"}

    resp = requests.get(api_url, headers=headers, allow_redirects=False)

    # Checking the response status code
    if resp.status_code == 200:
        dict_data = resp.json()
        subs = dict_data['data']['subscribers']
        return subs
    else:
        return 0  # if subreddit is invalid
