# MSA_microservice
# 파이썬 마이크로 서비스 스터디
# (책에서 참고한 소스 : https://github.com/Runnerly)




## microservice는 마이크로서비스 기본 구조
* 일반적인 어플리케이션이며, 순환구조를 구현해서, 마이크로서비스개발의 시작점으로 사용가능







### micro service의 기본 구조는 다음과 같다.

* setup.py : Distuil의 설정 파일로 프로젝트를 설치하고, 릴리스하는 데 사용
* Makefile : 프로젝트를 만들고 빌드하고 실행하기 위해 필요한 명령을 포함
* setting.ini : 애플리케이션 기본 설정이 들어있는 INI파일
* requirement.txt : pip형식을 따르는 프로젝트 의존성이 들어있음
* myservice/:
    * __init__.py 
    * app.py : app모듈
    * views/: 블루프린트를 구성하는 뷰를 포함한 디렉토리
        * __init__.py
        * home.py 루트 엔드포인트를 처리하는 home 블루프린트
* tests : 모든 테스트를 포함하는 디렉토리
    * __init__.py
    * test_home.py : home 블루프린트 뷰를 위한 테스트

app.py파일의 다음 코드는 Flakon의 create_app 헬퍼를 사용해서 
플라스크 app을 초기화 한다. create_app은 등록하려는 블루프린트 목록 같은 몇 개의 옵션을 인수로 받는다.

****





```
import os
from flakon import create_app
from myservice.views import blueprints

_HERE = os.path.dirname(__file__)
_SETTINGS = os.path.join(_HERE, 'settings.ini')

app = create_app(blueprints=blueprints,settings=_SETTINGS)
```






****

home.py 뷰는 Flakon의 JsonBlueprint 클래스를 사용한다. JsonBlueprint는 앞절에서
살펴봤던 에러 처리를 구현했다. 또한 Bottle프레임워크가 하는 것처럼 뷰가 반환하는 
객체가 딕셔너리라면 자동으로 jsonify()를 호출한다.






```
from flakon import JsonBlueprint
home = JsonBlueprint('home',__name__)

@home.route('/')
def index():
    #Home view.
    #This view will return an empty JSON mapping
    

    return {}
```






이 애플리케이션은 패키지 이름을 사용해서 플라스크의 기본명령으로 실행가능
FLASK_APP=myservice flask run

이로써 마이크로서비스에 대한 JSON 뷰를 빌드하는 것은 microservice/view에 필요한 모듈을 추가하고 관련된 테스트를 만드는 것으로 구성함









****


플라스크 마이크로서비스 요약


1. 플라스크는 WSGI 프로토콜로 단순한 요청/응답 메커니즘을 감싸고 있다. 
이렇게 해서 거의 표준 라이브러리만 사용해 애플리케이션을 개발할 수 있게 한다.

2. 플라스크는 쉽게 확장가능
3. 플라스크는 블루프린트,전역,시그널,템플릿 엔진,에러 핸들러, 디버거 같은 기능제공
4. microservice 플라스크의 기본 구조를 구현한 프로젝트로 설정파일로 INI파일을 사용하며, JSON으로 응답객체를 생성해 반환하는 단순한 앱이다.


****






### 테스트
* 마이크로서비스에서는 다음과 같은 5개 테스트로 분류한다.

1. 단위 테스트(Unit Test): 격리된 환경에서 클래스나 함수가 예상대로 동작하는지 확인한다.
2. 기능 테스트(Functionall test): 마이크로서비스가 고객의 관점에서 기대한 대로 동작 하는지 살피고, 잘못된 요청에 대해서도 정확히 응답하는지 검증한다.
3. 통합 테스트(Integration test): 마이크로서비스가 다른 서비스와 제대로 연동되는지 확인한다.
4. 부하 테스트(Load test) : 마이크로서비스의 성능을 측정한다.
5. 엔드 투 엔드 테스트 : 전체 시스템이 제대로 동작하는지 확인한다.

 





####  통합테스트
통합테스트는 실제 환경에서 실행한다.
통합테스트는 보통 개발이나 스테이징 환경에서 실행한다. 











#### 부하테스트
부하테스트의 목적은 트래픽이 증가된 상황에서 서비스의 병목 현상을 파악하고 조기 최적화(premature optimization)가 아닌 앞으로의 계획을 세우는 데 있다.
부하테스트를 만들면 다음질문에 대한 답을 얻을 수 있다.

* 특정사양을 갖춘 머신에서 하나의 인스턴스는 얼마나 많은 사용자를 받아들 일 수 있는가?
* 10/100/1000개의 동시요청에 대한 평균 응답시간은 얼마인가?  더 많은 동시성을 처리할 수 있는가?
* 서비스에 부하가 걸린 상황일 때 RAM과 CPU 중 어느 것을 더 소비하는가?
* 해당 서비스의 인스턴스를 더 추가해서 수평으로 확장할 수 있는가?
* 다른 서비스를 호출할 때 커넥션 풀을 사용할 수 있는가?
* 서비스를 한번 실행하면 성능저하없이 며칠동안 실행될 수 있는가?
* 사용량이 최고점에 한 번 도달한 뒤에도 서비스가 올바르게 동작하는가?

RPS : request per second










#### 이번 절에서 배운 내용을 정리해보면 다음과 같다.

* 기능 테스트는 가장 중요한 테스트다. 플라스크에서는 테스트에 app의 인스턴스를 만들어 연동하는 방식으로 쉽게 만들 수 있다.
* 단위 테스트는 훌륭한 수단이지만 모방을 남용하지 않게 주의해야한다.
* 통합 테스트는 기능 테스트와 비슷하지만 , 실제 환경에서 돌려야한다.
* 부하 테스트는 마이크로서비스의 병목점을 파악해 다음 단계의 계획을 세우는 데 유용하다.
* 엔드 투 엔드 테스트는 클라이언트가 실제로 사용하는 UI와 동일한 것을 사용해야 한다. 




***










#### pytest와 Tox 사용

* pytest 사용전 설치필수 
* pytest 명령은 test_로 시작하거나 _test로 끝나는 모든 모듈에서 test_접두사가 붙은 함수를 실행한다.
설치 : pip install pytest
실행 : pytest


* pytest와 연결해서 사용할 수 있는 도구로 Tox가 있다.
* 프로젝트가 여러 버전의 파이썬 버전을 필요로 하거나 가장 최근의 파이썬2나 파이썬 3에서만 동작하게 하고 싶다면 Tox는 테스트실행을 위한 환경을 자동으로 생성해준다.
* pip install tox로 설치하고 프로젝트 루트에 tox.ini 설정파일을 만든다. 
* tox 명령을 실행하면 각 파이썬 버전으로 분리된 환경을 만들고 패키지와 의존 라이브러리를 배포한 후 pytest 명령으로 테스트를 실행하는  과정이 자동으로 진행된다.
* 단일환경에서 tox e로 테스트실행도 가능하다. 예를 들면 tox e py36 같은 명령이다.


