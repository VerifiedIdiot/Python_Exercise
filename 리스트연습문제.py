# # 무작위 수를 ,로 기준하여 입력 받아 홀수와 짝수로 리스트에 나누어 담아 출력
#
# randomNumbers = list(map(int, input("홀짝 입력 : ").split(",")))
# print(randomNumbers)
#
# odd = []
# even = []
#
# for e in randomNumbers:
#     if e % 2 == 0 : even.append(e)
#     else: odd.append(e)
#
# print(f"짝수 :{even}")
# print(f"홀수 :{odd}")
#
# # 람다식 방법
#
# odd = list(filter(lambda e : e % 2 == 1, randomNumbers))
# even = list(filter(lambda e : e % 2 == 0, randomNumbers))
#
# print(f"짝수 :{even}")
# print(f"홀수 :{odd}")


# 1번 : 상근날도 , 초급
# 햄버거는 총 3종류 상덕버거, 중덕버거, 하덕버거가 있고, 음료는 콜라와 사이다 두 종류

# prices = list(map(int,input("가격을 입력해 주세요 : ").split(" ")))
# bug_prices = []
# drk_prices = []
# cnt = 0
# for i in range(3) :
#     bug_prices.append(prices[i])
# cnt = 0
# for i in range(2) :
#     drk_prices.append(prices[i+3])
#
# print(min(bug_prices))
# print(min(drk_prices))
# print(min(bug_prices)+min(drk_prices))

# prices = []
# while True :
#     prices.append(input(f"입력 해 주시오. : "))
#     if len(prices) == 5 : break

# 2번 : 저항, 증ㄱ,ㅂ

# colors = ("black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white")
# fir = colors.index(input())
# sec = colors.index(input())
# thr = colors.index(input())
# print(int(str(fir) + str(sec)) * (10 ** thr))


# 3번 : PC방 알바, 중급
# cnt = 0
# seat = [0] * 100
#
# N = int(input("손님의 수를 입력 : "))
#
# for e in range(N):
#     i = int(input("자리를 입력하세요: ")) - 1
#     if seat[i] == 1:
#         cnt += 1
#     else:
#         seat[i] = 1
# print(cnt)

val = input()
val = ''.join([char for char in val if char.isupper()])
print(val)





