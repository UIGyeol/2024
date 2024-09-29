# 연설문 데이터 분석

# 입력 파일 출력 파일 열기
infile = open("input.txt", "r")
outfile = open("output.txt", "w")

word_dic = {}

total_count = 0

for line in infile:
    line = line.rstrip()
    word_list = line.split()
    
    # word_list에 있는 단어 하나하나를 봐야함.
    for word in word_list:
        word=word.strip()
        # 단어 소문자 처리
        word=word.lower()
        # 단어에 . and , 없애기 단어 = 단어.strip(".") and 단어 = 단어.strip(",")
        word=word.strip(".,")
        # for 문이 돌때마다 total_count +1
        total_count+=1
        # 단어가 word_dic에 있으면
            # word_dic[단어] += 1
        if word in word_dic:
            word_dic[word]+=1
              
        # 없으면
            # word_dic[단어] = 1
        else: 
            word_dic[word] = 1
        
        


for word,count in word_dic.items():
    outfile.write(f'{word}:{count}\n')

print(f'최종 단어의 수는 {total_count}이다')
#sum 함수를 통해 맞는 지 확인
total = sum(word_dic.values())
print(f'sum을 통해 word_dic 키의 합은 {total}')

infile.close()
outfile.close()
