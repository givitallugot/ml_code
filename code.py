
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

뒷배경 변경하기
https://zephyrus1111.tistory.com/62

깃허브 설치
https://gitforwindows.org/

git bash 들어가기
git config --global user.name "유저 이름"
git config --global user.email "가입할 때 사용한 메일 주소"

git clone 링크
git init : 현재 디렉터리를 Git 저장소로 변환해줍니다.
git add : 파일을 원격 저장소에 추가합니다. ( 예시로 test1.py를 추가하려면 git add test1.py  실제 추가가 아니라 깃의 저장소의 스냅샷에 포함된다고 생각하면 될듯 합니다.)
git commit : 디렉토리의 변경과 추가를 저장소에 기록합니다. ( git commit -m "New File" : 커밋 시 남길 메시지)
git push : 로컬 저장소의 변경사항을 github에 반영합니다. ( git push origin master )
git checkout : 현재 위치하고 있지 않은 저장소를 체크아웃합니다. (예를 들어 master 브랜치를 보고 싶으면, git checkout master를 사용할 수 있습니다.)
git merge : 브랜치에서 하던 작업을 끝내고, 동료가 볼 수 있는 master브랜치로 합치는 과정입니다.
git pull : 로컬 저장소 작업할 때, 작업하고 있는 저장소의 최신 버전을 받아옵니다.

모델링

stacking
https://techblog-history-younghunjo1.tistory.com/103
