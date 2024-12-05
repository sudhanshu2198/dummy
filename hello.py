'''Comman mathematical functions'''

def add_numbers(a=6,b=9):
    '''Returns the some of two numbers'''
    return sum([a,b])

def subtract_numbers(c=8,d=7):
    '''Returns the subtraction of two numbers'''
    return c-d

p=add_numbers()
print(f"result of add number: {p}")

q=subtract_numbers(d=p)
print(f"result of subtract number: {q}")