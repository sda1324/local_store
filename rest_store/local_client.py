import requests
from rest_store.keys import LOCAL_KEY
#제외 지역리스트~

local_code = {
    '가평군': 41820,
    #'경기도': 41000,
    #'고양시': 41280,
    '과천시': 41290,
    '광명시': 41210,
    '광주시': 41610,
    #'구리시': 41310,
    #'군포시': 41410,
    '김포시': 41570,
    #'남양주시': 41360,
    '동두천시': 41250,
    '부천시': 41190,
    '성남시': 41130,
    #'수원시': 41110,
    '시흥시': 41390,
    '안산시': 41270,
    #'안성시': 41550,
    '안양시': 41170,
    '양주시': 41630,
    #'양평군': 41830,
    '여주시': 41670,
    #'연천군': 41800,
    #'오산시': 41370,
    #'용인시': 41460,
    '의왕시': 41430,
    #'의정부시': 41150,
    '이천시': 41500,
    #'파주시': 41480,
    '평택시': 41220,
    #'포천시': 41650,
    '하남시': 41450,
    #'화성시': 41590,
}

url = 'https://openapi.gg.go.kr/RegionMnyFacltStus'

params = {
    "Key": LOCAL_KEY,
    "Type": "json",
    "pSize": 100,
}


def getLocalStore(localName, page=44):
    params["SIGUN_CD"] = local_code[localName]
    params['pIndex'] = page
    result = requests.get(
        url=url,
        params=params
    )

    return result.json()


if __name__ == '__main__':
    print(getLocalStore('평택시'))