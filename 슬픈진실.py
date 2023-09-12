# 5 -> 총 테스트 횟수
# 5 50 50 70 80 100 => 각 케이스마다 평균이 넘는 % 구하기
# 5 100 95 90 80 70 60 50 => 각 케이스마다 평균이 넘는 % 구하기
# 3 70 90 80
# 3 70 90 81
# 9 100 99 98 97 96 95 94 93 91

case_count = int(input("케이스 횟수를 입력하세요 : "))
results = []

for i in range(case_count):
    grades = list(map(int, input().split()))

    avg = sum(grades[1:]) / len(grades[1:])
    passed_std = sum([1 for score in grades[1:] if score > avg])

    results.append(passed_std / (len(grades) - 1) * 100)

print("\n결과:")
for result in results:
    print(f"{result:.3f}%")

