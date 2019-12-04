from flask_restful import Resource

from rest_store.local_client import getLocalStore
from rest_store.naver_search_client import naverSearch


class LocalStore(Resource):
    local_result = []

    def __init__(self):
        local_result = []

    def get(self, local, query, page):
        i = 1
        if len(self.local_result) == 0:
            while(True):
                result = getLocalStore(local, i)['RegionMnyFacltStus'][1]['row']
                self.local_result.extend(result)
                i += 1
                if len(result) != 100:
                    break

        result = naverSearch(local + " " + query, 1 + (int(page)-1)*30)
        search_result = result['items']


        result = {
            'result': 'success'
        }
        items = []
        addresses = [local_item['REFINE_LOTNO_ADDR'].replace('번지', '') for local_item in self.local_result]
        for search_item in search_result:
            if search_item['address'].replace('번지', '') in addresses:
                item = {
                    'title': search_item['title'].replace('<b>', '').replace('</b>', ''),
                    'phone': search_item['telephone'],
                    'link': search_item['link'],
                    'local': self.local_result[addresses.index(search_item['address'].replace('번지', ''))]['SIGUN_NM'],
                    'address': search_item['address'],
                    'roadAddress': search_item['roadAddress'],
                    'category': search_item['category'],
                    'description': search_item['description'],
                    'LAT': self.local_result[addresses.index(search_item['address'].replace('번지', ''))]['REFINE_WGS84_LAT'],
                    'LOGT': self.local_result[addresses.index(search_item['address'].replace('번지', ''))]['REFINE_WGS84_LOGT']
                }
                items.append(item)
                result['items'] = items

        return result, 200

