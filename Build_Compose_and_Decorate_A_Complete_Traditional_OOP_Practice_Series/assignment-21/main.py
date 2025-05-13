# 21. Make a Custom Class Iterable
# Assignment:
# Create a class Countdown that takes a start number. Implement __iter__() and __next__() to make the object iterable in a for-loop, counting down to 0.

class Coutdown:
    def __init__(self, start_num):
        self.start_num = start_num

    def __iter__(self):
        return self

    def __next__(self):
        if self.start_num < 0:
            raise StopIteration
        value = self.start_num 
        self.start_num -= 1
        return value
    
for i in Coutdown(10):
    print(i)