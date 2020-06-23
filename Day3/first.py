a=1
b=2

print()
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print('나눗셈의 몫 : ', a//b)
print('나눗셈의 나머지 : ', a%b)

print(type(a+b))
print(type(a-b))
print(type(a*b))
print(type(a/b))
print(type(a//b))
print(type(a%b))

a="hello"
b='good'
print(a+b)
# print(a-b)
print(a*10)
print(a[1])
print(a[1:3])
print(a[:3])
print(a[2:])

print(a.replace("h","g"))
aa=a.replace("h","g")
print(a)
print(aa)

#while
i=0
while i < len(a) :
    print("a의 ",i,"번째 slicing : ", a[i])
    i=i+1
    
######### String ###########################
text = "whatever you want, make it real! Hack Your Life"

print(text.count('e')) # 문자열 안에 e가 몇 번 들어갔는지를 출력합니다. 

print(text.find('r')) # 문자열에서 r이 처음으로 나온 위치를 출력합니다. 없는 문자일 경우 -1을 출력합니다. 
print(text.index('k')) # 문자열에서 k가 처음으로 나온 위치를 출력합니다. 없는 문자일 경우 에러를 반환합니다. 

print(text.split(' ')) # 괄호 안의 문자를 기준으로 문자열을 나눕니다.

print(text.replace("make", "change")) # make를 change로 바꿉니다. 

text = "    Hack Your Life    "
print(text.strip()) # 공백을 삭제합니다. 
print(text.lstrip()) # 왼쪽 공백을 삭제합니다.
print(text.rstrip()) # 오른쪽 공백을 삭제합니다. 

######### List(변경가능) ###########################
array = [1,5,3,4,2,10,8]

new_array = array + [45, 29, 3555] 
print(new_array) # 이렇게 새로운 리스트를 붙일 수도 있습니다. 

letters = ['a', 'b', 'c', 'd']
result = len(letters)
print(result) # 문자열에서처럼 리스트의 길이를 출력할 수 있습니다.

#-------------------------------------------------------
mylist=list()
mylist2=[]
numList=[1,2,3]
charList=['a','b','c','d']
numCharList=[1,2,'life','is']
numListList=[1,2,['Life','is']]

print(numList)
print(charList)
print(numCharList)
print(numListList)

numList[2]=100
print(numList)

mylist.append("첫째")
mylist.append("둘째")
mylist.append("셋째")
print(mylist)
mylist.remove("둘째")
print(mylist)
mylist.pop()
print(mylist)

tmplist=[1,5,7,4,7,22]
tmplist.reverse() #역순
print(tmplist)
tmplist.sort()
print(tmplist)
# sorttmplist=[]
# sorttmplist=tmplist.sort()
# sorttmplist.reverse()
# print(sorttmplist)

# 리스트 중에 7이 있는 인덱스 출력
print(tmplist.count(7))

#-------------------------------------------------------

# 콤마로 구분된 문자열 만들기
tmp_str=",".join(charList)
print(tmp_str)

# 콤마로 구분된 문자열을 리스트로 만들기
return_list=tmp_str.split(",")
print(return_list)

######### Tuple(변경불가능) ###########################
tuple1 = ()
tuple2 = (1,)
tuple3 = (1,2,3)
tuple4 = 1,2,3
tuple5 = ('a','b',('ab','cd'))
print(tuple5)

#변경이불가능하다는것 말고는 list와 비슷한 속성을 가진다


######### Dictionary(변경불가능) ###########################
#key-value로 이루어진 자료형
mydict = {1:'hello'}
print(mydict[1])
mydict2=dict()
mydict22={}
mydict3 = {'이름':'장치훈','나이':12,'특징':['하나','둘']}
mydict3['추가']='내용'
print("*"*50,type(mydict2),type(mydict22))
print(mydict)
print(mydict3)
print(mydict3.keys())
print(mydict3.values())
print(mydict3.items()) #key,value 를 보여줌
print(mydict3['이름'])
print(mydict3.get('이름'))
print(mydict3.get('나이','입력을 안했습니다')) #get 할 내용이 없을 때
print(mydict3.get('없는요소','입력을 안했습니다'))

print("키가 딕셔너리 안에 있나?", '이름' in mydict3)







