
def display(name):
    def message():
        return "Hello"
    result = message()+name
    return result
print(display(' Ram'))


def perform(Activity):
    def routine():
        return "Walking"
    result = routine()+Activity
    return result
print (perform( " and take rest"))

