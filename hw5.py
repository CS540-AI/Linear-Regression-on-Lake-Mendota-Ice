import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv(sys.argv[1])
plt.plot(df["year"], df["days"])
plt.xlabel("Year")
plt.ylabel("Number of Frozen Days")
plt.savefig("plot.jpg")