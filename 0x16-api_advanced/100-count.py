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
import sys

# parameter definition
# tally = []
# after = None


def count_words(subreddit, word_list, kv_pairs={}, after="", count=0):
    """
    Method that returns  list containing the titles of all hot articles
    for a given subreddit.
    Args:
        subreddit: Name of the subreddit
        word_list: list of words to search in titles
        kv_pairs: key/value pairs of words
        after: next page of result
        count: matched results
    """
    api_url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)

    headers = {"User-Agent": "0x16.api.advanced.project by ALX/C:17"}
    lm = {"after": after, "limit": 100, "count": count}

    resp = requests.get(
            api_url, headers=headers, params=lm, allow_redirects=False
            )

    # handling exceptions
    try:
        output = resp.json()
        if resp.status_code == 404:
            raise Exception
    except Exception:
        print("")
        return
    # parsing the json response, printing the task requirements
    output = resp.json().get("data")
    after = resp.json().get("data").get("after")
    count = count + resp.json().get("data").get("dist")

    # appending the titles to the hotlist
    for x in output.get("children"):
        heading = x.get("data").get("title").lower().split()
        for y in word_list:
            if y.lower() in heading:
                for i in heading:
                    if i == y.lower():
                        tally = len(i)
                # tally = len([i for i in heading if i == word.lower()])
                if kv_pairs.get(y) is None:
                    kv_pairs[y] = tally
                else:
                    kv_pairs[y] = kv_pairs.get(y, 0) + tally
    # checking for None
    if after is None:
        if len(kv_pairs) == 0:
            print("")
            return
        kv_pairs = sorted(kv_pairs.items(), key=lambda kv: (-kv[1], kv[0]))
        for key, val in kv_pairs:
            print(f"{key}: {val}")
    else:
        count_words(subreddit, word_list, kv_pairs, after, count)
    """
    [h_lst.append(x.get("data").get("title")) for x in output.get("children")]
    # call function recursively if post is more
    if aft is not None:
        return recurse(subreddit, h_lst, aft, tally)
    return h_lst
    """
