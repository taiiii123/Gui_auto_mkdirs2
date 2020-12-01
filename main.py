import copy
import functools
import os
import sys

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog

# 自作モジュールをインポート
from mkdirs import *


class GuiApplication(ttk.Notebook):

    def __init__(self, master=None):
        super().__init__(master)

        style = ttk.Style()
        style.configure('new.TFrame',foreground='black', background='white')

        tab1 = ttk.Frame(self.master, style='new.TFrame')
        tab2 = ttk.Frame(self.master, style='new.TFrame')

        self.add(tab1, text='フォルダ名(番号付き)')
        self.add(tab2, text='都道府県名(番号付き)')

        Tab1(master=tab1)
        Tab2(master=tab2)

        self.pack()

    # ユーザーがディレクトリを指定する関数
    def dirdialog_clicked(self, entry):
        iDir = os.path.abspath(os.path.dirname(sys.argv[0]))
        iDir_path = filedialog.askdirectory(initialdir=iDir)
        entry.set(iDir_path)


class Tab1(ttk.Frame, GuiApplication):

    def __init__(self, master=None):
        super().__init__(master)

        style = ttk.Style()
        style.configure('Tab1.TFrame',foreground='black', background='white')
    # ========================================================================================================
        # Tab1のFrame1の作成
        frame1_tab1 = ttk.Frame(master, padding=10, relief='groove', style='Tab1.TFrame')
        frame1_tab1.grid(row=0, column=1, padx=20, pady=10, ipadx=30, sticky=E)

        # 「フォルダ参照」ラベルの作成
        dir_label = ttk.Label(frame1_tab1, text='フォルダ参照＞＞', padding=(25, 5, 5, 0), background='white')
        dir_label.pack(side=LEFT)

        # 「フォルダ参照」エントリーの作成
        self.entry1_tag1 = StringVar()
        dir_entry = ttk.Entry(frame1_tab1, textvariable=self.entry1_tag1, width=30)
        dir_entry.pack(side=LEFT)

        # 「フォルダ参照」ボタンの作成
        dir_button = ttk.Button(frame1_tab1, text='参照', command=lambda :super(Tab1, self).dirdialog_clicked(self.entry1_tag1))
        dir_button.pack(side=LEFT)
    # ========================================================================================================

        # Tab1のFrame2の作成
        frame2_tab1 = ttk.Frame(master, padding=10, style='Tab1.TFrame')
        frame2_tab1.grid(row=2, column=1, padx=20, sticky=E)

        # 「フォルダ名:」ラベルの作成
        dir_name_label= ttk.Label(frame2_tab1, text='フォルダ名:', padding=(5, 0), background='white')
        dir_name_label.pack(side=LEFT)

        # 「フォルダ名」エントリーの作成
        self.entry2_tag1 = StringVar()
        dir_name_entry= ttk.Entry(frame2_tab1, textvariable=self.entry2_tag1, justify='right', width=20)
        dir_name_entry.pack(side=LEFT)

        dir_name_label = ttk.Label(frame2_tab1, text='__', background='white')
        dir_name_label.pack(side=LEFT)

        # 「番号:」ラベルの作成
        dir_name_label = ttk.Label(frame2_tab1, text='No.', padding=(5, 0), background='white')
        dir_name_label.pack(side=LEFT)

        # 「フォルダ番号」エントリーの作成
        self.entry3_tag1 = StringVar()
        dir_nums_entry = ttk.Entry(frame2_tab1, textvariable=self.entry3_tag1, justify='right', width=10)
        dir_nums_entry.pack(side=LEFT)

        # 「まで」ラベルの作成
        until_dir_nums_label = ttk.Label(frame2_tab1, text='まで', padding=(0, 5, 8, 5), background='white')
        until_dir_nums_label.pack(side=LEFT)

        # コンボボックスの作成
        nums_kind = ["SERECT", "01-xx", "No.1-No.xx", "英語表記(One~)", "漢数字(一~)", "ローマ数字(I~)"]
        self.co = ttk.Combobox(frame2_tab1, state="readonly", values=nums_kind, width=12)
        self.co.set(nums_kind[0])
        self.co.pack(side=LEFT, padx=(2, 10))
    # ========================================================================================================
        # Tab1のFrame3の作成
        frame3_tab1 = ttk.Frame(master, padding=10, style='Tab1.TFrame')
        frame3_tab1.grid(row=4, column=1, padx=20, sticky=W)

        # 実行ボタンの設置
        create_dir_button = ttk.Button(frame3_tab1, text='作成', command=self.clicked_mkdir1)
        create_dir_button.pack(fill='x', padx=70, side='left')

        # キャンセルボタンの設置
        cancel_button = ttk.Button(frame3_tab1, text=('閉じる'), command=master.quit)
        cancel_button.pack(fill='x', padx=75, side='right')
    # ========================================================================================================

    # タブ1の「作成」ボタン押下時処理
    def clicked_mkdir1(self):
        dir_path = self.entry1_tag1.get()
        input_dirName = self.entry2_tag1.get()
        input_dirCount = self.entry3_tag1.get()

        if not dir_path and not input_dirName and not input_dirCount:
            messagebox.showerror('エラー', '何も入力されていません')
            return
        if not dir_path:
            messagebox.showerror('エラー', 'パスの指定がありません')
            return
        try:
            msg = messagebox.askyesno(
                '確認', 
                '作成先のパスはあっていますか?\n' +
                '--------------------------------\n' +
                '{}\n'.format(dir_path) + 
                '--------------------------------\n' +
                '作成しますがよろしいですか?')
            if msg == True:
                if int(input_dirCount) > 100:
                    messagebox.showwarning('警告', '最大、100個までのフォルダを作成することが可能です')
                    return
                if self.co.get() == "SERECT":
                    messagebox.showwarning('警告', '数字の表記が選択されていません')
                    return
                if self.co.get() == "01-xx":
                    mkdir_nums(dir_path, input_dirName, input_dirCount)
                elif self.co.get() == "No.1-No.xx":
                    mkdir_numbers(dir_path, input_dirName, input_dirCount)
                elif self.co.get() == "英語表記(One~)":
                    mkdir_eng_nums(dir_path, input_dirName, input_dirCount)
                elif self.co.get() == "漢数字(一~)":
                    mkdir_kansuuji(dir_path, input_dirName, input_dirCount)
                elif self.co.get() == "ローマ数字(I~)":
                    mkdir_roman_numbers(dir_path, input_dirName, input_dirCount)
                else:
                    return
                messagebox.showinfo('フォルダ作成情報', '{}個のフォルダが作成されました!'.format(input_dirCount))
        except ValueError:
            messagebox.showerror('エラー', '半角英数字で番号を入力してください')
        except Exception as e:
            print(e)



