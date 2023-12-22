Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pandas as pd
>>> import numpy as np
>>> import seaborn as sns
>>> import matplotlib.pyplot as plt
>>> import sklearn
>>> plt.show()
>>> income_df = pd.read_csv('C:/Users/MURALI/adult.csv')
>>> income_df.head()
   age          workclass  fnlwgt  ... hours-per-week  native-country  income
0   39          State-gov   77516  ...             40   United-States   <=50K
1   50   Self-emp-not-inc   83311  ...             13   United-States   <=50K
2   38            Private  215646  ...             40   United-States   <=50K
3   53            Private  234721  ...             40   United-States   <=50K
4   28            Private  338409  ...             40            Cuba   <=50K

[5 rows x 15 columns]
>>> income_df.describe()
                age        fnlwgt  ...  capital-loss  hours-per-week
count  32561.000000  3.256100e+04  ...  32561.000000    32561.000000
mean      38.581647  1.897784e+05  ...     87.303830       40.437456
std       13.640433  1.055500e+05  ...    402.960219       12.347429
min       17.000000  1.228500e+04  ...      0.000000        1.000000
25%       28.000000  1.178270e+05  ...      0.000000       40.000000
50%       37.000000  1.783560e+05  ...      0.000000       40.000000
75%       48.000000  2.370510e+05  ...      0.000000       45.000000
max       90.000000  1.484705e+06  ...   4356.000000       99.000000

[8 rows x 6 columns]
>>> income_df.isnull().sum()
age                0
workclass          0
fnlwgt             0
education          0
educational-num    0
marital-status     0
occupation         0
relationship       0
race               0
gender             0
capital-gain       0
capital-loss       0
hours-per-week     0
native-country     0
income             0
dtype: int64
>>> income_df.age = income_df.age.astype(float)
>>> income_df['hours-per-week'] = income_df['hours-per-week'].astype(float)
>>> my_df = income_df.dropna()
>>> my_df['predclass'] = my_df['income']
>>> del my_df['income']
>>> my_df['education-num'] = my_df['educational-num']
>>> del my_df['educational-num']
>>> my_df.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 32561 entries, 0 to 32560
Data columns (total 15 columns):
 #   Column          Non-Null Count  Dtype  
---  ------          --------------  -----  
 0   age             32561 non-null  float64
 1   workclass       32561 non-null  object 
 2   fnlwgt          32561 non-null  int64  
 3   education       32561 non-null  object 
 4   marital-status  32561 non-null  object 
 5   occupation      32561 non-null  object 
 6   relationship    32561 non-null  object 
 7   race            32561 non-null  object 
 8   gender          32561 non-null  object 
 9   capital-gain    32561 non-null  int64  
 10  capital-loss    32561 non-null  int64  
 11  hours-per-week  32561 non-null  float64
 12  native-country  32561 non-null  object 
 13  predclass       32561 non-null  object 
 14  education-num   32561 non-null  int64  
dtypes: float64(2), int64(4), object(9)
memory usage: 3.7+ MB
>>> my_df.isnull().sum()
age               0
workclass         0
fnlwgt            0
education         0
marital-status    0
occupation        0
relationship      0
race              0
gender            0
capital-gain      0
capital-loss      0
hours-per-week    0
native-country    0
predclass         0
education-num     0
dtype: int64
>>> print('workclass',my_df.workclass.unique())
workclass [' State-gov' ' Self-emp-not-inc' ' Private' ' Federal-gov' ' Local-gov'
 ' ?' ' Self-emp-inc' ' Without-pay' ' Never-worked']
>>> print('education',my_df.education.unique())
education [' Bachelors' ' HS-grad' ' 11th' ' Masters' ' 9th' ' Some-college'
 ' Assoc-acdm' ' Assoc-voc' ' 7th-8th' ' Doctorate' ' Prof-school'
 ' 5th-6th' ' 10th' ' 1st-4th' ' Preschool' ' 12th']
>>> print('martial-status',my_df['martial-status'].unique())
Traceback (most recent call last):
  File "C:\Users\MURALI\AppData\Local\Programs\Python\Python39\lib\site-packages\pandas\core\indexes\base.py", line 3621, in get_loc
    return self._engine.get_loc(casted_key)
  File "pandas\_libs\index.pyx", line 136, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index.pyx", line 163, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 5198, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 5206, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'martial-status'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    print('martial-status',my_df['martial-status'].unique())
  File "C:\Users\MURALI\AppData\Local\Programs\Python\Python39\lib\site-packages\pandas\core\frame.py", line 3505, in __getitem__
    indexer = self.columns.get_loc(key)
  File "C:\Users\MURALI\AppData\Local\Programs\Python\Python39\lib\site-packages\pandas\core\indexes\base.py", line 3623, in get_loc
    raise KeyError(key) from err
KeyError: 'martial-status'
>>> print('marital-status',my_df['marital-status'].unique())
marital-status [' Never-married' ' Married-civ-spouse' ' Divorced'
 ' Married-spouse-absent' ' Separated' ' Married-AF-spouse' ' Widowed']
>>> print('occupation',my_df.occupation.unique())
occupation [' Adm-clerical' ' Exec-managerial' ' Handlers-cleaners' ' Prof-specialty'
 ' Other-service' ' Sales' ' Craft-repair' ' Transport-moving'
 ' Farming-fishing' ' Machine-op-inspct' ' Tech-support' ' ?'
 ' Protective-serv' ' Armed-Forces' ' Priv-house-serv']
>>> print('relationship',my_df.relationship.unique())
relationship [' Not-in-family' ' Husband' ' Wife' ' Own-child' ' Unmarried'
 ' Other-relative']
>>> print('race',my_df.race.unique())
race [' White' ' Black' ' Asian-Pac-Islander' ' Amer-Indian-Eskimo' ' Other']
>>> print('native-country',my_df['native-country'].unique())
native-country [' United-States' ' Cuba' ' Jamaica' ' India' ' ?' ' Mexico' ' South'
 ' Puerto-Rico' ' Honduras' ' England' ' Canada' ' Germany' ' Iran'
 ' Philippines' ' Italy' ' Poland' ' Columbia' ' Cambodia' ' Thailand'
 ' Ecuador' ' Laos' ' Taiwan' ' Haiti' ' Portugal' ' Dominican-Republic'
 ' El-Salvador' ' France' ' Guatemala' ' China' ' Japan' ' Yugoslavia'
 ' Peru' ' Outlying-US(Guam-USVI-etc)' ' Scotland' ' Trinadad&Tobago'
 ' Greece' ' Nicaragua' ' Vietnam' ' Hong' ' Ireland' ' Hungary'
 ' Holand-Netherlands']
