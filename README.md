# local_store
 - ### Description
    경기도 지역화폐 가맹점을 검색하기 위한 open API 서비스 입니다.

 - ### URL
    ```
    GET http://localhost:8080/store/<local>/<query>/<page>
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
        |local|가평군, 경기도, 고양시, 과천시, 광명시, 광주시, 구리시, 군포시,</br> 김포시, 남양주시, 동두천시, 부천시, 성남시, 수원시, 시흥시, 안산시,</br> 안성시, 안양시, 양주시, 양평군, 여주시, 연천군, 오산시, 용인시,</br> 의왕시, 의정부시, 이천시, 파주시, 평택시, 포천시, 하남시, 화성시|
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
            "result": "success",
            "items": [
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
                    "LOGT": "127.1002153"
                }
            ]
         }
        ```

        
# Pakage
 - Flask
 - Flask_RESTful
 - Flask_WTF
 - Requests

# ToDo
1. api 구현
    - 이름 비교 기능 [ O ]
    - 속도 개선 [ ]
    - 오류 처리
        - 네이버 검색 결과 없을 때 예외처리 [ ]
        - 오류 코드 알려주기 [ O ]

2. api 요청 페이지 [ O ]
    - 오류 표시 [ O ]
    - 결과 표시 꾸미기 [ ]

3. api 활용 페이지 [ O ]

4. 깃허브 [ O ]

5. api 설명 페이지 [ O ]
    - description 보충(사용한 api들, 개선 사항 등등) [ ]

6. AWS 배포 [ ]

7. 보고서 [ ]

8. PPT [ ]