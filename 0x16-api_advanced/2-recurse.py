#!/usr/bin/python3
"""
It contains recursive function that quries reddit api
"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    url = 'https://www.reddit.com/r/{}/hot.json?after={}'.format(subreddit, after)
    user = {'User-Agent': 'Custom User Agent'}

    response = requests.get(url, headers=user)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        after = data['data']['after']
        if after is None:
            hot_list = get_children(posts, len(posts))
            return hot_list
        hot_list.append(recurse(subreddit, hot_list, after=after))
        hot_list = get_children(posts, len(posts))
    else:
        return None
    return hot_list

def get_children(hot_list, counter, return_list=[]):
    """
    Gets the children from the data
    """
    if counter == 0:
        return return_list
    return_list.append(hot_list[counter - 1]['data']['title'])
    return (get_children(hot_list, counter - 1, return_list))
