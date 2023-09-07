#   산술연산자 : 시작연산자(+, -, *, /) // (몫), ** (제곱연산자), %(나머지 연산자)

i = 10  # 값이 대입할 때 데이터 형이 결정됨, 왜냐하면 파이썬은 선언할 데이터형이 없음
j = 3

print(f"덧셈 : {i + j}")
print(f"뺄셈 : {i - j}")
print(f"곱셈 : {i * j}")
print(f"나눗셈 : {i / j}")
print(f"몫 : {i // j}")  #   나머지
print(f"나머지 : {i % j}")
print(f"제곱 : {i ** j}") #   제곱 , 자바와 다른 특이점

text = "Python!!!"
print(text + "Hello")
print(text + str(100))
print(text * 3)

i += 1  # 파이썬은 증감 연산자가 없음
print(f"증감연산자 시험 : {i}")

#   간단 예제   :   파이썬은 변수를 상수로 만드는 방법은 없으며, 관례상 변수 이름을 모두 대문자로 표시하면 상수로 간주하기로 함
TAX_RATE = 0.10, 0.11
# TAX_RATE[0] = 0.12    에러 발생
print(type(TAX_RATE))
income = int(input("당신의 수입은 ? ㅋ : "))
print(f"당신이 내야 할 세금 {income * TAX_RATE[0]:.2f} 입니다.")

#   관계 연산자 : AND(&&) => and,    OR(||) => or, NOT(!) => not

x = 10
y = 20
z = 30

result1 = (x > 0) and (x < y)
result2 = (x > 0) or (x > y)
result3 = not((x > 0) or (x > y))

print(result1, result2, result3, sep="\t")

#   다항(3항)연산자

num = int(input("정수 입력 : "))
rst = (num % 2 == 0) and "짝수" or "홀수"   # e => (e % 2 ==0) and "짝수" or "홀수"
print(f"{num}은 {rst}입니다.")

#   2진수 입력 받기 (0b)
number = 0b10101010101
#   8진수 입력 받기
number = 0o1234567
#   16진수 입력 받기
number = 0xffffff



# print(result2)
# print(result3)

# print("%d + %d = %d"%(i, j, i+j))       # 더하기
# print("%d - %d = %d"%(i, j, i-j))       # 빼기
# print("{} * {} = {}".format(i, j, i*j)) # 곱하기, 순서를 정할 수 있다.
# print(f"{i} ** {j} = {i**j}")           # 제곱 연산자
# print("%d / %d = %.2f"%(i, j, i/j))     # 나누기
# print("%d // %d = %d"%(i, j, i//j))     # 몫
# print(str(i) + " % " + str(j) + " = " +str(i%j)) # 나머지를 문자로 변경해서 출력

# text = "Python!!!"
# print(text + "Hello")
# print(text * 3)

