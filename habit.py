import time
oldtime = time.time()
time.sleep(20)
if time.time() - oldtime > 10:
	print("ten seconds have passed")
print("waiting")
