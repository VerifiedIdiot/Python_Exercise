#   1. 정해진 형식으로 시간을 입력 받아서 출력하기
#   입력 형식 : 22:5:5 => 오후 10시 05분 05초

#   2번. 3개의 정수를 입력 받아 최대값과 최소값 구하기

#   3번. 주민등록번호를 입력받아 생년월일, 성별, 나이 출력하기

#   4번. 갯수가 정해지지 않은 여러개의 정수를 입력 받아 합계와 평균 구하기

# time = input("시간을 입력하세요 (hh:mm:ss) 형식으로 : ")
# hour, minute, second = map(int, time.split(":"))
#
# if hour > 12:
#     hour -= 12
#     print(f"오후{hour:02}시{minute:02}분{second:02}초")
# else :
#     print(f"오전{hour:02}시{minute:02}분{second:02}초")
#
#
# first = int(input("1번째 정수를 입력하세요  : "))
# second = int(input("2번째 정수를 입력하세요  : "))
# third = int(input("3번째 정수를 입력하세요  : "))
#
# int_list = []
# int_list.extend([first, second, third])
# print(int_list)
# print(f"결과: {max(int_list)}, {min(int_list)}")
#
# info_list = []
# info = input("주민등록번호 , 이름 , 나이를 입려갛세요. ',' 로 구분 : ")
# info_list = info.split(",")
# print(f"주민등록번호 : {info_list[0]}, 이름 : {info_list[1]}, 나이 : {info_list[2]}")

input_list = []

while True:
    input_str = input("정수 아무거나 입력해봐 (그만!) 치면 종료 :")

    if input_str == "그만!":
        break
    try:
        input_int = int(input_str)
        input_list.append(input_int)
    except ValueError:
        print("정수야..")
print(f"합계 : {sum(input_list)}, 평균 : {sum(input_list) / len(input_list)}")

