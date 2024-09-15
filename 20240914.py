class car():
    def __init__(self,color,speed):
        self.color =color
        self.speed =speed
        self.printInfo()

        def speedUp(self):
            self.speed =self.speed +10
            if self.speed>100:
                print("너무 빠릅니다.")
            self.printInfo()

        def speedDown (self):
            if self.speed -10>0:
                self.speed -=10
            else:
                self.speed= 0
                self.printInfo()
        
        def printInfo(self):
            print(f"{self.color}자동차의 속도는 {self.speed}km/h이다")

        def setColor (self, color):
            self.color =color
        
        def getColor(self):
            return self.color
        
car1=car("black",0)
car1.printInfo()
car2=car("red",120)
car3=car("yellow", 30)
car4=car("blue",0)
car5=car("green",0)

car4.speedUp()
car2.speedDown()
print(car3.color)#색을 노랑에서 보라로 바꾸기
car3.color ="purple"
print(car3.color)#확인해보기
car3.setColor("pink")# 핑크로 바꿔보기
print(car3.color) 
print(car3.getColor()) 
car3.printInfo()
car5.speed = 80 #스피드 바꿔보기
car5.printInfo()
car5.speedUp()#속도변화
car5.speedUp()#속도변화
car5.printInfo()