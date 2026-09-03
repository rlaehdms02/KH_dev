import pandas as pd

df = (pd.read_csv('data/emp.csv'))

df["나이"] = df["나이"].fillna(df["나이"].median())
#결측치 도시 최빈값으로 채우기

x = df["도시"].mode()[0]
df["도시"] = df["도시"].fillna(x)

#결측치 연봉 해당 행 없애기
df = df.dropna(subset=["연봉","이름"])

#중복 제거
df.drop_duplicates(inplace=True)

#컬럼병 바꾸기
df.rename(columns={"도시":"지역"}, inplace=True)

#컬럼 삭제
df.drop(columns=["이름"], inplace=True)

#나이 컬럼의 타입 변경
df["나이"] = df["나이"].astype(int)
df["연봉"] = df["연봉"].astype(int)

#값 치환
df["지역"] = df["지역"].replace("서울", "한양")

#새로운 컬럼 만들기
df["월급"] = (df["연봉"] / 12).astype(int)

#정렬 인덱스 기준
#df = df.sort_index()

#그룹

#잔처리 이후 데이터 확인
print(df.head)

