class Stack:
    def __init__(self):
        self.stack=[]
    
    def isEmpty(self):
        return len(self.stack)==0
    
    def size(self):
        return len(self.stack)
    
    def push(self,ele):
        self.stack.append(ele)
    
    def pop (self):
        if not self.isEmpty():
            return self.stack.pop(-1)
    def peak (self):
        if not self.isEmpty():
            return self.stack[-1]
    def clear(self):
        self.stack =[]

even = Stack()
odd = Stack()
for i in range(10):
    if i % 2 == 0:
        even.push(i)
    else:
        odd.push(i)
print(f'even stack {even.stack}')
print(f'odd stack {odd.stack}')
# 각 stack에서 제일 마지막에 들어간 값 확인해보기.
print(f'event peak: {even.peak()}')
print(f'odd peak: {odd.peak()}')