>>> print('predclass',my_df.predclass.unique())
predclass [' <=50K' ' >50K']
>>> #predclass
>>> #my_df.loc[income_df['predclass'] == ' >50K', 'predclass'] = 1
>>> #my_df.loc[income_df['predclass'] == ' <=50K', 'predclass'] = 0
>>> #predclass1 = my_df[my_df['predclass'] == 1
>>> #predclass0 = my_df[my_df['predclass'] == 0
>>> plt.style.available
['Solarize_Light2', '_classic_test_patch', '_mpl-gallery', '_mpl-gallery-nogrid', 'bmh', 'classic', 'dark_background', 'fast', 'fivethirtyeight', 'ggplot', 'grayscale', 'seaborn', 'seaborn-bright', 'seaborn-colorblind', 'seaborn-dark', 'seaborn-dark-palette', 'seaborn-darkgrid', 'seaborn-deep', 'seaborn-muted', 'seaborn-notebook', 'seaborn-paper', 'seaborn-pastel', 'seaborn-poster', 'seaborn-talk', 'seaborn-ticks', 'seaborn-white', 'seaborn-whitegrid', 'tableau-colorblind10']
>>> fig = plt.figure(figsize=(20,1))
>>> plt.style.use('seaborn-ticks')
>>> sns.countplot(y="predclass", data=my_df)
<AxesSubplot:xlabel='count', ylabel='predclass'>
>>> #education
>>> #income_df[['education', 'education-num']].groupby(['education'], as_index=False).mean().sort_values(by='education-num', ascending=False)
>>> my_df['education'].replace('Preschool', 'dropout',inplace=True)
>>> my_df['education'].replace('10th', 'dropout',inplace=True)
>>> my_df['education'].replace('11th', 'dropout',inplace=True)
>>> my_df['education'].replace('12th', 'dropout',inplace=True)
>>> my_df['education'].replace('1st-4th', 'dropout',inplace=True)
>>> my_df['education'].replace('5th-6th', 'dropout',inplace=True)
>>> my_df['education'].replace('7th-8th', 'dropout',inplace=True)
>>> my_df['education'].replace('9th', 'dropout',inplace=True)
>>> my_df['education'].replace('HS-Grad', 'HighGrad',inplace=True)
>>> my_df['education'].replace('HS-grad', 'HighGrad',inplace=True)
>>> my_df['education'].replace('Some-college', 'CommunityCollege',inplace=True)
>>> my_df['education'].replace('Assoc-acdm', 'CommunityCollege',inplace=True)
>>> my_df['education'].replace('Assoc-voc', 'CommunityCollege',inplace=True)
>>> my_df['education'].replace('Bachelors', 'Bachelors',inplace=True)
>>> my_df['education'].replace('Masters', 'Masters',inplace=True)
>>> my_df['education'].replace('Prof-school', 'Masters',inplace=True)
>>> my_df['education'].replace('Doctorate', 'Doctorate',inplace=True)
>>> my_df[['education', 'education-num']].groupby(['education'], as_index=False).mean().sort_values(by='education-num', ascending=False)
        education  education-num
10      Doctorate           16.0
14    Prof-school           15.0
12        Masters           14.0
9       Bachelors           13.0
7      Assoc-acdm           12.0
8       Assoc-voc           11.0
15   Some-college           10.0
11        HS-grad            9.0
2            12th            8.0
1            11th            7.0
0            10th            6.0
6             9th            5.0
5         7th-8th            4.0
4         5th-6th            3.0
3         1st-4th            2.0
13      Preschool            1.0
>>> fig = plt.figure(figsize=(20,3))
>>> plt.style.use('seaborn-ticks')
>>> sns.countplot(y="education", data=my_df)
<AxesSubplot:xlabel='count', ylabel='education'>
>>> my_df['marital-status'].replace('Never-married', 'NotMarried',inplace=True)
>>> my_df['marital-status'].replace(['Married-AF-spouse'], 'Married',inplace=True)
>>> my_df['marital-status'].replace(['Married-civ-spouse'], 'Married',inplace=True)
>>> my_df['marital-status'].replace(['Married-spouse-absent'], 'NotMarried',inplace=True)
>>> my_df['marital-status'].replace(['Separated'], 'Separated',inplace=True)
>>> my_df['marital-status'].replace(['Divorced'], 'Separated',inplace=True)
>>> my_df['marital-status'].replace(['Widowed'], 'Widowed',inplace=True)
>>> fig = plt.figure(figsize=(20,2))
>>> plt.style.use('seaborn-ticks')
>>> sns.countplot(y="marital-status", data=my_df)
<AxesSubplot:xlabel='count', ylabel='marital-status'>
>>> plt.style.use('seaborn-ticks')
>>> plt.figure(figsize=(20,4))
<Figure size 2000x400 with 0 Axes>
>>> 
KeyboardInterrupt
>>> sns.countplot(y="occupation", data=my_df)
<AxesSubplot:xlabel='count', ylabel='occupation'>
>>> Income Classification Model | Kaggle
SyntaxError: invalid syntax
>>> plt.style.use('seaborn-ticks')
>>> plt.figure(figsize=(20,3))
<Figure size 2000x300 with 0 Axes>
>>> sns.countplot(y="workclass", data=my_df)
<AxesSubplot:xlabel='count', ylabel='workclass'>
>>> # grid = sns.FacetGrid(train_df, col='Pclass', hue='Survived')
#grid = sns.FacetGrid(my_df, col='predclass', row='workclass', size=2.2, aspect=1.6)
#grid.map(plt.hist, 'age', alpha=.5, bins=20)
#grid.add_legend()
>>> my_df['age_bin'] = pd.cut(my_df['age'], 20)
>>> plt.style.use('seaborn-ticks')
>>> fig = plt.figure(figsize=(20,5))
>>> plt.subplot(1, 2, 1)
<AxesSubplot:>
>>> sns.countplot(y="age_bin", data=my_df)
<AxesSubplot:xlabel='count', ylabel='age_bin'>
>>> plt.subplot(1, 2, 2)
<AxesSubplot:>
>>> sns.distplot(my_df[my_df['predclass'] == '>50K']['age'], kde_kws={"label": ">$50K"})

Warning (from warnings module):
  File "C:\Users\MURALI\AppData\Local\Programs\Python\Python39\lib\site-packages\seaborn\distributions.py", line 2619
    warnings.warn(msg, FutureWarning)
FutureWarning: `distplot` is a deprecated function and will be removed in a future version. Please adapt your code to use either `displot` (a figure-level function with similar flexibility) or `histplot` (an axes-level function for histograms).

Warning (from warnings module):
  File "C:\Users\MURALI\AppData\Local\Programs\Python\Python39\lib\site-packages\seaborn\distributions.py", line 2657
    line, = ax.plot(a.mean(), 0)
RuntimeWarning: Mean of empty slice.

Warning (from warnings module):
  File "C:\Users\MURALI\AppData\Local\Programs\Python\Python39\lib\site-packages\numpy\core\_methods.py", line 189
    ret = ret.dtype.type(ret / rcount)
RuntimeWarning: invalid value encountered in double_scalars

