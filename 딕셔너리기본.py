# 딕셔너리 : 키(Key)와 값(Value)의 한 쌍으로 이루어진 구조 (자바의 Map과 동일)
# 중괄호{}로 감싸서 선언, 쉼표(,)로 구분
# 키와 값은 콜론(:)으로 구분

coffee_menu = {"아메리카노" : 1500, "콜드브루" : 2500, "카푸치노" : 2000}
tea_menu = {"Black tea" : 3000, "Hibiscus tea" : 3500, "Jasmin tea" : 3000}
food_menu = {"Pound Cake" : 4000, "Tiramisu" : 4500, "Macaron" : 5000}

print(coffee_menu)
print(tea_menu)
print(food_menu)
print(coffee_menu["아메리카노"]) # 키로 출력
print(coffee_menu.get("콜드브루")) # get 메서드로 키를 넣어서 값을 확인하는 방법

# update 메서드(함수) : 딕셔너리의 데이터를 한꺼번에 변경

dict = {"곰돌이":30, "안유진":50, "장원영":60}
dict.update({"곰돌이": 100, "장원영": 100})
print(dict)

# 정보 얻기 : keys(), values(), items()
dict1 = {"자바": 80, "PHP": 90, "HTML": 70}

print(dict1.keys()) # 딕셔너리에 포함된 키를 확인
print(dict1.values())   # 딕셔너리에 포함된 값 확인
print(dict1.items())    # 딕셔너리에 포함된 각 쌍을 확인

print('HTML' in dict1)  # True
print('파이썬' in dict1)  # False
print(dict1.get("파이썬")) # 없으면 None, 있으면 키에 해당하는 값을 보여 줌
# 반복문에 키를 사용해 값을 가져오기
for key in coffee_menu :
    print(key, ":", coffee_menu[key])




