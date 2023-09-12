seat = [0] * 11
while True:
    start = int(input("[1]예매하기 , [2]종료하기: "))

    if start == 1:
        while True:
            choice = input("좌석을 입력하세요 (1 ~ 10) quit 시 종료 : ")
            if choice == "quit":
                break
            choice = int(choice)

            if 1 <= choice < len(seat):
                if seat[choice] == 0:
                    seat[choice] = 1
                    print(f"{choice}번 좌석이 예매되었습니다.")
                else:
                    print("이미 예매된 좌석입니다.")
            else:
                print("잘못된 좌석 번호입니다.")
    elif start == 2:
        print("예매 시스템을 종료합니다.")
        break

print(f"총 금액은 {seat.count(1) * 12000}원 입니다.")





# # 영화표 예매하기
# TICKET_PRICE = 12000
# seat = [0] * 10
#
# # 좌석 상태를 표시하는 메뉴 만들기
# def print_seat() :
#     for e in seat :  # 향상된 for문으로 좌석의 갯수 만큼 순회
#         if e == 0 : print("[ ]", end=" ")  # 판매 안된 좌석
#         else : print("[V]", end=" ")  # 판매된 좌석
#     print()
#
# # 총 매출액 구하기
# def amount() :
#     cnt = 0
#     for e in seat :
#         if e == 1 : cnt += 1  # 팔린 좌석의 총 갯수 구하기
#     return cnt * TICKET_PRICE
#
# # 좌석 예약 하기
# def select_seat() :
#     print_seat() # 현재 예약 가능한 좌석 보여 주기
#     num = int(input("좌석 번호를 선택 하세요 : ")) - 1    # 선택된 좌석번호는 1부터 시작하고 인덱스는 0 부터 시작 하기 때문에 -1
#     if seat[num] == 0 :
#         seat[num] = 1
#         print_seat()
#     else : print("이미 예약된 좌석 입니다.")
#
# while True :
#     sel = int(input("[1]예매하기 [2] 종료하기 : "))
#     if sel == 1 : select_seat()
#     else :
#         print(f"총 매출액 : {amount()}원")
#         break
