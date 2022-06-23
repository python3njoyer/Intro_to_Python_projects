# encapsulation is used in OOP to make certain variables private, or only visible to the devs
# protects data from unauthorized people

class Hello:
    def __init__(self, name):
        self.a = 10
        self._b = 20
        self.__c = 30

    def get_c(self):
        return self.__c

    def set_c(self, value):
        self.__c = value

hello = Hello('name')

print(hello.a)
print(hello._b)
# print(hello.__c)  # this attribute is hidden, will get an unresolved reference error

print(hello.get_c())  # the attribute can be accessed with this method

hello.set_c(35)
print(hello.get_c())  # the attribute can be changed with this method; won't work the normal way