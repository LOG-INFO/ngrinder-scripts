from net.grinder.script import Test
from net.grinder.script.Grinder import grinder
from HTTPClient import NVPair

# 테스트 생성
test1 = Test(1, "HTTP GET request")

# 실행될 요청
request = HTTPRequest()
test1.record(request)

# 테스트 실행
class TestRunner:
    # 테스트 초기화
    def __init__(self):
        self.url = "http://localhost:8080/hello"  # 호출할 URL

    # 스크립트 실행 메소드
    def __call__(self):
        result = request.GET(self.url)
        # 요청 결과 확인
        if result.statusCode != 200:
            grinder.statistics.forLastTest.success = 0  # 요청이 실패한 경우
        else:
            grinder.statistics.forLastTest.success = 1  # 요청이 성공한 경우

# 테스트 인스턴스 생성
testRunner = TestRunner()
