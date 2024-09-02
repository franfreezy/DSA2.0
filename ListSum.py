class ListSum():
    def __init__(self,array):
        self.array=array

    def sum(self):
        total=0
        index=0
        while index<len(self.array):
            total+=self.array[index]
            index+=1
        return total

if __name__== '__main__':
    mylist=ListSum([1,2])
    print(mylist.sum())