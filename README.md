# local_store
 - ### Description
    경기도 지역화폐 가맹점을 검색하기 위한 open API 서비스 입니다. 기존 경기데이터드림의 지역화폐 가맹점 현황 API와 네이버의 지역 검색 API를 활용하여 서비스를 제공합니다. 기존 지역화폐 API나 이를 이용한 어플리케이션의 검색기능이 부족하다고 생각하여 네이버 지역 검색 API를 더하였습니다. 이를 통해 더 나은 지역화폐 가맹점 검색 서비스를 제공합니다.

 - ### URL
    ```
    GET http://localhost:8080/store/{local}/{query}/{page}
    ```

 - ### 요청
    - ### 요청 변수 
        |요청 변수명|타입|설명|
        |---|:---:|---|
        |local|string|검색할 도시명(평택시)|
        |query|string|검색어|
        |page|int|검색 결과 중 요청할 페이지|

    - ### 도메인
        |요청 변수명|도메인|
        |------|---|
        |local|가평군, 과천시, 광명시, 광주시, 김포시, 동두천시,</br>부천시, 성남시, 시흥시, 안산시, 안양시, 양주시,</br>여주시, 의왕시, 이천시, 평택시, 하남시|
        |query|제한 없음(ex : 곱창)|
        |page|제한 없음|

    - ### 요청 예시
        ```
        http://localhost:8080/store/평택시/폐계닭/1
        ```

 - ### 응답
    - ### 출력 포맷
        ```
        json
        ```
      
    - ### 출력 변수
        |요청 변수명|타입|설명|
        |---|:---:|---|
        |title|string|가맹점 이름|
        |phone|string|전화번호|
        |link|string|가게 링크|
        |local|string|지역명|
        |address|string|지번 주소|
        |readAddress|string|도로명 주소|
        |category|string|가맹점 분류|
        |description|string|설명|
        |LAT|double|위도|
        |LOGT|double|경도|    
    
    - ### 응답 코드
       |HTTP 코드|설명|조치방안|
       |---|---|:---:|
       |200|성공|-|
       |400|파라미터 오류|요청 변수 값이 정상 범위인지 확인|
       |404|존재하지 않는 api|api 대상에 오타가 없는지 확인|
       |500|시스템 에러|서버 내부 에러 발생, 관리자에게 문의|        
        
    - ### 출력 예시
        ```json
        {
            "result": 200, 
            "items": [
                {
                    "title": "소문난폐계닭", 
                    "phone": "", 
                    "link": "", 
                    "local": "평택시", 
                    "address": "경기도 평택시 비전동 871-11", 
                    "roadAddress": "경기도 평택시 문화촌로11번길 7-14", 
                    "category": "한식>닭요리", 
                    "description": "", 
                    "LAT": "36.9968805", 
                    "LOGT": "127.1131973"
                }, 
                {
                    "title": "구군계닭집", 
                    "phone": "031-652-8394", 
                    "link": "http://cityfood.co.kr/h1/gugun", 
                    "local": "평택시", 
                    "address": "경기도 평택시 합정동 922-11", 
                    "roadAddress": "경기도 평택시 조개터로5번길 22-9", 
                    "category": "한식>닭요리", 
                    "description": "", 
                    "LAT": "36.9887899", 
                    "LOGT": "127.1002153"}
            ]
        }
        ```

        
# Pakage
 - Flask
 - Flask_RESTful
 - Flask_WTF
 - Requests
