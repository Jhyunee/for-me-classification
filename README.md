# for-me-classification
[2024-1 KGU Capstone Project] koBERT 모델을 이용한 다중 분류 모델
<br>
<br>

### ⚙️ Environment Settings
  1. Download [Python 3.7.9](https://www.python.org/downloads/release/python-379/) if not exist
     * Windows x86-64 executable installer
     * _(C:)_
  3. Create empty folder (model)
     * Place repository files in model directory
     * _(C:/KGU/model)_
  5. Open terminal in VSC, create virtual env (test)
     * _ctrl + shift + p_
     * `py -3.7 -m venv test`
  6. Activate virtual env (test) <br>
     > `cd test` <br> `cd scripts` <br> `activate.bat` <br>
     > `(deactivate)`
  7. `pip install -r requirements.txt`

<br>

### 🗂️ Final File Path

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
 │    ├── 📜spiece.model
```

<br>

### 🏃🏻‍♀️ Run app.py
  * default port : localhost:5000/test
  * _경로를 다르게 했을 경우, 에러 시 sentencepiece 수정_
