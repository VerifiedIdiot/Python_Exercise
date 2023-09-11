# 순차 검색과 이진 검색
### Python 순차 검색 횟수
# def search_list(a, x):
#     for i in range(0, len(a)):
#         if x == a[i]: return i
#     return -1
#
# v = [17, 92, 18, 33, 58, 7, 33, 42]
# print(search_list(v, 33))
# print(search_list(v, 18))
# print(search_list(v, 900))
#
#
# # 기본값 인자
# # 함수 선언 시 매개 변수에 대한 기본값을 정의함
# # 매개변수에 기본값이 정해져있으면 함수 호출 시 매개변수에 값을 집어 넣지 않으면 기본값이 출력됨
# def profile(name, year = 2, age = 18, school = "태양고"):
#     print(f"이름 : {name}, 학교 : {school}, 학번 : {year}, 나이 : {age}")
#
# profile("나희도")
# profile("고유림")
# profile("백이진", None, 22)


# 가변 매개변수
# 함수의 매개변수 앞에 *를 붙여주면 함수의 매개 변수를 몇개를 입력하든 함수 내에서 튜플로 인식 한다.
# def profile(name, age, *lang) :
#     print(f"이름 : {name}, 나이 : {age}", end= " ")
#     for e in lang :
#         print(e, end= " ")
#     print()
#
# profile("나희도", 18, "Python", "Java", "C", "C++", "React", "Kotlin")
# profile("조세호", 38, "Python", "Java", )
# profile("유재석", 48, "Python", "Java", "C", "C++",)


# knife = 10 # 칼을 10자루 준비
#
# def game(player, knife) :
#     knife -= player
#     print(f"남아 있는 칼은 {knife} 자루 입니다.")
#     return knife
#
# player = int(input("경기에 참여 하는 학생이 몇명 입니까? : "))
# knife = game(player, knife)
# print(f"경기에 사용하고 남은 칼은 {knife} 입니다.")
#
# def game(player) :
#     global knife
#     knife -= player
#     print(f"남아 있는 칼은 {knife} 자루 입니다.")
#
# player = int(input("경기에 참여 하는 학생이 몇명 입니까? : "))
# game(player)
# print(f"경기에 사용하고 남은 칼은 {knife} 입니다.")



