#Find the duplicate elements in a list of size n where each element is in the range 0 to n-1.#Find the duplicate elements in a list of size n where each element is in the range 0 to n-1.
class Duplicate():
    def __init__(self,array):
        self.array=array

    def sizeCalculation(self):    
        if(len(self.array))<10:
            size=10
        elif (len(self.array))<100:
            size=100
        return size
        
    class hash():
        def __init__(self,array,size):
            self.array=array
            self.size=size
        def hashtable(self):
            mydict={}
            for value in self.array:
                hashvalue=value%size
                if hashvalue not in mydict:
                    mydict[hashvalue] = []
                
                mydict[hashvalue].append(value)
            return mydict
    
def duplicateValues(mydict):
    
    duplicate={key for key, values in mydict.items() if len(values)>1}
    return duplicate

if __name__=='__main__':
    myarray=[1,3,5,7,6,2,3,56,4]
    Duplicate=Duplicate(myarray)
    size=Duplicate.sizeCalculation()
    hashing=Duplicate.hash(myarray,size)
    mydict=hashing.hashtable()
    print(mydict)
    print(duplicateValues(mydict))