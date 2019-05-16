import pandas as pd
from matplotlib import pyplot as plt

df = pd.DataFrame({'Year': range(1, 21)})
df['Balance'] = 100 * (1.05**df['Year'])

print(df)

plt.plot(df.Year, df.Balance, color='green')
plt.xlabel('Year')
plt.ylabel('Balance')
plt.grid()
plt.show()