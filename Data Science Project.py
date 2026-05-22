# We're actually going to be doing the work in this file -- as this one doesn't handle the mass text.
# Note that I DID use Copilot to quickly install Pandas because I got confused-- but nothing else!!
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Firstly, create a code that scans the data for specific data related to the gender and to the amount of hours spent on a game.
df= pd.read_csv("Gaming_Academic_Performance.csv")

new_df = df[["gender", "gaming_hours"]]
# Reminder that the argument is that the gender of the gamer does not affect their gaming hours.

columns_keeping = ["gender", "gaming_hours"]
new_df = df.drop(columns=df.columns.difference(columns_keeping))
print(new_df.info())
# Looking at some info; I heard printing the info first before visualising it is a safegaurd???


# Visualisation #1 -- Trend line / linear regression.
# Didn't finish this one...


# Visualisation #2 -- Singular univariate visualisation.
plt.figure(figsize=(8,5))
plt.hist(new_df['gaming_hours'].dropna(), bins=15, color='hotpink', edgecolor='deeppink')
plt.title('Distribution of Gaming Hours')
plt.xlabel('Gaming hours')
plt.ylabel('Occurrence Frequency')
plt.tight_layout()
plt.show()

# Visualisation #3 -- Shows the measure of spread.
data = new_df.dropna(subset=['gender', 'gaming_hours'])
data.boxplot(column='gaming_hours', by='gender', grid=False, figsize=(8,5))
plt.suptitle('')
plt.title('Gaming Hours by Gender')
plt.xlabel('Gender')
plt.ylabel('Gaming Hours')
plt.show()


# Visualisation #4 -- Singular bivariate visualisation.
mean_hours = df.groupby('gender')['gaming_hours'].mean()
fig, ax = plt.subplots(figsize=(8, 5))
ax.bar(mean_hours.index, mean_hours.values, color=['hotpink', 'skyblue', 'gold'])
ax.set_title('Gaming Hours in Correlation to Gender')
ax.set_xlabel('Gender')
ax.set_ylabel('Average Number of Hours Spent Gaming')
plt.show()
