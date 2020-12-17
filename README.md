# Gui_auto_mkdirs2

## 概要

自動でフォルダを作成するGUIアプリケーションです。  
詳しい解説はQittaに載せてるので[こちら]()を参照して下さい。
</br>

## 開発環境

|              OS         |      言語    |    ライブラリ   |
|:-----------------------:|:------------:|:---------------:|
| Windows 10 version 1909 | Python 3.9.1 | Pyinstaller 4.1 |  
</br>
ライブラリのインストール 

```
pip install pyinstaller
```

</br>

## ツールの使い方
1. リポジトリにあるbinフォルダの**GUI_auto_dirs2.exe**を実行して下さい。
2. 実行するとフォルダ名(番号付き)のタブと都道府県名(番号付き)のタブがあります。2つの動作手順は以下のようになります。        
---
- フォルダ名(番号付き)の作成手順は次の通りです。 
1. フォルダ名(番号付き)のタブを押します。
2. フォルダ参照📁で作成先フォルダのパスを指定します。
3. フォルダ名とフォルダ作成個数を入力します。
4. 数字の表記を選択します。
5. 「実行」ボタンを押すと参照先パスに指定した条件でフォルダが作成されます。
6. 「閉じる」ボタンでウィンドウを閉じることができます。
    - 実行動作は以下のようになります。</br>
<img width="50%" alt="フォルダ作成動画1.gif" src="https://user-images.githubusercontent.com/70006535/102442251-506c0e00-4067-11eb-954d-6aa8765aeacc.gif">
</br>
</br>

-  都道府県名(番号付き)の作成手順は次の通りです。
1. 都道府県名(番号付き)のタブを押します。
2. フォルダ参照📁で作成先フォルダのパスを指定します。
3. 作成したい都道府県名のフォルダ名を選択します。
5. 「実行」ボタンを押すと参照先パスに番号付きフォルダが作成されます。</br>尚、選択した都道府県名は北海道から沖縄県の順で、1~47の番号振りがされます。
6. 「閉じる」ボタンでウィンドウを閉じることができます。
    - 実行動作は以下のようになります。</br>
<img width="50%" alt="フォルダ作成動画2.gif" src="https://user-images.githubusercontent.com/70006535/102441755-3bdb4600-4066-11eb-8efe-dbc592dc138b.gif">

## プログラム
| ファイル名 |                   ファイル説明                      | 
|:----------:|:---------------------------------------------------:|
| main.py    | メインで実行し、主にGUIウィンドウを構成するファイル |  
| mkdirs.py  | フォルダを作成する関数をパッケージ化したファイル    |  
| ion.txt    | アイコン用のbase64データファイル                    |  

## 実行ファイル(.exe)を作成
実行ファイルを作成するためにコマンド(CUI)操作をします。

```:terminal
pyinstaller main.py --onefile --noconsole --icon=icon/desktopicon.ico
```

**icon.txt**が読み込めていないため、エラーが出ます。  
次に、**icon.txt**を読み込みために**main.spec**を書き換えをします。

```diff
# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['gui_auto_mkdirs2.py'],
             pathex=['C:\\Users\\...\\main.py],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
+ a.datas += [("icon.txt", ".//icon.txt", "DATA")]
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='gui_auto_mkdirs2',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False )

```

再び、ターミナルに戻り、次のコマンドを入力して実行していきます。

```:terminal
pyinstaller main.spec
```

実行した結果、**dist**フォルダに実行ファイルが生成されます。
