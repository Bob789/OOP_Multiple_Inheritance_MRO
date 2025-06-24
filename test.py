from idlelib.outwin import OutputWindow


class A:
    def process(self):
        print("A.process")

class B:
    def process(self):
        print("B.process")

class C(A, B):
    def process(self):
        print("C.process - before super()")
        super().process()
        print("C.process - after super()")

obj = C()
obj.process()
print(C.mro())
# Output
# C.process - before super()
# A.process
# C.process - after super()
# [<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>]

