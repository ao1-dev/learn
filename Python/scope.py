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

