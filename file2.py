from .file1 import ClassA
a = ClassA()
class ClassB:
    def methodB(self):
       return (a.methodA())
b = ClassB()
b.methodB()