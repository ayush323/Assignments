class stack:
    stackk = []
    def push(self, value):
        self.stackk.append(value)

    def pop(self):
        try:
            return self.stackk.pop()
        except:
            print("stack is empty can not pop the value")

    def display(self):
        print(self.stackk)

new_stack = stack()
n = int(input("enter the number of values you want to add in the stack"))
while n > 0:
   num = int(input("enter the value"))
   new_stack.push(num)
   n -= 1

print("stack before pop operation = ")
new_stack.display()
while True:
    k = int(input("press 1 if you want to perform pop operation else press 0"))
    if k == 1:
        new_stack.pop()
    else:
        break
        
print("stack after two pop operation = ")
new_stack.display()
