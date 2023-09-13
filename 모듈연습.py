# import math # math 모듈을 사용하기 위해서 import 함
#
# print(math.sin(1))

# 모듈 내에 함수(메서드) 특정 한 함수만 가져오고자 하는 경우
from math import sin, cos, tan
print(sin(1))
print(cos(1))
print(tan(1))

# alias
import math as m


# sys 모듈 : 시스템과 관련된 정보를 가지고 있는 모듈 입니다.
import sys
print("명령 줄 인수 : ", sys.argv)
print("명령 줄 인수 : ", sys.path[0])
sys.stdout.write("집가고싶다\n")
sys.stderr.write("못간다\n")

# os 모듈 : 운영체제와 상호 작용하기위한 기능을 제공 (파일 시스템 접근, 환경 변수 제어, 프로세스 관리 등)

import os
# 현재 작업 디렉토리
cwd = os.getcwd()
print("현재 작업 디렉토리:", cwd)

# 디렉토리 생성
os.mkdir("mydir")

# 파일 또는 디렉토리 존재 여부 확인
is_file = os.path.isfile("myfile.txt")
is_dir = os.path.isdir("mydir")
print("myfile.txt는 파일인가?", is_file)
print("mydir은 디렉토리인가?", is_dir)

# 시스템 명령 실행
os.system("ls -l")

