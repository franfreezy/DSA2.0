#17.  Write a method to find the sum of every number in an int number. Example: input= 1984, output should be 32 (1+9+8+4).
class SumOfNumberMakingANumber():
    def __init__(self,number):
        self.number=str(number)
    
    def sum(self):
        size=len(self.number)
        i=0
        total=0
        while i<size:
            total+=int(self.number[i])
            i+=1
        return total

if __name__ == "__main__":
    summation=SumOfNumberMakingANumber(1987)
    print(summation.sum())