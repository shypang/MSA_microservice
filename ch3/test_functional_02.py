# -*- coding: utf-8 -*-
import unittest 
import json 
import sys
sys.path.append('../ch2')

"""
예를 들어 API 일관성을 위해 5XX,4XX 에러가 발생했을 때의 에러 본문도 JSON으로 변환해서 돌려줘야한다.
다음코드는 /api 엔드포인트를 호출했을 때 json 형식의 500 에러를 제대로 받아오는지 test_raise()함수에서 검사한다. 또한 test_proper_404()테스트 함수는 
고의로 없는 페이지를 호출했을 때 404 에러를 제대로 반환하는지 검사한다. 
"""

_404 = "The requested URL was not found on the server. "\
 " If you entered the URL manually please check your "\
 "spelling and try again."

class TestApp(unittest.TestCase):
    def setUp(self):
        from flask_error import app as _app
        # app과 연동하기 위해 FlaskClient 인스턴스를 생성한다.
        self.app = _app.test_client()

    def test_raise(self):
        # /api를 호출하면 flask_error에서 고의로 에러를 발생시켜
        # json 형식의 500 에러 응답을 반환한다.
        hello = self.app.get('/api')
        if (sys.version_info > (3, 0)):
            body = json.loads(str(hello.data, 'utf8'))
        else:
            body = json.loads(str(hello.data).encode("utf8"))
        self.assertEqual(body['code'], 500)

    def test_proper_404(self):
        # 고의로 존재하지 않는 엔드포인트를 호출한다.
        hello = self.app.get('/dwdwqqwdwqd')

        # 존재하지 않는 엔드 포인트이므로 상태 코드는 404이어야 한다.
        self.assertEqual(hello.status_code, 404)

        # 또한, 에러 내용도 JSON 형식으로 받아온다.

        if (sys.version_info > (3, 0)):
            body = json.loads(str(hello.data, 'utf8'))
        else:
            body = json.loads(str(hello.data).encode("utf8"))
        self.assertEqual(body['code'], 404)
        self.assertEqual(body['message'], '404 Not Found')
        self.assertEqual(body['description'], _404)


if __name__ == '__main__':
    unittest.main()