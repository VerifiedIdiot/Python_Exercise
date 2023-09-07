#   1번 문제 : 세자리 정수를 입력 받은후 가장 큰 수 찾기    (1,2,3 => 3)


# first = int(input("1번째 정수를 입력하세요  : "))
# second = int(input("2번째 정수를 입력하세요  : "))
# third = int(input("3번째 정수를 입력하세요  : "))
#
# int_list = []
# int_list.extend([first, second, third])
# print(int_list)
# print(f"결과: {max(int_list)}, {min(int_list)}")


#   2번 문제 : 주/야간 근무시간을 입력 받아 아르바이트 급여 꼐산하기
    #   주간 근무 : 9620원
    #   야간 근무 : 주간 시급 * 1.5
    #   주간근무 [1], 야간근무[2]를 입력 하세요 :
    #   근무 시간을 입력 해 주세요 :
    #   입력한 시간 동안 근무한 주간 또는 야간 급여는 ___원 입니다.


user_input = input("주간근무 [1], 야간근무[2]를 입력 하세요 : ")
duty_time = [0, 0]
time_dur = int(input("근무 시간을 입력해 주세요"))

if user_input == "1":
    duty_time[0] = 9620 * time_dur
elif user_input == "2":
    duty_time[1] = (9620 * time_dur) * 1.5

print(f"주간급여는 {duty_time[0]}원 , 야간급여는 {duty_time[1]}원 입니다.")



#   3번 문제   : 문자열 추가하기
    # 2개의 문자열을 포인터 변수 s와 k에
    # 양의 정수를 정수형 변수 n에 각각 전달 받아 s 문자열의 뒤 부분의 n개 문자를 k문자열 앞에 끼워 넣는 코드 작성
    # s : seoul
    # k : korea
    # n : 2
    # 결과 : ulkorea

s = "seoul"
k = "korea"
n = 2
print(s[-n:] + k)








# def mixture(s, k, n):
#     return s[-n:] + k
# print(mixture(s, k, n))