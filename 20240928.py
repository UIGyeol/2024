import random

# 입력 파일 열기
infile = open("./hangman.txt", "r")
lines = infile.readlines()
word = random.choice(lines).rstrip()  # 랜덤으로 단어 선택
solution = list(word)
result = list('_' * len(word))     
turns = 10  
# 기회가 있을때 반복
while turns>=0:
    # 입력받아 비교할 변수 선정
    try_letter=input("알파벳 하나를 입력하세요")
    # 입력 철자가 랜덤 단어에 있으면
    if try_letter in word:
        # 기회 -1
        turns-=1
        if try_letter in result:
            print("중복된 값을 입력했습니다.")
        else:

            # 랜덤 단어 길이 만큼 for문을 돌면서 단어가 몇번째에 있는지를 찾음
            for i in range(len(word)):
                if word[i]==try_letter:
                
                # 찾았다면 그 철자를 이제 result에 입력하여 출력
                    result[i]=try_letter
                    print("Hit")
    print(result)
    # result가 사용자가 입력한 철자로만 이루어졌다면 성공 후 게임 종료
    if "_" not in result:
        print("성공! 축하드립니다.")
        break    
    #만약에 철자가 랜덤 단어에 없다면 실패라고 출력 후 기회 -1 
    if try_letter not in word:
        print("실패")
        turns-=1
        # 가지고 있는 기회가 없다면 실패
        if turns==0:
            print("가진 기회를 모두 잃었습니다.")
            break
   
                


infile.close()  # 파일 닫기
