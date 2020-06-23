### IF ######################################################################

# a=int(input("숫자를 입력해주세요 : ")) #int를 쓰지 않으면 문자로 판단함.

# # a=11
# if (a>10):
#     print("숫자가 10보다 큽니다.")  # 'go'는 안됨
# else:
#     print("숫자가 10보다 크지 않습니다.")



### WHILE ######################################################################

# i=1
# while True:
#     print(i)
#     i=i+1
#     i+=1
    
########control+C 는 중단시키는 단축키
    
    
### FOR ######################################################################

# for i in ["가","나","다","라",["마","바"]]:
#     print("출력 : ",i)

# for i in "안녕하세요! 장미선입니다.":
#     print("출력 : ",i)
    
# for i in range(1000):
#     print("출력 : ",i)
    
# print(list(range(10)))

# print(list(range(500,1000,50)))

### DEF ######################################################################

# tmp_str="안녕 나는 집에 가고 싶어. 아니 친구랑 놀고 싶엉"
# for i in range(len(tmp_str)):
#     print("출력 : ",tmp_str[i])
    
# def iterateFunc(str,num):
#   return print(str*num)

# iterateFunc("안녕",10)

### BREAK & CONTINUE ######################################################################

for i in [1,2,3,4]:
    if i==3:
        break
    print(i)

for i in [1,2,3,4]:
    if i==3:
        continue
    print(i)
    
### CLASS ######################################################################
class Do:
    def run(self):
        print("나는 달립니다.",self)
    
    def eat(self,food): 
        print("나는 다음을 먹습니다. : ",food)
    

miseon=Do()

print(miseon.run())
print(miseon.eat("양념치킨"))