Warning (from warnings module):
  File "C:\Users\MURALI\AppData\Local\Programs\Python\Python39\lib\site-packages\numpy\lib\histograms.py", line 906
    return n/db/n.sum(), bin_edges
RuntimeWarning: invalid value encountered in true_divide
<AxesSubplot:xlabel='age'>
>>> sns.distplot(my_df[my_df['predclass'] == '<=50K']['age'], kde_kws={"label": "<=$50K"})

Warning (from warnings module):
  File "C:\Users\MURALI\AppData\Local\Programs\Python\Python39\lib\site-packages\seaborn\distributions.py", line 2619
    warnings.warn(msg, FutureWarning)
FutureWarning: `distplot` is a deprecated function and will be removed in a future version. Please adapt your code to use either `displot` (a figure-level function with similar flexibility) or `histplot` (an axes-level function for histograms).

Warning (from warnings module):
  File "C:\Users\MURALI\AppData\Local\Programs\Python\Python39\lib\site-packages\seaborn\distributions.py", line 2657
    line, = ax.plot(a.mean(), 0)
RuntimeWarning: Mean of empty slice.

Warning (from warnings module):
  File "C:\Users\MURALI\AppData\Local\Programs\Python\Python39\lib\site-packages\numpy\core\_methods.py", line 189
    ret = ret.dtype.type(ret / rcount)
RuntimeWarning: invalid value encountered in double_scalars

Warning (from warnings module):
  File "C:\Users\MURALI\AppData\Local\Programs\Python\Python39\lib\site-packages\numpy\lib\histograms.py", line 906
    return n/db/n.sum(), bin_edges
RuntimeWarning: invalid value encountered in true_divide
<AxesSubplot:xlabel='age'>
>>> my_df[['predclass', 'age']].groupby(['predclass'], as_index=False).mean().sort_values(by='age', ascending=False)
  predclass        age
1      >50K  44.249841
0     <=50K  36.783738
>>> plt.style.use('seaborn-whitegrid')
>>> x, y, hue = "race", "prop", "gender"
>>> plt.figure(figsize=(20,5))
<Figure size 2000x500 with 0 Axes>
>>> f, axes = plt.subplots(1, 2)
>>> sns.countplot(x=x, hue=hue, data=my_df, ax=axes[0])
<AxesSubplot:xlabel='race', ylabel='count'>
>>> prop_df = (my_df[x].groupby(my_df[hue]).value_counts(normalize=True).rename(y).reset_index())
>>> sns.barplot(x=x, y=y, hue=hue, data=prop_df, ax=axes[1])
<AxesSubplot:xlabel='race', ylabel='prop'>
>>> my_df['hours-per-week_bin'] = pd.cut(my_df['hours-per-week'], 10)
>>> my_df['hours-per-week'] = my_df['hours-per-week']
>>> plt.style.use('seaborn-whitegrid')
>>> fig = plt.figure(figsize=(20,5))
>>> plt.subplot(1, 2, 1)
<AxesSubplot:>
>>> sns.countplot(y="hours-per-week_bin", data=my_df);
<AxesSubplot:xlabel='count', ylabel='hours-per-week_bin'>
>>> plt.subplot(1, 2, 2)
<AxesSubplot:>
>>> sns.distplot(my_df['hours-per-week']);

Warning (from warnings module):
  File "C:\Users\MURALI\AppData\Local\Programs\Python\Python39\lib\site-packages\seaborn\distributions.py", line 2619
    warnings.warn(msg, FutureWarning)
FutureWarning: `distplot` is a deprecated function and will be removed in a future version. Please adapt your code to use either `displot` (a figure-level function with similar flexibility) or `histplot` (an axes-level function for histograms).
<AxesSubplot:xlabel='hours-per-week', ylabel='Density'>
>>> sns.distplot(my_df[my_df['predclass'] == '>50K']['hours-per-week'], kde_kws={"label": ">$50K"})

Warning (from warnings module):
  File "C:\Users\MURALI\AppData\Local\Programs\Python\Python39\lib\site-packages\seaborn\distributions.py", line 2619
    warnings.warn(msg, FutureWarning)
FutureWarning: `distplot` is a deprecated function and will be removed in a future version. Please adapt your code to use either `displot` (a figure-level function with similar flexibility) or `histplot` (an axes-level function for histograms).

Warning (from warnings module):
  File "C:\Users\MURALI\AppData\Local\Programs\Python\Python39\lib\site-packages\seaborn\distributions.py", line 2657
    line, = ax.plot(a.mean(), 0)
RuntimeWarning: Mean of empty slice.

Warning (from warnings module):
  File "C:\Users\MURALI\AppData\Local\Programs\Python\Python39\lib\site-packages\numpy\core\_methods.py", line 189
    ret = ret.dtype.type(ret / rcount)
RuntimeWarning: invalid value encountered in double_scalars

Warning (from warnings module):
  File "C:\Users\MURALI\AppData\Local\Programs\Python\Python39\lib\site-packages\numpy\lib\histograms.py", line 906
    return n/db/n.sum(), bin_edges
RuntimeWarning: invalid value encountered in true_divide
<AxesSubplot:xlabel='hours-per-week', ylabel='Density'>
>>> sns.distplot(my_df[my_df['predclass'] == '<=50K']['hours-per-week'], kde_kws={"label": "<$50K"})

Warning (from warnings module):
  File "C:\Users\MURALI\AppData\Local\Programs\Python\Python39\lib\site-packages\seaborn\distributions.py", line 2619
    warnings.warn(msg, FutureWarning)
FutureWarning: `distplot` is a deprecated function and will be removed in a future version. Please adapt your code to use either `displot` (a figure-level function with similar flexibility) or `histplot` (an axes-level function for histograms).

Warning (from warnings module):
  File "C:\Users\MURALI\AppData\Local\Programs\Python\Python39\lib\site-packages\seaborn\distributions.py", line 2657
    line, = ax.plot(a.mean(), 0)
RuntimeWarning: Mean of empty slice.

Warning (from warnings module):
  File "C:\Users\MURALI\AppData\Local\Programs\Python\Python39\lib\site-packages\numpy\core\_methods.py", line 189
    ret = ret.dtype.type(ret / rcount)
RuntimeWarning: invalid value encountered in double_scalars

Warning (from warnings module):
  File "C:\Users\MURALI\AppData\Local\Programs\Python\Python39\lib\site-packages\numpy\lib\histograms.py", line 906
    return n/db/n.sum(), bin_edges
RuntimeWarning: invalid value encountered in true_divide
<AxesSubplot:xlabel='hours-per-week', ylabel='Density'>
>>> plt.ylim(0, None)
(0.0, 0.2509849644842426)
>>> plt.xlim(20, 60)
(20.0, 60.0)
>>> g = sns.jointplot(x = 'age', 
              y = 'hours-per-week',
              data = my_df, 
              kind = 'hex', 
              cmap= 'hot', 
              size=10)

