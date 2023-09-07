# 파이썬 입력
# 사용자의 입력을 받아 그 값을 프로그램에서 사용하고자 할 때 input()함수를 사용 합니다.

# print("이름을 입력 하세요 : ", end="")

# input 함수를 통해서 입력 받은 데이터는 문자열로 반환 , 필요시 원하는 데이터 형으로 변환이 필요
# name = input("이름을 입력 하세요 : ")
# print(f"당신의 이름은 {name} 입니다")
#
# age = int(input("나이를 입력 하세요 : "))
# print(f"당신의 나이는 {age} 입니다")
# print(type(age))
#
# addr = input("주소를 입력 하세요 : ")
# jobs = input("직업을 입력 하세요 : ")
# score = float(input("성적을을 입력 하세요 : "))
#
# print(f"하이용? '{name}'")
# print(f"""주소는 '{addr}',
# 직업은 '{jobs}',
# 나이는 '{age}'이며,
# 성적은 '{score}'이다.""")

# split 함수의 기본 기준값은 공백
# str1, str2 = input("이름과 주소 입력 : ").split()
# print(str1, str2)

# kor, eng, mat = map(int, input("국어 영어 수학").split())
# print(kor, eng, mat)

val = map(int, input("성적 입력 : ").split())
print(*val)
print(type(val))

# hour, min, sec = input("시:분:초 :").split(":")
# print(f"시간{hour} 분{min} 초{sec} 이다.")

# 시간을 24시간제이며 : 기준으로 입력 받은 후 오전과 오후로 출력하도록 변경
# hour, min, sec = map(int, input("시간 입력 : ").split(":"))
# if hour > 12:
#     hour -= 12
#     print(f"오후{hour:02}시{min:02}분{sec:02}초")
# else:
#     print(f"오전{hour:02}시{min:02}분{sec:02}초")
