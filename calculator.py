class Calculator:
    def sum(self, a, b):
        return a + b

    def difference(self, a, b):
        return a - b

    def product(self, a, b):
        return a * b


a=5
b=2
print(Calculator().sum(a,b))
print(Calculator().difference(a,b))
print(Calculator().product(a,b))
