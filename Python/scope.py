# Scope - local vs global

# Global
name = "pete" 

def greet():
    print(name) # reading global is ok

greet()

# Local
def local():
    name = "john"
    print("inside", name)

local()
print("outside", name) # name still "pete"

# This fails - python think x is local because you assign to it
count = 0

def bad():
    # count += 1 # UnboundLocalError
    pass

# Fix 1 - return a new value
def add_one(n):
    n = n + 1
    return n

count = add_one(count)
print(count)

# Fix 2 - works but avoid it
score = 0

def add_score():
    global score
    score += 10

add_score()
print(score)

# Nested fucntion - enclosing scope
def outer():
    msg = "hello"

    def inner():
        print(msg) # finds msg in outer

    inner()

outer()

