import random

print('가위바위보를 시작합니다.')

rps=['가위','바위','보']


while True:
    me=input('내세요 : ')
    
    if me not in rps:
        print('가위, 바위, 보 중 하나를 골라주세요. 종료합니다.')
        break

    com=random.choice(rps)

    print('결과 ---------- 컴퓨터 : ',com,' / 나 : ',me)
    
    if ((com=='가위')and(me=='바위')) or ((com=='바위')and(me=='보')) or ((com=='보')and(me=='가위')):
        print('이겼습니다.')
    elif com==me:
        print('비겼습니다.')
    else:
        print('졌습니다.')
