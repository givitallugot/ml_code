
from sklearn.preprocessing import LabelEncoder

enc = LabelEncoder()
data_clus['StockCode'] = enc.fit_transform(data['StockCode'])


from sklearn.preprocessing import MinMaxScaler

enc = MinMaxScaler()
data_clus[['Quantity', 'UnitPrice']] = enc.fit_transform(data_clus[['Quantity', 'UnitPrice']])


from sklearn.preprocessing import OneHotEncoder

enc = OneHotEncoder(handle_unknown='ignore')
enc_col = pd.DataFrame(enc.fit_transform(data[['ocean_proximity']]).toarray())
data = data.join(enc_col) # 변수 명이 0,1,2,3 으로 들어감


파이썬 머신러닝 완벽 가이드
https://github.com/wikibook/ml-definitive-guide
https://github.com/wikibook/ml-definitive-guide/blob/master/5%EC%9E%A5/5.9%20Regression%EC%8B%A4%EC%8A%B5-Bike%20Sharing%20Demand.ipynb
