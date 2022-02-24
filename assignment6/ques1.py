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
new_stack.push(1)
new_stack.push(2)
new_stack.push(3)
new_stack.push(4)
new_stack.push(5)
print("stack before pop operation = ")
new_stack.display()
k = new_stack.pop()
k1 = new_stack.pop()
print("stack after two pop operation = ")
new_stack.display()
