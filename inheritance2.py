class Tv:
    def __init__(self,model,brand):
        self.model=model
        self.brand=brand
    def features(self):
        print("this tv have good features:")
        print("this tv model:",self.model)
        print("this tv brand:",self.brand)
class SMARTTV(Tv):
    def __init__(self,model,brand,screensize,price,resolution):
        super().__init__(model,brand)
        self.screensize=screensize
        self.price=price
        self.resolution=resolution

    def newfeatures(self):
        print("this smart have new features:")
        print("this new smarttv screensize:",self.screensize)
        print("this new smarttv price:",self.price)
        print("this nem smarttv resolution:", self.resolution)

S=SMARTTV("A1","MI","1080","18000","UHD")
S.features()
S.newfeatures()
