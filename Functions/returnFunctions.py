
def greet():
    def message():
        return "Hello"
    return message
fun = greet()
print(fun())

