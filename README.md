# Name-Card
## 3조 명함 코드

명함 관리 프로그램 작성

디스플레이는 3개를 만듭니다. 
(1) 1. 명함 입력, 2. 명함 수정, 3. 명함 삭제, 4. 명함 목록 보기, 5. 종료
(2) 1. 이름, 2. 이메일 주소, 3. 전화 번호, 4. 직장/학교
(3) 1. 이름, 2. 이메일 주소, 3. 전화 번호, 4. 직장/학교, 5. 전체 삭제

명함은 리스트로 1. 명함 번호 2. 이름, 3. 이메일 주소, 4. 전화 번호, 5. 직장/학교를 선택해서 입력/수정/삭제가 가능해야 함.

먼저 card_list = 명함 목록이라는 빈 리스트

list = 명함을 적을 빈 리스트

이름, 이메일, 전화번호, 직장/학교

명함 수정 설명

우선 현재 명함이 존재하는지 여부 판다
존재한다고 판단된 경우,
명함 번호 또는 이름을 입력하여 해당 명함의 인덱스를 찾는다.
이후 해당명함에서 수정할 영역을 선택한다.
선택한 영역을 수정하고 저장한다
다시 메인메뉴로 나간다.