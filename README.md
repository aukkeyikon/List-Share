# list_share

## 動機
TwitterのListを非公開じゃなくて限定公開みたいにしたいなぁと思って作った。

## 機能
#### getAllList.py
入力したUserが持っているリストの一覧を返してくれる

#### addListUser_fromText.py
リストのOwnerと名前(getAllList.pyで返されるslug)を入力すると、指定した形(screen_nameもしくはID)で.txtを返してくれる
この.txtを共有すると限定公開っぽいことができる。

#### getListUserAll.py
addListUser_fromText.pyで出力されたデータを読み取って、リストを新たに作成する。

---
## 補足
応用することでリストの複製も可能。
リストの名前は英数字で構成されているのならslugを気にすることなく作成することができる。
