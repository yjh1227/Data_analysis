
# coding: utf-8

# In[1]:


# 展示时隐藏代码
import IPython.core.display as di
di.display_html('<script>jQuery(function() {if (jQuery("body.notebook_app").length == 0) { jQuery(".input_area").toggle(); jQuery(".prompt").toggle();}});</script>', raw=True)


# In[13]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[14]:


from IPython .display import Image
display(Image(r'data/白酒地域分布.png'))


# In[15]:


from IPython .display import Image
display(Image(r'data/地区产量前10.png'))


# In[16]:


display(Image(r'data/白酒香型.png'))


# In[17]:


s = pd.read_csv(r'data/company_count.csv')
s['亏损比例'] = s['亏损企业数']/s['企业数']
s.index = [str(i) for i in range(2003, 2017)]
del s['时间']
s


# In[18]:


fig = plt.figure()
fig.set_figheight(4)
fig.set_figwidth(15)

plt.subplot(131)
s['企业数'].plot(kind='line', marker='o')
plt.title('企业数')
plt.grid(axis='y', linestyle='--')

plt.subplot(132)
s['亏损企业数'].plot(kind='line', marker='o')
plt.title('亏损企业数')
plt.grid(axis='y', linestyle='--')

plt.subplot(133)
s['亏损比例'].plot(kind='line', marker='o')
plt.title('亏损比例')
plt.grid(axis='y', linestyle='--')

plt.savefig(r'pic/行业企业数.png')
plt.show();


# In[19]:


import matplotlib.ticker as mtick
fmt = '%.0f%%'  #不保留小数
yticks = mtick.FormatStrFormatter(fmt)

s = pd.DataFrame()
s['收入'] = [2661.14, 3746.67, 4461, 5018, 5258.89, 5558.86, 6125.74]
s['CR4收入'] = [401.64, 599.22, 824.82, 810.96, 726.1, 772.71, 888.93]
s['CR4占比'] = s['CR4收入']/s['收入']*100
s.index = range(2010, 2017)

fig = plt.figure()

ax = s[['收入', 'CR4收入']].plot(kind='bar', use_index=True)
ax.grid(linestyle='--', linewidth=1, axis='y')
plt.title('CR4收入及占比')
plt.ylabel('单位：亿元')
plt.legend(('收入', 'CR4收入'))

ax2 = ax.twinx()
ax2.plot(ax.get_xticks(), s[['CR4占比']], linestyle='-', marker='o', linewidth=2.0)
ax2.yaxis.set_major_formatter(yticks)
plt.ylabel('CR4占比')
plt.legend(('CR4占比', ), loc='upper center')

plt.savefig(r'pic/CR4收入及占比.png')
plt.show();


# In[20]:


from IPython.display import display, Image
# display(Image(r'pic/1.png', width=100))
display(Image(r'pic/白酒统计口径.png'))


# In[21]:


output = pd.read_csv(r'data/月度数据.csv', skiprows=2, skipfooter=2, engine='python')


# In[22]:


s = []
for i in output['时间']:
    s.append(i.replace('年', '-').replace('月', ''))
output.index = [pd.to_datetime(t) for t in s]


# In[23]:


del output['时间']


# In[24]:


output.columns = ['白酒当期产量', '白酒累计产量', '白酒同比增长', '白酒累计增长']


# In[25]:


output['白酒当期产量'].plot(kind='line', figsize = (10, 5))
# plt.grid(axis='y', linestyle='--')
plt.title('白酒每月产量')
plt.ylabel('单位：万千升')
plt.grid(linestyle='--')
plt.savefig(r'pic/白酒每月产量.png')
plt.show();


# In[26]:


s = output['白酒当期产量'][-12:]
# s.index = ['201607', '201608', '201609', '201610', '201611', '201612', '201701', '201702', '201703', '201704', '201705', '201706']
a = pd.date_range(start='2016-07', end='2017-07', freq='M')
a = [str(i)[:7] for i in a]

s.index = a
s.plot(kind='bar')
plt.grid(axis='y', linestyle='--')
plt.title('最近一年每月产量')
plt.ylabel('单位：万千升')
# plt.grid(linestyle='--')
plt.savefig(r'pic/最近一年每月产量.png')
plt.show();


