# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 11:18:26 2022

@author: User
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import scipy.stats as stats

import statsmodels.api as sm
from statsmodels.formula.api import ols


df=pd.read_csv("onewayanova.txt",sep="\t")
df_m=pd.melt(df.reset_index(),id_vars=['index'],value_vars=['A','B','C','D'])
df_m.columns=['index','students','marks']
print(df_m)

"""
plt.subplot(2,1,1)
sns.boxplot(df_m['students'],df_m['marks'])
plt.subplot(2,1,1)
sns.swarmplot(df_m['students'],df_m['marks'])
"""

"""
fvalue, pvalue=stats.f_oneway(df['A'],df['B'],df['C'],df['D'])
print(fvalue, pvalue)
"""

model = ols ('marks ~ students', data=df_m)
results=model.fit()
result_table=sm.stats.anova_lm(results,typ=2)
print(result_table)