Warning (from warnings module):
  File "C:\Users\MURALI\AppData\Local\Programs\Python\Python39\lib\site-packages\seaborn\axisgrid.py", line 2182
    warnings.warn(msg, UserWarning)
UserWarning: The `size` parameter has been renamed to `height`; please update your code.
>>> g = sns.jointplot(x = 'age',y = 'hours-per-week',data = my_df,kind = 'hex',cmap= 'hot',height=10)
>>> sns.regplot(my_df.age, my_df['hours-per-week'], ax=g.ax_joint, scatter=False, color='grey')

Warning (from warnings module):
  File "C:\Users\MURALI\AppData\Local\Programs\Python\Python39\lib\site-packages\seaborn\_decorators.py", line 36
    warnings.warn(
FutureWarning: Pass the following variables as keyword args: x, y. From version 0.12, the only valid positional argument will be `data`, and passing other arguments without an explicit keyword will result in an error or misinterpretation.
<AxesSubplot:xlabel='age', ylabel='hours-per-week'>
>>> my_df.head()
    age          workclass  ...        age_bin hours-per-week_bin
0  39.0          State-gov  ...  (38.9, 42.55]       (30.4, 40.2]
1  50.0   Self-emp-not-inc  ...  (49.85, 53.5]       (10.8, 20.6]
2  38.0            Private  ...  (35.25, 38.9]       (30.4, 40.2]
3  53.0            Private  ...  (49.85, 53.5]       (30.4, 40.2]
4  28.0            Private  ...  (27.95, 31.6]       (30.4, 40.2]

[5 rows x 17 columns]
>>> my_df['age-hours'] = my_df['age']*my_df['hours-per-week']
>>> my_df['age-hours_bin'] = pd.cut(my_df['age-hours'], 10)
>>> plt.style.use('seaborn-whitegrid')
>>> fig = plt.figure(figsize=(20,5))
>>> plt.subplot(1, 2, 1)
<AxesSubplot:>
>>> sns.countplot(y="age-hours_bin", data=my_df);
<AxesSubplot:xlabel='count', ylabel='age-hours_bin'>
>>> plt.subplot(1, 2, 2)
<AxesSubplot:>
>>> sns.distplot(my_df[my_df['predclass'] == '>50K']['age-hours'], kde_kws={"label": ">$50K"})

Warning (from warnings module):
  File "C:\Users\MURALI\AppData\Local\Programs\Python\Python39\lib\site-packages\seaborn\distributions.py", line 2619
    warnings.warn(msg, FutureWarning)
FutureWarning: `distplot` is a deprecated function and will be removed in a future version. Please adapt your code to use either `displot` (a figure-level function with similar flexibility) or `histplot` (an axes-level function for histograms).

Warning (from warnings module):
  File "C:\Users\MURALI\AppData\Local\Programs\Python\Python39\lib\site-packages\seaborn\distributions.py", line 2657
    line, = ax.plot(a.mean(), 0)
RuntimeWarning: Mean of empty slice.

Warning (from warnings module):
  File "C:\Users\MURALI\AppData\Local\Programs\Python\Python39\lib\site-packages\numpy\core\_methods.py", line 189
    ret = ret.dtype.type(ret / rcount)
RuntimeWarning: invalid value encountered in double_scalars

Warning (from warnings module):
  File "C:\Users\MURALI\AppData\Local\Programs\Python\Python39\lib\site-packages\numpy\lib\histograms.py", line 906
    return n/db/n.sum(), bin_edges
RuntimeWarning: invalid value encountered in true_divide
<AxesSubplot:xlabel='age-hours'>
>>> sns.distplot(my_df[my_df['predclass'] == '<=50K']['age-hours'], kde_kws={"label": "<$50K"})

Warning (from warnings module):
  File "C:\Users\MURALI\AppData\Local\Programs\Python\Python39\lib\site-packages\seaborn\distributions.py", line 2619
    warnings.warn(msg, FutureWarning)
FutureWarning: `distplot` is a deprecated function and will be removed in a future version. Please adapt your code to use either `displot` (a figure-level function with similar flexibility) or `histplot` (an axes-level function for histograms).

Warning (from warnings module):
  File "C:\Users\MURALI\AppData\Local\Programs\Python\Python39\lib\site-packages\seaborn\distributions.py", line 2657
    line, = ax.plot(a.mean(), 0)
RuntimeWarning: Mean of empty slice.

Warning (from warnings module):
  File "C:\Users\MURALI\AppData\Local\Programs\Python\Python39\lib\site-packages\numpy\core\_methods.py", line 189
    ret = ret.dtype.type(ret / rcount)
RuntimeWarning: invalid value encountered in double_scalars

Warning (from warnings module):
  File "C:\Users\MURALI\AppData\Local\Programs\Python\Python39\lib\site-packages\numpy\lib\histograms.py", line 906
    return n/db/n.sum(), bin_edges
RuntimeWarning: invalid value encountered in true_divide
<AxesSubplot:xlabel='age-hours'>
>>> pp = sns.pairplot(my_df, hue = 'predclass', palette = 'deep', size=3, diag_kind = 'kde', diag_kws=dict(shade=True), plot_kws=dict(s=20) )

Warning (from warnings module):
  File "C:\Users\MURALI\AppData\Local\Programs\Python\Python39\lib\site-packages\seaborn\axisgrid.py", line 2076
    warnings.warn(msg, UserWarning)
UserWarning: The `size` parameter has been renamed to `height`; please update your code.
 pp = sns.pairplot(my_df, hue = 'predclass', palette = 'deep', size=3, diag_kind = 'kde', diag_kws=dict(shade=True), plot_kws=dict(s=20) )
>>>  pp = sns.pairplot(my_df, hue = 'predclass', palette = 'deep', height=3, diag_kind = 'kde', diag_kws=dict(shade=True), plot_kws=dict(s=20) )
 
SyntaxError: unexpected indent
>>> p = sns.pairplot(my_df, hue = 'predclass', palette = 'deep', height=3, diag_kind = 'kde', diag_kws=dict(shade=True), plot_kws=dict(s=20) )
>>> pp.set(xticklabels=[])
<seaborn.axisgrid.PairGrid object at 0x000002DA5F1D06D0>
>>> def correlation_heatmap(df):
	_ , ax = plt.subplots(figsize =(14, 12))
	 colormap = sns.diverging_palette(220, 10, as_cmap = True)
	 
SyntaxError: unexpected indent
>>>  colormap = sns.diverging_palette(220, 10, as_cmap = True)
 
SyntaxError: unexpected indent
>>> colormap = sns.diverging_palette(220, 10, as_cmap = True)
>>> _ = sns.heatmap(
df.corr(), cmap = "YlGn",square=True,cbar_kws={'shrink':.9 },ax=ax,annot=True,linewidths=0.1,vmax=1.0, linecolor='white',annot_kws={'fontsize':12 })
Traceback (most recent call last):
  File "<pyshell#132>", line 2, in <module>
    df.corr(), cmap = "YlGn",square=True,cbar_kws={'shrink':.9 },ax=ax,annot=True,linewidths=0.1,vmax=1.0, linecolor='white',annot_kws={'fontsize':12 })
