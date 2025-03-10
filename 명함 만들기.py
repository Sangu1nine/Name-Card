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
# while menu != '5':
    #print(display)
    #menu = int(input())
    # 위의 3개 단순하게 아래 한 문장으로 생략수정함 14:03 jjw
    menu = input(display).strip()

    # 1. 명함 입력
    if menu == 1 :
        name = input('이름 입력 >').strip()
        email = input('이메일 주소 입력 >').strip()
        tel = input('전화번호 입력 >').strip()
        belong = input ('직장 또는 학교 입력 >').strip()
        
        card.append([name,email,tel,belong])
        card[len(card)-1].insert(0,len(card))
        #print("명함이 입력되었습니다", card)
        # 단순한 명함입력보단 사람의 이름이 출력이 좋아보임 14:05 jjw
        print(f"{name}님의 명함이 입력되었습니다.", card)

    # 2. 명함 수정
    elif menu == 2 :
        print(card, "\n", card_display)
'''
        # 예외 처리
        if int(card_num)-1 > card[-1][0] :
            print("해당 번호가 없습니다.")
            card_num = input('수정할 명함 번호 입력 >')
'''
# 예외 처리를 if에서 잘못된점이 발견되어 while로 수정함 14:19 jjw

        while True:
        card_num = input('수정할 명함 번호 입력 > ')

        # 명함 번호가 유효한지 확인
        if 1 <= int(card_num) <= len(card):
            card_num = int(card_num)  # 유효한 명함 번호가 입력되었을 경우
            break
        else:
            print("해당 번호가 없습니다. 다시 입력해주세요.")  # 존재하지 않는 번호일 경우

        # 예외처리가 없어서 추가 했음(71~78) 14:22 jjw
        # 수정할 부분 번호 입력 받기
        while True:
            number = int(input('수정할 부분 > '))
            
            # 1~4 사이의 숫자가 아닌 경우 예외 처리
            if 1 <= number <= 4:
                break  # 유효한 입력이 들어오면 루프 종료
            else:
                print("잘못된 번호입니다. 1~4 사이의 번호를 입력해주세요.")  # 잘못된 번호 입력 시 메시지 출력

        # 명함 수정
        if number == 1:
            card[int(card_num)-1][1] = input('수정할 이름 입력 > ')
        elif number == 2:
            card[int(card_num)-1][2] = input('수정할 이메일 주소 입력 > ')
        elif number == 3:
            card[int(card_num)-1][3] = input('수정할 전화번호 입력 > ')
        elif number == 4:
            card[int(card_num)-1][4] = input('수정할 직장 또는 학교 입력 > ')

        print("명함이 수정되었습니다:", card[int(card_num)-1])


    # 3. 명함 삭제
    elif menu == 3:
        print(card_display2)

        # 아래 예외처리들을 추가함 (99~117) 14:25 jjw
        # 삭제할 명함 번호 입력 받기
        while True:
            card_num = input('삭제할 명함의 번호 입력 > ')
            
            # 명함 번호가 유효한지 확인
            if 1 <= int(card_num) <= len(card):
                card_num = int(card_num)  # 유효한 명함 번호가 입력되었을 경우
                break
            else:
                print("해당 번호가 없습니다. 다시 입력해주세요.")  # 존재하지 않는 번호일 경우

        # 삭제할 항목 번호 입력 받기
        while True:
            number = int(input('삭제할 항목 번호 입력 > '))
            
            # 1~5 사이의 숫자만 유효
            if 1 <= number <= 5:
                break  # 유효한 번호가 입력되면 루프 종료
            else:
                print("잘못된 번호입니다. 1~5 사이의 번호를 입력해주세요.")  # 잘못된 번호 입력 시 메시지 출력

        # 명함 삭제
        if number == 1:
            del card[card_num - 1][1]
        elif number == 2:
            del card[card_num - 1][2]
        elif number == 3:
            del card[card_num - 1][3]
        elif number == 4:
            del card[card_num - 1][4]
        elif number == 5:
            del card[card_num - 1]
            
        print("명함이 삭제되었습니다:", card)

    # 4. 명함 목록 보기
    elif menu == 4 :
        print(card)

    # 5. 종료
    elif menu == 5 :
        print('프로그램 종료')
        sys.exit()
        
    # 잘못된 입력 처리
    else :
        print("메뉴 선택을 잘못하셨습니다.")

