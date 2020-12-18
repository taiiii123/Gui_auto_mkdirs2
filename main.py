import copy
import functools
import os
import re
import sys

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog

from mkdirs import *


class GuiApplication(ttk.Notebook):

    def __init__(self, master=None):
        super().__init__(master)

        # Tabに適用する文字と背景の色の設定
        tab_style = ttk.Style()
        tab_style.configure(
            'new.TFrame', foreground='black', background='white')

        tab1 = ttk.Frame(self.master, style='new.TFrame')
        tab2 = ttk.Frame(self.master, style='new.TFrame')

        self.add(tab1, text='フォルダ名(番号付き)')
        self.add(tab2, text='都道府県名(番号付き)')

        Tab1(master=tab1)
        Tab2(master=tab2)

        self.pack()

    def dirdialog_clicked(self, entry):
        iDir = os.path.abspath(os.path.dirname(sys.argv[0]))
        iDir_path = filedialog.askdirectory(initialdir=iDir)
        entry.set(iDir_path)


class Tab1(ttk.Frame, GuiApplication):

    def __init__(self, master=None):
        super().__init__(master)

        style = ttk.Style()
        style.configure('Tab1.TFrame', foreground='black', background='white')
    # ========================================================================================================
        frame1_tab1 = ttk.Frame(
            master, padding=10, relief='groove', style='Tab1.TFrame')
        frame1_tab1.grid(row=0, column=1, padx=20, pady=10, ipadx=30, sticky=E)

        dir_label = ttk.Label(frame1_tab1, text='フォルダ参照＞＞',
                              padding=(25, 5, 5, 0), background='white')
        dir_label.pack(side=LEFT)

        self.entry1_tag1 = StringVar()
        dir_entry = ttk.Entry(
            frame1_tab1, textvariable=self.entry1_tag1, width=30)
        dir_entry.pack(side=LEFT)

        dir_button = ttk.Button(frame1_tab1, text='参照', command=lambda: super(
            Tab1, self).dirdialog_clicked(self.entry1_tag1))
        dir_button.pack(side=LEFT)
    # ========================================================================================================
        frame2_tab1 = ttk.Frame(master, padding=10, style='Tab1.TFrame')
        frame2_tab1.grid(row=2, column=1, padx=20, sticky=E)

        dir_name_label = ttk.Label(
            frame2_tab1, text='フォルダ名:', padding=(5, 0), background='white')
        dir_name_label.pack(side=LEFT)

        self.entry2_tag1 = StringVar()
        dir_name_entry = ttk.Entry(
            frame2_tab1, textvariable=self.entry2_tag1, justify='right', width=20)
        dir_name_entry.pack(side=LEFT)

        dir_name_label = ttk.Label(frame2_tab1, text='__', background='white')
        dir_name_label.pack(side=LEFT)

        dir_name_label = ttk.Label(
            frame2_tab1, text='No.', padding=(5, 0), background='white')
        dir_name_label.pack(side=LEFT)

        self.entry3_tag1 = StringVar()
        dir_nums_entry = ttk.Entry(
            frame2_tab1, textvariable=self.entry3_tag1, justify='right', width=10)
        dir_nums_entry.pack(side=LEFT)

        until_dir_nums_label = ttk.Label(
            frame2_tab1, text='まで', padding=(0, 5, 8, 5), background='white')
        until_dir_nums_label.pack(side=LEFT)

        nums_kind = ["SERECT", "01-xx", "No.1-No.xx",
                     "英語表記(One~)", "漢数字(一~)", "ローマ数字(I~)"]
        self.co = ttk.Combobox(
            frame2_tab1, state="readonly", values=nums_kind, width=12)
        self.co.set(nums_kind[0])
        self.co.pack(side=LEFT, padx=(2, 10))
    # ========================================================================================================
        frame3_tab1 = ttk.Frame(master, padding=10, style='Tab1.TFrame')
        frame3_tab1.grid(row=4, column=1, padx=20, sticky=W)

        create_dir_button = ttk.Button(
            frame3_tab1, text='作成', command=self.clicked_mkdir_button)
        create_dir_button.pack(fill='x', padx=70, side='left')

        cancel_button = ttk.Button(
            frame3_tab1, text=('閉じる'), command=master.quit)
        cancel_button.pack(fill='x', padx=75, side='right')
    # ========================================================================================================

    def clicked_mkdir_button(self):
        dir_path = self.entry1_tag1.get()
        input_dirName = self.entry2_tag1.get()
        input_dirCount = self.entry3_tag1.get()

        match_head_drive_path = re.search(r'^[A-Z]:/', dir_path)

        if (dir_path, input_dirName, input_dirCount) == (False, False, False):
            messagebox.showerror('エラー', '何も入力されていません。')
            return
        if not dir_path:
            messagebox.showerror('エラー', 'パスの指定がありません。')
            return
        elif not match_head_drive_path:
            messagebox.showerror('エラー', '正しいパスを入力してください!')
            return

        try:
            ismessage = messagebox.askyesno(
                '確認',
                '作成先のパスはあっていますか?\n'
                + '-------------------------------------------------------------------------------\n'
                + '{}\n'.format(dir_path)
                + '-------------------------------------------------------------------------------\n'
                + '作成しますがよろしいですか?')
            if ismessage == True:
                if int(input_dirCount) > 100:
                    messagebox.showwarning('警告', '最大、100個までのフォルダを作成することが可能です。')
                    return
                if self.co.get() == "SERECT":
                    messagebox.showwarning('警告', '数字の表記が選択されていません。')
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
                messagebox.showinfo(
                    'フォルダ作成情報', '{}個のフォルダが作成されました!'.format(input_dirCount))
                return
        except ValueError:
            messagebox.showerror('エラー', '半角英数字で番号を入力してください。')
            return
        except Exception as e:
            print('エラー :', e)
            messagebox.showerror('エラー', '予期しないエラーが発生しました。')
            return


