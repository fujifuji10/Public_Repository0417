# __init__.py

# from . import base1 #同じ階層のbase1の読み取り
#  #同じ階層のbase1の読み取り
# from . import base2 #同じ階層のbase1の読み取り

from .base1 import print_msg as base1_msg #同じ階層のbase1の読み取り
from .base2 import print_msg as base2_msg #同じ階層のbase1の読み取り

# __init__を使うと、外部から読み取る際に、読み込み先を間接的に定義して読み込むことができる。

__all__ = ['base2_msg']#ここですべてインポートする際に対象を選択することができる
from dir1 import *