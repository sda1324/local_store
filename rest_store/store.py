from flask_restful import Resource

from rest_store.local_client import getLocalStore
from rest_store.naver_search_client import naverSearch

from difflib import SequenceMatcher


class LocalStore(Resource):
    local_result = []

    def __init__(self):
        local_result = []

    def get(self, local, query, page):
        if local and query and page:
            print("ddddddddd")
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
                i = 0
                count = addresses.count(search_item['address'].replace('번지', ''))
                for j in range(count):

                    idx = addresses.index(search_item['address'].replace('번지', ''), i)
                    i = idx+1;
                    search_title = search_item['title'].replace('<b>', '').replace('</b>', '')
                    local_name = self.local_result[idx]['CMPNM_NM']
                    print(search_title, local_name)

                    if SequenceMatcher(None, search_title, local_name).ratio() > 0.8 :
                        item = {
                            'title': search_item['title'].replace('<b>', '').replace('</b>', ''),
                            'phone': search_item['telephone'],
                            'link': search_item['link'],
                            'local': self.local_result[idx]['SIGUN_NM'],
                            'address': search_item['address'],
                            'roadAddress': search_item['roadAddress'],
                            'category': search_item['category'],
                            'description': search_item['description'],
                            'LAT': self.local_result[idx]['REFINE_WGS84_LAT'],
                            'LOGT': self.local_result[idx]['REFINE_WGS84_LOGT']
                        }
                        items.append(item)

        result['items'] = items

        return result, 200

