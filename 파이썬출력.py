# 파이썬의 다양한 출력 방법

name = "곰돌이사육사"
age = 20
gender = "남성"
jobs = "소프트웨어 개발자"
addr = "서울시 강남구 역삼동"

# C언어 스타일 : 서식지정자를 사용하는 방식
print("=" * 5, "C 스타일", "=" * 5)
# 자바의 " ".repeat() 과 같음
print("이름 : %s" %(name))
print("나이 : %d" %(age))
print("성별 : %s" %(gender))
print("직업 : %s" %(jobs))
print("주소 : %s" %(addr))
print("")

# 파이썬 스타일 : 3.6 ver 이전 방법
print("=" * 5, "파이썬 3.6 이전 스타일", "=" *5)
print("이름과 주소 : {} {}".format(name, addr))
print("나이 : {} ".format(age))

# 파이썬 현재 스타일 : 3.6 ver 이후 방식 , f와 {}를 사용해서 출력하는 방식

print("=" * 5, "파이썬 현재 스타일", "=" *5)
print(f"이름 : {name}")
print(f"나이 : {age}, 성별 : {gender}, 직업 : {jobs}")

# 자바 스타일 : 문자열 연결 방법 (+) 을 사용
print("=" * 5, "자바 스타일", "=" *5)
print("이름 : " + name)
print("나이 : " + str(age))
print("주소 : " + addr)

# 출력 시 정렬
# < 좌측 정렬
# > 우측 정렬 , 생략 가능
# ^ 중앙 정렬

print("|{:5}|".format(10))
print("|{:<5}|".format(10))
print("|{:^6}|".format(10))

num = 10
print(f"|{num:>5}|")
print(f"|{num:<5}|")
print(f"|{num:^6}|")

PI = 3.14159265
print(f"{PI:.2f}")  # 소수점 2개 이하 제거




