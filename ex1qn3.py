#largest number in the list.
class Largest():
    def __init__(self,array):
        self.array=array

    def large(self):
        return max(self.array)

if __name__=='__main__':
    mylist=Largest([1,56,2,44])
    print(mylist.large())
