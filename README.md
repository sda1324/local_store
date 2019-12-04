# Readme
 - ### 요청
    - #### 요청 변수
    
        |요청 변수명|타입|설명|
        |---|:---:|---|
        |지역명|string|검색할 도시명(평택시)|
        |쿼리|string|검색어|
        |페이지|int|검색 결과 중 요청할 페이지|
        
    - #### 도메인
        
        |요청 변수명|도메인|
        |------|---|
        |지역명|가평군, 경기도, 고양시, 과천시, 광명시, 광주시, 구리시, 군포시,</br> 김포시, 남양주시, 동두천시, 부천시, 성남시, 수원시, 시흥시, 안산시,</br> 안성시, 안양시, 양주시, 양평군, 여주시, 연천군, 오산시, 용인시,</br> 의왕시, 의정부시, 이천시, 파주시, 평택시, 포천시, 하남시, 화성시|
        |쿼리|제한 없음(ex : 곱창)|
        |페이지|제한 없음|

    - #### 요청 예시
      ```
      http://localhost:8080/store/평택시/폐계닭/1
      ```

 - ### 응답
    - #### 출력 변수
    
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
    
    - 출력 예시
 - ### 응답 코드
    - 400 error
    - 404 error
    - 500 error

# Pakage
 - Flask
 - Flask_RESTful
 - Flask_Markdown
 - Flask_WTF
 - Requests

# ToDo
1. api 구현
    - 이름 비교 기능 [ O ]
    - 속도 개선
    - 오류 처리
        - 네이버 검색 결과 없을 때 예외처리
        - 오류 코드 알려주기

2. api 요청 페이지 [ O ]

3. api 활용 페이지 [ ]

4. 깃허브 [ O ]

5. AWS 배포 [ ]

6. api 설명 페이지 [ ]

7. 보고서 [ ]

8. PPT [ ]

9. ss