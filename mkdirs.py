# 数字の表記:標準01～XX、No.01～No.XX、漢数字(一～百)、英数字(One～One_Hundred)、ローマ数字(Ⅰ～C)、              

import os

from tkinter import messagebox


# 英語表記の数字の一覧
ENG_NUMS = ( 
    "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", 
    "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen", 
    "Twenty", "Twenty_One", "Twenty_Two", "Twenty_Three", "Twenty_Four", "Twenty_Five", "Twenty_Six", "Twenty_Seven", "Twenty_Eight", "Twenty_Nine", 
    "Thirty", "Thirty_One", "Thirty_Two", "Thirty_Three", "Thirty_Four", "Thirty_Five", "Thirty_Six", "Thirty_Seven", "Thirty_Eight", "Thirty_Nine", 
    "Forty", "Forty_One", "Forty_Two", "Forty_Three", "Forty_Four", "Forty_Five", "Forty_Six", "Forty_Seven", "Forty_Eight", "Forty_Nine", 
    "Fifty", "Fifty_One", "Fifty_Two", "Fifty_Three", "Fifty_Four", "Fifty_Five", "Fifty_Six", "Fifty_Seven", "Fifty_Eight", "Fifty_Nine", 
    "Sixty", "Sixty_One", "Sixty_Two", "Sixty_Three", "Sixty_Four", "Sixty_Five", "Sixty_Six", "Sixty_Seven", "Sixty_Eight", "Sixty_Nine", 
    "Seventy", "Seventy_One", "Seventy_Two", "Seventy_Three", "Seventy_Four", "Seventy_Five", "Seventy_Six", "Seventy_Seven", "Seventy_Eight", "Seventy_Nine", 
    "Eighty", "Eighty_One", "Eighty_Two", "Eighty_Three", "Eighty_Four", "Eighty_Five", "Eighty_Six", "Eighty_Seven", "Eighty_Eight", "Eighty_Nine", 
    "Ninety", "Ninety_One", "Ninety_Two", "Ninety_Three", "Ninety_Four", "Ninety_Five", "Ninety_Six", "Ninety_Seven", "Ninety_Eight", "Ninety_Nine", 
    "One_Hundred"
)

# 漢数字の一覧
KANSUUJI = (
    "一", "二", "三", "四", "五", "六", "七", "八", "九",
    "十", "十一", "十二", "十三", "十四", "十五", "十六", "十七", "十八", "十九",
    "二十", "二十一", "二十二", "二十三", "二十四", "二十五", "二十六", "二十七", "二十八", "二十九",
    "三十", "三十一", "三十二", "三十三", "三十四", "三十五", "三十六", "三十七", "三十八", "三十九",
    "四十", "四十一", "四十二", "四十三", "四十四", "四十五", "四十六", "四十七", "四十八", "四十九",
    "五十", "五十一", "五十二", "五十三", "五十四", "五十五", "五十六", "五十七", "五十八", "五十九",
    "六十", "六十一", "六十二", "六十三", "六十四", "六十五", "六十六", "六十七", "六十八", "六十九",
    "七十", "七十一", "七十二", "七十三", "七十四", "七十五", "七十六", "七十七", "七十八", "七十九",
    "八十", "八十一", "八十二", "八十三", "八十四", "八十五", "八十六", "八十七", "八十八", "八十九",
    "九十", "九十一", "九十二", "九十三", "九十四", "九十五", "九十六", "九十七", "九十八", "九十九",
    "百"
)

# ローマ数字の一覧
ROMAN_NUMBERS = ( 
    "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", 
    "X", "XI", "XII", "XIII", "XIV", "XV", "XVI", "XVII", "XVIII", "XIX", 
    "XX", "XXI", "XXII", "XXIII", "XXIV", "XXV", "XXVI", "XXVII", "XXVIII", "XXIX", 
    "XXX", "XXXI", "XXXII", "XXXIII", "XXXIV", "XXXV", "XXXVI", "XXXVII", "XXXVIII", "XXXIX", 
    "XL", "XLI", "XLII", "XLIII", "XLIV", "XLV", "XLVI", "XLVII", "XLVIII", "XLIX", 
    "L", "LI", "LII", "LIII", "LIV", "LV", "LVI", "LVII", "LVIII", "LIX", 
    "LX", "LXI", "LXII", "LXIII", "LXIV", "LXV", "LXVI", "LXVII", "LXVIII", "LXIX", 
    "LXX", "LXXI", "LXXII", "LXXIII", "LXXIV", "LXXV", "LXXVI", "LXXVII", "LXXVIII", "LXXIX", 
    "LXXX", "LXXXI", "LXXXII", "LXXXIII", "LXXXIV", "LXXXV", "LXXXVI", "LXXXVII", "LXXXVIII", "LXXXIX", 
    "XC", "XCI", "XCII", "XCIII", "XCIV", "XCV", "XCVI", "XCVII", "XCVIII", "XCIX", 
    "C"
)

