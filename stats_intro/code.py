# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#path of the data file- path
data = pd.read_csv(path)
data['Gender'].replace('-','Agender',inplace=True)
gender_count = data['Gender'].value_counts()
gender_count.plot.box()
#Code starts here 




# --------------
#Code starts here
alignment = data['Alignment'].value_counts()
alignment.plot.pie(title='Character Alignment')



# --------------
#Code starts here
sc_df = data.loc[:,['Strength','Combat']]
sc_covariance = np.round((sc_df['Strength'].cov(sc_df['Combat'])),decimals=2)
sc_strength = sc_df['Strength'].std()
sc_combat = sc_df['Combat'].std()

sc_pearson = sc_df['Strength'].corr(sc_df['Combat'],method='pearson')
ic_df = data.loc[:,['Intelligence','Combat']]
ic_covariance=np.round((ic_df['Intelligence'].cov(ic_df['Combat'])),decimals=2)
ic_intelligence=ic_df['Intelligence'].std()
ic_combat=ic_df['Combat'].std()
ic_pearson = ic_df['Intelligence'].corr(ic_df['Combat'],method='pearson')
print(sc_covariance)
print(ic_covariance)


# --------------
#Code starts here
total_high = data['Total'].quantile(0.99)
super_best = data[data['Total']>total_high]
super_best_names = list(super_best.Name.unique())
print(super_best_names)


# --------------
#Code starts here
fig,(ax_1,ax_2,ax_3) = plt.subplots(3,1)
data['Intelligence'].plot.box(ax=ax_1,title='Intelligence')
data['Speed'].plot.box(ax=ax_2,title='Speed')
data['Power'].plot.box(ax=ax_3,title='Power')
fig.tight_layout()
plt.legend()
plt.show()


