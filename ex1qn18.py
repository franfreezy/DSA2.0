#Write a method to compute Sum(N) = 1+2+3+…+N.
class Sum():
    def __init__(self,N):
        self.N=N

    def addition(self):
        total=0
        
        while self.N>0:
            
            total+=self.N
            (self.N)-=1
            
        
        return total

if __name__ =="__main__":
    sum=Sum(4)
    print(sum.addition())
