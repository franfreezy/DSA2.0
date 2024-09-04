#sum of all the elements of a two dimensional list
class SumList():
    def __init__(self,array):
        self.array=array

    def sum(self):
        rows=len(self.array)
        row = 0
        cols=len(self.array[row])
        col = 0
        total=0
        for row in range(rows):
            for col in range(cols):
                total+=self.array[row][col]

        return total


if __name__=="__main__":
    mylist=SumList([[1,2,6],[2,1,3]])
    print(mylist.sum())