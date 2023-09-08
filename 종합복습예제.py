name = (input("이름을 입력 하세요 : "))
gen_type = ""
while True:
    age = input("나이를 입력하세요 : ")

    if age.isdigit():
        age = int(age)
        if 0 < age < 200:
            break
        print("나이를 잘못 입력 하셨습니다. 다시 입력 하세요.")
    else:
        print("숫자만 입력하세요.")

while True:
    gender = input("성별을 입력 :")
    if str == type(gender) and gender == "m" or gender == "M":
        break
    elif str == type(gender) and gender == "f" or gender == "F":
        break
    else:
        print("다시 입력하세요.")

while True:
    jobs = input("직업을 입력 하세요 : ")
    if jobs != str :
        break
    else: print("직업이 잘못 입력되었습니다. 다시 입력해주세요.")

if gender == 'M' or gender == 'm':
    gen_type = "남성"
elif gender == "f" or gender == "F":
    gen_type = "여성"

print("회원정보")
print(f"이름 : {name}")
print(f"나이 : {age}")
print(f"성별 : {gen_type}")
print(f"직업 : {jobs}")

