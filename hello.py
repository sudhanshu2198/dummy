def add_numbers(a=6,b=9):
    '''Returns the some of two numbers'''
    return a+b

def subtract_numbers(c=8,d=7):
    '''Returns the subtraction of two numbers'''
    return c-d

def divide_numbers(e=9,f=8):
    '''Returns the division of two numbers'''
    return e/f

p=add_numbers()
print(f"result of add number: {p}")

q=subtract_numbers(d=p)
print(f"result of subtract number: {q}")

m=divide_numbers(e=q,f=p)
print(f"result of divide number: {m}")

r=subtract_numbers(m,p)
print(f"result of add number: {r}")