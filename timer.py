import time
import subprocess
import sys
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'numpy']) 
import numpy
print(time.time())
arr = np.array([1,2,3])
print(arr)
