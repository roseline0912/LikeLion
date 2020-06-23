def gugudan(dan):
    for i in range(1,19):
        print (dan,' x ',i,' = ',dan*i)


print('18단을 시작합니다.')
while True:
    dan=int(input('몇 단을 볼까요? : '))  #input을 int로 바꿔주는 것이 포인트
    gugudan(dan)