NameError: name 'df' is not defined
>>> df.corr(), cmap = "YlGn",square=True,cbar_kws={'shrink':.9 },ax=ax,annot=True,linewidths=0.1,vmax=1.0, linecolor='white',annot_kws={'fontsize':12 })
SyntaxError: cannot assign to function call
>>> _ = sns.heatmap(
        df.corr(), 
        cmap = "YlGn",
        square=True, 
        cbar_kws={'shrink':.9 }, 
        ax=ax,
        annot=True, 
        linewidths=0.1,vmax=1.0, linecolor='white',
        annot_kws={'fontsize':12 }
    )
Traceback (most recent call last):
  File "<pyshell#134>", line 2, in <module>
    df.corr(),
NameError: name 'df' is not defined
>>> plt.title('Pearson Correlation of Features', y=1.05, size=15)
Text(0.5, 1.05, 'Pearson Correlation of Features')
>>> correlation_heatmap(my_df)
Traceback (most recent call last):
  File "<pyshell#136>", line 1, in <module>
    correlation_heatmap(my_df)
NameError: name 'correlation_heatmap' is not defined
>>> def correlation_heatmap(df):
	 _ , ax = plt.subplots(figsize =(14, 12))
	  colormap = sns.diverging_palette(220, 10, as_cmap = True)
	  
SyntaxError: unexpected indent
>>> def correlation_heatmap(df):
	 _ , ax = plt.subplots(figsize =(14, 12))
	colormap = sns.diverging_palette(220, 10, as_cmap = True)
	
SyntaxError: unindent does not match any outer indentation level
>>> def correlation_heatmap(df):
	 _ , ax = plt.subplots(figsize =(14, 12))
	  colormap = sns.diverging_palette(220, 10, as_cmap = True)
	  
SyntaxError: unexpected indent
>>> def correlation_heatmap(df):
	 _ , ax = plt.subplots(figsize =(14, 12)) colormap = sns.diverging_palette(220, 10, as_cmap = True)
	 
SyntaxError: invalid syntax
>>> def correlation_heatmap(df):
	 _ , ax = plt.subplots(figsize =(14, 12))colormap = sns.diverging_palette(220, 10, as_cmap = True)
	 
SyntaxError: invalid syntax
>>> def correlation_heatmap(df):
	 _ , ax = plt.subplots(figsize =(14, 12))
	 colormap = sns.diverging_palette(220, 10, as_cmap = True)
	 _ = sns.heatmap(
		 df.corr(),
		 cmap = "YlGn",
		  square=True,
		 cbar_kws={'shrink':.9 },
		 ax=ax,
		 annot=True,
		 linewidths=0.1,vmax=1.0, linecolor='white',
		 annot_kws={'fontsize':12 }
		 )
	 plt.title('Pearson Correlation of Features', y=1.05, size=15)
	 correlation_heatmap(my_df)

	 
>>> my_df.tail()
        age      workclass  ...  age-hours     age-hours_bin
32556  27.0        Private  ...     1026.0   (909.9, 1798.8]
32557  40.0        Private  ...     1600.0   (909.9, 1798.8]
32558  58.0        Private  ...     2320.0  (1798.8, 2687.7]
32559  22.0        Private  ...      440.0   (12.111, 909.9]
32560  52.0   Self-emp-inc  ...     2080.0  (1798.8, 2687.7]

[5 rows x 19 columns]
>>> import math
>>> def plot_bivariate_bar(dataset, hue, cols=5, width=20, height=15, hspace=0.2, wspace=0.5):
	 dataset = dataset.select_dtypes(include=[np.object])
	 plt.style.use('seaborn-whitegrid')
	 fig = plt.figure(figsize=(width,height))
	 fig.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=wspace, hspace=hspace)
	 rows = math.ceil(float(dataset.shape[1]) / cols)
	 for i, column in enumerate(dataset.columns):
		ax = fig.add_subplot(rows, cols, i + 1)
		
SyntaxError: inconsistent use of tabs and spaces in indentation
>>> import mathdef plot_bivariate_bar(dataset, hue, cols=5, width=20, height=15, hspace=0.2, wspace=0.5):
	 dataset = dataset.select_dtypes(include=[np.object])
	 plt.style.use('seaborn-whitegrid')
	 fig = plt.figure(figsize=(width,height))
	 fig.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=wspace, hspace=hspace)
	 rows = math.ceil(float(dataset.shape[1]) / cols)
	 for i, column in enumerate(dataset.columns):
		 
SyntaxError: invalid syntax
>>> import math
>>> def plot_bivariate_bar(dataset, hue, cols=5, width=20, height=15, hspace=0.2, wspace=0.5):
	 dataset = dataset.select_dtypes(include=[np.object])
	 plt.style.use('seaborn-whitegrid')
	 fig = plt.figure(figsize=(width,height))
	 fig.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=wspace, hspace=hspace)
	 rows = math.ceil(float(dataset.shape[1]) / cols)
	 for i, column in enumerate(dataset.columns):
		 ax = fig.add_subplot(rows, cols, i + 1)
		 ax.set_title(column)
		 if dataset.dtypes[column] == np.object:
			  g = sns.countplot(y=column, hue=hue, data=dataset)
			  substrings = [s.get_text()[:10] for s in g.get_ytickl
					g.set(yticklabels=substrings)
KeyboardInterrupt
>>> bivariate_df = my_df.loc[:, ['workclass', 'education', 
           'marital-status', 'occupation', 
           'relationship', 'race', 'gender','predclass']]
>>> plot_bivariate_bar(bivariate_df, hue='predclass', cols=2, width=20, height=15, hspace=0.4, wspace=0.5)
Traceback (most recent call last):
  File "<pyshell#207>", line 1, in <module>
    plot_bivariate_bar(bivariate_df, hue='predclass', cols=2, width=20, height=15, hspace=0.4, wspace=0.5)
NameError: name 'plot_bivariate_bar' is not defined
>>> import math
>>> def plot_bivariate_bar(dataset, hue, cols=5, width=20, height=15, hspace=0.2, wspace=0.5):
	 dataset = dataset.select_dtypes(include=[np.object])
	 plt.style.use('seaborn-whitegrid')
	 fig = plt.figure(figsize=(width,height))
	 fig.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=wspace, hspace=hspace)
	 rows = math.ceil(float(dataset.shape[1]) / cols)
	 for i, column in enumerate(dataset.columns):
		 ax = fig.add_subplot(rows, cols, i + 1)
		 ax.set_title(column)
		 if dataset.dtypes[column] == np.object:
			  g = sns.countplot(y=column, hue=hue, data=dataset)
			  substrings = [s.get_text()[:10] for s in g.get_yticklables]
			  g.set(yticklabels=substrings)
			  bivariate_df = my_df.loc[:, ['workclass', 'education', 
           'marital-status', 'occupation', 
           'relationship', 'race', 'gender','predclass']]
			  plot_bivariate_bar(bivariate_df, hue='predclass', cols=2, width=20, height=15, hspace=0.4, wspace=0.5)

			  
