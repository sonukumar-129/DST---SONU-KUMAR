# -*- coding: utf-8 -*-
"""prefix-postfix sonukumar

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GcYSGGjvCrjAAti6f4rYv5sOfRklH936
"""

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