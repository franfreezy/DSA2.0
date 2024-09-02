#Write a method, which will search a list for some given value.
class SequentialSearch():
    def __init__(self, array, value):
        self.array=array
        self.value=value

    def search(self):
        if (self.value  not in self.array):
            print('value not in the list')
        else:
            index= [i for i, x in enumerate(self.array) if x == self.value]
            print(index)

if __name__ == "__main__":
    lookup=SequentialSearch([1,23,5,7,1],1)
    lookup.search()