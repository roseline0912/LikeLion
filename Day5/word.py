print('끝말잇기를 시작합니다')
start_word=input()


while True:
    if len(start_word)!=3:
        print('3음절의 글자를 입력해주세요.종료합니다.')
        break
    else:
        print('정답')
    
    new_word=input()
    
    if len(new_word)!=3:
        print('3음절의 글자를 입력해주세요. 종료합니다.')
        break
    elif start_word[2]!=new_word[0]:
        print('끝 글자가 맞지 않습니다. 종료합니다.')
        break
    else:
        start_word=new_word
    
    
