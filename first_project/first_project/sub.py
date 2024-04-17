VAR = 'sub'
def sample_a():
  print('sample_a関数を実行')
  

class ClassA:
  
  def print_a(self):
    print('ClassAのprint_aを実行')

if __name__== '__main__': #__name__＝実行環境を表している。mainの時だけ実行 sub.pyを直接実行した時だけと言うこと
#これもめちゃくちゃ使うらしい。
  print('subファイルをimport')