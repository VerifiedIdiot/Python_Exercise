# 영식 요금제 : 30초에 10원
# 민식 요금제 : 60초에 15원


# cnt = int(input())  # 통화 횟수
# call = list(map(int, input().split()))  # 통화 횟수에 대한 통화 시간
# y_pay = m_pay = 0
# for i in range(cnt) :
#     y_pay += (call[i] // 30) * 10 + 10
#     m_pay += (call[i] // 60) * 15 + 15
#
# if y_pay > m_pay:
#     print("M", m_pay)
# elif y_pay < m_pay:
#     print("M", m_pay)
# else:
#     print("M", m_pay)

# 대소문자 바꾸기
# 영어 소문자와 대문자로 이루어진 단어를 입력받은 뒤, 대문자는 소문자로, 소문자는 대문자로 바꾸어 출력하는 프로그램을 작성하시오.


# rst = ""
# for e in input() : # 입력 받는 문자열 만큼 자동 순회
#     if e.islower():
#         rst += e.upper()
#     else :
#         rst += e.lower()
# print(rst)

# 숫자의 개수
# A= 150, B = 266, C = 427 이라면, A x b c = 150 x 266 x 427 = 17037300
# 1부터 9까지의 숫자가 각각 몇 번 쓰였는지 차례로 한 줄에 하나씩 출력

a, b, c = map(int, input("정수 3개 입력 : ").split())
total_val = str(a * b * c)  # a * b * c 결과를 문자열 변환

for i in range(10) :
    print(total_val.count(str(i)))  # 문자열의 각 요소를 count한다 중복된 요소가 있으면 count 증가

