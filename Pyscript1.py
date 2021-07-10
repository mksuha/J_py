#!/usr/bin/env python
# coding: utf-8

# In[5]:


#!/usr/bin/env python
#coding: utf-8

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import sys
import os.path as path

arg = sys.argv[1]
print("Reading {}".format(arg))
df = pd.read_csv ('regrex1.csv')

x = df.x
y = df.y

plt.scatter(x,y)
plt.title('regrex1')
plt.xlabel('x')
plt.ylabel('y')
plt.savefig("Pyscript_scatter.png")

x = df.x.to_numpy()
y = df.y.to_numpy()
m, b = np.polyfit(x, y, 1)
print(m)
print(b)
plt.plot(x, y, 'o')
plt.plot(x, m*x + b)

              # Saving output of the plot to a png file
plt.savefig("Pyscript_fit.png")


# In[ ]:




