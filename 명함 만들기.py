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


menu = ''
card = []
while menu != '5':
    print(display)
    menu = int(input())


    if menu == 1 :
        name = input('이름 입력 >').strip()
        email = input('이메일 주소 입력 >').strip()
        tel = input('전화번호 입력 >').strip()
        belong = input ('직장 또는 학교 입력 >').strip()
        card.append([name,email,tel,belong])
        card[len(card)-1].insert(0,len(card))
        print("명함이 입력되었습니다", card)


    elif menu == 2 :
        print(card, "\n", card_display)
        card_num = input('수정할 명함 번호 입력 >')
        if int(card_num)-1 > card[-1][0] :
            print("해당 번호가 없습니다.")
            card_num = input('수정할 명함 번호 입력 >')
        number = int(input('수정할 부분 >'))
        if number == 1 :
            card[int(card_num)-1][0] = input('수정할 이름 입력>')
        if number == 2 :
            card[int(card_num)-1][1] = input('수정할 이메일 주소 입력 >')
        if number == 3 :
            card[int(card_num)-1][2] = input('수정할 전화번호 입력 >')
        if number == 4 :
            card[int(card_num)-1][3] = input('수정할 직장 또는 학교 입력 >')
        print("명함이 수정되었습니다", card[int(card_num)-1])


    elif menu == 3 :
        print(card_display2)
        card_num = input('삭제할 명함의 번호 입력 >')
        number = int(input('삭제할 항목 번호 입력 >'))
        if number == 1 :
            del card[int(card_num)-1][0]
        if number == 2 :
            del card[int(card_num)-1][1]
        if number == 3 :
            del card[int(card_num)-1][2]
        if number == 4 :
            del card[int(card_num)-1][3]
        if number == 5 :
            del card[int(card_num)-1]
       
        print("명함이 삭제되었습니다", card)
    elif menu == 4 :
        print(card)


    elif menu == 5 :
        print('프로그램 종료')
        sys.exit()
    else :
        print("메뉴 선택을 잘못하셨습니다.")
