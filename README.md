## all-travel
이 프로그램은 여러 기능을 포함하는 여행 프로그램입니다. 이 프로그램을 통해 사용자는 키워드, 월로 여행지를 추천받을 수 있습니다. 또한 예산 관리를 위해 전체 예산을 등록하고 지출을 등록하면 잔액을 확인할 수 있습니다. 간단한 메모와 사진 등록을 통해 앨범을 만들어 여행지의 추억을 남길 수 있으며 친구 등록도 가능합니다.

## 구현 언어
Python

## 개발 환경
vscode

## 준비 단계
우선 프로그램 실행 전 cmd에서 pip install pillow를 통해 pillow를 설치해야 합니다.

## 실행 과정
1. 로그인 : main.py를 실행시키면 초기 로그인 화면이 보입니다. 로그인 화면에서는 UserID와 Password를 입력 후 Login 버튼을 통해 로그인할 수 있습니다.

2. 회원가입 : 회원가입을 하기 위해서는 초기 로그인 화면에서 Sign up 버튼을 통해 회원가입 창을 열 수 있습니다. 회원가입을 위해서 UserID, Password, Name, Email을 입력하고 Sign up 버튼을 누르면 회원가입이 완료됩니다.

3. 로그아웃 : 로그인한 뒤 보이는 화면은 메인 화면입니다. 해당 화면에서 Logout 버튼을 통해 로그아웃이 가능합니다.

4. 키워드, 월로 여행지 추천 : 키워드로 여행지를 추천받으려면 메인화면에서 Search Travel by Keyword 버튼을 누르고 Select Keyword 옆에 있는 버튼을 통해 키워드를 선택한 뒤 Search 버튼을 누르면 됩니다. Back을 통해 메인화면으로 돌아갈 수 있습니다.
마찬가지로 메인화면에서 Search Travel by Month 버튼을 누르고 Select Month 옆에 있는 버튼을 통해 월을 선택한 뒤 Search 버튼을 누르면 월로 여행지를 추천받을 수 있습니다.

5. 예산 관리 : 예산 관리 기능을 사용하려면 메인화면에서 Budget Management 버튼을 누르면 됩니다. 이후 Budget ID(예산 관리 ID로 임의로 정하면 됩니다.), Total Amount(총예산)를 입력하고 Create Budget 버튼을 누르면 총예산 등록이 완료됩니다. 이후 Add Expense 버튼을 통해 지출을 입력하고 Add Expense 버튼을 누른 뒤 Check Remaining Budget 버튼을 누르면 남은 예산을 확인할 수 있습니다. Back을 통해 메인화면으로 돌아올 수 있습니다.

6. 앨범 : 메인화면에서 Album 버튼을 누르면 앨범 기능을 사용할 수 있습니다. Register Photo 버튼을 누르고 Select Photo 버튼을 통해 사진을 앨범에 등록할 수 있고, Register Memo 버튼을 누르고 메모를 입력한 뒤 Register Memo 버튼을 눌러 메모를 앨범에 등록할 수 있습니다. 이후 Check Album 버튼을 통해 등록된 사진과 메모로 만들어진 앨범을 확인할 수 있습니다. Back을 통해 메인화면으로 돌아올 수 있습니다.
