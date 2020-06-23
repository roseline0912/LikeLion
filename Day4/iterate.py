# a = 0
# while a < 10:
#     print(a,"는 10보다 작아요")
#     a +=1

# a = 0
# while a < 10:
#     print(a,"는 10보다 작아요")
#     a +=1
#     if a == 5:
#         break
a= 0
while a < 10:
    if a == 5:
        a +=1
        continue
    print(a,"는 10보다 작아요")
    a +=1

myrange = range(1,10)
myrange2 = range(5)
myrange3 = range(1,100,10)

for i in myrange:
    print(i)

for i in myrange2:
    print(i)
    
for i in myrange3:
    print(i)
    
