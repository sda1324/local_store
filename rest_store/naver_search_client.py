import requests
from rest_store.keys import NAVER_ID, NAVER_KEY

url = 'https://openapi.naver.com/v1/search/local.json'

headers = {
    'X-Naver-Client-Id': NAVER_ID,
    'X-Naver-Client-Secret': NAVER_KEY
}

params = {
    'display': 30,
    'sort': 'random',
}


def naverSearch(query, start=1):
    params['query'] = query
    params['start'] = start
    result = requests.get(
        url=url,
        params=params,
        headers=headers
    )

    return result.json()


if __name__ == '__main__':
    naverSearch('평택 곱창')