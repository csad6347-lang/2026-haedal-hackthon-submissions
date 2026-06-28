# 2026-haedal-hackton-submissions
**2026 해달 해커톤 대체과제 제출 레포지토리입니다**

# 해달 준회원 프로그래머스 과제 제출 레포

## 📁 제출 방식 (폴더 구조)
> Step 1. 이 레포를 **Fork** (우측 상단 Fork 버튼)
>
> Step 2. 로컬에 git clone
>
> Step 3. **`problems/<Programmers_ID>/`** 폴더 생성
>
> Step 4. 그 안에 아래 10개 문제 파일 생성 (`<문제번호>.<확장자>`)

### 파일 생성 예시 👇

```text
problems/
└─ <Programmers_ID>/
   ├─ 12904.py       # 가장 긴 팰린드롬
   ├─ 120852.py      # 소인수분해
   ├─ 12906.py       # 같은 숫자는 싫어
   ├─ 12949.py       # 행렬의 곱셈
   ├─ 120892.py      # 암호 해독
   ├─ 12945.py       # 피보나치 수
   ├─ 42885.py       # 구명보트
   ├─ 12953.py       # N개의 최소공배수
   ├─ 12921.py       # 소수찾기
   └─ 132267.py      # 콜라 문제
   (총 10개, 언어 자유)
```

> 파일 이름은 반드시 **`<문제번호>.<확장자>`** 형식으로 작성해주세요.  
> 언어는 자유입니다 (Python, C, C++, Java, JavaScript 등).

## 📌 제출 문제 목록 (10개)

| 번호 | 문제 이름 | 링크 |
| ---- | --------- | ---- |
| 12904 | 가장 긴 팰린드롬 | https://school.programmers.co.kr/learn/courses/30/lessons/12904 |
| 120852 | 소인수분해 | https://school.programmers.co.kr/learn/courses/30/lessons/120852 |
| 12906 | 같은 숫자는 싫어 | https://school.programmers.co.kr/learn/courses/30/lessons/12906 |
| 12949 | 행렬의 곱셈 | https://school.programmers.co.kr/learn/courses/30/lessons/12949 |
| 120892 | 암호 해독 | https://school.programmers.co.kr/learn/courses/30/lessons/120892 |
| 12945 | 피보나치 수 | https://school.programmers.co.kr/learn/courses/30/lessons/12945 |
| 42885 | 구명보트 | https://school.programmers.co.kr/learn/courses/30/lessons/42885 |
| 12953 | N개의 최소공배수 | https://school.programmers.co.kr/learn/courses/30/lessons/12953 |
| 12921 | 소수찾기 | https://school.programmers.co.kr/learn/courses/30/lessons/12921 |
| 132267 | 콜라 문제 | https://school.programmers.co.kr/learn/courses/30/lessons/132267 |

## Pull Request 생성

- **base** repository: `KNU-HAEDAL/2026-haedal-hackthon-submissions`
- base branch: `main`
- **head** repository: `yourID/2026-haedal-hackthon-submissions`
- compare branch: `main`

## 📌 PR 작성 규칙

- **PR 제목**: `[준회원과제_본인이름] Programmers_ID`
- **PR 본문**: 아래 템플릿 형식 준수 (PR 생성 시 자동으로 채워집니다)

```markdown
### 👤 Programmers 아이디
`your_programmers_id`

### 📒 제출한 문제 (10개) & 통과 인증 스크린샷

**12904 - 가장 긴 팰린드롬**
<!-- 스크린샷을 여기에 드래그&드롭 -->

**120852 - 소인수분해**
<!-- 스크린샷을 여기에 드래그&드롭 -->

**12906 - 같은 숫자는 싫어**
<!-- 스크린샷을 여기에 드래그&드롭 -->

**12949 - 행렬의 곱셈**
<!-- 스크린샷을 여기에 드래그&드롭 -->

**120892 - 암호 해독**
<!-- 스크린샷을 여기에 드래그&드롭 -->

**12945 - 피보나치 수**
<!-- 스크린샷을 여기에 드래그&드롭 -->

**42885 - 구명보트**
<!-- 스크린샷을 여기에 드래그&드롭 -->

**12953 - N개의 최소공배수**
<!-- 스크린샷을 여기에 드래그&드롭 -->

**12921 - 소수찾기**
<!-- 스크린샷을 여기에 드래그&드롭 -->

**132267 - 콜라 문제**
<!-- 스크린샷을 여기에 드래그&드롭 -->
```

## 통과 확인
PR을 올리면 GitHub Actions CI가 두 가지를 자동으로 검사합니다:

1. **코드 파일 확인** — `problems/<ID>/` 폴더에 10개 파일이 모두 있는지 체크
2. **스크린샷 확인** — PR 본문에 이미지가 10개 이상 첨부되어 있는지 체크

두 항목 모두 통과되면 ✅ 체크가 표시됩니다.

## ⚠️ 주의사항
- 폴더명은 반드시 **본인 Programmers 아이디**와 일치해야 합니다
- 파일명은 반드시 **`<문제번호>.<확장자>`** 형식이어야 합니다 (예: `12904.py`)
- PR 본문의 백틱(`` ` ``) 안 아이디가 폴더명과 일치해야 CI가 통과됩니다
- **각 문제 통과 스크린샷 10개를 PR 본문에 반드시 첨부해야 합니다**
