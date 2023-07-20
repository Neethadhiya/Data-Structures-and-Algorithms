def create_stack():
    stack=list ()
    return stack
def isEmpty(stack):
    return len(stack)==0
def push(stack,num):
    stack.append(num)
    print("pushed item",num)
def pop(stack):
    if isEmpty(stack):
        print("Stack is empty")
        return 
    stack.pop()
    return stack
def show(stack):
    print("stack elements are")
    for i in stack:
        print(i)

stack=create_stack()
push(stack,1)
push(stack,99)
pop(stack)
show(stack)

