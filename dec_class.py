class Decor_class:
    def __call__(self, funct):
        def decor():
            print("decorate_function")
            funct()
        return decor

decor_function=Decor_class()
@decor_function
def funct():
    print("funct")

funct()