#Find average of all the elements in a list.
class average():
    def __init__(self,array):
        self.array=array
        self.total=0


    def sum(self):
        
        i=0
        while i<len(self.array):
            self.total+=self.array[i]
            i+=1
        return self.total

    def avg(self):
        self.total=self.sum()
        average=(self.total)/len(self.array)
        return average
if __name__ == "__main__":
    mylist=average([1,2,7,2])
    print(mylist.avg())