class Tab2(ttk.Frame, GuiApplication):

    def __init__(self, master=None):
        super().__init__(master)

        self.TODOUFUKEN = ("北海道", "青森県", "岩手県", "宮城県", "秋田県", "山形県", "福島県", "茨城県", "栃木県", "群馬県",
                           "埼玉県", "千葉県", "東京都", "神奈川県", "新潟県", "富山県", "石川県", "福井県", "山梨県", "長野県",
                           "岐阜県", "静岡県", "愛知県", "三重県", "滋賀県", "京都府", "大阪府", "兵庫県", "奈良県", "和歌山県",
                           "鳥取県", "島根県", "岡山県", "広島県", "山口県", "徳島県", "香川県", "愛媛県", "高知県", "福岡県",
                           "佐賀県", "長崎県", "熊本県", "大分県", "宮崎県", "鹿児島県", "沖縄県")

        #  チェックされたときに変更するリスト(リスト内:全てFalse)
        self.check_todoufuken = [False for fal in range(len(self.TODOUFUKEN))]

        # チェックボックスで選択された都道府県名を格納するリスト
        self.mkdirs_list = []

        style = ttk.Style()
        style.configure('Tab2.TFrame', foreground='black', background='white')
        style.configure('OFF_Checkbox.TCheckbutton',
                        foreground='#000000', background='white')
        style.configure('ON_Checkbox.TCheckbutton',
                        foreground='#0F1FFF', background='white')
    # ========================================================================================================
        frame1_tab2 = ttk.Frame(
            master, padding=10, relief='groove', style='Tab2.TFrame')
        frame1_tab2.grid(row=0, column=1, padx=30, pady=10, ipadx=20, sticky=E)

        dir_label = ttk.Label(frame1_tab2, text='フォルダ参照＞＞',
                              padding=(25, 5, 5, 0), background='white')
        dir_label.pack(side=LEFT)

        entry1_tag2 = StringVar()
        dir_entry = ttk.Entry(frame1_tab2, textvariable=entry1_tag2, width=30)
        dir_entry.pack(side=LEFT)

        dir_button = ttk.Button(frame1_tab2, text='参照', command=lambda: super(
            Tab2, self).dirdialog_clicked(entry1_tag2))
        dir_button.pack(side=LEFT)
    # ========================================================================================================
        frame2_tab2 = LabelFrame(master, text='都道府県', background='white')
        frame2_tab2.grid(row=2, column=1, ipadx=0, ipady=5, sticky=N+S)

        cols = 5
        rows = (len(self.TODOUFUKEN) // cols) + 1  # 10
        self.place_checkboxes_for_prefectures(
            rows, cols, frame2_tab2, checkset=False, checkcolor='OFF_Checkbox.TCheckbutton')

        select_all_button = functools.partial(
            self.check_all_checkeboxes, frame2_tab2, rows, cols)
        all_check_button = Button(
            frame2_tab2, text='全選択', command=select_all_button, overrelief='groove')
        all_check_button.grid(row=rows, column=3)

        unselect_all_button = functools.partial(
            self.clear_all_checkeboxes, frame2_tab2, rows, cols)
        all_check_button = Button(
            frame2_tab2, text='全解除', command=unselect_all_button, overrelief='groove')
        all_check_button.grid(row=rows, column=4)
    # ========================================================================================================
        frame3_tab2 = ttk.Frame(master, padding=(
            0, 15, 0, 25), style='Tab2.TFrame')
        frame3_tab2.grid(row=4, column=1, padx=30, sticky=W)

        create_dir_button = ttk.Button(
            frame3_tab2, text='作成', command=lambda: self.clicked_mkdirs_todoufuken(entry1_tag2))
        create_dir_button.pack(fill='x', padx=70, side='left')

        cancel_button = ttk.Button(
            frame3_tab2, text=('閉じる'), command=master.quit)
        cancel_button.pack(fill='x', padx=75, side='right')
    # ========================================================================================================

    def place_checkboxes_for_prefectures(self, rows, cols, frame, checkset=None, checkcolor=None):
        for row in range(rows):  
            for col in range(cols):  
                v = BooleanVar()
                v.set(checkset)
                if (row + col*10) < len(self.TODOUFUKEN):
                    f = functools.partial(self.after_cb, frame, row, col, v)
                    cb = ttk.Checkbutton(
                        frame, padding=10, text=self.TODOUFUKEN[row + col*10], style=checkcolor, variable=v, command=f)
                    cb.grid(row=row, column=col)

    def after_cb(self, frame, row, col, var):
        if (row + col*10) > len(self.TODOUFUKEN):
            return
        elif var.get() == True:
            self.check_todoufuken[row + col*10] = True
            f = functools.partial(self.after_cb, frame, row, col, var)
            cb = ttk.Checkbutton(frame, padding=10, text='{}'.format(
                self.TODOUFUKEN[row + col*10]), style='ON_Checkbox.TCheckbutton', variable=var, command=f)
            cb.grid(row=row, column=col)
        else:
            self.check_todoufuken[row + col*10] = False
            f = functools.partial(self.after_cb, frame, row, col, var)
            cb = ttk.Checkbutton(frame, padding=10, text='{}'.format(
                self.TODOUFUKEN[row + col*10]), style='OFF_Checkbox.TCheckbutton', variable=var, command=f)
            cb.grid(row=row, column=col)

        self.mkdirs_list = [self.TODOUFUKEN[i] for i in range(
            len(self.TODOUFUKEN)) if self.check_todoufuken[i] == True]

    def check_all_checkeboxes(self, frame, rows, cols):
        self.mkdirs_list = list(copy.copy(self.TODOUFUKEN))
        self.check_todoufuken.clear()

        for _ in range(len(self.TODOUFUKEN)):
            self.check_todoufuken.append(True)

        self.place_checkboxes_for_prefectures(
            rows, cols, frame, checkset=True, checkcolor='ON_Checkbox.TCheckbutton')

    def clear_all_checkeboxes(self, frame, rows, cols):
        self.mkdirs_list.clear()
        self.check_todoufuken = [False for fal in range(len(self.TODOUFUKEN))]

        self.place_checkboxes_for_prefectures(
            rows, cols, frame, checkset=False, checkcolor='OFF_Checkbox.TCheckbutton')

    def clicked_mkdirs_todoufuken(self, entry1_tag2):
        dir_path = entry1_tag2.get()

        match_head_drive_path = re.search(r'^[A-Z]:/', dir_path)

        if not dir_path:
            messagebox.showerror('エラー', 'パスの指定がありません。')
            return
        elif not match_head_drive_path:
            messagebox.showerror('エラー', '正しいパスを入力してください!')
            return
        try:
            if not self.mkdirs_list:
                messagebox.showerror('エラー', '都道府県名が選択されていません。')
                return
            else:
                ismessage = messagebox.askyesno(
                    '確認',
                    '作成先のパスはあっていますか?\n'
                    + '-------------------------------------------------------------------------------\n'
                    + '{}\n'.format(dir_path)
                    + '-------------------------------------------------------------------------------\n'
                    + '作成しますがよろしいですか?')
                if ismessage == True:
                    mkdir_todoufuken(dir_path, self.mkdirs_list)
                    messagebox.showinfo('フォルダ作成情報', 'フォルダが作成されました。')
                    return
        except FileExistsError:
            messagebox.showwarning('警告', '既に同じ名前のフォルダが存在します。')
            return
        except Exception as e:
            print('エラー', e)
            messagebox.showerror('エラー', '予期しないエラーが発生しました。')
            return


if __name__ == "__main__":

    win = Tk()
    win.title('自動フォルダ作成ツール')
    win.configure(background='white')

    # icon.txtまでのパスを取得
    def resource_path(relative_path):
        if hasattr(sys, '_MEIPASS'):
            return os.path.join(sys._MEIPASS, relative_path)
        return os.path.join(os.path.abspath("."), relative_path)

    # ウィンドウの大きさ変更イベント
    def changed_tab(event):
        nb = event.widget
        text = nb.tab(nb.select(), 'text')
        if text in winsize:
            win.geometry(winsize[text])

    icon_text = resource_path('icon/icon.txt')
    with open(icon_text, 'r') as f:
        icon_data = f.read()

    # アイコンの設置(base64)
    win.tk.call('wm', 'iconphoto', win._w, PhotoImage(data=icon_data))

    app = GuiApplication(master=win)

    winsize = {
        'フォルダ名(番号付き)': "500x190",
        '都道府県名(番号付き)': "500x580",
    }

    app.bind('<<NotebookTabChanged>>', changed_tab)

    app.mainloop()
