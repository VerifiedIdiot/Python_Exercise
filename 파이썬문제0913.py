# 1. 배수찾기 (초급)
# 첫째줄에 n이 주어짐, 다음 줄 부터 값이 주어 짐
# 목록에 있는 수가 n의 배수인지 아닌지 판별
# 0을 입력하면 목록이 끝남

# 배수진 판별기

# n = int(input("n값을 입력하시오: "))
# list1 = []
#
# while True :
#     num = int(input("리스트에 담을 수 입력 ㄱ :"))
#     if num == 0:
#         break
#     list1.append(num)
#
# for i in list1 :
#     if i % n > 0 :
#         print(f"{i}는 {n}의 배수가 아니오.")
#     else:
#         print(f"{i}는 {n}의 배수가 맞소.")

# 피타고라스 문제

list2 = []
while True:
    list2 = list(map(int, input("입력 ㄱ : ").split(",")))
    if sum(list2) == 0:
        break
    list2.sort()
    if  list2[0]**2 + list2[1]**2 == list2[2]**2 :
        print("맞소")
    else:
        print("틀렸소")