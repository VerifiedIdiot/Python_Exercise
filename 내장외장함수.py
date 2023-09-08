# 내장함수 : 파이썬이 기본적으로 제공, import가 필요 없음
# 외장함수 : 파이썬이 기본적으로 제공, import가 필요함


# 큰값 작은값 찾기

# print(max(1, 2, 3, 4, 5), min(1, 2, 3, 4, 5))
#
# # 총 합 구하기
# print(sum([1, 2, 3, 4, 5]))  # 리스트에 대한 총 합
# print(sum((1, 2, 3, 4, 5)))  # 튜플에 대한 총 합
# # num = list(map(int, input("정수값 입력 : ").split()))
# # print(f"입력 받은 수의 총 합 : {sum(num)}")
# # print(f"입력 받은 수의 평균 : {sum(num)/len(num)}")
#
# # 몫과 나머지 구하기
# print(f"몫과 나머지 : {divmod(10, 4)}")  # 튜플의 동작 원리

# 여러개의 값을 한번에 입력 받아 리스트로 만들기
# 최대값, 최소값, 합계, 평균
# 몫과 나머지

# data = list(map(int,input("입력해라 :").split(",")))
#
# max_data = max(data)
# min_data = min(data)
# sum_data = sum(data)
# len_data = sum(data)/len(data)
#
# print(f"최대값은 : {max_data} , 최소값은 : {min_data} , 총합은 : {sum_data}, 몫은 : {len_data} 몫과 나머지는 : {divmod(sum(data),len(data))}")


# 정렬
my_list = [1,2,3,4,45,56,7,777,88,99,100]
# 내림 차순
print(sorted(my_list, reverse=True))
# 오름 차순
print(sorted(my_list))