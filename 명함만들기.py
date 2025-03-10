import sys

display = '''
--------------------------------------------------------------
1. 명함 입력 2. 명함 수정 3. 명함 삭제 4. 명함 목록 보기 5. 종료
--------------------------------------------------------------
메뉴 번호를 선택하세요 >>> '''

card_display = '''
--------------------------------------------------------------
1. 이름, 2. 이메일 주소, 3. 전화 번호, 4. 직장/학교
--------------------------------------------------------------
메뉴 번호를 선택하세요 >>> '''

card_display2 = '''
--------------------------------------------------------------
1. 이름, 2. 이메일 주소, 3. 전화 번호, 4. 직장/학교, 5. 전체 삭제
--------------------------------------------------------------
메뉴 번호를 선택하세요 >>> '''

# 명함 정보를 저장할 리스트
menu = ''
card = []

while True:
    menu = input(display).strip()

    # 1. 명함 입력
    if menu == '1':
        name = input('이름 입력 > ').strip()
        email = input('이메일 주소 입력 > ').strip()
        tel = input('전화번호 입력 > ').strip()
        belong = input('직장 또는 학교 입력 > ').strip()

        card.append([name, email, tel, belong])
        card[len(card) - 1].insert(0, len(card))
        print(f"{name}님의 명함이 입력되었습니다.", card)

    # 2. 명함 수정
    elif menu == '2':
        print(card, "\n", card_display)

        while True:
            card_num = input('수정할 명함 번호 입력 > ')

            if 1 <= int(card_num) <= len(card):
                card_num = int(card_num)
                break
            else:
                print("해당 번호가 없습니다. 다시 입력해주세요.")

        while True:
            number = int(input('수정할 부분 > '))

            if 1 <= number <= 4:
                break
            else:
                print("잘못된 번호입니다. 1~4 사이의 번호를 입력해주세요.")

        if number == 1:
            card[card_num - 1][1] = input('수정할 이름 입력 > ')
        elif number == 2:
            card[card_num - 1][2] = input('수정할 이메일 주소 입력 > ')
        elif number == 3:
            card[card_num - 1][3] = input('수정할 전화번호 입력 > ')
        elif number == 4:
            card[card_num - 1][4] = input('수정할 직장 또는 학교 입력 > ')

        print("명함이 수정되었습니다:", card[card_num - 1])

    # 3. 명함 삭제
    elif menu == '3':
        print(card_display2)

        while True:
            card_num = input('삭제할 명함의 번호 입력 > ')

            if 1 <= int(card_num) <= len(card):
                card_num = int(card_num)
                break
            else:
                print("해당 번호가 없습니다. 다시 입력해주세요.")

        while True:
            number = int(input('삭제할 항목 번호 입력 > '))

            if 1 <= number <= 5:
                break
            else:
                print("잘못된 번호입니다. 1~5 사이의 번호를 입력해주세요.")

        if number == 1:
            card[card_num - 1][1] = "None"
        elif number == 2:
            card[card_num - 1][2] = "None"
        elif number == 3:
            card[card_num - 1][3] = "None"
        elif number == 4:
            card[card_num - 1][4] = "None"
        elif number == 5:
            del card[card_num - 1]

        print("명함이 삭제되었습니다:", card)

    elif menu == '4':
        if not card:
            print("저장된 명함이 없습니다.")
        else:
            print("\n==================== 명함 목록 ====================")
            for c in card:
                print(f"번호: {c[0]}")
                print(f"이름: {c[1]}")
                print(f"이메일: {c[2]}")
                print(f"전화번호: {c[3]}")
                print(f"직장/학교: {c[4]}")
                print("--------------------------------------------------")


    # 5. 종료
    elif menu == '5':
        print('프로그램 종료')
        sys.exit()

    # 잘못된 입력 처리
    else:
        print("메뉴 선택을 잘못하셨습니다.")
