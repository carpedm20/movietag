![alt_tag](http://4.bp.blogspot.com/-bA0dalRit_A/U5BkjF2lOTI/AAAAAAAAD2Y/makxPjOGN2I/s1600/logo_red.png)

MovieTag
-------------

Find a movie with any tag you want!

Documentation
-------------

The documentation is available at ???


Developement Histroy
--------------------

1. 영화를 태그로 검색하는 서비스를 만들기로 계획
 - steam의 게임 태그 라는 새로운 기능을 보게됨
 - 빅데이터(블로그 글)를 이용해 음식점을 추천해 주는 다이닝코드 를 보게됨
 - 로멘스 처럼 거대한 카테고라기 아닌 첫사랑, 이별 과 같은 keyword로 영화를 찾고 싶음
2. 영화 리뷰 파싱
 - json 파일로 저장
 - json 에서 tag를 {"text": "첫사랑", "freq": 1} 로 저장했으나, 쿼리 낭비를 막기 위해 {"첫사랑": 1} 로 구조 변환
3. 형태소 분석
 - 처음에는 lucene-korean-analyzer를 사용
 - 용언, 체언을 구분 못하고, 초기 버전에는 단어의 frequency를 알 방법이 없는 단점이 있음
 - 다음으로 사용한 opensource는 mecab-ko 와 mecab-ko-dic
 - 용언, 체언을 세세하게 분류한 결과가 나오는 등의 장점
4. DB 구축
 - 처음에는 django 프로젝트와 연동을 위해 python 코드로 sqlite 에 집어 넣음
 - DB에 import 하는 속도(file-io)가 너무 느림 & file-io에 lock이 걸려 멀티프로세스를 만들 수 없음 (6일 정도 소요 될 거라 예상)
 - mysql 로 DB 변경
 - 넣는 속도가 sqlite 보다 월등히 빠르며, 멀티 프로세스로 돌려도 lock 처리를 mysql이 알아서 해주는 장점 (1~2일 소요)
 - 하지만 특정 tag에 대한 영화들을 tag의 frequency로 정렬하는 속도가 느림.
 - 파싱 결과가 json이라는 것에 착안해 mongodb를 사용
 - mongoimport를 이용해 몇 초만에 db에 들어감 (json파일이 너무 커서 오류 발생. 그래서 작게 잘라 넣었음)
5. Web 구축
 - Django webframework 사용 (이번 기회에 mean stack을 공부하려고 했으나... 빠른 개발을 위해 포기)
 - jquery, bootstrap, bootstrap-twipsy, d3, flat-ui, jquery-masonry, jquery-imagesloaded 등 이용
 - 태그 검색 기능 완성
 * infinite scroll 기능 개발 중...
6. 긍정 부정 리뷰
 - 파싱한 리뷰 데이터를 이용해 리뷰의 긍정, 부정을 deep-learning 을 이용해 분석할 계획
 - 먼저 리뷰를 형태소 분석을 통해서 명사, 형용사 리스트를 만듦
 - 리뷰에 어떤 형용사와 명사가 사용되었는지를 바탕으로 learning 시작
 - learning시 label은 리뷰의 별점 및 영화의 평균 별점이 사용될 예정



Screenshot
----------

![alt_tag](http://3.bp.blogspot.com/-xJ26vfyGTkE/U5BkjcRsyFI/AAAAAAAAD2c/dRWxviq7H8E/s1600/screenshot.png)

![alt_tag](http://1.bp.blogspot.com/-SWuaT4ztYsI/U5BlnJRslUI/AAAAAAAAD2w/obLLeYKJ0w8/s1600/screenshot2.png)

![alt_tag](http://2.bp.blogspot.com/-quHw9iA83wc/U5Bmxh_L7JI/AAAAAAAAD24/sSIA-25Gux4/s1600/screenshot3.png)

Copyright
---------

Copyright © 2014 Kim Tae Hoon.

The MIT License (MIT)