# In[27]:


output_year = output[output.index.month == 12]
output_year.index = range(1989, 2017)


# In[28]:


output_year['白酒累计产量'].plot(marker='o')
plt.title('白酒历年产量')
plt.ylabel('单位：万千升')
plt.grid(linestyle='--')
plt.savefig(r'pic/白酒历年产量.png')
plt.show();


# In[29]:


sales = pd.read_csv(r'data/季度数据.csv', skiprows=2, skipfooter=1, engine='python')


# In[30]:


sales.index = pd.date_range(start='1998Q1', end='2017Q3', freq='Q')


# In[31]:


del sales['时间']


# In[32]:


sales.columns = ['白酒累计销售', '白酒产销率', '产销率同比', '库存比年初增长']


# In[33]:


sales['白酒产销率'].plot(kind='line', figsize = (10, 5))
# plt.grid(axis='y', linestyle='--')
plt.title('白酒每季产销率')
# plt.ylabel('单位：万千升')
plt.grid(axis='y', linestyle='--')
plt.savefig(r'pic/白酒每季产销率.png')
plt.show();


# In[34]:


sales_year = sales[sales.index.month == 12]


# In[35]:


sales_year.index = range(1998, 2017)


# In[36]:


sales_year


# In[37]:


sales_year['白酒累计销售'].plot(marker='o')
# plt.grid(axis='y', linestyle='--')
plt.title('白酒历年销量')
plt.ylabel('单位：万千升')
plt.grid(axis='y', linestyle='--')
plt.savefig(r'pic/白酒历年销量.png')
plt.show();


# In[38]:


sales_year['库存比年初增长'].plot(marker='o')
# plt.grid(axis='y', linestyle='--')
plt.title('白酒历年库存变化率')
# plt.ylabel('单位：万千升')
plt.grid(axis='y', linestyle='--')
plt.savefig(r'pic/白酒历年库存变化率.png')
plt.show();


# In[39]:


import matplotlib.ticker as mtick
fmt = '%.0f%%'  #不保留小数
yticks = mtick.FormatStrFormatter(fmt)

s = pd.DataFrame()
s['产量'] = output_year['白酒累计产量'][-19:]
s['销量'] = sales_year['白酒累计销售']
s['产量增速'] = s['产量'].pct_change(axis=0)*100
s['销量增速'] = s['销量'].pct_change(axis=0)*100
s.index = range(1998, 2017)

fig = plt.figure()

ax = s[['产量', '销量']].plot(kind='bar', use_index=True)
ax.grid(linestyle='--', linewidth=1, axis='y')
plt.title('产销量及增速')
plt.ylabel('单位：万千升')
plt.legend(('产量', '销量'))

ax2 = ax.twinx()
ax2.plot(ax.get_xticks(), s[['产量增速', '销量增速']], linestyle='-', marker='o', linewidth=2.0)
ax2.yaxis.set_major_formatter(yticks)
plt.ylabel('增速')
plt.legend(('产量增速', '销量增速'), loc='upper center')

plt.savefig(r'pic/产销量及增速.png')
plt.show();


# In[40]:


s = pd.DataFrame()
s['销售收入'] = [741.07, 971.4, 1241.96, 1574.85, 2095.17, 2661.14, 3746.67, 4461, 5018, 5258.89, 5558.86, 6125.74]
s['销量'] = [358.1, 383.9, 485.2, 562.1, 628.5, 873.3, 1021.8, 1126.7, 1166.2, 1202.6, 1278.8, 1305.7]
s['销售单价'] = s['销售收入'] / s['销量']
s['销售收入增速'] = s['销售收入'].pct_change(axis=0) * 100
s['销售单价增速'] = s['销售单价'].pct_change(axis=0) * 100
s.index = range(2005, 2017)
# s.to_csv(r'data/销售收入.csv')
fig = plt.figure()

ax = s[['销售收入']].plot(kind='bar', use_index=True)
ax.grid(linestyle='--', linewidth=1, axis='y')
plt.title('销售收入及增速')
plt.ylabel('单位：亿元')
plt.legend(('销售收入', ))

