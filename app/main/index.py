# file name : index.py
# pwd : /project_name/app/main/index.py
 
from flask import Blueprint, request, render_template, flash, redirect, url_for
from flask import current_app as app
# 추가할 모듈이 있다면 추가

# index 파일이 들어갔을 때 어떻게 이름을 설정할지 결정하는 부분 
# url_prefix=  URL을 어떻게 뒤에 붙일지 결정하는 부분
main= Blueprint('main', __name__, url_prefix='/')
 
# 파일 내부에서 어떤 경로로 나타낼지 결정하는 부분
@main.route('/main', methods=['GET'])
# url_for에서 사용될 함수 이름 확인
def index():
      # /main/index.html은 사실 /project_name/app/templates/main/index.html을 가리킵니다.
      return render_template('/main/index.html')

# 이제 13번 라인에서 불려들일 template 파일 즉, HTML 파일을 작성해주어야 합니다.
