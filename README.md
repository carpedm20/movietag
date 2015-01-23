MovieTag
-------------

![alt_tag](https://raw.githubusercontent.com/carpedm20/movietag/master/content/logo.png)

Find a movie to watch with any tags you want!

Tags are automatically generated with morpheme analysis of big data.

Percentage of positive and negative reviews will be given through deep learning.


Documentation
-------------

The documentation is available at ???


Development History
-------------------

1. Plan to make a web service which can search any movie with **tags**
 - saw a new feature **Game tag** from **steam**
 - saw a restaurant recommendation service "[Dining code](http://www.diningcode.com/)" using big data (reviews from blogs)
 - want to find a movie not with a category like **Romance** but with a tag like **first love**, **farewell** etc.
2. Movie review **parsing**
 - save data as **json**
3. **Morpheme** analysis
 - first, used [lucene-korean-analyzer](https://github.com/need4spd/lucene-Korean-Analyzer)
 - have a weakness that cannot distinguish **predicate** and **uninflected word** and hard to get **word frequencies** from reviews
 - next, used [mecab-ko](https://bitbucket.org/eunjeon/mecab-ko) and [mecab-ko-dic](https://bitbucket.org/eunjeon/mecab-ko-dic)
 - can get details from review like **predicate** and **uninflected word** information
D4. Build a DB
 - to connect with **django**, write a python code that import json data to **SQLite**
 - but too slow file-io and cannot write a multi-thread code because of file lock (estimated time to import all data was 6 days)
 - change DB to **MySQL**
 - faster file-io and possible to write a multi-thread code (1~2 days)
 - but sorting a movie with a specific tag was too slow
 - plan to use **Apache Cassandra**, but found that it has slower read than write from google.
 - data was json, so used **MongoDB**
 - data import was finished only in a few seconds with `mongoimport` (Assert failure on mongorestore (b.empty()) error occured because of huge json file. so split the data into small files)
 - DB querying speed was fater than **MySQL** (hooray~)
 - Conclusion : Text indexing of **MongoDB** make faster speed than raw query of **MySQL** + **Django**
5. Build a web
 - used **Django webframework**
 - Back-end : used Django, [South](http://south.aeracode.org/), [endless-pagination](https://github.com/frankban/django-endless-pagination) etc.
 - Front-end : used jQuery, Bootstrap, [Bootstrap-twipsy](http://okonski.org/twipsy-bootstrap/docs/javascript.html), [D3](http://d3js.org/), [Flat-UI](https://github.com/designmodo/Flat-UI), [jQuery-Masonry](http://desandro.github.io/masonry/), [imagesloaded](https://github.com/desandro/imagesloaded) etc.
 - complete **tag search** feature.
 * developing infinite scroll...
6. Positive & Negative review
 * with review data and using **Logistic regression** and **Deep learning**, plan to distinguish reviews into positive and negative review.
 * first, make an adjective and noun list by using morpheme analysis.
 * star point of review and movie will be used as a **label** in machine learning

Developement Histroy (Korean)
-----------------------------

1. 영화를 **태그**로 검색하는 서비스를 만들기로 계획
 - **steam**의 게임 태그 라는 새로운 기능을 보게됨
 - 빅데이터(블로그 글)를 이용해 음식점을 추천해 주는 [다이닝 코드](http://www.diningcode.com/) 를 보게됨
 - 로멘스처럼 거대한 카테고라기 아닌 **첫사랑**, **이별** 과 같은 keyword로 영화를 찾고 싶음
2. 영화 리뷰 **파싱**
 - json 파일로 저장
 - json 에서 tag를 {"text": "첫사랑", "freq": 1} 로 저장했으나, 쿼리 낭비를 막기 위해 {"첫사랑": 1} 로 구조 변환
3. **형태소** 분석
 - 처음에는 [lucene-korean-analyzer](https://github.com/need4spd/lucene-Korean-Analyzer)를 사용
 - 용언, 체언을 구분 못하고, 초기 버전에는 단어의 frequency를 알 방법이 없는 단점이 있음
 - 다음으로 사용한 opensource는 [mecab-ko](https://bitbucket.org/eunjeon/mecab-ko) 와 [mecab-ko-dic](https://bitbucket.org/eunjeon/mecab-ko-dic)
 - 용언, 체언을 세세하게 분류한 결과가 나오는 등의 장점
4. DB 구축
 - 처음에는 django 프로젝트와 연동을 위해 python 코드로 **SQLite** 에 집어 넣음
 - DB에 import 하는 속도(file-io)가 너무 느림 & file-io에 lock이 걸려 멀티쓰레드를만들 수 없음 (6일 정도 소요 될 거라 예상)
 - **MySQL** 로 DB 변경
 - 넣는 속도가 sqlite 보다 월등히 빠르며, 멀티쓰레드로 돌려도 lock 처리를 MySQL이 알아서 해주는 장점 (1~2일 소요)
 - 하지만 특정 tag에 대한 영화들을 tag의 frequency로 정렬하는 속도가 느림.
 - **Apache Cassandra** 를 사용하려 했으나 짧은 구글링으로 write보다 read가 느리다는 글을 보게됨. read가 월등히 많을것이기 때문에 탈락
 - 파싱 결과가 json이라는 것에 착안해 **MongoDB**를 사용
 - `mongoimport`를 이용해 몇 초만에 db에 들어감 (json파일이 너무 커서 Assert failure on mongorestore (b.empty()) 오류 발생. 그래서 작게 잘라 넣었음)
 - DB querying 속도가 월등히 빨라짐 (만세!)
 - 결론 : **MongoDB**의 Text indexing 기능 때문에 raw query가 **MySQL** + **Django** ORM 보다 훨씬 빠른것으로 보인다
5. Web 구축
 - **Django webframework** 사용 (이번 기회에 **MEAN** stack을 공부하려고 했으나... 빠른 개발을 위해 포기)
 - Back-end : Django, [South](http://south.aeracode.org/), [endless-pagination](https://github.com/frankban/django-endless-pagination) 등 사용
 - Front-end : jQuery, Bootstrap, [Bootstrap-twipsy](http://okonski.org/twipsy-bootstrap/docs/javascript.html), [D3](http://d3js.org/), [Flat-UI](https://github.com/designmodo/Flat-UI), [jQuery-Masonry](http://desandro.github.io/masonry/), [imagesloaded](https://github.com/desandro/imagesloaded) 등 사용
 - 태그 검색 기능 완성
 * infinite scroll 기능 개발 중...
6. 긍정 부정 리뷰
 * 파싱한 리뷰 데이터를 이용해 리뷰의 긍정, 부정을 먼저 단일 형용사, 명사와 자주 같이 등장하는 형용사, 명사 pair들을 이용해 **Logistic regression** 을 이용해 본 후에 **Deep learning** 을 이용해 분석할 계획
 * 먼저 리뷰를 형태소 분석을 통해서 명사, 형용사 리스트를 만듦
 * 리뷰에 어떤 형용사와 명사가 사용되었는지를 바탕으로 learning 시작
 * learning시 label은 리뷰의 별점 및 영화의 평균 별점이 사용될 예정



Screenshot
----------

![alt_tag](https://raw.githubusercontent.com/carpedm20/movietag/master/content/screenshot1.png)

![alt_tag](https://raw.githubusercontent.com/carpedm20/movietag/master/content/screenshot2.png)

![alt_tag](https://raw.githubusercontent.com/carpedm20/movietag/master/content/console1.png)

![alt_tag](https://raw.githubusercontent.com/carpedm20/movietag/master/content/console2.png)

Copyright
---------

Copyright © 2014 Kim Tae Hoon.

The MIT License (MIT)