ax2 = ax.twinx()
ax2.plot(
    ax.get_xticks(), s[['销售收入增速']], color='r', linestyle='-', marker='o', linewidth=2.0)
ax2.yaxis.set_major_formatter(yticks)
plt.ylabel('增速')
plt.legend(('增速', ), loc='upper center')

plt.savefig(r'pic/销售收入及增速.png')
plt.show()


# In[41]:


fig = plt.figure()

ax = s[['销售单价']].plot(kind='bar', use_index=True)
ax.grid(linestyle='--', linewidth=1, axis='y')
plt.title('销售单价及增速')
plt.ylabel('单位：万元/千升')
plt.legend(('销售单价', ))

ax2 = ax.twinx()
ax2.plot(ax.get_xticks(), s[['销售单价增速']], color='r', linestyle='-', marker='o', linewidth=2.0)
ax2.yaxis.set_major_formatter(yticks)
plt.ylabel('增速')
plt.legend(('增速',), loc='upper center')

plt.savefig(r'pic/销售单价及增速.png')
plt.show();


# In[42]:


display(Image(r'data/白酒需求.jpg'))


# In[43]:


s = pd.DataFrame()
s['固定资产投资'] = [88773.62, 109998.2, 137323.94, 172828.4, 224598.77, 251683.77, 311485.13, 374694.74, 446294.09, 512020.65, 561999.83]
s['餐饮业营业额'] = [1260.2, 1573.6, 1907.22, 2592.82, 2686.36, 3195.14, 3809.05, 4419.85, 4533.33, 4615.3, 4864.01]
s['城镇人均收入'] = [10493, 11759.5, 13785.8, 15780.8, 17174.7, 19109.4, 21809.8, 24564.7, 26467, 28843.85, 31194.83]
s['投资增长率'] = s['固定资产投资'].pct_change(axis=0) * 100
s['餐饮增长率'] = s['餐饮业营业额'].pct_change(axis=0) * 100
s['城镇收入增长率'] = s['城镇人均收入'].pct_change(axis=0) * 100

s.index = range(2005, 2016)

fig = plt.figure()
fig.set_figheight(4)
fig.set_figwidth(15)

plt.subplot(131)
s['投资增长率'].plot(kind='line', marker='o')
plt.title('投资增长率')
plt.grid(axis='y', linestyle='--')

plt.subplot(132)
s['餐饮增长率'].plot(kind='line', marker='o')
plt.title('餐饮增长率')
plt.grid(axis='y', linestyle='--')

plt.subplot(133)
s['城镇收入增长率'].plot(kind='line', marker='o')
plt.title('城镇收入增长率')
plt.grid(axis='y', linestyle='--')

plt.savefig(r'pic/投资餐饮收入增长率.png')
plt.show();


# In[44]:


population_age = pd.read_csv(r'data/人口年龄结构.csv', skiprows=2, skipfooter=2, engine='python')
population_age.index = range(1989, 2016)
# population_age.iloc[1:, 7:13].sum(axis=1)


# In[45]:


people_2 = pd.read_csv(r'data/人口年龄结构_抽样.csv', skiprows=2, skipfooter=2, engine='python')


people_2.iloc[1:, 7:13]

a = people_2.iloc[1:, 7:13].sum(axis=1)

b = people_2.iloc[1:, 1]

# 25-54岁人群所占比例
c = a/b


# In[46]:


fig = plt.figure()
fig.set_figheight(4)
fig.set_figwidth(16)

plt.subplot(141)
population_age['年末总人口(万人)'].plot(kind='line', marker='o')
plt.title('人口数')
plt.ylabel('单位：万人')
plt.grid(axis='y', linestyle='--')

plt.subplot(142)
population_age['0-14岁人口(万人)'].plot(kind='line', marker='o')
plt.title('0-14岁人口数')
plt.grid(axis='y', linestyle='--')

plt.subplot(143)
population_age['15-64岁人口(万人)'].plot(kind='line', marker='o')
plt.title('15-64岁人口数')
plt.grid(axis='y', linestyle='--')

plt.subplot(144)
population_age['65岁及以上人口(万人)'].plot(kind='line', marker='o')
plt.title('65岁以上人口数')
plt.grid(axis='y', linestyle='--')

