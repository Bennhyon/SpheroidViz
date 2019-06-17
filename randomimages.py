# small script made to test the program
from PIL import Image
from numpy import random
import os
import sys
import time
import threading
def CreateRandomImages(width=100 ,height=100, n=10, name="image-", extension="png", path="RandomImages/", wait=0, clear=False):
    path = os.path.dirname(os.path.realpath(__file__))+"/"+path
    if clear:
        ls = os.listdir(path)
        for file in ls:
            if name in file:
                os.unlink(path+file)
    print("CTRL+C to stop")
    try:
        for i in range(n):
            dim = random.rand(100,100,3)*i
            im = Image.fromarray(dim.astype('uint8')).convert("RGBA")
            im.save(path+name+str(i)+"."+extension)
            if wait > 0:
                time.sleep(wait)
    except KeyboardInterrupt:
        print("\nStopped, exiting..")
        time.sleep(1)
        exit()
    except Exception as e:
        print(e)
#thread = threading.Thread(target=CreateRandomImages, daemon=True, kwargs={"width":500,"height":500,"n":500,"wait":0.2, "extension":"png","path":"Randomed2/", "clear":True})
#thread.start()
CreateRandomImages(width=500,height=500,n=500,wait=0.2, extension="png",path="Randomedlol/", clear=True)