설치 : pip install tox 







***









#### 개발자 문서

코드변경이 있을 때마다  문서 역시 변경돼야 한다.
문서화에 관한것은 다음과 같다.

* 어떻게 설계 됐는가?
* 어떻게 설치 하는가?
* 어떻게 테스트를 실행하는가?
* 사용 가능한 API에는 어떤 것들이 있고, 입/출력 데이터는 무엇인가?

* 파이썬 문서화를 위해 조그 브랜드(Georg Brandl)이 개발한 스핑크스(Sphinx)는 파이썬 커뮤니티에서 표준처럼 사용되고 있다.


* 스핑크스, tox 내용 정리
* 스핑크스는 뛰어난 기능을 제공하는  프로젝트 문서화 도구다.
* 문서를 소스코드처럼 다루면 관리하기 쉽다.
* 변경이 발생했을 떄 Tox를 사용해서 문서를 다시 생성할 수 있다.
* 문서에 코드를 직접 쓰지 않고, 소스에서 코드를 자동으로 읽어오게 하면 항상 최신버전의 문서를 유지할 수 있다.







#### 샘플 Runnerly 설계

ch4에서 다루는 내용은 다음과 같다.

* Runnerly 앱과 사용자 스토리 소개
* 모놀리식 Runnerly 개발
* 모놀리식 Runnerly를 마이크로 서비스로 분리

* Runnerly 앱은 마라톤과 조깅등 달리기를 좋아하는 사람들을 위한 앱이고 샘플 프로젝트임
* 사용자스토리 : 
* 사용자는 이메일로 Runnerly 계정을 만들수 있음
* 사용자는 Runnerly에 접속해서 사용자 프로필을 스트라바 계정에 연결함
* 접속한 사용자는 지난 10회 달리기 기록을 대시보드에서 볼 수 있음
* 접속한 사용자는 참여하고 싶은 대회 추가가능, 다른사용자도 해당대회를 대시보드에서 볼 수 있음
* 등록된 사용자는 이메일로 월간 보고서를 받는다. 이 보고서는 한달간 운동을 어떻게 했는지 보여준다.
* 접속한 사용자는 대회를 위해 훈련계획을 선택할 수 있고, 대시보드에서 훈련계획을 볼 수 있음










위의 사용자스토리에서 컴포넌트를 뽑으면 다음과 같음

* 앱은 사용자를 데이터 베이스에 추가하고, 등록시에 사용된 이메일이 사용자 소유가 맞는지 검증하는 방법이 필요
* 앱은 패스워드로 사용자를 인증한다.
* 스트라바에서 데이터를 사져오기 위해 사용자 프로필에 스트라바 토큰을 저장한다.
* 달리기 외에 대회와 훈련계획을 데이터베이스에 저장한다.
* 훈련계획은 대회에서 좋은 성적을 거두기 위해 특정 기간동안 연습할 달리기 목록이다. 훈련계획을 충실히 세우기 위해 나이,성별,체중,건강수준같은 사용자 정보가 필요함
* 월간보고서는 디비를 조회하고 요약본을 생성해서 이메일로 전송한다. 





***



* 모놀리식 설계

* 모델(Model) : 데이터를 관리한다.
* 뷰(View) : 모델을 웹,PDF 등 , 특정 방법으로 출력한다.
* 컨트롤러(Controller) : 모델을 조정해서 상태를 변경한다.







* 모델

SQLAlchemy를 사용하는 플라스크 앱에서는 디비 스키마를 나타내는 클래스가 모델 역활을 한다.
Runnerly의 디비 테이틀은 다음과 같다.

User : 자격증명(Credentials)을 비롯한 사용자 정보
Run  : 스트라바에서 가져온 달리기 기록과 훈련 계획의 달리기 목록
Race : 사용자가 추가한 대회 목록으로 날짜, 장소, 거리가 포함됨
Plan : 연습일정을 모아둔 훈련 계획








***


다음 코드는 SQLAlchemy 클래스를 사용한 User 테이블 정의의 일부다


```

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    email = db.Column(db.Unicode(128), nullable=False)
    firstname = db.Column(db.Unicode(128))
    lastname = db.Column(db.Unicode(128))
    password = db.Column(db.Unicode(128))
    strava_token = db.Column(db.String(128))
    age = db.Column(db.Integer)
    weight=db.Column(db.Numeric(4,1))
    max_hr=db.Column(db.Integer)
    rest_hr=db.Column(db.Integer)
    vo2max=db.Column(db.Numeric(4,2))

```





* 뷰와 템플릿 

요청이 들어오면 뷰가 호출되고 Flask-SQLAlchemy가 애플리케이션 컨텍스트 안에 디비 세션 객체를 설정한다. 다음코드는 /users 엔드포인트가 호출됐을 때
뷰에서 User 테이블을 조회한다.






```

from flask import Flask, render_template

app=Flask(__name__)

@users.route('/users')
def _users():
    #db.session.query 함수 호출시 디비에서 쿼리를 수행하고 User테이블의 모든 결과가 users 객체에 저장된다.
    # 이 객체는 렌더링을 위해 users.html jinja 템플릿에 전달된다.
    users=db.session.query(User)

    return render_template("users.html",users=users)

if __name__ == '__main__':
    db.init_app(app)
    db.create_all(app=app)
    app.run()


```





진자 템플릿은 다음과같은 템플릿을 이용해서 사용자정보를 표시하는 HTML페이지를 생성한다.

```

<html>
    <body>
        <h1> User List</h1>
        <ul> 
            {% for user in users: %}
            <li>
                {{user.firstname}} {{user.lastname}}
            </li>
        </ul>
    </body>
</html>




```


*** 

웹에서 데이터를 편집하려면 WTForms를 사용해서 각 모델에 대한 form을 생성할 수 있다. WTForms는 파이썬 정의를 사용해서 HTML 폼을 생성하는 라이브러리로 
요청에 포함된 데이터가 올바른 지 검증한 후에 모델을 변경하게 해준다.

CSRF(Cross-Site Request Forgery)토큰은 로그인할 때 악의적인 서드파티 웹사이트가 잘못된 폼을 앱에 보낼수 없게 한다. 



***


