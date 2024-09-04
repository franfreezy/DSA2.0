#smallest element in the list.
class Smallest():
    def __init__(self,array):
        self.array=array

    def small(self):
        return min(self.array)

if __name__=='__main__':
    mylist=Smallest([1,56,2,1,44])
    print(mylist.small())
