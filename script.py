import seaborn as sns
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('all_data.csv')
print(df.head())

df.rename(columns={"Life expectancy at birth (years)": "life_expectancy"}, inplace=True)


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



########### Has GDP increased over time in the six nations? ###########
# plt.figure(figsize=(8, 6))
# sns.lineplot(x='Year', y='GDP', hue='Country', data=df)
# plt.title("GDP Over the Years")
# plt.show()
# plt.close()
########### GDP is increased for USA and China but for other countries, it remains constant ###########



########### Is there a correlation between GDP and life expectancy of a country? ###########
# plt.figure(figsize=(8, 6))
# sns.scatterplot(x='life_expectancy', y='GDP', hue='Country', data=df)
# plt.title("Relation between GDP and Life expectancy")
# plt.show()
# plt.close()
########### There is a positive correlation for every country except Zimbabwe ###########



########### What is the average life expectancy in these nations? ###########
average_life_expectancy = df.groupby('Country').mean('life_expectancy').life_expectancy
plt.figure(figsize=(8, 6))
plt.title("Average Life Expectancy")
sns.barplot(x=average_life_expectancy.index, y=average_life_expectancy.values, palette='husl')
plt.xticks(rotation=45)
plt.show()
plt.close()

########### ###########




