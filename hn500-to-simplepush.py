#!/usr/bin/env python3

from multiprocessing import Pool
import requests

# TODO: Add Wallabag integration as bonus points.

SIMPLEPUSH_ID = '{{ SIX CHARACTER SIMPLEPUSH ID HERE }}'
BASE_URL = 'https://hacker-news.firebaseio.com/v0'


def main():
    with open('.hn-to-simplepush.history', 'a+') as history_file:
        history_file.seek(0)
        seen_ids = {int(line) for line in history_file}

        topstories_ids = requests.get('{}/topstories.json'.format(BASE_URL)).json()

        with Pool(8) as pool:
            urls = []
            for topstory_id in topstories_ids[:30]:
                if topstory_id not in seen_ids:
                    urls.append('{}/item/{}.json'.format(BASE_URL, topstory_id))

            for topstory_id, topstory_r in zip(topstories_ids, pool.imap(requests.get, urls)):
                topstory = topstory_r.json()

                if topstory['score'] > 500:
                    print('HN ID:', topstory_id)

                    requests.post('https://api.simplepush.io/send', data={
                        'key': SIMPLEPUSH_ID,
                        'title': 'HN500: ' + topstory['title'],
                        'msg': topstory['url']
                    })

                    history_file.write('{}\n'.format(topstory_id))


if __name__ == '__main__':
    main()