class Tab2(ttk.Frame, GuiApplication):

    def __init__(self, master=None):
        super().__init__(master)

        # 都道府県名の一覧情報
        self.TODOUFUKEN = ("北海道", "青森県", "岩手県", "宮城県", "秋田県", "山形県", "福島県", "茨城県", "栃木県", "群馬県",
                            "埼玉県", "千葉県", "東京都", "神奈川県", "新潟県", "富山県", "石川県", "福井県", "山梨県", "長野県",
                            "岐阜県", "静岡県", "愛知県", "三重県", "滋賀県", "京都府", "大阪府", "兵庫県", "奈良県", "和歌山県",
                            "鳥取県", "島根県", "岡山県", "広島県", "山口県", "徳島県", "香川県", "愛媛県", "高知県", "福岡県",
                            "佐賀県", "長崎県", "熊本県", "大分県", "宮崎県", "鹿児島県", "沖縄県")

        # チェックされたときに変更するリスト(リスト内:全てFalse)
        self.check_todoufuken = [False for fal in range(len(self.TODOUFUKEN))]

        # チェックボックスで選択された都道府県名を格納するリスト
        self.mkdirs_list = []

        style = ttk.Style()
        style.configure('Tab2.TFrame', foreground='black', background='white')
        style.configure('Tab2_OFF_Check.TCheckbutton', foreground='#000000', background='white')
        style.configure('Tab2_ON_Check.TCheckbutton', foreground='#0F1FFF', background='white')
    # ========================================================================================================
        # Tab2のFrame1の作成
        frame1_tab2 = ttk.Frame(master, padding=10, relief='groove', style='Tab2.TFrame')
        frame1_tab2.grid(row=0, column=1, padx=30, pady=10, ipadx=20, sticky=E)

        # 「フォルダ参照」ラベルの作成
        dir_label = ttk.Label(frame1_tab2, text='フォルダ参照＞＞', padding=(25, 5, 5, 0), background='white')
        dir_label.pack(side=LEFT)

        # 「フォルダ参照」エントリーの作成
        entry1_tag2 = StringVar()
        dir_entry = ttk.Entry(frame1_tab2, textvariable=entry1_tag2, width=30)
        dir_entry.pack(side=LEFT)

        # 「フォルダ参照」ボタンの作成
        dir_button = ttk.Button(frame1_tab2, text='参照', command=lambda :super(Tab2, self).dirdialog_clicked(entry1_tag2))
        dir_button.pack(side=LEFT)
    # ========================================================================================================
        # Tab2のFrame2の作成
        frame2_tab2 = LabelFrame(master, text='都道府県', background='white')
        frame2_tab2.grid(row=2, column=1, ipadx=0, ipady=5, sticky=N+S)

        # チェックボタンを設置
        # 10 × 5の行列 47個の項目
        cols = 5
        rows = (len(self.TODOUFUKEN) // cols) + 1  # 10

        for row in range(rows):  # 行
            for col in range(cols):  # 列
                v = BooleanVar()
                v.set(False)
                if (row+col*10) < len(self.TODOUFUKEN):  
                    f = functools.partial(self.after_cb, frame2_tab2, row, col, v)
                    cb = ttk.Checkbutton(frame2_tab2, padding=10, text=self.TODOUFUKEN[row+col*10], style='Tab2_OFF_Check.TCheckbutton',variable=v, command=f)  
                    cb.grid(row=row, column=col)

        # 「全選択」ボタンを設置
        slc_all_btn = functools.partial(self.check_all_checkeboxes, frame2_tab2, rows, cols)
        all_check_button = Button(frame2_tab2, text='全選択', command=slc_all_btn, overrelief='groove')
        all_check_button.grid(row=rows, column=3)

        unslc_all_btn = functools.partial(self.clear_all_checkeboxes, frame2_tab2, rows, cols)
        all_check_button = Button(frame2_tab2, text='全解除', command=unslc_all_btn, overrelief='groove')
        all_check_button.grid(row=rows, column=4)
    # ========================================================================================================
        # Tab2のFrame3の作成
        frame3_tab2 = ttk.Frame(master, padding=(0, 15, 0, 25), style='Tab2.TFrame')
        frame3_tab2.grid(row=4, column=1, padx=30, sticky=W)

        # 実行ボタンの設置
        create_dir_button = ttk.Button(frame3_tab2, text='作成', command=lambda: self.clicked_mkdir2(entry1_tag2))
        create_dir_button.pack(fill='x', padx=70, side='left')

        # キャンセルボタンの設置
        cancel_button = ttk.Button(frame3_tab2, text=('閉じる'), command=master.quit)
        cancel_button.pack(fill='x', padx=75, side='right')
    # ========================================================================================================

    # チェックボックスを押下したときの関数
    def after_cb(self, frame, row, col, var):
        if (row+col*10) > len(self.TODOUFUKEN):  
            return
        elif var.get() == True:
            self.check_todoufuken[row+col*10] = True
            f = functools.partial(self.after_cb, frame, row, col, var)
            cb = ttk.Checkbutton(frame, padding=10, text='{}'.format(self.TODOUFUKEN[row+col*10]), style='Tab2_ON_Check.TCheckbutton', variable=var, command=f)
            cb.grid(row=row, column=col)
        else:
            self.check_todoufuken[row+col*10] = False
            f = functools.partial(self.after_cb, frame, row, col, var)
            cb = ttk.Checkbutton(frame, padding=10, text='{}'.format(self.TODOUFUKEN[row+col*10]), style='Tab2_OFF_Check.TCheckbutton', variable=var, command=f)
            cb.grid(row=row, column=col)

        self.mkdirs_list = [self.TODOUFUKEN[i] for i in range(len(self.TODOUFUKEN)) if self.check_todoufuken[i] == True]

    # 「全選択」ボタンを押下したときの関数
    def check_all_checkeboxes(self, frame, rows, cols):
        self.mkdirs_list = list(copy.copy(self.TODOUFUKEN))
        self.check_todoufuken.clear()

        for _ in range(len(self.TODOUFUKEN)):
            self.check_todoufuken.append(True)

        for row in range(rows):
            for col in range(cols):
                v = BooleanVar()
                v.set(True)
                f = functools.partial(self.after_cb, frame, row, col, v)
                if (row+col*10) < len(self.TODOUFUKEN):
                    cb = ttk.Checkbutton(frame, padding=10, text=self.TODOUFUKEN[row+col*10], style='Tab2_ON_Check.TCheckbutton', variable=v, command=f)
                    cb.grid(row=row, column=col)

    # 「全解除」ボタンを押下したときの関数
    def clear_all_checkeboxes(self, frame, rows, cols):
        self.mkdirs_list.clear()
        self.check_todoufuken = [False for fal in range(len(self.TODOUFUKEN))]

        for row in range(rows):  # 行
            for col in range(cols):  # 列
                v = BooleanVar()
                v.set(False)
                f = functools.partial(self.after_cb, frame, row, col, v)
                if (row+col*10) < len(self.TODOUFUKEN):
                    cb = ttk.Checkbutton(frame, padding=10, text=self.TODOUFUKEN[row+col*10], style='Tab2_OFF_Check.TCheckbutton', variable=v, command=f)  
                    cb.grid(row=row, column=col)

    # タブ2の「作成」ボタンを押したときの処理
    def clicked_mkdir2(self, entry1_tag2):
        dir_path = entry1_tag2.get()
        if not dir_path:
            messagebox.showerror('エラー', 'パスの指定がありません')
            return
        try:
            if not self.mkdirs_list:
                messagebox.showerror('エラー', '都道府県名が選択されていません')
                return
            else:
                msg = messagebox.askyesno(
                '確認', 
                '作成先のパスはあっていますか?\n' +
                '--------------------------------\n' +
                '{}\n'.format(dir_path) + 
                '--------------------------------\n' +
                '作成しますがよろしいですか?')
                if msg == True:
                    mkdir_todoufuken(dir_path, self.mkdirs_list)
                    messagebox.showinfo('フォルダ作成情報', 'フォルダが作成されました')
                    return

        except FileExistsError:
            messagebox.showwarning('警告', '既に同じ名前のフォルダが存在します')
            return


if __name__ == "__main__":

    # rootの作成
    root = Tk()
    root.title('自動フォルダ作成ツール')
    root.configure(background='white')

    def resource_path(relative_path):
        if hasattr(sys, '_MEIPASS'):
            return os.path.join(sys._MEIPASS, relative_path)
        return os.path.join(os.path.abspath("."), relative_path)

    # アイコンデータを読み込み(Base64)
    icon_text = resource_path('icon.txt')
    with open(icon_text, 'r') as f:
        icon_data = f.read()

    # アイコンの設置(base64)
    root.tk.call('wm', 'iconphoto', root._w, PhotoImage(data=icon_data))
    
    app = GuiApplication(master=root)

    winsize = {
        'フォルダ名(番号付き)': "500x190",
        '都道府県名(番号付き)': "500x580",
    }

    def changed(event):
        nb = event.widget
        text = nb.tab(nb.select(), 'text')
        if text in winsize:
            root.geometry(winsize[text])
    app.bind('<<NotebookTabChanged>>', changed)

    app.mainloop()

# spec
# a.datas += [("icon.txt", ".//icon.txt", "DATA")]
# app = BUNDLE(exe,
            #  name='Main.app',
            # info_plist={ 'NSHighResolutionCapable': 'True'})