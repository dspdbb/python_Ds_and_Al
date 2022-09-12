class Stack:
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        return self.stack.pop()

    def get_top(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            return None

    def is_empty(self):
        return len(self.stack) == 0


# a = Stack()
# a.push(1)
# a.push(2)
# a.push(3)
# a.push(4)
# print(a.pop())
# a.pop()
# a.pop()
# print(a.get_top())


# 需要每一个都是一对，不能交错
def brace_math(s):
    matche = {'}': '{', ']': '[', ')': '('}
    stack = Stack()
    for ch in s:
        if ch in {'(', '[', '{'}:
            stack.push(ch)
        else:
            if stack.is_empty():
                return False
            elif stack.get_top() == matche[ch]:
                stack.pop()
            else:
                return False
    if stack.is_empty():
        return True
    else:
        return False


print(brace_math('[[]]{}{}(())))(((({{{'))
print(brace_math('{{((}}[[))]]'))
print(brace_math('{([])}[]'))
print(brace_math('(){}'))
