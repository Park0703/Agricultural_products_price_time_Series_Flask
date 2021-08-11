from flask import Flask, g, Response, make_response, request
from datetime import date, datetime

app = Flask(__name__)
app.debug = True

def ymd(fmt) :
    def trans(date_str) :
        return datetime.strptime(date_str, fmt)
    return trans

@app.route("/dt") # response
def dt() :
    datestr = request.values.get('date', date.today(), type = ymd('%Y-%m-%d'))
    return "우리나라 시간 형식 " + str(datestr)

# app.config['SERVER_NAME'] = 'local.com:5000'

@app.route("/sd")
def helloworld_local() :
    
    return "hello local.com"

@app.route("/sd", subdomain = "g")
def helloworld() :
    return "hello g.local.com"

@app.route("/rp")
def rp() :
    # q = request.args.gets('q') # 똑같은 parameter 처리할 때
    q = request.args.getlist('q') # 라우터를 좀더 가변적으로 해줌, parameters
    # get은 args, post 는 form
    return "q=%s"%str(q) # 

# @app.before_request # 라우터기능
# def before_request() :
#     print("before_request!")
#     g.str = "한글" # 접속자수 등 처리할 때





# 띄우는 창 # response, 모델기능
@app.route("/gg") # response
def helloworld2() :
    return "hello Flask world" + getattr(g, "str", "111")
  
@app.route("/res1")
def res1() :
    custom_res = Response("Custom Response", 201, {"test":"ttt"})# 헤더
    return make_response(custom_res) # 응답으로 내려보넨다 : 큰데이터를 내려보낼때 이걸로해야 안정적임

@app.route("/test_wsgi") # 값보내기
def wsgi_test() :
    def application(environ, start_response) :
        body = 'The request method was %s'%environ['REQUEST_METHOD']
        headers = [ ('Content-Type', 'test/plain'), # 
                    ('Content-Length', str(len(body)))]
        start_response('200 OK', headers)
        return [ body ]
    return make_response(application)

# Request URL: http://192.168.75.85:5000/res1
# Request Method: GET
# Status Code: 201 CREATED
# Remote Address: 192.168.75.85:5000
# Referrer Policy: strict-origin-when-cross-origin




# 구동되는 환경
# from helloflask import app
# app.run()