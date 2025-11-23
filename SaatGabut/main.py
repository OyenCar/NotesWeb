import pandas as pd
import numpy as np

df = pd.DataFrame(np.arange(1,20,0.5),columns=["Angka"])

print(df[(df["Angka"] < 10) & (df["Angka"] > 5)])