#!/usr/bin/python3
"""
Title: Recursive function
Description: Write a recursive function that queries the Reddit API and
        returns a list containing the titles of all hot articles for a
        given subreddit. If no results are found for the given subreddit,
        the function should return None
Author: @a_idk scripting
"""

import requests


def recurse(subreddit, h_lst=[], aft=None, tally=0):
    """
    Method that returns  list containing the titles of all hot articles
    for a given subreddit.
    Args:
        subreddit: Name of the subreddit
        h_lst: The hotlist
    """
    api_url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)

    headers = {"User-Agent": "0x16.api.advanced.project by ALX/C:17"}
    lm = {"limit": 100, "after": aft, "count": tally}

    resp = requests.get(
            api_url, headers=headers, params=lm, allow_redirects=False
            )
    # Checking the response status code
    if resp.status_code == 404:
        # print('None')
        return None
    # parsing the json response, printing the task requirements
    output = resp.json().get("data")
    aft = resp.json().get("data").get("after")
    tally = tally + resp.json().get("data").get("dist")
    # appending the titles to the hotlist
    [h_lst.append(x.get("data").get("title")) for x in output.get("children")]
    # call function recursively if post is more
    if aft is not None:
        return recurse(subreddit, h_lst, aft, tally)
    return h_lst
