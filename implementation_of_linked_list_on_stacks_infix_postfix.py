# -*- coding: utf-8 -*-
"""IMPLEMENTATION OF LINKED LIST ON STACKS INFIX POSTFIX

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1oigl2gSln-qGk08nOU7sLBfzls8cowjl
"""

class Node:
  def __init__(self,x):
    self.data=x
    self.next=None
class stack:
  def __init__(self):
    self.top=None

  def push(self,x):
    x=int(input("enter the element to be inserted in the stack"))
    new=Node(x)
    if self.top is None:
      self.top=new
      self.top.next=None
    else:
      new.next=self.top
      self.top=new

  def pop(self):
    if self.top is None:
      print("stack is empty")
    elif self.top.next is None:
      print("popped element is:",self.top.data)
      self.top=None
    else:
      temp=self.top
      print("popped element is:",self.top.data)
      print(" _ _ _ _ _ _ _ _ _  _ _ _ _ _ _ _ _ ")
      self.top=temp.next
      temp=None

  def display(self):
    if self.top is None:
      print("stack is empty")
      print(" _ _ _ _ _ _ _ _ _  _ _ _ _ _ _ _ _ ")

    else:
      print("Elements stacks are empty")
      temp=self.top
      while temp:
        print(temp.data)
        temp=temp.next
      print("top of the stack is ",self.top.data)
      print(" _ _ _ _ _ _ _ _ _  _ _ _ _ _ _ _ _ ")

s=stack()
while(1):
  print("enter the option from below")
  print("1-push opertaion\n 2-pop operation\n 3-display operation\n 4 exit")
  choice=int(input())
  print(" _ _ _ _ _ _ _ _ _  _ _ _ _ _ _ _ _ ")

  if choice==1:
    num=int(input("enter your number"))
    s.push(num)
    print(" _ _ _ _ _ _ _ _ _  _ _ _ _ _ _ _ _ ")

  elif choice==2:
    print("popped element")
    s.pop()
    print(" _ _ _ _ _ _ _ _ _  _ _ _ _ _ _ _ _ ")

  elif choice==3:
    print("display the data")
    s.display()
  elif choice==4:
    print("exit")
    break
  else:
    print("enter the correct option")

"""Converting_infix_postfix _and _Evaluation_of_Postfix_expression"""

def precedence(a):
    if a=="+" or a=="-":
        return 1
    if a=="*" or a=="/":
        return 2

a = list(input("Enter the infix notation separated by space: ").split(" "))
postfix = ""
opstack = []
for i in a:
    if i in ["+", "-", "*", "/"]:
        if((len(opstack)==0) or (precedence(i)>precedence(opstack[-1]))):
            opstack.append(i)
        else:
            postfix+=opstack.pop()
            opstack.append(i)
    elif i==" ":
        continue
    else:
        postfix+=i
while(len(opstack)!=0):
    postfix+=opstack.pop()
print(postfix)

def precedence(a):
    if a=="+" or a=="-":
        return 1
    if a=="*" or a=="/":
        return 2

a = list(input("Enter the infix notation separated by space: ").split(" "))
postfix = ""
opstack = []
for i in a:
    if i in ["+", "-", "*", "/"]:
        if((len(opstack)==0) or (precedence(i)>precedence(opstack[-1]))):
            opstack.append(i)
        else:
            postfix+=opstack.pop()
            opstack.append(i)
    elif i==" ":
        continue
    else:
        postfix+=i
while(len(opstack)!=0):
    postfix+=opstack.pop()
print(postfix)

def precedence(a):
    if a=="+" or a=="-":
        return 1
    if a=="*" or a=="/":
        return 2

a = list(input("Enter the infix notation separated by space: ").split(" "))
postfix = ""
opstack = []
for i in a:
    if i in ["+", "-", "*", "/"]:
        if((len(opstack)==0) or (precedence(i)>precedence(opstack[-1]))):
            opstack.append(i)
        else:
            postfix+=opstack.pop()
            opstack.append(i)
    elif i==" ":
        continue
    else:
        postfix+=i
while(len(opstack)!=0):
    postfix+=opstack.pop()
print(postfix)

def precedence(a):
    if a=="+" or a=="-":
        return 1
    if a=="*" or a=="/":
        return 2

a = list(input("Enter the infix notation separated by space: ").split(" "))
postfix = ""
opstack = []
for i in a:
    if i in ["+", "-", "*", "/"]:
        if((len(opstack)==0) or (precedence(i)>precedence(opstack[-1]))):
            opstack.append(i)
        else:
            postfix+=opstack.pop()
            opstack.append(i)
    elif i==" ":
        continue
    else:
        postfix+=i
while(len(opstack)!=0):
    postfix+=opstack.pop()
print(postfix)

def is_operand(char):
    return char.isalnum()

def evaluate_postfix(postfix_expression):
    stack = []

    for char in postfix_expression:
        if is_operand(char):
            stack.append(float(char))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()

            if char == '+':
                result = operand1 + operand2
            elif char == '-':
                result = operand1 - operand2
            elif char == '*':
                result = operand1 * operand2
            elif char == '/':
                result = operand1 / operand2

            stack.append(result)

    return stack.pop()

postfix_expression = "34+5*6-"
result = evaluate_postfix(postfix_expression)
print("Postfix Expression:", postfix_expression)
print("Result:", result)

def is_operator(char):
    return char in {'+', '-', '*', '/'}

def precedence(operator):
    if operator == '+' or operator == '-':
        return 1
    elif operator == '*' or operator == '/':
        return 2
    else:
        return 0

def infix_to_postfix(infix_expression):
    stack = []
    postfix_expression = []

    for char in infix_expression:
        if char.isalnum():
            postfix_expression.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                postfix_expression.append(stack.pop())
            stack.pop()
        elif is_operator(char):
            while stack and precedence(stack[-1]) >= precedence(char):
                postfix_expression.append(stack.pop())
            stack.append(char)

    while stack:
        postfix_expression.append(stack.pop())

    return ''.join(postfix_expression)
infix_expression = "(a+b)*c+d"
postfix_expression = infix_to_postfix(infix_expression)
print("Infix Expression:", infix_expression)
print("Postfix Expression:", postfix_expression)

def factorial(n):
  if(n==0 or n==1):
    return 1
  else:
    return n * factorial(n-1)
n=int(input("enter the value"))
res=factorial(n)
print(res)

def fibonacci (n):
  if n<=0:
    print("incorrect input")
  elif n==1:
    return 0
  elif n==2:
    return 1
  else:
    return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(5))

def fibonacci(n):
  if n<=1:
    return n
  else:
    return (fibonacci(n-1)+fibonacci(n-2))
n_terms=int(input("enter your valid number"))
if n_terms<=0:
  print("invalid input")
else:
  print("fibonaccci series")
for i in range (n_terms):
  print(fibonacci(i))

