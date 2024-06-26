# 🚩 for-me-classification
**[[2024-1 KGU Capstone Project]](https://github.com/Jhyunee/for-me) koBERT 모델을 이용한 다중 분류 모델** <br>

### In this repository ... <br>
      🚀 Run pytorch Classification model on Flask Server
      🚀 Connect SpringBoot & Flask

### Content
  [1. ⚙️ Environment Settings](#%EF%B8%8F-environment-settings)  <br>
  [2. 🏃🏻‍♀️ Run Flask Server](#%EF%B8%8F-run-flask-server)  <br>
  [3. 🍃 SpringBoot 연동 Test](#-springboot-연동-test)

<br>
<br>

## ⚙️ Environment Settings

  **1. Download [Python 3.7.9](https://www.python.org/downloads/release/python-379/) if not exist** <br>
  * Windows x86-64 executable installer 
  * _설치 경로 ex. (C:\Python37)_

<br>
  
  **2. VSC settings > python.python path 검색** <br>
  * _Python: Default Interpreter Path = (C:\Python37) 지정 - 1. 파이썬 설치 경로_ <br>
  	![image](https://github.com/Jhyunee/for-me-classification/assets/104143072/806d9252-8df9-4bdd-a6c4-04881a5262a2)

  * `$ python -V # 3.7.9 ` ✅


<br>
  
  **3. 가상환경 생성 (create virtual env)**
  * 빈 폴더 _(C:\KGU\model)_ 생성 → vsc에서 file > open folder
  * In VSC terminal
    * `$ python -m venv test`  _# test 이름의 가상환경 생성_
    * 잘 생성되면 model 밑에 test 폴더 생김 _(C:\KGU\model\test)_

<br>
  
  **4. pyvenv.cfg 확인**
```
      home = C:\Python37  # (1.에서 설치한 Python 3.7.9 path)
      include-system-site-packages = true
```

<br>
  
  **5. 가상환경 실행**
```
      $ cd test
      $ cd scripts
      $ activate.bat
      # 종료 시 deactivate
```

<br>

  **6. Python interpreter : test**
  * 위에서 만든 가상환경(test)으로 지정
    * 단축키 [ctrl + shift + p] 에서 python interpreter 검색
    * 안보일 경우 refresh 🔃
  * 잘 설정이 된 경우 밑에서 app.py 파일 열면 우하단에서 확인 가능
    ![image](https://github.com/Jhyunee/for-me-classification/assets/104143072/60b9446b-f155-4338-a020-827c12ba7260)


<br>

  **7. File Setting**
➡️ 모두 test 폴더 내로 _(C:\KGU\model\test)_
  * [for-me-classification repository](https://github.com/Jhyunee/for-me-classification) 파일 다운로드 <br>
    `app.py` <br>
	  `model.py` <br>
	  `requirements.txt` <br>
  * 1_made_test_state.pt 파일 다운로드 <br>

<br>

  **8. requirements 설치**
```
  # requirements.txt 파일이 있는 경로(test)에서 실행 - 상위 폴더로 이동 = $ cd..
  # target path =  YOUR_VENV_PATH
  $ python -m  pip install -r requirements.txt --target C:\KGU\model\test\Lib\site-packages
```
  ![image](https://github.com/Jhyunee/for-me-classification/assets/104143072/97aef0b3-6ae9-4a48-8c81-d87ee4a83090)
  * 위와 같이 에러 나와도 👌🏻🆗
  * 여기까지 설정이 모두 완료 되면 ⬇️

<br>
  
### 🗂️ Your File Path should be like ...

```
📦model
 ├── 📂test
 │    ├── 📂__pychache__
 │    ├── 📂Include
 │    ├── 📂Lib
 │    ├── 📂Scripts
 │    ├── 📜1_made_test_state.pt
 │    ├── 📜app.py
 │    ├── 📜model.py
 │    ├── 📜pyvenv.cfg
```

<br>
<br>

## 🏃🏻‍♀️ Run Flask Server
  * Run app.py ▶️
  * default port : **localhost:5000/**
  * Success Running Flask server 👍🏻
    ![image](https://github.com/Jhyunee/for-me-classification/assets/104143072/5e302b6a-4ced-45a8-ae1e-4e363604efc3)

<br>

### ⚠️ If ERROR occurs ...

  * `OSError ~ : Illegal byte sequence Error` 아래와 같은 형식의 오류 <br>
  * 원인 : 경로에 한글이 있어서 나는 에러
  * 해결 : ⬇️

**1. C:\KGU\model\test\Lib\site-packages\sentencepiece\__init__.py 수정**
   ```
        def LoadFromFile(self, arg):
          try:
            arg = arg.replace("\\","/")
            return _sentencepiece.SentencePieceProcessor_LoadFromFile(self, arg)
          except OSError:
            # YOUR_PT_FILE_PATH
            path = "C:/KGU/model/test/" # test ; your virtunal env name
            arg = path + arg.split("/")[-1]
            return _sentencepiece.SentencePieceProcessor_LoadFromFile(self, arg)
   ```

<br>

**2. 파란 라인 경로 따라가서 해당 파일 복사 → test 파일 내에 붙이기**
  ![image](https://github.com/Jhyunee/for-me-classification/assets/104143072/0a22f303-c8c1-4804-9c9e-c6fe09426ecb)
  * test 파일 외 다른 곳에 위치시키고 싶다면 위의 except문 path 수정!


<br>
<br>

## 🍃 SpringBoot 연동 Test
  * Flask ↔️ SpringBoot 데이터 주고 예측값 받기

  **1. Flask 서버 켜기**
  * 가상환경 실행
  * app.py 실행
  * 확인 : `localhost:5000`

<br>

  **2. [for-me](https://github.com/ongsim0629/for-me) Spring 서버 켜기 (Backend)**
  * `localhost:8080/api/checklists` 에 데이터 POST (postman 이용) <br>
  ```
	{
		"name": # YOUR_CHECKLIST_TEST_DATA
		"user_id": # YOUR_TEST_ID
	}
  ```

<br>

  ### 👏🏻 All Succeeded !
  * **Spring ➡️ Flask 보낸 데이터 확인** 
    `>>> Data from Springboot : # YOUR_CHECKLIST_TEST_DATA`

  * **Flask ➡️ Spring 받은 예측값 확인**
    `"category": # YOUR_PREDICT_RESULT`
    * 예측값은 `localhost:5000/send` 에서도 확인 가능
    
    ![image](https://github.com/Jhyunee/for-me-classification/assets/104143072/82841d87-750b-429e-8849-985abec34e47)
