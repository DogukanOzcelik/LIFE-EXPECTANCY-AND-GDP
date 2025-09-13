import seaborn as sns
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('all_data.csv')
print(df.head())

df.rename(columns={"Life expectancy at birth (years)": "life_expentancy"}, inplace=True)


########### Has life expectancy increased over time in the six nations? ###########
# plt.figure(figsize=(10, 8))
# ax = plt.subplot(2, 1, 1)
# sns.lineplot(x="Year", y="life_expentancy", data=df)

# print(df.Year.unique())
# ax.set_xticks(df.Year.unique())
# plt.xticks(rotation=45)

# plt.subplot(2, 1, 2)
# sns.boxplot(x="Year", y="life_expentancy", data=df)
# plt.xticks(rotation=45)

# plt.tight_layout()
# plt.show()
# plt.close()
########### Life expectancy tend to be increasing over time in the six nations. ###########

