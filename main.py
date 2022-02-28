import printutils
import time as t
import random

loader_amount = 100
loaders = []

for i in range(loader_amount):
	loaders.append(printutils.Loader(20,20, loader_name="Training neural net layer "+str(i)+"\t", overide_last=False))
for loader in loaders:
	for i in range(20):
		t.sleep(random.random()*0.001)
		if(random.random()<0.05):
			t.sleep(random.random()*0.3)
		loader.progress()