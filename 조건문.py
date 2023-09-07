#   제어문이란 ? 조건문과 반복문을 의미하며 순차적인 흐름을 제어하는 목적으로 사용 된다.

# n = int(input("정수를 입력 하세요 : "))
#
# if n > 100 :
#     print(f"{n}은 100 보다 큽니다.")
# elif n < 100 :
#     print(f"{n}은 100보다 작습니다.")
# else :
#     print("입력값은 100과 같아요")

#   조건문에서 문자열 비교

season = input("현재 계절을 입력 하세요 : ")

if season == "spring":
    print("봄이 왔어요.")
elif season == "summer":
    print("여름이 왔어요.")
elif season == "fall":
    print("가을 입니다.")
elif season == "winter":
    print("겨울이네요")
else:
    print("계절 입력 오류.")
