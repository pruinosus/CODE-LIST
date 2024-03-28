#= = = = = = = = = = = = = = = = = = = = = = = = = = 

                   # 연관 : 딕샤너리 #
                # 판다스 라이브러리 사용법 #

#= = = = = = = = = = = = = = = = = = = = = = = = = =

import numpy as np
import pandas as pd
from numpy import *
from pandas import *

a =pd.Series([1,2,3,4])
print(a)

b =pd.Series([1,2,3], index=['a','b','c'])
print(b)

region1=Series(['서울','부산','대구','대전','광주'])
region1

region2=Series(['서울','부산','대구','대전','광주'], index=['a','b','가','d','500'])
region2

region2=pd.Series(['서울','부산','대구','대전','광주'], index=['a','b','c','d','e'])
region2

dic2={'city': '서울','year':2018}
data2=pd.Series(dic2)
data2

dic3={'city': ['서울'],'year':2018}#시리즈 1차원
data3=pd.Series(dic3) ; data3

dic4={'city': ['서울'],'year':2018}#
data4=pd.DataFrame(dic4) ; data4

dic5 ={'city':['서울','부산','대전','대구','광주'],
        'year':[2017,2017,2018,2018,2018],
        'temp':[18,20,19,21,20]}
data5=pd.DataFrame(dic5);data5

dic6 ={'city':['서울','부산','대전','대구','광주'],
        'year':[2017,2017,2018,2018,2018],
        'temp':[18,20,19,21,20]}
data6=pd.Series(dic6);data6

type(data5)
type(data6)
a=data5['city'];a
type(a)
#data5['부산']
b=data5[['year','temp']];b#한개이상일때 대갈호 두개
type(b)

data5.index=['가','a',5.2,'라','기린'];data5#인덱스는 문자도 올수있고 정수도 올수았고 다 올수았음
data5.columns=['도시','연도','날씨'];data5
#data5['city']
data5['도시']   
data5[['도시','날씨']]
#data5.도시


data5.loc['기린']
data5.loc[5.2]
data5.set_index('도시')
data5
data8=data5.set_index('도시'); data8
data5.set_index('도시',inplace=True); data5#대체
data5.loc['대전']
data5.iloc[1:4]
cars=[50,40,20,30,10]
data5['car']=cars#car는 리스트
data5

data5['high1']=data5.car>=30
data5

data5['high2']=data5.car>=40;data5

data5.drop('high1',axis=1)

a=data5.drop('high2',axis=1)

data5.drop('high1',axis=1,inplace=True)#inplace=Tru이게 있어야 진짜 지우는거
data5

data5.drop('대구',axis=0,inplace=True)
data5

