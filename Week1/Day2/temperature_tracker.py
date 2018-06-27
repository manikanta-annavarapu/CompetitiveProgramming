class TempTracker(object):

    # Implement methods to track the max, min, mean, and mode
    temp=[]
    total=0
    mode =0
    min=0
    max=0
    count=0
    dict1={}
    def insert(self, temperature):
        self.count=self.count+1
        self.total=self.total+temperature
        if(len(self.dict1)==0):
            self.min = temperature
            self.max = temperature
            self.mode = temperature
            self.dict1[temperature]=1
        elif(temperature in self.dict1.keys()):
            if(self.min>temperature):
                self.min=temperature
            if(self.max<temperature):
                self.max=temperature
            self.dict1[temperature]=self.dict1[temperature]+1
            if(self.dict1[temperature]>self.dict1[self.mode]):
                self.mode = temperature
        else:
            if(self.min>temperature):
                self.min=temperature
            if(self.max<temperature):
                self.max=temperature
            self.dict1[temperature]=1
            
    def get_max(self):
        return self.max

    def get_min(self):
        return self.min

    def get_mean(self):
        return self.total/self.count

    def get_mode(self):
        return self.mode

tracker = TempTracker()

tracker.insert(50)
print(['max','min','mean','mode'])
print([tracker.get_max(), tracker.get_min(),tracker.get_mean(),tracker.get_mode()])
tracker.insert(80)
print([tracker.get_max(), tracker.get_min(),tracker.get_mean(),tracker.get_mode()])
tracker.insert(80)
print([tracker.get_max(), tracker.get_min(),tracker.get_mean(),tracker.get_mode()])
tracker.insert(30)
print([tracker.get_max(), tracker.get_min(),tracker.get_mean(),tracker.get_mode()])