# 📇 Name-Card  
## 💼 3조 명함 관리 프로그램

---

### 📝 프로그램 소개  
명함 관리 프로그램을 작성한다.  
명함은 리스트 형태로 관리되며, **입력 / 수정 / 삭제 / 목록 보기 / 종료** 기능을 포함한다.

---

### 🖥️ 디스플레이 구성 (3개 화면)
1. **메인 메뉴**
    - 1. 명함 입력  
    - 2. 명함 수정  
    - 3. 명함 삭제  
    - 4. 명함 목록 보기  
    - 5. 종료  

2. **명함 항목 입력/수정 화면**
    - 1. 이름  
    - 2. 이메일 주소  
    - 3. 전화 번호  
    - 4. 직장/학교  

3. **명함 삭제 화면**
    - 1. 이름  
    - 2. 이메일 주소  
    - 3. 전화 번호  
    - 4. 직장/학교  
    - 5. 전체 삭제  

---

### 🗂️ 명함 데이터 구조
- 각 명함은 리스트 형태로 구성됨:  
  `[명함 번호, 이름, 이메일 주소, 전화 번호, 직장/학교]`
- 전체 명함 목록은 `card`라는 리스트로 저장됨

---

### ✏️ 기능 상세

#### 🔹 명함 입력
1. `input()`으로 이름, 이메일, 전화번호, 직장/학교 입력 받음  
2. `strip()`을 통해 공백 제거  
3. 입력 받은 값을 변수에 저장 후 리스트(`card`)로 구성  
4. `card`를 `card_list`에 `append()`  
5. 명함 번호는 `card_list`의 인덱스를 기반으로 부여  
6. `"명함이 입력되었습니다"` 메시지 출력

---

#### 🔹 명함 수정
1. 현재 명함 존재 여부 확인  
2. 존재할 경우, 명함 번호 또는 이름 입력받아 해당 명함 검색  
3. 수정할 항목 선택 후 수정  
4. 수정 후 저장하고 메인 메뉴로 복귀  

---

#### 🔹 명함 삭제
1. 현재 명함 존재 여부 확인  
2. 삭제할 명함 항목 선택  
3. 해당 항목 삭제  
4. 메인 메뉴로 복귀  

---

#### 🔹 명함 목록 보기
1. 현재 명함 존재 여부 확인  
2. 전체 명함 목록 출력  
3. 메인 메뉴로 복귀  

---

#### 🔹 종료
- 프로그램 종료

---

