import sys

display = '''
-----------------------------------------------------------------
1. 명함 입력 2. 명함 수정 3. 명함 삭제 4. 명함 목록 보기 5. 종료
-----------------------------------------------------------------
메뉴 번호를 선택하세요 >>> '''

card_display = '''
-----------------------------------------------------------------
1. 이름, 2. 이메일 주소, 3. 전화 번호, 4. 직장/학교
-----------------------------------------------------------------
메뉴 번호를 선택하세요 >>> '''

card_display2 = '''
-----------------------------------------------------------------
1. 이름, 2. 이메일 주소, 3. 전화 번호, 4. 직장/학교, 5. 전체 삭제
-----------------------------------------------------------------
메뉴 번호를 선택하세요 >>> '''

menu = ''
card = []
while menu != '5':
    menu = int(input(display))

    if menu == 1 :
        name = input('이름 입력 >').strip()
        email = input('이메일 주소 입력 >').strip()
        tel = input('전화번호 입력 >').strip()
        belong = input ('직장 또는 학교 입력 >').strip()
        card.append([name,email,tel,belong])
        card[len(card)-1].insert(0,len(card))
        print("명함이 입력되었습니다", card)