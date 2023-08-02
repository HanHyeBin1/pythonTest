import pandas as pd

# csv 파일 가져오기
csvData = pd.read_csv('my_data.csv')

# Unnamed: 0 대신 컬럼 이름 새로 부여 후 해당 열 삭제
csvData.rename(columns={'Unnamed: 0': 'replaceName'}, inplace=True)
csvData.drop(columns=['replaceName'], inplace=True)

# index 열 제거
csvData.reset_index(drop=True, inplace=True)

# name에 해당되는 영문 이름을 한글로 변경
name_mapping = {
    'Alice': '앨리스',
    'Bob': '밥',
    'Charlie': '찰리',
    'james': '제임스'
}

csvData['name'] = csvData['name'].map(name_mapping)

# salary에 해당되는 숫자를 000 세자리 단위로 콤마를 넣어서 값을 바꿔 넣기
csvData['salary'] = csvData['salary'].apply(lambda x: "{0:,}".format(x))

# CSV 파일로 저장하기
csvData.to_csv('modifyData.csv', index=False)

print(csvData.to_string(index=False))
