class Memory:
    def __init__(self,internal,secondary,ram):
        self.internal=internal
        self.secondary=secondary
        self.ram=ram

    def memoryinfo(self):
        print("memory internal:",self.internal)
        print("memory secondary:",self.secondary)
        print("memory ram:",self.ram)


class Mobile:
    def __init__(self,model,brand,price,memory): 
        self.model=model 
        self.brand=brand 
        self.price=price
        self.memory=memory



    def mobileinfo(self):
        print("mobile model:",self.model)
        print("mobile brand:",self.brand)
        print("mobile price:",self.price)
        print("mobile memory:",end=" ")
        self.memory.memoryinfo()

A=Memory("8GB","2GB","64GB")
B=Mobile("B12","OPPO","15000",A)
B.mobileinfo()
        