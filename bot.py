import numpy as np
import gam as gg
class bt:
    def __init__(self,par):
        self.score=0
        self.xx=0
        self.yy=0
        self.w1=par['w1']
        self.w2=par['w2']
        self.img=par['Img']
        self.hmk=par['hmk']
        self.pixscr=0
        # player velocity, max velocity, downward accleration, accleration on flap
        self.playerVelY    =  -9   # player's velocity along Y, default same as playerFlapped
        self.playerMaxVelY =  10   # max vel along Y, max descend speed
        self.playerMinVelY =  -8   # min vel along Y, max ascend speed
        self.playerAccY    =   1   # players downward accleration
        self.playerRot     =  45   # player's rotation
        self.playerVelRot  =   3   # angular speed
        self.playerRotThr  =  20   # rotation threshold
        self.playerFlapAcc =  -9   # players speed on flapping
        self.playerFlapped = False # True when player flaps
        #print("Object initialised")
        pass
    
    def update(self,hd,vd,hd1,vd1):
        hd=hd/gg.SCREENWIDTH #horizontal distance from pipe
        vd=vd/gg.SCREENHEIGHT #vertical distance from ground
        aa=self.forp(hd,vd,hd1,vd1)
        if(aa==True):
            if self.yy> -2 * self.img.get_height():
                self.playerVelY = self.playerFlapAcc
                self.playerFlapped = True
        
        #print("updation has ocured",aa)
        pass
        
        
    #forward prop    
    def forp(self,hd,vd,hd1,vd1):
        x=np.array([hd,vd])
        x=x.reshape((2,1))
        z1=np.dot(self.w1,x)
        a1=np.tanh(z1)
        
        z2=np.dot(self.w2,a1)
        a2=self.sigmoid(z2)
        
        #flap if a2 is >0.5
        if(a2>=0.5):
            return True
        else:
            return False
    def sigmoid(self,z):
        return 1/(1+np.exp(-z))
    def updscr(self):
        self.pixscr+=1
        return
    def initxy(self):
        self.xx=0.1*gg.SCREENWIDTH
        self.yy=np.random.randint(0,gg.SCREENHEIGHT)