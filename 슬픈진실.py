
def orderby() :
    grades = list(map(int, input().split()))
    avg = sum(grades[1:]) / len(grades[1:])
    passed_std = 0
    for i in range (1 , len(grades)) :
        if grades[i] > avg : passed_std += 1
    return passed_std / (len(grades)-1) * 100




case_count = int(input("케이스 횟수를 입력하세요 : "))
list_obj = []
for i in range(case_count) :
    list_obj.append(orderby())

for i in range(case_count) :
    print(f"{list_obj[i]:.3f}%")