웹에서 데이터를 편집하려면 WTForms를 사용해서 각 모델에 대한 폼을 생성할 수 있다. WTForms는 파이썬 정의를 사용해서 HTML폼을 생성하는 라이브러리로,
요청에 포함된 데이터가 올바른 지 검증한 후에 모델을 변경하게 해준다.

Flask-WTF(https://flask-wtf.readthedocs.io)프로젝트는 플라스크에서 사용하기 위한 목적으로 만들어졌으며, CSRF 토큰을 이용하는 보안 폼처럼
몇 개의 유용한 통합이 추가됐다.



***

```
from flask_wtf import 
import wtforms as f
from wtforms.validators import DataRequired

class UserForm(FlaskForm):
    email = f.StringField('email', validators=[DataRequired()])
    firstname = f.StringField('firstname')
    lastname = f.StringField('lastname)
    password = f.PasswordField('password')
    age=f.IntegerField('age')
    weight=f.FloatField('weight')
    max_hr=f.IntegerField('max_hr')
    rest_hr=f.IntegerField('rest_hr')
    vo2max=f.FloatField('vo2max')

    display=['email', 'firstname' , 'lastname', 'password','age','weight','max_hr','rest_hr','vo2max']

```
***

display속성은 폼이 렌더링될 때 템플릿이 정렬된 필드목록으로 반복되게 해준다. 그 외는 WTForms 기본 필드 클래스를 사용해서 user 테이블에 대한 폼을 생성한다. 

WTForms의 필드문서에서 전체 목록을 볼 수 있다

생성된 UserForm은 뷰에서 2개의 목적을 갖고 사용된다. 첫번째는 GET 요청시에 폼을 표시하는 것이고, 두 번째는 사용자가 POST 호출로 폼을 전송할 때 데이터베이스를 업데이트하는 것이다.

***
```
@users.route('/create_user', methods=['GET','POST'])
@admin_required
def create_user():
    form = UserForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            new_user=User()
            form.populate_obj(new_user)
            db.session.add(new_user)
            db.session.commit()
            return redirect('/users')
    return render_template('create_user.html',form=form)

```
***

UserForm 클래스는 POST 데이터를 검증하기 위한 함수뿐만 아니라 값을 User 객체로 직렬화하는 함수도 갖고 있다. 
데이터가 올바르지 않으면 사용자에게 에러를 출력할 경우를 대비해서 폼 인스턴스가 field.errors에 에러 목록을 보관한다.

***
```
<html>
    <body>
        <form action="" method="POST">
            {{ form.hidden_tag() }}
                <dl>
                    {% for field in form.display %}
                        <dt>{{ form[field].label }}</dt>
                        <dd>{{ form[field]() }}</dd>
                        {% if form[field].errors %}
                            {% for e in form[field].errors %}
                                <p class="help-block">{{ e }}</p>
                            {% endfor %}
                        {% endif %}
                    {% endfor %}
                </dl>
                <p>
                <input type=submit value="Publish">
        </form>
    </body>
</html>
```

***
```
form.hidden_tag()함수는 CSRF 토큰처럼 모든 숨겨진 필드를 렌더링한다. 필요하다면 애플리케이션의 모든 폼에서 같은 패턴을 재사용하기도 쉽다. 

<dl> 요소는 설명 목록을 나타냅니다. <dl>은 <dt>로 표기한 용어와 <dd> 요소로 표기한 설명 그룹의 목록을 감싸서 설명 목록을 생성합니다. 주로 용어사전 구현이나 메타데이터(키-값 쌍 목록)를 표시할 때 사용합니다.
```



Runnerly에서는 훈련 계획과 대회 정보 추가를 위한 폼을 생성할 때 이 패턴을 재사용한다. 
템플릿은 제네릭한 특성이 있어서 Jinja 매크로를 사용해 모든 폼에서 사용할 수 있다.
대부분은 SQLAlchemy 모델 하나당 form 클래스 하나를 작성한다.

WTForms-Alchemy(https://wtforms-alchemy.readthedocs.io/en/latest/) 프로젝트를 사용하면 SQLAlchemy 모델에 기반을 둔 폼을 자동으로 만들 수 있다. 
앞에서 수동으로 UserForm을 만들었는데 WTForms-Alchemy를 활용하면 SQLAlchemy 모델만 지정하면 되므로 작업이 훨씬 단순해진다.

***
```
from wtforms_alchemy import ModelForm

class UserForm(ModelForm):
    class Meta:
        model=User
```
***

실제로는 폼을 수동으로 조정하는 과정이 종종 필요하지만, WTForms-Alchemy를 사용해서 작업을 시작하는 것은 좋은 방법이 될 수 있다.

현재까지 살펴본 내용을 요약하면 다음과 같다.

* SQLAlchemy를 사용해 데이터베이스 모델을 생성했다.(모델)
* 모델을 통해 데이터베이스와 상호작용하는 뷰와 폼을 생성했다. (뷰와 템플릿)

그러나 완전한 모놀리식 앱을 개발하는 데 필요한 두가지가 빠졌다.

* 백그라운드 작업 :  주기적으로 스트라바에서 결과를 얻고 월간 보고서를 생성
* 인증(Authentication) 및 허가(authorization):사용자의 로그인 처리 및 자신의 정보만 수정할 수 있게 제한



***

#### 백그라운드 작업

파이썬에서 백그라운드 작업을 처리하는 일반적인 방법은 분산 태스크 큐를 이용해 별도 프로세스에서 작업을 실행해주는 Celery를 사용하는 것이다.
이 때 메시지 브로커라고 부르는 중개자가 앱과 Celery간에 메시지를 주고받는 역활을 담당한다. 

예를 들면 앱이 Celery가 무언가를 실행해주기 바란다면 메시지를 브로커에 추가한다. Celery는 이를 폴링해서 작업을 처리한다.
메시지 브로커는 대표적으로 redis,RabbitMQ등이 있다.


 다음과 같은 코드를 참고하면 된다.

작업실행을 담당하는 부분을 워커라고 부르고 Celery 클래스를 통해 시작할 수 있다. 
플라스크앱에서 Celery를 사요하려면 다음과 같이 Celery 객체의 인스턴스를 만들고 @celery.task 데코레이터로 백그라운드 작업을 표시한다. 


***
```
from celery import Celery
from stravalib import Client
from monolith.database import db, User, Run

BACKEND = BROKER = 'redis://localhost:6379'
celery = Celery(__name__, backend=BACKEND, broker=BROKER)

_APP = None


@celery.task
def fetch_all_runs():
    global _APP
    # lazy init
    if _APP is None:
        from monolith.app import create_app
        app = create_app()
        db.init_app(app)
    else:
        app = _APP

    runs_fetched = {}

    with app.app_context():
        q = db.session.query(User)
        for user in q:
            if user.strava_token is None:
                continue
            print('Fetching Strava for %s' % user.email)
            runs_fetched[user.id] = fetch_runs(user)

    return runs_fetched


def activity2run(user, activity):
    """Used by fetch_runs to convert a strava run into a DB entry.
    """
    run = Run()
    run.runner = user
    run.strava_id = activity.id
    run.name = activity.name
    run.distance = activity.distance
    run.elapsed_time = activity.elapsed_time.total_seconds()
    run.average_speed = activity.average_speed
    run.average_heartrate = activity.average_heartrate
    run.total_elevation_gain = activity.total_elevation_gain
    run.start_date = activity.start_date
    return run


def fetch_runs(user):
    client = Client(access_token=user.strava_token)
    runs = 0

    for activity in client.get_activities(limit=10):
        if activity.type != 'Run':
            continue
        q = db.session.query(Run).filter(Run.strava_id == activity.id)
        run = q.first()

        if run is None:
            db.session.add(activity2run(user, activity))
            runs += 1

    db.session.commit()
    return runs
```
***

이 모듈은 레디스 브로커에서 작업을 가져오는 완전한 Celery 애플리케이션이다 pip install 명령으로 celery와 redis 파이썬 패키지를 설치한 후 celery worker -A background 명령과 함께
이 모듈을 실행할 수 있다. 결국 Celery 워커는 분리된 프로세스에서 레디스에 등록된 함수를 실행하게 된다. 

Celery 서비스는 플라스크 앱에 레디스에 메시지를 전달하면 실행되서 어떤 면에서는 그 자체를 마이크로서비스로 볼 수 있다. 또한 레디스 서버와
Celery를 다른 서버에서 실행할 수도 있다. 

백그라운드 워커를 실행하는 또 다른 이유는 주기적인 작업실행이 필요할 때다. 플라스크앱이 매 시간마다 작업을 실행하는 대신 Celery의 주기적 태스크기능을 사용할 수 있다.


스트라바 토큰
다음으로 필요한 작업은 각 사용자의 스트라바 토큰을 얻어 user테이블에 저장하는 것이다.
이는 OAuth2 댄스를 통해 이뤄짐. 연결된 사용자가 Runnerly 사용허가를 위해 스트라바로 리다이렉트되고 , 허가를 받으면 OAuth2 코드와 함께 다시 Runnerly로 리다이렉트 된다.
OAuth2 코드는 저장할 수 있는 토큰으로 변환가능하다.


stravalib 라이브러리는 이 과정을 처리하기 위해 몇가지 기능을 제공하는데 첫번째는 authorization_url()함수다. 이 함수는 OAuth2 처리를 시작하기 위해
사용자에게 표시되는 전체 URL을 반환한다.


***
```
app.config['STRAVA_CLIENT_ID'] = 'runnerly-strava-id'
app.config['STRAVA_CLIENT_SECRET'] = 'runnerly-strava-secret'

def get_strava_auth_url():
    client = Client()
    client_id = app.config['STRAVA_CLIENT_ID']
    redirect='http://127.0.0.1:5000/strava_auth'
    url=client.authorization_url(client_id=client_id, redirect_uri=redirect)
    
    return url


```
***

위 코드에서 "redirect"변수는  앱이 접근 권한을 받은 후 스타라바가 리다이렉트 하는 URL이다. 여기서는 앱이 로컬에서 실행된다.
get_strava_auth_url()함수는 연결된  Runnerly 사용자에게 링크를 표시하기 위해 사용한다.

사용자가 스트라바 사이트에서 Runnerly 사용을 허용하면 /strava_auth 뷰는 토큰과 교환할 수 있는 코드를 얻는다. 토큰은 앞으로 스트라바 요청시에 사용된다.
stravalib 라이브러리의 CLient 클래스는 변환을 위한 exchange_code_for_token() 함수를 제공한다.


뷰는 단순히 토큰을 user 디비에 복사한다.

***
```
@auth.route('/strava_auth')
@login_required
def _strava_auth():
    code = request.args.get('code')
    client = Client()
    xc = client.exchange_code_for_token 
    access_token = xc(client_id=auth.app.config['STRAVA_CLIENT_ID']
        client_secret=auth.app.config['STRAVA_CLIENT_SECRET'],code=code)
    current_user.strava_token=access_token
    db.session.add(current_user)
    db.session.commit()
    return redirect('/')
```
***

* 인증과 허가
모놀리식은 단순한 기본인증을 사용한다.
이 때는 사용자의 자격증명 Authorization헤더에 실어 보낸다.

패스워드에 관한 가장 단순한 보호방법은 패스워드를 저장할 때 원래패스워드로 되돌릴 수 없는 해시 형태로 저장하는 것이다.
이렇게 하면 서버가 손상되도 패스워드가 유출될 위험을 최소화할 수 있다.



일반적으로 전송계층은 앱의 보안약점이 아니다. 요청을 받은 뒤 서비스에서 발생하는 일이 가장 중요하다. 인증 처리과정중에는 공격자가 패스워드를 가로챌 수도 있다.

Werkzeug는 해시를 다루는 몇가지 유틸리티를 제공한다. 
User 클래스에 포함된 generate_password_hash()와 check_password_hash()가 그 중 하나다.


User 클래스에 패스워드를 설정하고 검증하는 함수를 추가하자.


***
```
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    __tablename__ = 'user'
    # ... all the Column


    def __init__(self, *args, **kw):
        super(User,self).__init__(*args, **kw)
        self._authenticated=False
    
    # set_password 함수는 새 사용자가 디비에 생성될 때 패스워드 해시값을 생성해서 User 모델에 저장한다. 
    def set_password(self,password):
        self.password = generate_password_hash(password)
    
    @property
    def is_authenticated(self):
        return self._authenticated
    
    #패스워드를 검증하기위한 모든 시도는 authenticate()를 통해 해시를 비교하게 된다.
    def authenticate(self,password):
        checked = check_password_hash(self.password,password)
        self._authenticated = checked
        return self._authenticated

```
***
Flask-Login은 현재 플라스크 세션에 사용자 정보를 설정하는 2개의 함수 login_user(), logout_user()를 제공한다. 
login_user()함수가 호출되면 플라스크 세션에 사용자 ID가 저장되고, 클라이언트 측에 쿠키가 설정된다. 사용자가 로그아웃하기 전까지는 다음 요청시에 
이 정보를 재사용할 수 있다.


이 매커니즘이 동작하려면 LoginManager 인스턴스가 애플리케이션 시작시에 만들어져야한다.

다음코드에 LoginManager 생성 및 로그인, 로그아웃 뷰 함수가 있다.
***
```
from flask_login import current_user, LoginManager

@auth.route('/login', methods=['GET','POST'])
def login():
     form=LoginForm()
     if form.validate_on_submit():
        email,password = form.data['email'], form.data['password']
        q=db.session.query(User).filter(User.email==email)
        user=q.first()
        if user is not None and user.authenticate(password):
            login_user(user)
            return redirect('/')
    return render_template('login.html',form=form)

@auth.route("/logout")
def logout():
    logout_user()
    return redirect('/')

login_manager = LoginManager()
login_manager.init_app(app)

#@login_manager.user_loader 데코레이트 함수는 Flask-Login이 저장된 사용자 ID를 실제 사용자 인스턴스로 변환할 때 사용한다.
@login_manager.user_loader
def load_user(user_id):
    user = User.query.get(user_id)
    if user is not None:
        user._authenticated = True
    return user

```
***
@login_manager.user_loader 데코레이트 함수는 Flask-Login이 저장된 사용자 ID를 실제 사용자 인스턴스로 변환할 때 사용한다.
인증처리는  로그인 뷰에서 user.authenticate()를 호출할 때 처리된다. 그런 다음 login_user(user_id)에서 세션에 저장된다.

@login_required 데코레이터는 로그인하지 않은 뷰에 대한 접근을 Unauthorized 에러와 함께 거부한다.


#### 모놀리식으로 함께 묶기

모놀리식은 훌륭한 방법이고 개발단계의 첫번째 목표가 될 수 있다. 그러나 TDD를 통해 진행해야한다.

앱을 만들기위해 다음과 같은 확장과 라이브러리를 사용한다.

Flask-SQLAlchemy와 SQLAlchemy: 모델을 위해 사용한다.
Flask-WTF와 WTForms : 모든 폼을 위해 사용한다.
Celery와 레디스 :백그라운드 처리와 주기적인 태스크를 위해 사용한다.
Flask-Login: 인증과 허가를 위해 사용한다. 






![구조](Runnerly_structure.png)









일반적으로  플라스크 애플리케이션을 하나의 레디스, 하나의 Celery 인스턴스와 함께 동일 서버에 배포하고 아파치나 nginx 같은 웹서버를 통해 요청을 처리한다.









### Runnerly 서비스 연동


* 서비스간의 연동은 동기,비동기 모두 필요하다.
* 5장에서 다룰 내용은 다음과 같다.


```
다른 서비스를 동기식으로 호출하는 효과적인 방법
다른 서비스를 비동기식으로 호출하는 방법과 이벤트를 통해 다른 서비스와 커뮤니케이션 하는 방법
네트워크 의존성이 있는 서비스를 테스트하는 방법
```


#### 동기식 호출

마이크로서비스 사이의 동기식 연동은 JSON 형식의 RESTful API를 통해 처리할 수 있다.
HTTP와 JSON은 표준처럼 굳어져있고 가장 많이 쓰는 패턴이다.

어떤 프로젝트는 REST API 대신 HTTP를 통한 원격 프로시저 호출(RPC , Remote Procedure Call)을 사용하기도 한다.
RPC에서는 엔드포인트 URL의 일부분인 액션에 중점을 둔다. , REST에서는 리소스에 초점을 두며, 액션은 HTTP 메소드로 정의된다.

HTTP 요청을 보내기 위해 HTTP 클라이언트를 사용한다. 파이썬의 http.client모듈이 있지만
대개의 경우 requests 라이브러리는 향상된 API와 기능을 기본으로 제공하기 때문에
requests 라이브러리로 클라이언트 작업을 쉽게 할 수 있다.


requests 라이브러리의 HTTP 요청은 세션 개념을 기반으로 만들어졌으며, 가장 사용하기 좋은 방법은 Session 객체를 만들고 다른 서비스와 연동시에 
이를 재사용하는 것이다.

Session 객체는 앱이 보내는 모든 요청에 공통적으로 설정해야하는 인증 정보와 기본 헤더 값을 갖고있다. 
예를 들어 다음 코드에서 Session 객체는 Content-Type 헤더와 인증 정보를 자동으로 생성한다.





* 커넥션 풀링
  
requests 라이브러리는 내부적으로 urllib3를 사용한다. urllib3는 호출하는 각 호스트당 하나의 커넥션 풀을 생성하고
해당 호스트를 다시 호출할 때 재사용한다. 따라서 여러분의 서비스가 다른 서비스를 여러 개 호출하더라도 커넥션의 재사용에 대해 
걱정할 필요는 없다. requests라이브러리가 알아서 처리해준다.

하지만 플라스크는 동기프레임워크이므로 싱글 스레드로 실행한다면 requests 라이브러리의 커넥션 풀링이 그리 도움되지 않는다.
하나의 요청이 완전히 처리된 이후에만 그 다음 요청이 처리되기 때문이다. 이런 상항에서 reuqest는 원격호스트당 오직 하나의 연결만 유지한다.

멀티스레드 환경에서 플라스크 앱이 실행되고 많은 커넥션이 맺어지면 커넥션 풀링은 다른 서비스에 대한 커넥션 수를 제어하는 데 중요한 역활을 한다.

HttpTimeoutAdapter 클래스를 커넥션 풀을 조정하는 데 사용할 수 있다. 이 클래스는 HTTPAdapter 클래스를  상속하는데 HTTPAdapter 생성자에서
urllib3 커넥션 풀 옵션을 조정할 수 있다.

HTTPAdapter 생성자에는 다음과 같은 옵션을 설정할 수 있다.

```

pool_connections : 커넥션 풀의 수로 기본값은 DEFAULT_POOLSIZE(10)이다.
pool_maxsize : 커넥션 풀에 저장되는 최댓값으로, 기본값은 DEFAULT_POOLSIZE(10)이다.
max_retries : 각 커넥션의 최대 재시도 횟수다.
pool_block : 커넥션 풀이 pool_maxsize에 도달 했을 때 동작 방식을 결정한다.
true로 설정하면 커넥션 풀이 가득 찼을 때 더 이상 연결을 생성하지 않고 대기한다.
false로 설정하면 커넥션 풀이 가득 찼더라도 새로운 연결을 생성한다. 이 옵션은 호스트에 대한 커넥션 수를 최대화하는데 유용함



```


예를 들어 다음코드에서 앱이 멀티스레드로 동작하면 25개의 동시커넥션을 처리할 수 있다.
```

adapter = HTTPTimeoutAdapter(max_retries=retries, timeout=timeout, pool_connections=25)


```
***

```
스레드는 하나, 프로세스는 여러개로  생성하는 방법이 좋다.
다른 서비스에 대한 호출속도를 높일 수 있는 한 가지 방법은 HTTP 캐시헤더를 사용하는것이다.

캐싱은 GET이나 HEAD처럼 모든 읽기 전용 엔드포인트를 를 호출할 때 적용함
캐싱을 구현하는 가장 단순한 방법은 응답에 ETag헤더를 보내주는 것

```

***

* 데이터 전송 효율 높이기

데이터 전송시에는 압축을 사용하거나, 바이너리 형식으로 변환해서 보내는 방법을 사용한다. 이렇게 하면 데이터 크기를 줄여서 처리시간을 향상시킬 수 있다.

GZIP 압축
대역폭을 줄이는 가장 단순한 방법은 GZIP 압축을 사용하는 것이다.
이렇게 하면 네트워크를 통해 전송되는 모든 정보가 더 작아진다.

다음과 같은 nginx 설정은 플라스크 앱이 5000번 포트에서 application/json 형식의 모든 응답에 대해 GZIP 압축을 사용한다.

http {

    gzip on;
    gzip_types application/json;
    gzip_proxied any;
    gzip_vary on;

    server{
        listen 80;
        server_name localhost;
        location / {
            proxy_pass http://localhost:5000;

        }
    }
}


바이너리 데이터
마이크로 서비스에서 많은 데이터를 처리해야 한다면 바이너리 데이터를 사용해서 네트워크 대역폭을 줄이고 성능도 향상시킬 수 있다.
주로 사용되는 2개의 바이너리 형식은 프로토콜 버퍼(protobuf)와 MessagePack이다.



* GZIP을 사용했을 때는 MessagePack과 JSON에 비해 약 15배나 더 크기가 줄어든다.


* 마이크로서비스에서 동기식 호출에 대해 배운 내용을 정리하면 다음과 같다.

 * 다른 서비스를 호출 하기위한 http 클라이언트로 request 라이브러리를 사용할 수 있다.
   이 라이브러리는 타임아웃, 에러 처리를 위한 기능과 커넥션 풀 등을 제공한다.
* 다른 서비스를 호출할 때 멀티 스레드를 사용하면 마이크로 서비스의 성능을 향상시킬 수 있지만 플라스크가 동기식 프레임워크이므로 위험 요소 또한
   존재한다. Gevent 같은 솔루션을 사용하는 방법도 있다.
* HTTP 캐시 헤더를 구현하면 동일한 데이터 요청시 속도가 향상된다.
* GZIP 압축은 요청과 응답 크기를 줄이는 효과적인 방법이며, 사용법도 단순하다.
* 바이너리 데이터는 JSON에 비해 매력적인 대안이지만 때에 따라서는 이득을 얻지 못할 수도 있다.
  



Celery가 작업 큐를 만들수 있지만 복잡한 메시지를 처리해야 한다면 RabbitMQ가 좋은 대안이 될 수 있다.
RabbitMQ 브로커 설치 : https://www.rabbitmq.com/download.html

RabbitMQ 브로커는 TCP 서버의 일종으로 내부에 큐를 관리하며, RPC호출을 통해 게시자에서 구독자로 메시지를 가져온다. 
Celery를 같이 사용할 수 있는건 RabbitMQ의 많은 기능중 하나다.

RabbitMQ는 AMQP(Advanced Message Queuing Protocol)을 구현했다.

AMQP는 queue, exchange, binding이라는 세 개의 개념으로 구성된다.

* queue는 메시지를 보관하고 소비자가 메시지를 선택하기를 기다린다.
* exchange는 게시자가 새 메시지를 추가하기 위한 진입점이다.
* binding은 메시지가 exchange에서 queue로 라우팅되는 방법을 정의한다.



* 비동기 관련해서 내용을 정리해보면 다음과 같다.

* 작업이 지연될 여지가 있는 경우 항상 비동기 호출을 사용해야 한다. 요청이 블록되는 경우는 최대한 피해야 한다.
* Celery를 사용해 백그라운드 작업을 처리하는 것은 좋은 방법이다.
* 서비스 간의 커뮤니케이션이 항상 태스크 큐를 제한하는 것은 아니다.
* 서비스 간 상호 의존성을 막으려면 이벤트를 활용하는 것이 좋다.
* rabbitMQ 같은 브로커를 사용하면 마이크로서비스가 메시지를 통해 서로 연동되는 완전한 이벤트 시스템을 만들 수 있다.
* Pika는 메시지를 게시하거나 가져올 때 사용할 수 있다.




다음예제에서 echo 태스크는 독립형 마이크로 서비스로 실행되며 
이름도 알고 있기 때문에 send_task()만 호출해서 실행할 수 있다. 코드를 임포트할 필요가 없으며, 모든 상호작용은 레디스를 통해 발생한다.
```
import celery
redis='redis://localhost:6379'
app=Celery(__name__, backend=redis, broker=redis)
f=app.send_task('echo',['meh'])
f.get()

>> 'meh'


```

* 서비스 연동 요약
5장에서 requests 라이브러리의 session을 사용해서 다른 서비스를 동기식으로 연동하는 방법 , 그리고 Celery 워커나 RabbitMQ를 기반으로 하는 향상된 메시지 패턴을 사용해서
비동기로 연동하는 방법을 알아봤음



* 6장 서비스 모니터링 요약 
6장에서 마이크로 서비스와 웹서버 계층에서 지표를 추가하는 방법을 살펴봤고, 마이크로 서비스에서 생성된  모든 로그와 성능 지표를 중앙 집중화
하기 위해 Graylog 사용방법도 다뤘다.
Graylog는 엘라스틱서치를 사용해서 데이터를 저장하기 때문에 업무능률을 향상시키는 뛰어난 검색기능을 제공한다. 


#### * 7장 서비스 보안

OAuth2 프로토콜로 사용자와 서비스 양쪽 모두를 인증하는데 사용할 수 있고, 마이크로서비스에 인증과 권한부여를 추가할 때 유연성을 제공한다.
이러한 인증 구현은 서비스간의 연동을 보호하는 데 목적이 있다.

서비스 보안을 통해 시스템 교란이나 남용을 막을 수 있다. 

7장에서 배울 내용을 정리하면 다음과 같다.

* OAuth2 프로토콜 개요
* 토큰 기반 인증의 동작 흐름
* JWT 표준을 이해하고 TokenDealer 마이크로 서비스에 적용
* 웹 애플리케이션 방화벽 구현 방법
* 마이크로서비스 보안 코드를 위한 몇 가지 모범 사례

##### * OAuth2 프로토콜

OAuth2는 웹 앱과 사용자, 웹앱 사이의 연동을 보호하기 위해 널리 채택된 표준이고, 꽤 복잡한 여러 개의 RFC(Request for Comments)를 기반으로 하기 때문에 완전히 이해하기 어려움
```
 RFC는 ARPANET 프로젝트 수행시 작성하는 일련의 문서들에 그 기원을 두고 있으며,
     - 사실상 인터넷 기술과 관련된 공식 문서의 성격을 띄고 있음
```

OAuth2의 핵심은 호출자(Caller)를 인증하는 역활의 중앙 서비스를 두고 , 이 중앙 서비스가 코드나 토큰 형태로 접근 권한을 부여하는 것이다. 
접근 권한이 부여된 코드나 토큰을 열쇠(Key)라고 하자. 사용자나 서비스는 열쇠를 사용해서 문을 열고 필요한 리소스에 접근함
물론 해당 리소스를 소유한 서비스는 그 열쇠가 맞는 열쇠인지 확인한 다음 문을 열어줌


![샘플구조](OAuth2_first.png)


4장의 스트라바 마이크로 서비스를 구현할때도 사용했다. 이 서비스는 스트라바의 인증 서비스로부터 접근 권한을 부여 받은 후 사용자를 대신해서
스트라바 API와 연동된다. 이 방식을 승인 코드 부여(Authorization Code Grant)라고 부르며, 가장 많이 사용되는 권한 부여 방식이다.
 사용자, 인증 서비스, 그리고 서드파티가 관여하므로 3자 (3-legged) O-Auth로 부르기도 한다. 스트라바는 자신들의 API를 호출하기 위해 필요한 코드를 생성해주고, 
 우리가 만들었던 스트라바 Celery 워커는 요청을 보낼 때 이 코드를 사용한다.


 위 구조에서 사용자는 샘플 APP에 접속하는데, 이 샘플 App은 필요한 정보를 얻기 위해 스트라바 서비스에 연결해야한다. 
* "1. 사용자가 샘플 App을 호출하면,"
* "2. 샘플 App이 스트라바 API 스트라바 API 접근 권한을 얻기 위해 사용자를 스트라바 서비스로 리다이렉트 한다. "
* "3. 사용자가 샘플 App이 스트라바 API를 사용할 수 있도록 승낙하면 샘플 App은 HTTP 콜백을 통해 승인 코드를 획득하고 스트라바 API를 사용할 수 있게 된다."
  
한편 마이크로 서비스에서는 사용자의 개입 없이 서비스와 서비스 사이의 인증이 필요한 경우도 있다. 이때는 클라이언트 자격증명 부여(CCG : Client Credentials Grant)라는
또 다른 권한 부여방식을 사용한다.


```
CCG (클라이언트 자격증명 부여 ) 참고 자료 : https://datatracker.ietf.org/doc/html/rfc6749#section-4.4
```

클라이언트 자격증명 방식이 승인 코드 방식과 구분되는 중요한 차이점은 특정 웹페이지로 리다이렉트하지 않는다는 점이다.
그 대신 토큰과 교환할 수 있는 비밀키와 함께 암시적으로 승인된다.

이 2개의 권한 부여방식을 사용하면 시스템의 인증 및 권한 부여와 관련된 모든 요소를 중앙에 모아 둘 수 있다.
따라서 마이크로서비스에 OAuth2를 적용하면 서비스를 인증하고, 서비스간의 연동 방식을 추적해 보안 이슈를 줄일 수 있는 좋은 해결책이 된다.


* 토큰 기반 인증

서비스가 사용자 개입없이 다른 서비스에 접근해야 한다면 클라이언트 자격증명 방식을 사용한다.

이 방식의 기본 개념은 마치 일반 사용자와 동일하게 서비스 역시 인증서비스에 연결해서 인증을 거친 후 다른 서비스를 호출할 때 필요한 토큰을 요청하는 것이다.

토큰은 비밀번호와 같은 개념으로 특정 리소스에 접근할 수 있다는 증명이다. 호출의 주체가  사용자인지, 서비스인지 상관없이 토큰을 소유하고 있으면 리소스에 접근이 가능하다.

인증이나 권한부여에 필요한 어떤 정보도 토큰에 포함될 수 있다.
이 정보들은 다음과 같다.

  * 사용자이름이나 ID
  *  토큰 소유자가 수행 가능한 작업의 범위, 이를테면 읽기,쓰기 등
  *  토큰이 발급된 타임스탬프(Timestamp)
  *  토큰의 유효시간을 알 수 있는 만료(expiration) 타임스탬프
 
토큰은 보통 서비스를 사용할 수 있다는 증명이 포함된 채 만들어진다.
여기서 "포함된 채" 라는 말은 토큰의 유효성을 검증하기 위해 외부 서비스를 호출할 필요가 없다는 뜻!
서비스 간의 종속성이 추가되지 않는 바람직한 방법이다.

구현에 따라 토큰은 다른 마이크로서비스에 연결하는데 사용되기도 한다.
OAuth2는 토큰에 JWT 표준을 사용한다.


* JWT 표준
JSON 웹 토큰을 지칭하는 말로 RFC7519에 설명된 표준이며, 토큰을 표현하는 데 자주 사용된다.

JWT는 3개의 점(.)으로 구분되는 길이가 긴 문자열이다.

* 헤더(Header) : 사용된 해시 알고리즘처럼 토큰과 관련된 정보를 제공한다.
* 페이로드(Payload) : 실제 데이터
* 서명(Signature) : 올바른 토큰인지 검사하기 위한 해시 값


JWT토큰은 base64로 인코딩 되므로 쿼리 문자열에 사용할 수 있다 다음은 인코딩된 형식의 JWT토큰이다.

```
eyJhbGci0iJIUzI1NiTsInR5cCI6IkpXVCJ9
.
eyJ1c2VyIjoidGFyZwsifQ
.
0eMWz6ahNsf-TKg8LQNdNMnFHNtReb0x3NMs0eY64WA



출력 목적으로 토큰을 3줄로 나눠서 표시했지만 , 실제 토큰은 한 줄로 표시한다. 
```




```
서명을 제외하면 JWT 토큰의 각 부분은 JSON 맵으로 이뤄졌다. 헤더는 보통 typ와 alg 키를 포함하는데, typ 키의 값으로 
JWT 토큰이란 걸 알 수 있으며, alg 키는 사용된 해시 알고리즘을 나타낸다.

페이로드는 필요한 어떤 내용도 포함할 수 있다. RFC7519에서는 정보의 각 필드를 JWT 클레임(Claim)이라고 부른다.

RFC는 등록된 클레임 이름(Registered Claim Name)이라고 부르는 , 토큰이 포함될 수 있는 클레임 항목을 미리 정의하고 있다.이들 중 일부를 정리하면 다음과 같다.

* iss: 토큰을 생성한 엔티티(entity)의 이름, 즉 토큰(발급자, issue)를 나타낸다. 보통 호스트 이름이기 때문에 클라이언트는 /.well-known/jwks.json을 요청해서 공개 키를 알아낼 수 있다.
* exp: 토큰 만료 시간(Expiration Time)을 의미한다.
* nbt: 토큰이 유효해지는 시간(Not Before Time)을 나타낸다.
* aud: 토큰이 누구에게 발급됐는지, 수신자(Audience)를 나타낸다. 
* iat: 토큰이 언제 발급 됐는지(Issued At)를 나타낸다.

다음의 예제 페이로드에는 몇 개의 타임스탬프와 함께 사용자 정의 클레임인 user_id가 들어있다.
이 토큰은 2018년 2월 6일 화요일 오후 6:20:15부터 24시간 동안 사용가능하다.

{

    "iss" : "https://tokendealer.example.com",
    "aud" : "runnerly.io",
    "iat" : 1517822415, // 2018년 2월 5일 월요일 오후 6:20:15
    "nbt" : 1517908815, // 2018년 2월 6일 화요일 오후 6:20:15
    "exp" : 1517995215, // 2018년 2월 7일 수요일 오후 6:20:15
    "user_id" : 1234
}

이와 같은 클레임은 토큰을 일정 시간만큼만 유효한 상태로 유지할 수 있도록 하는 유연성을 제공한다.

마이크로 서비스의 성격에 따라 토큰의 TTL(Time To Live)를 매우짧게, 또는 무한하게 할 수 있다.
예를 들면 마이크로 서비스가 시스템 내의 다른 서비스와 연동된다면 매번 토큰을 생성할 필요 없이
일정 시간 동안 유지되도록 토큰을 만드는 것이 좋다.

반면에 토큰이 시스템 바깥의 여러 곳에 분산된다면 가능한 한 짧은 시간 동안만 유효하게 만드는 것이 좋다.

JWT 토큰의 마지막 부분은 서명이다. 서명은 헤더와 페이로드의 서명된 해시를 포함한다.
서명과 해시에는 여러 개의 알고리즘이 사용된다. 일부는 비밀 키를 기반으로 하며 일부는 공개 키와 비밀 키 쌍을  기반으로 한다.


```




* TokenDealer 사용
  
  다음 구조에서 데이터 서비스와 스트라바 워커가 연결되는 3은 인증이 필요하다. 데이터 서비스에 데이터를 추가하는 작업은
  권한이 부여된 서비스만 가능하게 통제해야 된다.

![구조](TokenDealer.png)


* 웹어플리케이션 방화벽
* 오픈 웹 애플리케이션보안프로젝트(OWASP) - https://owasp.org/는 잘못된 동작으로부터 웹을 보호하는 방법을 배울 수 있는 참고자료
* 광범위한 공격을 피하는 데 사용할 수 있는 ModSecurity(https://github.com/coreruleset)


마이크로 서비스 기반 앱은 웹에 게시된 모든 것이 공격받을 수 있다.
하지만 모놀리식 앱과 다르게 HTML 사용자 인터페이스나 공용API를 통해 사용자와 직접 연결하지 않으므로 잠재적 공격범위는 줄어든다.

일반적인 공격형태는 다음과 같다.

* SQL 주입(SQL Injection) : 공격자가 요청을 보내면서 , SQL쿼리문을 실어 보낸다.
    서버에서 요청 내용 중 일부(일반적으로 인수를 사용함)을 사용해서 SQL 쿼리를 만든다면 공격자가 보낸 쿼리가 실행된다. 
    파이썬에서는 SQLAlchemy를 사용해서 이런 리스크를 피할 수 있다.

* 크로스사이트 스크립팅(XSS , Cross Site Scripting) : 이 공격은 HTML을 표시하는 웹 페이지에서만 발생한다. 공격자는 페이지에 자신의 HTML 코드를 삽입하고,
  정상적인 웹사이트인 것처럼 사용자를 속여서 특정행동을 하도록 유도한다.

* 크로스사이트 요청 위조 (XSRF/CSRF, Cross-Site Request Forgery) : 이 공격은 또 다른 웹사이트에서 사용자의 자격증명을 재사용하는 방법으로 서비스를 공격한다.
  전형적인 CSRF 공격은 POST요청을 사용한다. 예를 들어 악성 웹사이트가 링크를 표시하고 사용자가 클릭하면 해당 사용자의 자격증명을 이용해 공격대상 웹 사이트로 POST 요청을 보낸다. 

많은 공격들이 PHP 기반 시스템을 대상으로 한다.  로컬파일 취약점(LFI : Local File Inclusion) , 원격 파일 취약점(RFI : Remote File Inclusion ), 원격 코드 실행(Remote Code Execution)은 모두 클라이언트 입력이나 서버 파일을 드러내는 식으로 서버를 속여서 의도한바를 실행함

올바른 요청도 대규모로 보내면 서버는 이 요청을 처리하는데 모든 리소스를 사용하고 결국 서비스 거부  DoS 상황이 발생함


* CORS
  클라이언트 자바스크립트가 다른 도메인에 AJAX 요청을 보내는 것은 잠재적인 보안위협이 된다. 클라이언트 페이지에서 실행된 자바스크립트 코드가, 소유하지 않은 다른
  도메인에 요청을 보내면 악성 자바스크립트 코드가 실행돼 사용자에게 피해를 입힐 수 있다.

  비동기 요청이 만들어질 때 동일한 도메인 내의 요청인지 확인하는 동일 원본 정책(Same-origin-policy)은 바로 이런 이유 떄문에 생겨났다.

  보안이외에도 다른 웹 앱이 여러분의 대역폭을 사용하지 못하게 막는 방법이기도 하다.

  다른 도메인과 리소스를 공유해야 할 필요가 있다면 규칙을 설정해서 해당 도메인이 리소스에 접근하게 할 수 있다. 이 개념이 바로 CORS(Cross-Origin-Resourece Sharing)이라고
  알려진 교차 원본 리소스 공유의 핵심이다.

  서비스에 AJAX 요청을 보낼 때 Origin 헤더를 추가하면 해당 서비스가 허가된 도메인 목록에 있는지 확인할 수 있다. 허가된 도메인이 아닌 경우 CORS 프로토콜은
  허가된 도메인 목록이 포함된 헤더를 다시 보낸다. CORS에는 또한 프리플라이트(preflight) 메커니즘이 있는데, 엔드포인트 호출 시에 OPTIONS를 사용해서 해당 호출의
  허가 여부를 미리 알아내는 것이다. 

