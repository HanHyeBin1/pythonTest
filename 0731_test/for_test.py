# 파이썬으로 일부 중복되는 element를 저장하고 최소 element가 10개이상 되는 배열을 만든다. 
# 그리고 set() 구문 없이 오로지 for in 문으로 배열의 중복된 값을 없애는 코드를 작성하기

stringlist = ['aa', 'bb', 'ee', 'aa', 'ff', 'kk', 'ee', 'hh', 'pp', 'kk']

emptylist = [] #하나하나 비교 하기 위해, 비교 대상을 하나씩 추가할 수 있는 빈 리스트 선언

for i in stringlist: #stringlist 하나하나 확인 하면서 emptylist에 중복 되지 않으면 추가
    if i not in emptylist: 
        emptylist.append(i)

print(emptylist)      
