class Fruits:
    def __init__(self,ele):
        self.ele=ele

    def __contains__(self,ele):
        return ele in self.ele
    
    def __len__(self):
        return len(self.ele)
    
    def __iter__(self):
        return self
    

Fruits_list=Fruits(["Apple","Banana","Orange"])
print(len(Fruits_list))
