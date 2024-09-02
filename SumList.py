#Write a method that will return the sum of all the elements of the integer list givenlist and its size as an argument.
class ListSum():
    def __init__(self, array):
        self.array=array

    def sum(self):
        total=0
        i=0
        while i<len(self.array):
            total+=self.array[i]
            i+=1

        return total

def ArrayConstruction():
    print('How many elements are in your array:')
    index=0
    k=int(input())
    Array=[None for index in range(k)] #without which our array runs out of index
    while index<k:
        print('input number:')
        Array[index]=int(input())
        index+=1
    return Array



if __name__=='__main__':
    print('A program that prints sum of numbers in a list')
    
    Array=ArrayConstruction()
    sum=ListSum(Array)
    print(sum.sum())