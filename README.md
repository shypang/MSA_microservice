# MSA_microservice
# 파이썬 마이크로 서비스 스터디

## microservice는 마이크로서비스 기본 구조
일반적인 어플리케이션이며, 순환구조를 구현해서, 마이크로서비스개발의 시작점으로 사용가능

## Flakon은 또 다른 샘플프로젝트를 사용함
Flakon은 INI와 JSON을 사용해서 플라스크 애플리케이션의 구성과 초기화를 담당함


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

import os
from flakon import create_app
from myservice.views import blueprints

_HERE = os.path.dirname(__file__)
_SETTINGS = os.path.join(_HERE, 'settings.ini')

app = create_app(blueprints=blueprints,settings=_SETTINGS)

****

home.py 뷰는 Flakon의 JsonBlueprint 클래스를 사용한다. JsonBlueprint는 앞절에서
살펴봤던 에러 처리를 구현했다. 또한 Bottle프레임워크가 하는 것처럼 뷰가 반환하는 
객체가 딕셔너리라면 자동으로 jsonify()를 호출한다.

from flakon import JsonBlueprint
home = JsonBlueprint('home',__name__)

@home.route('/')
def index():
    """Home view.

    This view will return an empty JSON mapping
    """

    return {}

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



다음 코드는 SQLAlchemy 클래스를 사용한 User 테이블 정의의 일부다

```
***

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

***
* 뷰와 템플릿 

요청이 들어오면 뷰가 호출되고 Flask-SQLAlchemy가 애플리케이션 컨텍스트 안에 디비 세션 객체를 설정한다. 다음코드는 /users 엔드포인트가 호출됐을 때
뷰에서 User 테이블을 조회한다.


***

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


***




진자 템플릿은 다음과같은 템플릿을 이용해서 사용자정보를 표시하는 HTML페이지를 생성한다.

***

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




***


웹에서 데이터를 편집하려면 WTForms를 사용해서 각 모델에 대한 form을 생성할 수 있다. WTForms는 파이썬 정의를 사용해서 HTML 폼을 생성하는 라이브러리로 
요청에 포함된 데이터가 올바른 지 검증한 후에 모델을 변경하게 해준다.

CSRF(Cross-Site Request Forgery)토큰은 로그인할 때 악의적인 서드파티 웹사이트가 잘못된 폼을 앱에 보낼수 없게 한다. 



***


웹에서 데이터를 편집하려면 WTForms를 사용해서 각 모델에 대한 폼을 생성할 수 있다. WTForms는 파이썬 정의를 사용해서 HTML폼을 생성하는 라이브러리로,
요청에 포함된 데이터가 올바른 지 검증한 후에 모델을 변경하게 해준다.

Flask-WTF(https://flask-wtf.readthedocs.io)프로젝트는 플라스크에서 사용하기 위한 목적으로 만들어졌으며, CSRF 토큰을 이용하는 보안 폼처럼
몇 개의 유용한 통합이 추가됐다.

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


***

display속성은 폼이 렌더링될 때 템플릿이 정렬된 필드목록으로 반복되게 해준다. 그 외는 WTForms 기본 필드 클래스를 사용해서 user 테이블에 대한 폼을 생성한다. 

WTForms의 필드문서에서 전체 목록을 볼 수 있다

생성된 UserForm은 뷰에서 2개의 목적을 갖고 사용된다. 첫번째는 GET 요청시에 폼을 표시하는 것이고, 두 번째는 사용자가 POST 호출로 폼을 전송할 때 데이터베이스를 업데이트하는 것이다.

***

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


***

UserForm 클래스는 POST 데이터를 검증하기 위한 함수뿐만 아니라 값을 User 객체로 직렬화하는 함수도 갖고 있다. 
데이터가 올바르지 않으면 사용자에게 에러를 출력할 경우를 대비해서 폼 인스턴스가 field.errors에 에러 목록을 보관한다.

***

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


***

form.hidden_tag()함수는 CSRF 토큰처럼 모든 숨겨진 필드를 렌더링한다. 필요하다면 애플리케이션의 모든 폼에서 같은 패턴을 재사용하기도 쉽다. 

<dl> 요소는 설명 목록을 나타냅니다. <dl>은 <dt>로 표기한 용어와 <dd> 요소로 표기한 설명 그룹의 목록을 감싸서 설명 목록을 생성합니다. 주로 용어사전 구현이나 메타데이터(키-값 쌍 목록)를 표시할 때 사용합니다.



Runnerly에서는 훈련 계획과 대회 정보 추가를 위한 폼을 생성할 때 이 패턴을 재사용한다. 
템플릿은 제네릭한 특성이 있어서 Jinja 매크로를 사용해 모든 폼에서 사용할 수 있다.
대부분은 SQLAlchemy 모델 하나당 form 클래스 하나를 작성한다.

WTForms-Alchemy(https://wtforms-alchemy.readthedocs.io/en/latest/) 프로젝트를 사용하면 SQLAlchemy 모델에 기반을 둔 폼을 자동으로 만들 수 있다. 
앞에서 수동으로 UserForm을 만들었는데 WTForms-Alchemy를 활용하면 SQLAlchemy 모델만 지정하면 되므로 작업이 훨씬 단순해진다.

***
from wtforms_alchemy import ModelForm

class UserForm(ModelForm):
    class Meta:
        model=User

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

