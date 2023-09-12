# x = 0
# a = 70 * x
# b = (170 * x) - 1000
#
#
# if a > b :
#     print(-1)
# if b >= a :
#     print(1)
#
# what is the value of x ?


a , b , c = map(int, input("고정비용 , 가변비용 , 판매비용을 입력 :").split(","))

if b > c :
    print("이러면 손익분기점 x")
cnt = 0
if c > b :
    while True :
        cnt += 1
        if (c * cnt) - a > b * cnt :
            break
    print(cnt)
