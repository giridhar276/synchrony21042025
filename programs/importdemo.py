#method1
import math # all the methods of math are importing to your program
print(math.log(1))
print(math.cos(2))


#method2 - using alias
import matplotlib.pyplot as plt
plt.plot([10,20],[30,40])
plt.show()

#method3  # only tan() and log() are imported # all the methods are NOT imported
from math import tan,log
print(tan(1))
print(log(2))
