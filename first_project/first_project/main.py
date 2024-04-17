# # import sys

# # print(sys.path)
# # sys.path.append('D:\\')
# # print(sys.path)

# # import sub importで同じ階層のファイルをインポートできる
# # sub.sample_a() 関数の実行、クラスを呼び出して、インスタンスを作成したりファイルの変数を直接呼び出したりできる
# # class_a = sub.ClassA()
# # class_a.print_a()
# # print(sub.VAR)

# #別のimport方法
# # from sub import sample_a as sa, ClassA as ca
# # # sample_aをsaと名前をつけて実行、クラスAもcaとして実行
# # sa()

# # ins = ca() #クラスAのインスタンスかをしてprint_aをじっこう
# # ins.print_a()
# # # from ● import 関数名（クラス名、変数名）等で呼び出しもできる

# #ディレクトリを作成

# import dir1.base1 as base1

# # dir1.base1.print_msg()
# # base1.print_msg()
# import dir1.base2 as base2
# # base2.print_msg()

# from dir1.base1 import print_msg as base1_print
# from dir1.base2 import print_msg as base2_print

# base1_print()
# base2_print()

# # # __init__をやろう
# from dir1 import *

# base1.print_msg()
# base2.print_msg()

from dir1 import *
from dir1 import base1_msg

base1_msg()
base2_msg()