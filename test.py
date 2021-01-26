#comment
# print("Hello World")

# 演算
# print(1+1)
# print(1-1)
# print(2*2)
# print(10/2)
# print(5%3)

# 変数
# unko = 'l_size'
# login_id = 'sihisincfb0293'
# unko_length = 0
# unko_times = 5.5

# print(type(unko))
# print(unko_times)
# print(unko_times)

# unko_shitai = False #ブーリアン型

# 条件分岐と関係演算子
# if else elif
# if unko_length > 7:
#     print('ooi') ネスト
# elif unko_length == 0:
#     print('nai')
# else:
#     print('sukunai')
    
# 関数
# def unko_funbaru(arg):
#      unko_status = arg
    
#      if(unko_status < 10):
#          return 'mada daijoubu'
#      else:
#          return 'yabai'

# print()
# type()

# list
# unko_list = ['unko_small', 'unko_medium', 'unko_lerge']
# print(unko_list[1])

# for
# for i in range(11):
#     print(unko_funbaru(i))

# for item in unko_list:
#     print(item)

# with ファイル開始から閉じるまで自動で終えてくれる
# open() 
# with open('./unko.text', 'r') as file:
    # print(file.mode)
    # print(file.name)
    # print(file.read())
    
# クラス, インスタンス　クラス名は大文字から クラス内の関数はメソッド
# class Card:
#     def __init__(self, date, user_name): #コンストラクタ
#         self.date = date
#         self.user_name = user_name
#     def message(self):
#         return 'この投稿は' + self.user_name + 'さんが' + self.date + 'に投稿しました'

# date_a = '2020-01-01'
# user_name_a = 'taro'
# card_a = Card(date_a, user_name_a)

# date_b = '2020-01-03'
# user_name_b = 'kayoko'
# card_b = Card(date_b, user_name_b)

# print(card_b.message())

# import
# import math
# print(math.pi)

# NumPy
# Pandas
# Flask
# Django

import numpy

numpy_list = [3, 1, 5, 10, 2093, 303, 239]
print(numpy.sum(numpy_list))