>>> from matplotlib import pyplot
>>> a4_dims = (20, 5)
>>> fig, ax = pyplot.subplots(figsize=a4_dims)
>>> ax = sns.violinplot(x="occupation", y="age", hue="predclass",data=my_df, gridsize=100, palette="muted", split=True, saturation=0.75)
>>> ax
<AxesSubplot:xlabel='occupation', ylabel='age'>
>>> from sklearn.cluster import KMeans
>>> from matplotlib import cm
>>> from sklearn.metrics import silhouette_samples
>>> from sklearn.metrics import silhouette_score
>>> from sklearn.metrics import accuracy_score
>>> from sklearn.metrics import accuracy_scorefrom sklearn.decomposition import PCA
SyntaxError: invalid syntax
>>> from sklearn.decomposition import PCA
>>> from pandas.tools.plotting import scatter_matrix
Traceback (most recent call last):
  File "<pyshell#231>", line 1, in <module>
    from pandas.tools.plotting import scatter_matrix
ModuleNotFoundError: No module named 'pandas.tools'
>>> my_df = my_df.apply(LabelEncoder().fit_transform)
Traceback (most recent call last):
  File "<pyshell#232>", line 1, in <module>
    my_df = my_df.apply(LabelEncoder().fit_transform)
NameError: name 'LabelEncoder' is not defined
>>> from sklearn.linear_model import LogisticRegression
>>> from sklearn import svm
>>> from sklearn.ensemble import RandomForestClassifier
>>> from sklearn.neighbors import KNeighborsClassifier
>>> from sklearn.naive_bayes import GaussianNB
>>> from sklearn.tree import DecisionTreeClassifier
>>> from sklearn import metrics
>>> 
KeyboardInterrupt
>>> from sklearn.metrics import confusion_matrix
>>> from sklearn.svm import SVR
>>> from sklearn.preprocessing import LabelEncoder
>>> from sklearn.model_selection import train_test_split
>>> my_df = my_df.apply(LabelEncoder().fit_transform)
>>> my_df.head()
   age  workclass  fnlwgt  ...  hours-per-week_bin  age-hours  age-hours_bin
0   22          7    2671  ...                   3        631              1
1   33          6    2926  ...                   1        290              0
2   21          4   14086  ...                   3        620              1
3   36          4   15336  ...                   3        810              2
4   11          4   19355  ...                   3        477              1

[5 rows x 19 columns]
>>> drop_elements = ['education', 'native-country', 'predclass', 'age_bin', 'age-hours_bin','hours-per-week_bin']
>>> y = my_df["predclass"]
>>> X = my_df.drop(drop_elements, axis=1)
>>> X.head()
   age  workclass  fnlwgt  ...  hours-per-week  education-num  age-hours
0   22          7    2671  ...              39             12        631
1   33          6    2926  ...              12             12        290
2   21          4   14086  ...              39              8        620
3   36          4   15336  ...              39              6        810
4   11          4   19355  ...              39             12        477

[5 rows x 13 columns]
>>> X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=2)
>>> from sklearn import preprocessing
>>> from sklearn.preprocessing import StandardScaler
>>> std_scale = preprocessing.StandardScaler().fit(my_df.drop('predclass', axis=1))
>>> X = std_scale.transform(my_df.drop('predclass', axis=1))
>>> y = my_df['predclass']
>>> target_names = [0,1]
>>> colors = ['blue','yellow','pink']
>>> lw = 2
>>> alpha = 0.3
>>> plt.style.use('seaborn-whitegrid')
>>> plt.style.use('seaborn-whitegrid')
>>> plt.figure(2, figsize=(20, 8))
<Figure size 2000x300 with 1 Axes>
>>> plt.subplot(1, 2, 1)
<AxesSubplot:>
>>> pca = PCA(n_components=2)
>>> X_r = pca.fit(X).transform(X)
>>> for color, i, target_name in zip(colors, [0, 1], target_names):
	plt.scatter(X_r[y == i, 0], X_r[y == i, 1],
		    color=color,
		    alpha=alpha,
		    lw=lw,
		    label=target_name)
	plt.legend(loc='best', shadow=False, scatterpoints=1)
	plt.title('First two PCA directions');
	ax = plt.subplot(1, 2, 2, projection='3d')
	pca = PCA(n_components=3)
	X_reduced = pca.fit(X).transform(X)
	for color, i, target_name in zip(colors, [0, 1], target_names):
		ax.scatter(X_reduced[y == i, 0], X_reduced[y == i, 1], X_reduced[y == i, 2],
			   color=color,
			   alpha=alpha,
			   lw=lw,
			   label=target_name)

		
