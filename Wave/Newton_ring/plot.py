import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
data = pd.read_csv("data.csv")

x = data["x"]

y = data["Ycal"]
p=[13,13]
q=[0.400,0.277]
r=[13,8.28]
s=[0.277,0.275]

fig, ax = plt.subplots()

plt.style.use("seaborn")
plt.grid(True)
ax.plot(x,y)
ax.plot(p,q,color='#444444',linestyle='dashed')

ax.plot(r,s,color='#444444',linestyle='dashed')
ax.set_xlabel("No of rings")
ax.set_ylabel("$D^2$(in $cm^2$)")
plt.xticks(np.arange(1, 21, 1.0))

plt.yticks(np.arange(0, 0.6666667, 0.025))
ax.annotate("(13,0.400)", (13, 0.400),xytext=(13.5,0.400))
ax.annotate("(13,0.277)", (13, 0.277),xytext=(13.5,0.250))
ax.annotate("(8.28,0.275)", (8.28, 0.275),xytext=(8.28,0.250))
plt.tight_layout()
ax.legend()


plt.show()
