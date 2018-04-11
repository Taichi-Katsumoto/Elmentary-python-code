'''
Created on 2018/04/11

@author: Taichi
'''


import numpy as np # NumPyモジュールをインポート
a = np.array([1,2,3]) # ndarrayインスタンスを生成。
type(a) # クラスを確認
b = np.array([[1,2,3], [4,5,6]]) # これで2-dimensional array(2次元配列)
b.T # 転置
a.T # a.ndim < 2なので変化なし。
a.data # メモリの位置を示す。
a.dtype # データ型

#https://deepage.net/features/numpy-ndarray.html