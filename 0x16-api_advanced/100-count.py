import requests

def count_words(subreddit, word_list, after=None, counts={}):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100&after={after}"
    headers = {'User-Agent': 'Custom User Agent'}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']

        if not posts:
            sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0].lower()))
            for word, count in sorted_counts:
                print(f"{word}: {count}")
            return

        for post in posts:
            title = post['data']['title'].lower()
            words = title.split()

            for word in word_list:
                if word.lower() in words:
                    if word in counts:
                        counts[word] += words.count(word.lower())
                    else:
                        counts[word] = words.count(word.lower())

        after = data['data']['after']
        if after:
            return count_words(subreddit, word_list, after, counts)
        else:
            sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0].lower()))
            for word, count in sorted_counts:
                print(f"{word}: {count}")
            return

    else:
        return
