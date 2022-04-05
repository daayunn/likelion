price=(int(input("금액을 넣어주세요:")))

while True:
    menu={"1. 콜라":500, "2. 커피":400, "3. 사이다":300, "4. 율무차": 200}
    menu_price = list(menu.values())
    print("[멋사네 음료수]")
    print("현재 금액 %d원" %(price))

    for drink, prices in menu.items():
        print("%s - %s 원" %(drink, prices))

    num=int(input("음료를 선택해주세요: "))-1

    exchange=price-menu_price[num]

    if exchange<0:
        print("금액이 부족합니다.")
        break
    elif exchange==0:
        print("잔액은 ", exchange, "원입니다. 이용해주셔서 감사합니다.")
        break
    else:
        print("잔액은 ", exchange, "원입니다.")
        qa=input("추가로 구매하시겠습니까?(Y/N): ")

        if(qa=="Y"):
            price=exchange
            continue
        else:
            print("이용해주셔서 감사합니다.")
            break