plt.savefig(r'pic/人口数数据.png')
plt.show();


# In[47]:


income = pd.read_csv(r'data/城乡人均收入年度数据.csv', skiprows=2, skipfooter=2, engine='python')


# In[48]:


s = pd.DataFrame()
s['城镇人均收入'] = income['城镇居民家庭人均可支配收入(元)']
s['农村人均收入'] = income['农村居民家庭人均纯收入(元)']
s.index = range(1989, 2013)

s.plot(marker='o')
plt.grid(axis='y', linestyle='--')
plt.title('城乡人均收入')
plt.ylabel('单位：元')
plt.savefig(r'pic/城乡人均收入.png')
plt.show()


# In[49]:


s = pd.DataFrame()
s['城镇人均收入'] = income['城镇居民家庭人均可支配收入(元)'][-18:]
s['农村人均收入'] = income['农村居民家庭人均纯收入(元)'][-18:]
s['城镇人均消耗'] = [9.93, 9.72, 9.55, 9.68, 9.61, 10.01, 9.68, 9.12, 9.39, 8.94, 8.85, 9.12, 9.14, 7.62, 7.99, 7.02, 6.76, 6.88]
s['农村人均消耗'] = [6.53, 7.11, 7.13, 6.98, 6.98, 7.02, 7.1, 7.5, 7.67, 7.84, 9.59, 9.97, 10.18, 9.67, 10.08, 9.74, 10.15, 10.04]
s.index = range(1995, 2013)

fig = plt.figure()

ax = s[['城镇人均消耗', '农村人均消耗']].plot(kind='bar', use_index=True)
ax.grid(linestyle='--', linewidth=1, axis='y')
plt.title('城乡人均收入及酒类消耗')
plt.ylabel('单位：千克')
plt.legend(('城镇消耗', '农村消耗'), bbox_to_anchor=(-0.1, 0.95))

ax2 = ax.twinx()
ax2.plot(ax.get_xticks(), s[['城镇人均收入', '农村人均收入']], linestyle='-', marker='o', linewidth=2.0)
plt.ylabel('人均收入：元')
plt.legend(('城镇收入', '农村收入'), bbox_to_anchor=(-0.1, 0.75))

plt.savefig(r'pic/城乡人均收入及酒类消耗.png')
plt.show();


# In[50]:


s.T


# In[51]:


display(Image(r'data/OPEC.png'))


# In[52]:


display(Image(r'data/Global_consumption_percapita_2010.png'))


# In[53]:


display(Image(r'data/人均酒精量测算.png'))


# In[54]:


s = pd.DataFrame()
s['15-64'] = population_age['15-64岁人口(万人)'][-13:]
s['白酒销量'] = [i for i in sales_year['白酒累计销售'][-13:]]
sales_year['白酒累计销售'][-13:]
s['15-64人均'] = s['白酒销量']/s['15-64']*1000
s.index = range(2003, 2016)
s


# In[55]:


s = pd.DataFrame()
s['城镇人均消耗'] = [9.93, 9.72, 9.55, 9.68, 9.61, 10.01, 9.68, 9.12, 9.39, 8.94, 8.85, 9.12, 9.14, 7.62, 7.99, 7.02, 6.76, 6.88]
s['农村人均消耗'] = [6.53, 7.11, 7.13, 6.98, 6.98, 7.02, 7.1, 7.5, 7.67, 7.84, 9.59, 9.97, 10.18, 9.67, 10.08, 9.74, 10.15, 10.04]
s.index = range(1995, 2013)
s.plot(marker='o')
plt.grid(axis='y', linestyle='--')
plt.title('城乡人均酒类消耗')
plt.ylabel('单位：千克')
plt.savefig(r'pic/城乡人均酒类消耗.png')
plt.show()


# In[56]:


countryside = pd.read_csv(r'data/countryside.csv')
countryside


# In[57]:


del countryside['时间']
countryside.index = range(2005, 2012)


# In[58]:


countryside.plot(kind='bar')
plt.grid(axis='y', linestyle='--')
plt.legend(bbox_to_anchor=(1, 0.75))
plt.title('农村各地区人均酒类消费')
plt.ylabel('单位：千克')
plt.show()

