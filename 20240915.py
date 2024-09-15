def create_student(name,korean, math, english, science):
    return {
        "name" : name,
        "korean" : korean,
        "math": math,
        "english": english,
        "science": science
    }

students = [
    create_student("윤인성", 87,98,88,95),
    create_student("연하진", 92,98,96,98),
    create_student("구지연", 76,96,94,90),
    create_student("나선주", 98,92,96,92),
    create_student("윤아린", 95,98,98,98),
    create_student("윤명월", 64,88,92,92),
]

print("이름","총점","평균", sep="\t")
for student in students: 
    score_sum = student["korean"]+ student["math"]+\
        student["english"]+ student["science"]
    score_average= score_sum/4
    print(student["name"], score_sum,score_average,sep="\t")


# printing MBTI and favorite singer
def create_introducing(name,MBTI,comment):
    return {
        "name": name,
        "MBTI" : MBTI,
        "comment" : comment
    }
introducing =[create_introducing("Sammy","ENFJ","I am so happy to learn new field"),
              create_introducing("EJ.H","INTJ","Breaking through! That is my motto."),
              create_introducing("Ari","ESTJ","Never let it go!"),
              create_introducing("Hailie","ISTP","Hi there!! We got this!")]

print("Name","MBTI","comment", sep="\t")

for student in introducing: 
    print(student["name"],student["MBTI"],student["comment"], sep="\t")