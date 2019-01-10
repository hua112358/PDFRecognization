import pandas as pd
import numpy as np
import sys


a = pd.DataFrame(np.random.randint(0, 10, (10, 5)))
b = pd.DataFrame(np.random.randint(0, 10, (10, 5)))

print(a)
print(a.mean())

mean = a.mean(axis = 1).values
print(mean)
print(mean < 5)
print((mean < 5).mean())