<matplotlib.collections.PathCollection object at 0x000002DA07485250>
<matplotlib.legend.Legend object at 0x000002DA07485100>
Text(0.5, 1.0, 'First two PCA directions')
<mpl_toolkits.mplot3d.art3d.Path3DCollection object at 0x000002DA07518F10>
<mpl_toolkits.mplot3d.art3d.Path3DCollection object at 0x000002DA07509460>
Traceback (most recent call last):
  File "<pyshell#288>", line 2, in <module>
    plt.scatter(X_r[y == i, 0], X_r[y == i, 1],
  File "C:\Users\MURALI\AppData\Local\Programs\Python\Python39\lib\site-packages\matplotlib\pyplot.py", line 2819, in scatter
    __ret = gca().scatter(
  File "C:\Users\MURALI\AppData\Local\Programs\Python\Python39\lib\site-packages\matplotlib\__init__.py", line 1412, in inner
    return func(ax, *map(sanitize_sequence, args), **kwargs)
  File "C:\Users\MURALI\AppData\Local\Programs\Python\Python39\lib\site-packages\mpl_toolkits\mplot3d\axes3d.py", line 2389, in scatter
    patches = super().scatter(xs, ys, s=s, c=c, *args, **kwargs)
  File "C:\Users\MURALI\AppData\Local\Programs\Python\Python39\lib\site-packages\matplotlib\__init__.py", line 1412, in inner
    return func(ax, *map(sanitize_sequence, args), **kwargs)
  File "C:\Users\MURALI\AppData\Local\Programs\Python\Python39\lib\site-packages\matplotlib\axes\_axes.py", line 4371, in scatter
    raise ValueError(
ValueError: s must be a scalar, or float array-like with the same size as x and y
>>> for color, i, target_name in zip(colors, [0, 1], target_names):
	plt.scatter(X_r[y == i, 0], X_r[y == i, 1],
		    color=color,
		    alpha=alpha,
		    lw=lw,
		    label=target_name)
	plt.legend(loc='best', shadow=False, scatterpoints=1)
	plt.title('First two PCA directions');
	ax = plt.subplot(1, 2, 2, projection='3d')
	pca = PCA(n_components=3)
	X_reduced = pca.fit(X).transform(X)
	for color, i, target_name in zip(colors, [0, 1], target_names):
		ax.scatter(X_reduced[y == i, 0], X_reduced[y == i, 1], X_reduced[y == i, 2],
			   color=color,
			   alpha=alpha,
			   lw=lw,
			   label=target_name)
		plt.legend(loc='best', shadow=False, scatterpoints=1)
		ax.set_title("First three PCA directions")
		ax.set_xlabel("1st eigenvector")
		ax.set_ylabel("2nd eigenvector")
		ax.set_zlabel("3rd eigenvector")
		ax.view_init(30, 10)

		
Traceback (most recent call last):
  File "<pyshell#303>", line 2, in <module>
    plt.scatter(X_r[y == i, 0], X_r[y == i, 1],
  File "C:\Users\MURALI\AppData\Local\Programs\Python\Python39\lib\site-packages\matplotlib\pyplot.py", line 2819, in scatter
    __ret = gca().scatter(
  File "C:\Users\MURALI\AppData\Local\Programs\Python\Python39\lib\site-packages\matplotlib\__init__.py", line 1412, in inner
    return func(ax, *map(sanitize_sequence, args), **kwargs)
  File "C:\Users\MURALI\AppData\Local\Programs\Python\Python39\lib\site-packages\mpl_toolkits\mplot3d\axes3d.py", line 2389, in scatter
    patches = super().scatter(xs, ys, s=s, c=c, *args, **kwargs)
  File "C:\Users\MURALI\AppData\Local\Programs\Python\Python39\lib\site-packages\matplotlib\__init__.py", line 1412, in inner
    return func(ax, *map(sanitize_sequence, args), **kwargs)
  File "C:\Users\MURALI\AppData\Local\Programs\Python\Python39\lib\site-packages\matplotlib\axes\_axes.py", line 4371, in scatter
    raise ValueError(
ValueError: s must be a scalar, or float array-like with the same size as x and y
>>> sc = StandardScaler()
>>> X_train_std = sc.fit_transform(X_train)
>>> pca = PCA(n_components=None)
>>> x_train_pca = pca.fit_transform(X_train_std)
>>> a = pca.explained_variance_ratio_
>>> a_running = a.cumsum()
>>> a_running
array([0.21141111, 0.31530474, 0.40936437, 0.49090168, 0.57059516,
       0.64780627, 0.72145442, 0.79187467, 0.85444727, 0.91412814,
       0.96824953, 0.99798581, 1.        ])
>>> from sklearn.linear_model import Perceptron
>>> ppn = Perceptron(eta0=1, random_state=1)
>>> ppn.fit(X_train, y_train)
Perceptron(eta0=1, random_state=1)
>>> /opt/conda/lib/python3.6/site-packages/sklearn/linear_model/stochastic_gradient.py:128: FutureWarning: max_iter and tol parameters have been added in <class 'sklearn.linear_model.perceptron.Perceptron'> in 0.19. If both are left unset, they default to max_iter=5 and tol=None. If tol is not None, max_iter defaults to max_iter=1000. From 0.21, default max_iter will be 1000, and default tol will be 1e-3.
  "and default tol will be 1e-3." % type(self), FutureWarning)
  
SyntaxError: invalid syntax
>>> y_pred = ppn.predict(X_test)
>>> accuracy_score(y_pred,y_test)
0.24366651312759097
>>> from sklearn.model_selection import cross_val_score
>>> score_ppn=cross_val_score(ppn, X,y, cv=5)
>>> score_ppn.mean()
0.7616789761999342
>>> gaussian = GaussianNB()
>>> gaussian.fit(X_train, y_train)
GaussianNB()
>>> score_gaussian = gaussian.score(X_test,y_test)
>>> print('The accuracy of Gaussian Naive Bayes is', score_gaussian)
The accuracy of Gaussian Naive Bayes is 0.8140641793336404
>>> from sklearn.svm import SVC
>>> svc = SVC(gamma=0.22)
>>> svc.fit(X_train, y_train)
SVC(gamma=0.22)
>>> score_svc = svc.score(X_test,y_test)
>>> print('The accuracy of SVC is', score_svc)
The accuracy of SVC is 0.7571011822508829
>>> svc_radical =svm.SVC(kernel='rbf',C=1,gamma=0.22)
>>> svc_radical.fit(X_train,y_train.values.ravel())
SVC(C=1, gamma=0.22)
>>> score_svc_radical = svc_radical.score(X_test,y_test)
>>> print('The accuracy of Radical SVC Model is', score_svc_radical)
The accuracy of Radical SVC Model is 0.7571011822508829
>>> logreg = LogisticRegression()
>>> logreg.fit(X_train, y_train)

Warning (from warnings module):
  File "C:\Users\MURALI\AppData\Local\Programs\Python\Python39\lib\site-packages\sklearn\linear_model\_logistic.py", line 444
    n_iter_i = _check_optimize_result(
ConvergenceWarning: lbfgs failed to converge (status=1):
STOP: TOTAL NO. of ITERATIONS REACHED LIMIT.

Increase the number of iterations (max_iter) or scale the data as shown in:
    https://scikit-learn.org/stable/modules/preprocessing.html
Please also refer to the documentation for alternative solver options:
    https://scikit-learn.org/stable/modules/linear_model.html#logistic-regression
LogisticRegression()
>>> score_logreg = logreg.score(X_test,y_test)
>>> print('The accuracy of the Logistic Regression is', score_logreg)
The accuracy of the Logistic Regression is 0.8023952095808383
>>> randomforest = RandomForestClassifier()
>>> randomforest.fit(X_train, y_train)
RandomForestClassifier()
>>> score_randomforest = randomforest.score(X_test,y_test)
>>> print('The accuracy of the Random Forest Model is', score_randomforest)
The accuracy of the Random Forest Model is 0.84692154153232
>>> knn = KNeighborsClassifier()
>>> knn.fit(X_train, y_train)
KNeighborsClassifier()
>>> score_knn = knn.score(X_test,y_test)
>>> print('The accuracy of the KNN Model is',score_knn)
The accuracy of the KNN Model is 0.7581759557807461
>>> from sklearn.model_selection import KFold
>>> from sklearn.model_selection import cross_val_score
>>> from sklearn.model_selection import cross_val_predict
>>> kfold = KFold(n_splits=10, random_state=22) #
Traceback (most recent call last):
  File "<pyshell#348>", line 1, in <module>
    kfold = KFold(n_splits=10, random_state=22) #
  File "C:\Users\MURALI\AppData\Local\Programs\Python\Python39\lib\site-packages\sklearn\model_selection\_split.py", line 435, in __init__
    super().__init__(n_splits=n_splits, shuffle=shuffle, random_state=random_state)
  File "C:\Users\MURALI\AppData\Local\Programs\Python\Python39\lib\site-packages\sklearn\model_selection\_split.py", line 296, in __init__
    raise ValueError(
ValueError: Setting a random_state has no effect since shuffle is False. You should leave random_state to its default (None), or set shuffle=True.
>>> kfold = KFold(n_splits=10, random_state=22)
Traceback (most recent call last):
  File "<pyshell#349>", line 1, in <module>
    kfold = KFold(n_splits=10, random_state=22)
  File "C:\Users\MURALI\AppData\Local\Programs\Python\Python39\lib\site-packages\sklearn\model_selection\_split.py", line 435, in __init__
    super().__init__(n_splits=n_splits, shuffle=shuffle, random_state=random_state)
  File "C:\Users\MURALI\AppData\Local\Programs\Python\Python39\lib\site-packages\sklearn\model_selection\_split.py", line 296, in __init__
    raise ValueError(
ValueError: Setting a random_state has no effect since shuffle is False. You should leave random_state to its default (None), or set shuffle=True.
>>> kfold = KFold(n_splits=10, random_state=null)
Traceback (most recent call last):
  File "<pyshell#350>", line 1, in <module>
    kfold = KFold(n_splits=10, random_state=null)
NameError: name 'null' is not defined
>>> kfold = KFold(n_splits=10, random_state=0)
Traceback (most recent call last):
  File "<pyshell#351>", line 1, in <module>
    kfold = KFold(n_splits=10, random_state=0)
  File "C:\Users\MURALI\AppData\Local\Programs\Python\Python39\lib\site-packages\sklearn\model_selection\_split.py", line 435, in __init__
    super().__init__(n_splits=n_splits, shuffle=shuffle, random_state=random_state)
  File "C:\Users\MURALI\AppData\Local\Programs\Python\Python39\lib\site-packages\sklearn\model_selection\_split.py", line 296, in __init__
    raise ValueError(
ValueError: Setting a random_state has no effect since shuffle is False. You should leave random_state to its default (None), or set shuffle=True.
>>> kfold = KFold(n_splits=10, random_state='none')
Traceback (most recent call last):
  File "<pyshell#352>", line 1, in <module>
    kfold = KFold(n_splits=10, random_state='none')
  File "C:\Users\MURALI\AppData\Local\Programs\Python\Python39\lib\site-packages\sklearn\model_selection\_split.py", line 435, in __init__
    super().__init__(n_splits=n_splits, shuffle=shuffle, random_state=random_state)
  File "C:\Users\MURALI\AppData\Local\Programs\Python\Python39\lib\site-packages\sklearn\model_selection\_split.py", line 296, in __init__
    raise ValueError(
ValueError: Setting a random_state has no effect since shuffle is False. You should leave random_state to its default (None), or set shuffle=True.
>>> xyz=[]
>>> accuracy=[]
>>> std=[]
>>> classifiers=['Naive Bayes','Linear Svm','Radial Svm','Logistic Regression','Decision Tree','KNN','Random Forest']
>>> models=[GaussianNB(), svm.SVC(kernel='linear'),svm.SVC(kernel='rbf'),LogisticRegression(),DecisionTreeClassifier(),KNeighborsClassifier(n_neighbors=9),RandomForestClassifier(n_estimators=100)]
>>> KNeighborsClassifier(n_neighbors=9),RandomForestClassifier(n_estimators=100)]
SyntaxError: unmatched ']'
>>> for i in models:
	model = i
	cv_result = cross_val_score(model,X,y, cv = kfold,scoring = "accuracy")
	cv_result=cv_result
	cv_result=cv_result
	xyz.append(cv_result.mean())
	std.append(cv_result.std())
	accuracy.append(cv_result)
	models_dataframe=pd.DataFrame({'CV Mean':xyz,'Std':std},index=classifiers)
	models_dataframe

	
Traceback (most recent call last):
  File "<pyshell#378>", line 3, in <module>
    cv_result = cross_val_score(model,X,y, cv = kfold,scoring = "accuracy")
NameError: name 'kfold' is not defined
>>> def_kfold(): = KFold(n_splits=10, random_state='none')
SyntaxError: invalid syntax
>>> def_kfold(): =
SyntaxError: invalid syntax
>>> def_kfold():
	
SyntaxError: invalid syntax
>>> def_kfold()
Traceback (most recent call last):
  File "<pyshell#382>", line 1, in <module>
    def_kfold()
NameError: name 'def_kfold' is not defined
>>> def_kfold();
Traceback (most recent call last):
  File "<pyshell#383>", line 1, in <module>
    def_kfold();
NameError: name 'def_kfold' is not defined
>>> kfold = KFold(n_splits=10, random_state='none')
Traceback (most recent call last):
  File "<pyshell#384>", line 1, in <module>
    kfold = KFold(n_splits=10, random_state='none')
  File "C:\Users\MURALI\AppData\Local\Programs\Python\Python39\lib\site-packages\sklearn\model_selection\_split.py", line 435, in __init__
    super().__init__(n_splits=n_splits, shuffle=shuffle, random_state=random_state)
  File "C:\Users\MURALI\AppData\Local\Programs\Python\Python39\lib\site-packages\sklearn\model_selection\_split.py", line 296, in __init__
    raise ValueError(
ValueError: Setting a random_state has no effect since shuffle is False. You should leave random_state to its default (None), or set shuffle=True.
>>> 
>>> kfold = KFold(n_splits=10)
>>> xyz=[]
>>> accuracy=[]
>>> std=[]
>>> classifiers=['Naive Bayes','Linear Svm','Radial Svm','Logistic Regression','Decision Tree','KNN','Random Forest']
>>> models=[GaussianNB(), svm.SVC(kernel='linear'),svm.SVC(kernel='rbf'),LogisticRegression(),DecisionTreeClassifier(),KNeighborsClassifier(n_neighbors=9),RandomForestClassifier(n_estimators=100)]
>>> for i in models:
	model = i
	cv_result = cross_val_score(model,X,y, cv = kfold,scoring = "accuracy")
	cv_result=cv_result
	cv_result=cv_result
	xyz.append(cv_result.mean())
	std.append(cv_result.std())
	accuracy.append(cv_result)
	models_dataframe=pd.DataFrame({'CV Mean':xyz,'Std':std},index=classifiers)
	models_dataframe

	
                     CV Mean       Std
Naive Bayes          0.80925  0.004776
Linear Svm           0.80925  0.004776
Radial Svm           0.80925  0.004776
Logistic Regression  0.80925  0.004776
Decision Tree        0.80925  0.004776
KNN                  0.80925  0.004776
Random Forest        0.80925  0.004776
