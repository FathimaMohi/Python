#Decorators in python
'''Decorators are a very poewerful and useful tool in python since it allows
programmers to modify the behaviour of a function or class.
Decoratos allow us to wrap another function in order to extend the behaviour
of the wrapped function without permanently modifying it.'''
#example1
def shout(text):
    return text.upper()
print(shout('Hello'))
greet=shout
print(greet('Good Afternoon'))
#Example2
def shout(text):
    return text.upper()
def whisper(text):
    return text.lower()
def greet(func):
    greeting=func('hii how are you')
    print(greeting)
greet(shout)
greet(whisper)
#Generator Function in python
''' A generator function in python is defined like a normal function ,but whenever
it needs to generate a value, it does so with the yield keyword rather than return
if the body of a def contains yield, the function automatically becomes a python generator
function'''
#Example1
def simpleGeneratorfun():
    yield 1
    yield 2
    yield 3
#Driver code to check above generator function
for value in simpleGeneratorfun():
    print(value)
#Example 2
#A generator function
def generatorfun():
    yield 1
    yield 2
    yield 3
#x is  a generater
x=generatorfun()
#iterating over the gernerator object using next
#in python 3,__next__()
print(next(x))
print(next(x))
print(next(x))