""" タブ1で利用するフォルダ作成関数 """
def mkdir_nums(dir_path , dir_name , dir_count ):
    """ 
    数字表記のディレクトリ名を作成します

    Parameters
    ----------
    dir_path : str
        作成先のディレクトリパス。
    dir_name : str
        フォルダの作成名。
    dir_count : str
        フォルダ作成個数。
    """
    dir_count = int(dir_count)
    if dir_count < 10:
        for count in range(1, dir_count + 1):
            os.makedirs(dir_path + '/' + '{}_0{}'.format(dir_name, count), exist_ok=True)
    else:
        for count in range(1, 10):
            os.makedirs(dir_path + '/' + '{}_0{}'.format(dir_name, count), exist_ok=True)
        for count in range(10, dir_count + 1):
            os.makedirs(dir_path + '/' + '{}_{}'.format(dir_name, count), exist_ok=True)

def mkdir_numbers(dir_path, dir_name, dir_count):
    """ 
    数字(No.付き)表記のディレクトリ名を作成します

    Parameters
    ----------
    dir_path : str
        作成先のディレクトリパス。
    dir_name : str
        フォルダの作成名。
    dir_count : str
        フォルダ作成個数。
    """
    for count in range(1, int(dir_count) + 1):
        os.makedirs(dir_path + '/' + '{}_No.{}'.format(dir_name, count), exist_ok=True)


def mkdir_eng_nums(dir_path, dir_name, dir_count):
    """ 
    英語表記(One~)のディレクトリ名を作成します

    Parameters
    ----------
    dir_path : str
        作成先のディレクトリパス。
    dir_name : str
        フォルダの作成名。
    dir_count : str
        フォルダ作成個数。
    """
    for count in range(0, int(dir_count)):
        os.makedirs(dir_path + '/' + '{}_{}'.format(dir_name, ENG_NUMS[count]), exist_ok=True)

# 漢数字表記(一~)のディレクトリ名を作成する関数
def mkdir_kansuuji(dir_path, dir_name, dir_count):
    """ 
    漢数字表記(一~)のディレクトリ名を作成します

    Parameters
    ----------
    dir_path : str
        作成先のディレクトリパス。
    dir_name : str
        フォルダの作成名。
    dir_count : str
        フォルダ作成個数。
    """
    for count in range(0, int(dir_count)):
        os.makedirs(dir_path + '/' + '{}_{}'.format(dir_name, KANSUUJI[count]), exist_ok=True)

def mkdir_roman_numbers(dir_path, dir_name, dir_count):
    """ 
    ローマ数字表記(Ⅰ~)のディレクトリ名を作成します

    Parameters
    ----------
    dir_path : str
        作成先のディレクトリパス。
    dir_name : str
        フォルダの作成名。
    dir_count : str
        フォルダ作成個数。
    """
    for count in range(0, int(dir_count)):
        os.makedirs(dir_path + '/' + '{}_{}'.format(dir_name, ROMAN_NUMBERS[count]), exist_ok=True)

""" タブ2で利用するフォルダ作成関数 """
# チェックボックスで選択した都道府県名のディレクトリを作成する関数
def mkdir_todoufuken(dir_path :str, mkdirs_list :list):
    """ 
    チェックボックスで選択したディレクトリ名を作成します

    Parameters
    ----------
    dir_path : str
        作成先のディレクトリパス。
    mkdirs_list : list of str
        作成するフォルダ名のリスト。
    """
    for todoufuken_idx, todoufuken in enumerate(mkdirs_list):
        if todoufuken_idx < 9:
            os.mkdir(dir_path + '/' + '0{}{}'.format(todoufuken_idx+1, todoufuken))
        else:
            os.mkdir(dir_path + '/' + '{}{}'.format(todoufuken_idx+1, todoufuken))
