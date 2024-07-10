import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import math
import plotly.express as px
from plotly.subplots import make_subplots
from matplotlib.font_manager import FontProperties as font

# 設定字型的路徑
font = font(fname="ChocolateClassicalSans-Regular.ttf")

# 讀取CSV文件
df = pd.read_csv("game_data_資料整理.csv",encoding='utf-16',delimiter='\t')

# 轉換發售日期為日期格式
df['發售日期'] = pd.to_datetime(df['發售日期'])

# 添加年份欄位
df['發售年份'] = df['發售日期'].dt.year

# 設置 seaborn 圖表風格為帶有白色網格的風格
sns.set_style("darkgrid")

# 同時設置 matplotlib 的 rc 參數
plt.rcParams['axes.facecolor'] = 'black'
plt.rcParams['figure.facecolor'] = 'black'
plt.rcParams['axes.edgecolor'] = 'white'
plt.rcParams['axes.labelcolor'] = 'white'
plt.rcParams['xtick.color'] = 'white'
plt.rcParams['ytick.color'] = 'white'
plt.rcParams['grid.color'] = 'gray'
plt.rcParams['text.color'] = 'white'
plt.rcParams['legend.facecolor'] = 'black'
plt.rcParams['legend.edgecolor'] = 'white'

# 圖表一 繪製遊戲發售趨勢圖（按年份）(小型開發商製作)(銷售數量大於一千套)

# 創建一個大小為 12x6 吋的圖表和一個子圖
fig, ax = plt.subplots(figsize=(12, 6))

# 篩選出販售數量大於10000的資料
filtered_df = df[(df['售出數量'] > 1000) & (df['開發商分級'] == '小型開發商') & (df['發售年份'] >= 2006) & (df['發售年份'] < 2024) & (df['玩家評價次數'] >= 100) & (df['玩家評價分數'] != 0)]

# 計算每年的遊戲數量並按照年份排序
games_count_per_year = filtered_df['發售年份'].value_counts().reset_index()
games_count_per_year.columns = ['發售年份', '遊戲數量']
games_count_per_year = games_count_per_year.sort_values(by='發售年份')

# 繪製柱形圖，指定順序為按照年份排序
sns.barplot(x='發售年份', y='遊戲數量', data=games_count_per_year, palette='hsv', order=games_count_per_year['發售年份'], ax=ax)

# 設置圖表標題和標籤
plt.title('遊戲發售趨勢圖(按年份)(小型開發商製作)(銷售數量大於一千套)', fontproperties=font, fontsize=20)
plt.xticks(rotation=45, fontproperties=font, fontsize=10)
plt.yticks(rotation=0, fontproperties=font, fontsize=10)
plt.xlabel('日期', fontproperties=font, fontsize=15)
plt.ylabel('數    \n量    ', rotation=0, fontproperties=font, fontsize=15)

# 在每個柱狀條上顯示數量
for p in ax.patches:
    ax.annotate(format(p.get_height(), '.0f'), 
                (p.get_x() + p.get_width() / 2., p.get_height()), 
                ha = 'center', va = 'baseline', 
                fontsize = 10, color = 'black', fontproperties=font, xytext = (0, 1),
                textcoords = 'offset points')
# 顯示圖表
plt.show()

#------------------------------------------------------------------------#

#圖表二 繪製遊戲發售趨勢圖（按年份）(大型開發商製作)(銷售數量大於一千套)

# 創建一個大小為 12x6 吋的圖表和一個子圖
fig, ax = plt.subplots(figsize=(12, 6))

# 篩選出販售數量大於1000的資料
filtered_df = df[(df['售出數量'] > 1000) & (df['開發商分級'] == '大型開發商') & (df['發售年份'] >= 2006 ) & (df['發售年份'] < 2024) & (df['玩家評價次數'] >= 100) & (df['玩家評價分數'] != 0)]

# 計算每年的遊戲數量並按照年份排序
games_count_per_year = filtered_df['發售年份'].value_counts().reset_index()
games_count_per_year.columns = ['發售年份', '遊戲數量']
games_count_per_year = games_count_per_year.sort_values(by='發售年份')

# 繪製柱形圖，指定順序為按照年份排序
sns.barplot(x='發售年份', y='遊戲數量', data=games_count_per_year, palette='hsv', order=games_count_per_year['發售年份'], ax=ax)

# 設置圖表標題和標籤
plt.title('遊戲發售趨勢圖(按年份)(大型開發商製作)(銷售數量大於一千套)', fontproperties=font, fontsize=20)
plt.xticks(rotation=45, fontproperties=font, fontsize=10)
plt.yticks(rotation=0, fontproperties=font, fontsize=10)
plt.xlabel('日期', fontproperties=font, fontsize=15)
plt.ylabel('數    \n量    ', rotation=0, fontproperties=font, fontsize=15)

# 在每個柱狀條上顯示數量
for p in ax.patches:
    ax.annotate(format(p.get_height(), '.0f'), 
                (p.get_x() + p.get_width() / 2., p.get_height()), 
                ha = 'center', va = 'baseline', 
                fontsize = 10, color = 'black', fontproperties=font, xytext = (0, 1),
                textcoords = 'offset points')
    
plt.show()

#------------------------------------------------------------------------#


#圖表三 繪製遊戲發售趨勢圖（按年份）(中型開發商製作)(銷售數量大於一千套)

# 創建一個大小為 12x6 吋的圖表和一個子圖
fig, ax = plt.subplots(figsize=(12, 6))

# 篩選出販售數量大於1000的資料
filtered_df = df[(df['售出數量'] > 1000) & (df['開發商分級'] == '中型開發商') & (df['發售年份'] >= 2006 ) & (df['發售年份'] < 2024) & (df['玩家評價次數'] >= 100) & (df['玩家評價分數'] != 0)]

# 計算每年的遊戲數量並按照年份排序
games_count_per_year = filtered_df['發售年份'].value_counts().reset_index()
games_count_per_year.columns = ['發售年份', '遊戲數量']
games_count_per_year = games_count_per_year.sort_values(by='發售年份')

# 繪製柱形圖，指定順序為按照年份排序
sns.barplot(x='發售年份', y='遊戲數量', data=games_count_per_year, palette='hsv', order=games_count_per_year['發售年份'], ax=ax)

# 設置圖表標題和標籤
plt.title('遊戲發售趨勢圖(按年份)(中型開發商製作)(銷售數量大於一千套)', fontproperties=font, fontsize=20)
plt.xticks(rotation=45, fontproperties=font, fontsize=10)
plt.yticks(rotation=0, fontproperties=font, fontsize=10)
plt.xlabel('日期', fontproperties=font, fontsize=15)
plt.ylabel('數    \n量    ', rotation=0, fontproperties=font, fontsize=15)

# 在每個柱狀條上顯示數量
for p in ax.patches:
    ax.annotate(format(p.get_height(), '.0f'), 
                (p.get_x() + p.get_width() / 2., p.get_height()), 
                ha = 'center', va = 'baseline', 
                fontsize = 10, color = 'black', fontproperties=font, xytext = (0, 1),
                textcoords = 'offset points')
    
plt.show()

#------------------------------------------------------------------------#

#圖表四 繪製遊戲發售趨勢圖（按年份）(業餘愛好製作)(銷售數量大於一千套)

# 創建一個大小為 12x6 吋的圖表和一個子圖
fig, ax = plt.subplots(figsize=(12, 6))

# 篩選出販售數量大於1000的資料
filtered_df = df[(df['售出數量'] > 1000) & (df['開發商分級'] == '業餘愛好') & (df['發售年份'] >= 2006 ) & (df['發售年份'] < 2024) & (df['玩家評價次數'] >= 100) & (df['玩家評價分數'] != 0)]

# 計算每年的遊戲數量並按照年份排序
games_count_per_year = filtered_df['發售年份'].value_counts().reset_index()
games_count_per_year.columns = ['發售年份', '遊戲數量']
games_count_per_year = games_count_per_year.sort_values(by='發售年份')

# 繪製柱形圖，指定順序為按照年份排序
sns.barplot(x='發售年份', y='遊戲數量', data=games_count_per_year, palette='hsv', order=games_count_per_year['發售年份'], ax=ax)

# 設置圖表標題和標籤
plt.title('遊戲發售趨勢圖(按年份)(業餘愛好製作)(銷售數量大於一千套)', fontproperties=font, fontsize=20)
plt.xticks(rotation=45, fontproperties=font, fontsize=10)
plt.yticks(rotation=0, fontproperties=font, fontsize=10)
plt.xlabel('日期', fontproperties=font, fontsize=15)
plt.ylabel('數    \n量    ', rotation=0, fontproperties=font, fontsize=15)

# 在每個柱狀條上顯示數量
for p in ax.patches:
    ax.annotate(format(p.get_height(), '.0f'), 
                (p.get_x() + p.get_width() / 2., p.get_height()), 
                ha = 'center', va = 'baseline', 
                fontsize = 10, color = 'black', fontproperties=font, xytext = (0, 1),
                textcoords = 'offset points')
    
plt.show()

#------------------------------------------------------------------------#

#圖表四 繪製遊戲發售趨勢圖（按年份）(銷售數量大於一千套) 圓餅圖

# 篩選出販售數量大於1000的資料
filtered_df = df[(df['售出數量'] > 1000) & (df['發售年份'] >= 2006 ) & (df['發售年份'] < 2024) & (df['玩家評價次數'] >= 100) & (df['玩家評價分數'] != 0)]

# 計算每個開發商的遊戲數量
games_count_per_developer = filtered_df['開發商分級'].value_counts().reset_index()
games_count_per_developer.columns = ['開發商分級', '遊戲數量']

# 使用 Plotly Express 創建圓餅圖
fig = px.pie(games_count_per_developer, values='遊戲數量', names='開發商分級', title='分級&遊戲數量分佈')

# 更新圓餅圖內部字體大小
fig.update_traces(textposition='inside', textinfo='percent+label', textfont_size=14)

# 更新佈局以調整標題字體大小和圖表大小
fig.update_layout(title_font_size=18, width=600, height=600)

# 顯示圖表
fig.show()

#------------------------------------------------------------------------#

#圖表五 玩家評價分數平均數&玩家評價次數平均數

# 篩選出販售數量大於1000的資料
filtered_df = df[(df['售出數量'] > 1000)& (df['發售年份'] >= 2006) & (df['發售年份'] < 2024) & (df['玩家評價次數'] >= 100) & (df['玩家評價分數'] != 0)]

# 按照開發商分級分組，計算 '玩家評價分數' 和 '玩家評價次數' 的平均值
avg_ratings = filtered_df.groupby('開發商分級')[['玩家評價分數', '玩家評價次數']].mean().reset_index()

# 定義顏色列表
colors_1 = ['#FF9999', '#66B2FF', '#99FF99', '#FFCC99']
colors_2 = ['#FF6666', '#3399FF', '#66FF66', '#FF9966']

# 圖表大小
plt.figure(figsize=(12, 6))

# 繪製玩家評價分數
plt.subplot(1, 2, 1)
bars1 = plt.bar(avg_ratings['開發商分級'], avg_ratings['玩家評價分數'], color=colors_1)
plt.title('玩家評價分數平均數', fontproperties=font, fontsize=20)
plt.xticks(rotation=0, fontproperties=font, fontsize=10)
plt.yticks(rotation=0, fontproperties=font, fontsize=10)
plt.xlabel('開發商分級', fontproperties=font, fontsize=15)
plt.ylabel('玩    \n家    \n評    \n價    \n分    \n數    ', rotation=0, fontproperties=font, fontsize=15)

# 在每個柱狀條上顯示數值
for bar in bars1:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, yval, round(yval, 2), va='bottom', ha='center', fontproperties=font, fontsize=10)

# 繪製玩家評價次數
plt.subplot(1, 2, 2)
bars2 = plt.bar(avg_ratings['開發商分級'], avg_ratings['玩家評價次數'], color=colors_2)
plt.title('玩家評價次數平均數', fontproperties=font, fontsize=20)
plt.xticks(rotation=0, fontproperties=font, fontsize=10)
plt.yticks(rotation=0, fontproperties=font, fontsize=10)
plt.xlabel('開發商分級', fontproperties=font, fontsize=15)
plt.ylabel('玩    \n家    \n評    \n價    \n次    \n數    ', rotation=0, fontproperties=font, fontsize=15)

# 在每個柱狀條上顯示數值，並且無條件進位
for bar in bars2:
    yval = bar.get_height()
    yval_ceil = math.ceil(yval)  # 無條件進位
    plt.text(bar.get_x() + bar.get_width() / 2, yval_ceil, yval_ceil, va='bottom', ha='center', fontproperties=font, fontsize=10)

# 調整佈局
plt.tight_layout()

# 顯示圖表
plt.show()

# 使用 Plotly Express 創建圓餅圖
fig1 = px.pie(avg_ratings, values='玩家評價分數', names='開發商分級', title='玩家評價分數平均數')
fig2 = px.pie(avg_ratings, values='玩家評價次數', names='開發商分級', title='玩家評價次數平均數')

# 創建子圖
fig = make_subplots(rows=1, cols=2, specs=[[{'type':'domain'}, {'type':'domain'}]],
                    subplot_titles=['玩家評價分數平均數', '玩家評價次數平均數'])

# 添加第一個圓餅圖到子圖中
fig.add_trace(fig1.data[0], row=1, col=1)

# 添加第二個圓餅圖到子圖中
fig.add_trace(fig2.data[0], row=1, col=2)

# 更新佈局以調整字體大小
fig.update_layout(
    title_text='玩家評價分數&次數',
    font=dict(size=18),  # 調整整體字體大小
    annotations=[dict(font=dict(size=16))]  # 調整子圖標題字體大小
)

# 更新圓餅圖內部字體大小
for data in fig.data:
    data.textfont.size = 14  # 調整標籤字體大小
                  
fig.update_traces(textposition='inside', textinfo='percent+label')

# 顯示圖表
fig.show()

#------------------------------------------------------------------------#

#圖表六 玩家評價分布

# # 篩選出販售數量大於1000的資料
# filtered_df = df[(df['售出數量'] > 1000)& (df['發售年份'] >= 2006) & (df['發售年份'] < 2024) & (df['玩家評價次數'] >= 100) & (df['玩家評價分數'] != 0)]

# # 設置主題和調色板
# sns.set_theme(style="whitegrid", palette="muted")

# # 繪製玩家評價分布圖，根據開發商分級進行顏色區分
# plt.figure(figsize=(12, 6))
# ax = sns.swarmplot(data=filtered_df, x="開發商分級", y="玩家評價分數", palette="deep")

# # 設置圖表標題和標籤
# plt.title('玩家評價分布', fontproperties=font, fontsize=20)
# plt.xticks(rotation=0, fontproperties=font, fontsize=10)
# plt.yticks(rotation=0, fontproperties=font, fontsize=10)
# plt.xlabel('開發商分級', fontproperties=font, fontsize=15)
# plt.ylabel('玩    \n家    \n評    \n價    ', rotation=0, fontproperties=font, fontsize=15)

# # 顯示圖表
# plt.show()

#------------------------------------------------------------------------#

#圖表七 分級&總收入 分級&銷售數量

# 篩選出販售數量大於10000的資料
filtered_df = df[(df['售出數量'] > 1000)& (df['發售年份'] >= 2006) & (df['發售年份'] < 2024) & (df['玩家評價次數'] >= 100) & (df['玩家評價分數'] != 0)]

# 按照開發商分級分組，計算 '銷售總額' 和 '售出數量' 的平均值
avg_ratings = filtered_df.groupby('開發商分級')[['銷售總額', '售出數量']].sum().reset_index()

# 將銷售總額轉換為"多少億"
avg_ratings['銷售總額(億)'] = avg_ratings['銷售總額'] / 1e8

# 將售出數量轉換為"多少萬"
avg_ratings['售出數量(億)'] = avg_ratings['售出數量'] / 1e8

# 定義顏色列表
colors_1 = ['#FF9999', '#66B2FF', '#99FF99', '#FFCC99']
colors_2 = ['#FF6666', '#3399FF', '#66FF66', '#FF9966']

# 圖表大小
plt.figure(figsize=(12, 6))

# 繪製銷售總額(億)
plt.subplot(1, 2, 1)
bars1 = plt.bar(avg_ratings['開發商分級'], avg_ratings['銷售總額(億)'], color=colors_1)
plt.title('分級&總收入', fontproperties=font, fontsize=20)
plt.xticks(rotation=0, fontproperties=font, fontsize=10)
plt.yticks(rotation=0, fontproperties=font, fontsize=10)
plt.xlabel('開發商分級', fontproperties=font, fontsize=15)
plt.ylabel(' 總    \n 收    \n 入    \n(億)    ', rotation=0, fontproperties=font, fontsize=15)

# 在每個柱狀條上顯示數值
for bar in bars1:
    yval = bar.get_height()
    yval_ceil = math.ceil(yval)  # 無條件進位
    plt.text(bar.get_x() + bar.get_width() / 2, yval_ceil, f'{yval_ceil}億', va='bottom', ha='center', fontproperties=font, fontsize=10)

# 繪製售出數量(萬)
plt.subplot(1, 2, 2)
bars2 = plt.bar(avg_ratings['開發商分級'], avg_ratings['售出數量(億)'], color=colors_2)
plt.title('分級&銷售數量', fontproperties=font, fontsize=20)
plt.xticks(rotation=0, fontproperties=font, fontsize=10)
plt.yticks(rotation=0, fontproperties=font, fontsize=10)
plt.xlabel('開發商分級', fontproperties=font, fontsize=15)
plt.ylabel(' 銷    \n 售    \n 數    \n 量    \n(億)    ', rotation=0, fontproperties=font, fontsize=15)

# 在每個柱狀條上顯示數值，並且無條件進位
for bar in bars2:
    yval = bar.get_height()
    yval_ceil = round(yval,2)  # 無條件進位
    plt.text(bar.get_x() + bar.get_width() / 1.8, yval_ceil, f'{yval_ceil}億', va='bottom', ha='center', fontproperties=font, fontsize=10)

# 調整佈局
plt.tight_layout()

# 顯示圖表
plt.show()

# 柔和的顏色序列
soft_colors = px.colors.qualitative.Pastel

# 使用 Plotly Express 創建圓餅圖
fig1 = px.pie(avg_ratings, values='銷售總額(億)', names='開發商分級', title='分級&總收入', color_discrete_sequence=soft_colors)
fig2 = px.pie(avg_ratings, values='售出數量(億)', names='開發商分級', title='分級&銷售數量', color_discrete_sequence=soft_colors)

# 創建子圖
fig = make_subplots(rows=1, cols=2, specs=[[{'type':'domain'}, {'type':'domain'}]],
                    subplot_titles=['分級&總收入', '分級&銷售數量'])

# 添加第一個圓餅圖到子圖中
fig.add_trace(fig1.data[0], row=1, col=1)

# 添加第二個圓餅圖到子圖中
fig.add_trace(fig2.data[0], row=1, col=2)

# 更新佈局以調整字體大小
fig.update_layout(
    title_text='分級:總收入&銷售數量',
    font=dict(size=18),  # 調整整體字體大小
    annotations=[dict(font=dict(size=16))]  # 調整子圖標題字體大小
)

# 更新圓餅圖內部字體大小
for data in fig.data:
    data.textfont.size = 14  # 調整標籤字體大小
                  
fig.update_traces(textposition='inside', textinfo='percent+label')

# 顯示圖表
fig.show()

#------------------------------------------------------------------------#

# 圖表八 遊戲數量&總收入(按年份)(小型開發商製作)(銷售數量大於一千套)

# 創建一個大小為 12x6 吋的圖表和一個子圖
fig, ax = plt.subplots(figsize=(12, 6))

# 篩選出販售數量大於10000的資料
filtered_df = df[(df['售出數量'] > 1000) & (df['開發商分級'] == '小型開發商') & (df['發售年份'] >= 2006) & (df['發售年份'] < 2024) & (df['玩家評價次數'] >= 100) & (df['玩家評價分數'] != 0)]

# 計算每年的銷售總額並按照年份排序
sales_per_year = filtered_df.groupby('發售年份')['銷售總額'].sum().reset_index()
sales_per_year = sales_per_year.sort_values(by='發售年份')

# 將銷售總額轉換為"多少億"
sales_per_year['銷售總額(億)'] = sales_per_year['銷售總額'] / 1e8

# 繪製柱形圖，指定順序為按照年份排序
sns.barplot(x='發售年份', y='銷售總額(億)', data=sales_per_year, palette='hsv', ax=ax)

# 設置圖表標題和標籤
plt.title('遊戲數量&總收入(按年份)(小型開發商製作)(銷售數量大於一千套)', fontproperties=font, fontsize=20)
plt.xticks(rotation=45, fontproperties=font, fontsize=10)
plt.yticks(rotation=0, fontproperties=font, fontsize=10)
plt.xlabel('日期', fontproperties=font, fontsize=15)
plt.ylabel(' 總    \n 收    \n 入    \n(億)    ', rotation=0, fontproperties=font, fontsize=15)

# 在每個柱狀條上顯示金額（億）
for p in ax.patches:
    ax.annotate(f'{p.get_height():.1f} 億',
                (p.get_x() + p.get_width() / 2., p.get_height()),
                ha = 'center', va = 'baseline',
                fontsize = 10, color = 'black', fontproperties=font, xytext = (0, 1),
                textcoords = 'offset points')

# 顯示圖表
plt.show()

#------------------------------------------------------------------------#

# 圖表九 遊戲數量&總收入(按年份)(大型開發商)(銷售數量大於一千套)

# 創建一個大小為 12x6 吋的圖表和一個子圖
fig, ax = plt.subplots(figsize=(12, 6))

# 篩選出販售數量大於10000的資料
filtered_df = df[(df['售出數量'] > 1000) & (df['開發商分級'] == '大型開發商') & (df['發售年份'] >= 2006) & (df['發售年份'] < 2024) & (df['玩家評價次數'] >= 100) & (df['玩家評價分數'] != 0)]

# 計算每年的銷售總額並按照年份排序
sales_per_year = filtered_df.groupby('發售年份')['銷售總額'].sum().reset_index()
sales_per_year = sales_per_year.sort_values(by='發售年份')

# 將銷售總額轉換為"多少億"
sales_per_year['銷售總額(億)'] = sales_per_year['銷售總額'] / 1e8

# 繪製柱形圖，指定順序為按照年份排序
sns.barplot(x='發售年份', y='銷售總額(億)', data=sales_per_year, palette='hsv', ax=ax)

# 設置圖表標題和標籤
plt.title('遊戲數量&總收入(按年份)(大型開發商)(銷售數量大於一千套)', fontproperties=font, fontsize=20)
plt.xticks(rotation=45, fontproperties=font, fontsize=10)
plt.yticks(rotation=0, fontproperties=font, fontsize=10)
plt.xlabel('日期', fontproperties=font, fontsize=15)
plt.ylabel(' 總    \n 收    \n 入    \n(億)    ', rotation=0, fontproperties=font, fontsize=15)

# 在每個柱狀條上顯示金額（億）
for p in ax.patches:
    ax.annotate(f'{p.get_height():.1f} 億',
                (p.get_x() + p.get_width() / 2., p.get_height()),
                ha = 'center', va = 'baseline',
                fontsize = 10, color = 'black', fontproperties=font, xytext = (0, 1),
                textcoords = 'offset points')

# 顯示圖表
plt.show()

#------------------------------------------------------------------------#

# 圖表十 遊戲數量&總收入(按年份)(中型開發商製作)(銷售數量大於一千套)

# 創建一個大小為 12x6 吋的圖表和一個子圖
fig, ax = plt.subplots(figsize=(12, 6))

# 篩選出販售數量大於10000的資料
filtered_df = df[(df['售出數量'] > 1000) & (df['開發商分級'] == '中型開發商') & (df['發售年份'] >= 2006) & (df['發售年份'] < 2024) & (df['玩家評價次數'] >= 100) & (df['玩家評價分數'] != 0)]

# 計算每年的銷售總額並按照年份排序
sales_per_year = filtered_df.groupby('發售年份')['銷售總額'].sum().reset_index()
sales_per_year = sales_per_year.sort_values(by='發售年份')

# 將銷售總額轉換為"多少億"
sales_per_year['銷售總額(億)'] = sales_per_year['銷售總額'] / 1e8

# 繪製柱形圖，指定順序為按照年份排序
sns.barplot(x='發售年份', y='銷售總額(億)', data=sales_per_year, palette='hsv', ax=ax)

# 設置圖表標題和標籤
plt.title('遊戲數量&總收入(按年份)(中型開發商製作)(銷售數量大於一千套)', fontproperties=font, fontsize=20)
plt.xticks(rotation=45, fontproperties=font, fontsize=10)
plt.yticks(rotation=0, fontproperties=font, fontsize=10)
plt.xlabel('日期', fontproperties=font, fontsize=15)
plt.ylabel(' 總    \n 收    \n 入    \n(億)    ', rotation=0, fontproperties=font, fontsize=15)

# 在每個柱狀條上顯示金額（億）
for p in ax.patches:
    ax.annotate(f'{p.get_height():.1f} 億',
                (p.get_x() + p.get_width() / 2., p.get_height()),
                ha = 'center', va = 'baseline',
                fontsize = 10, color = 'black', fontproperties=font, xytext = (0, 1),
                textcoords = 'offset points')

# 顯示圖表
plt.show()

#------------------------------------------------------------------------#

# 圖表十一 遊戲數量&總收入(按年份)(業餘愛好)(銷售數量大於一千套)

# 創建一個大小為 12x6 吋的圖表和一個子圖
fig, ax = plt.subplots(figsize=(12, 6))

# 篩選出販售數量大於10000的資料
filtered_df = df[(df['售出數量'] > 1000) & (df['開發商分級'] == '業餘愛好') & (df['發售年份'] >= 2006) & (df['發售年份'] < 2024) & (df['玩家評價次數'] >= 100) & (df['玩家評價分數'] != 0)]

# 計算每年的銷售總額並按照年份排序
sales_per_year = filtered_df.groupby('發售年份')['銷售總額'].sum().reset_index()
sales_per_year = sales_per_year.sort_values(by='發售年份')

# 將銷售總額轉換為"多少億"
sales_per_year['銷售總額(億)'] = sales_per_year['銷售總額'] / 1e8

# 繪製柱形圖，指定順序為按照年份排序
sns.barplot(x='發售年份', y='銷售總額(億)', data=sales_per_year, palette='hsv', ax=ax)

# 設置圖表標題和標籤
plt.title('遊戲數量&總收入(按年份)(業餘愛好製作)(銷售數量大於一千套)', fontproperties=font, fontsize=20)
plt.xticks(rotation=45, fontproperties=font, fontsize=10)
plt.yticks(rotation=0, fontproperties=font, fontsize=10)
plt.xlabel('日期', fontproperties=font, fontsize=15)
plt.ylabel(' 總    \n 收    \n 入    \n(億)    ', rotation=0, fontproperties=font, fontsize=15)

# 在每個柱狀條上顯示金額（億）
for p in ax.patches:
    ax.annotate(f'{p.get_height():.3f} 億',
                (p.get_x() + p.get_width() / 2., p.get_height()),
                ha = 'center', va = 'baseline',
                fontsize = 10, color = 'black', fontproperties=font, xytext = (0, 1),
                textcoords = 'offset points')

# 顯示圖表
plt.show()

#------------------------------------------------------------------------#

#圖表十二 分級&單價

# 篩選出販售數量大於10000的資料
filtered_df = df[(df['售出數量'] > 1000)& (df['發售年份'] >= 2006) & (df['發售年份'] < 2024) & (df['玩家評價次數'] >= 100) & (df['玩家評價分數'] != 0) & (df['主要模式'] != 'Free Game')]

# 按照開發商分級分組，計算 '銷售總額' 和 '售出數量' 的平均值
avg_ratings = filtered_df.groupby('開發商分級')['遊戲單價'].mean().reset_index()

# 定義顏色列表
colors_1 = ['#FF9999', '#66B2FF', '#99FF99', '#FFCC99']

# 圖表大小
plt.figure(figsize=(6, 6))

# 繪製分級&遊戲單價
bars1 = plt.bar(avg_ratings['開發商分級'], avg_ratings['遊戲單價'], color=colors_1)
plt.title('分級&遊戲單價', fontproperties=font, fontsize=20)
plt.xticks(rotation=0, fontproperties=font, fontsize=10)
plt.yticks(rotation=0, fontproperties=font, fontsize=10)
plt.xlabel('開發商分級', fontproperties=font, fontsize=15)
plt.ylabel('遊    \n戲    \n單    \n價    ', rotation=0, fontproperties=font, fontsize=15)

# 在每個柱狀條上顯示數值
for bar in bars1:
    yval = bar.get_height()
    yval_ceil = math.ceil(yval)  # 無條件進位
    plt.text(bar.get_x() + bar.get_width() / 2, yval_ceil, yval_ceil, va='bottom', ha='center', fontproperties=font, fontsize=10)

# 顯示圖表
plt.show()

#------------------------------------------------------------------------#

# 圖表十三 主流模式&銷售總額(億)(小型開發商製作)(銷售數量大於一千套)

# 定義篩選標籤的條件
tags = ['Battle Royale', 'MOBA', 'FPS', 'Sandbox', 'Open World', 'RPG', 'RTS', 'Strategy']
modes = ['Free Game']

# 初始化每個標籤對應列表
by_tag = []

# 篩選出販售數量大於1000的資料
filtered_df = df[(df['售出數量'] > 1000) & (df['開發商分級'] == '小型開發商') & (df['發售年份'] >= 2006) & (df['發售年份'] < 2024) & (df['玩家評價次數'] >= 100) & (df['玩家評價分數'] != 0)]

# 遍歷每個標籤，計算銷售總額
for tag in tags:
    tag_sales = filtered_df[filtered_df['標籤'].str.contains(tag, case=False, na=False)]['銷售總額'].sum()
    by_tag.append(tag_sales)

# 遍歷每個遊戲模式，計算銷售總額
for mode in modes:
    mode_sales = filtered_df[filtered_df['主要模式'].str.contains(mode, case=False, na=False)]['銷售總額'].sum()
    by_tag.append(mode_sales)

# 處理遊戲名稱包含 "Online" 的情況
online_sales = filtered_df[filtered_df['遊戲名稱'].str.contains('Online', case=False, na=False)]['銷售總額'].sum()
by_tag.append(online_sales)

# 將銷售總額轉換成億
by_tag = [sales / 1e8 for sales in by_tag]

# 準備繪圖數據
x_labels = tags + modes + ['Online game']
y_values = by_tag

# 使用 seaborn 庫繪製長條圖，並設置不同的顏色
plt.figure(figsize=(12, 6))
sns.barplot(x=x_labels, y=y_values, palette='hsv')

# 添加數值標籤
for i, val in enumerate(y_values):
    plt.text(i, val + 0.5, f'{val:.0f}億', ha='center', va='bottom', fontproperties=font, fontsize=10)

# 添加標題和標籤
plt.title('主流模式&銷售總額(億)(小型開發商製作)(銷售數量大於一千套)', fontproperties=font, fontsize=16)
plt.xlabel('主流模式', fontproperties=font, fontsize=14)
plt.ylabel(' 總    \n 收    \n 入    \n(億)    ', rotation=0, fontproperties=font, fontsize=14)
plt.xticks(rotation=45, fontproperties=font, fontsize=10)
plt.yticks(rotation=0, fontproperties=font, fontsize=10)

# 顯示圖表
plt.tight_layout()
plt.show()

#------------------------------------------------------------------------#

# 圖表十四 主流模式&銷售總額(億)(大型開發商製作)(銷售數量大於一千套)

# 定義篩選標籤的條件
tags = ['Battle Royale', 'MOBA', 'FPS', 'Sandbox', 'Open World', 'RPG', 'RTS', 'Strategy']
modes = ['Free Game']

# 初始化每個標籤對應列表
by_tag = []

# 篩選出販售數量大於1000的資料
filtered_df = df[(df['售出數量'] > 1000) & (df['開發商分級'] == '大型開發商') & (df['發售年份'] >= 2006) & (df['發售年份'] < 2024) & (df['玩家評價次數'] >= 100) & (df['玩家評價分數'] != 0)]

# 遍歷每個標籤，計算銷售總額
for tag in tags:
    tag_sales = filtered_df[filtered_df['標籤'].str.contains(tag, case=False, na=False)]['銷售總額'].sum()
    by_tag.append(tag_sales)

# 遍歷每個遊戲模式，計算銷售總額
for mode in modes:
    mode_sales = filtered_df[filtered_df['主要模式'].str.contains(mode, case=False, na=False)]['銷售總額'].sum()
    by_tag.append(mode_sales)

# 處理遊戲名稱包含 "Online" 的情況
online_sales = filtered_df[filtered_df['遊戲名稱'].str.contains('Online', case=False, na=False)]['銷售總額'].sum()
by_tag.append(online_sales)

# 將銷售總額轉換成億
by_tag = [sales / 1e8 for sales in by_tag]

# 準備繪圖數據
x_labels = tags + modes + ['Online game']
y_values = by_tag

# 使用 seaborn 庫繪製長條圖，並設置不同的顏色
plt.figure(figsize=(12, 6))
sns.barplot(x=x_labels, y=y_values, palette='hsv')

# 添加數值標籤
for i, val in enumerate(y_values):
    plt.text(i, val + 0.5, f'{val:.0f}億', ha='center', va='bottom', fontproperties=font, fontsize=10)

# 添加標題和標籤
plt.title('主流模式&銷售總額(億)(大型開發商製作)(銷售數量大於一千套)', fontproperties=font, fontsize=16)
plt.xlabel('主流模式', fontproperties=font, fontsize=14)
plt.ylabel(' 總    \n 收    \n 入    \n(億)    ', rotation=0, fontproperties=font, fontsize=14)
plt.xticks(rotation=45, fontproperties=font, fontsize=10)
plt.yticks(rotation=0, fontproperties=font, fontsize=10)

# 顯示圖表
plt.tight_layout()
plt.show()

#------------------------------------------------------------------------#

# 圖表十五 主流模式&銷售總額(億)(中型開發商製作)(銷售數量大於一千套)

# 定義篩選標籤的條件
tags = ['Battle Royale', 'MOBA', 'FPS', 'Sandbox', 'Open World', 'RPG', 'RTS', 'Strategy']
modes = ['Free Game']

# 初始化每個標籤對應列表
by_tag = []

# 篩選出販售數量大於1000的資料
filtered_df = df[(df['售出數量'] > 1000) & (df['開發商分級'] == '中型開發商') & (df['發售年份'] >= 2006) & (df['發售年份'] < 2024) & (df['玩家評價次數'] >= 100) & (df['玩家評價分數'] != 0)]

# 遍歷每個標籤，計算銷售總額
for tag in tags:
    tag_sales = filtered_df[filtered_df['標籤'].str.contains(tag, case=False, na=False)]['銷售總額'].sum()
    by_tag.append(tag_sales)

# 遍歷每個遊戲模式，計算銷售總額
for mode in modes:
    mode_sales = filtered_df[filtered_df['主要模式'].str.contains(mode, case=False, na=False)]['銷售總額'].sum()
    by_tag.append(mode_sales)

# 處理遊戲名稱包含 "Online" 的情況
online_sales = filtered_df[filtered_df['遊戲名稱'].str.contains('Online', case=False, na=False)]['銷售總額'].sum()
by_tag.append(online_sales)

# 將銷售總額轉換成億
by_tag = [sales / 1e8 for sales in by_tag]

# 準備繪圖數據
x_labels = tags + modes + ['Online game']
y_values = by_tag

# 使用 seaborn 庫繪製長條圖，並設置不同的顏色
plt.figure(figsize=(12, 6))
sns.barplot(x=x_labels, y=y_values, palette='hsv')

# 添加數值標籤
for i, val in enumerate(y_values):
    plt.text(i, val + 0.5, f'{val:.0f}億', ha='center', va='bottom', fontproperties=font, fontsize=10)

# 添加標題和標籤
plt.title('主流模式&銷售總額(億)(中型開發商製作)(銷售數量大於一千套)', fontproperties=font, fontsize=16)
plt.xlabel('主流模式', fontproperties=font, fontsize=14)
plt.ylabel(' 總    \n 收    \n 入    \n(億)    ', rotation=0, fontproperties=font, fontsize=14)
plt.xticks(rotation=45, fontproperties=font, fontsize=10)
plt.yticks(rotation=0, fontproperties=font, fontsize=10)

# 顯示圖表
plt.tight_layout()
plt.show()

#------------------------------------------------------------------------#

# 圖表十六 主流模式&銷售總額(億)(業餘愛好)(銷售數量大於一千套)

# 定義篩選標籤的條件
tags = ['Battle Royale', 'MOBA', 'FPS', 'Sandbox', 'Open World', 'RPG', 'RTS', 'Strategy']
modes = ['Free Game']

# 初始化每個標籤對應列表
by_tag = []

# 篩選出販售數量大於1000的資料
filtered_df = df[(df['售出數量'] > 1000) & (df['開發商分級'] == '業餘愛好') & (df['發售年份'] >= 2006) & (df['發售年份'] < 2024) & (df['玩家評價次數'] >= 100) & (df['玩家評價分數'] != 0)]

# 遍歷每個標籤，計算銷售總額
for tag in tags:
    tag_sales = filtered_df[filtered_df['標籤'].str.contains(tag, case=False, na=False)]['銷售總額'].sum()
    by_tag.append(tag_sales)

# 遍歷每個遊戲模式，計算銷售總額
for mode in modes:
    mode_sales = filtered_df[filtered_df['主要模式'].str.contains(mode, case=False, na=False)]['銷售總額'].sum()
    by_tag.append(mode_sales)

# 處理遊戲名稱包含 "Online" 的情況
online_sales = filtered_df[filtered_df['遊戲名稱'].str.contains('Online', case=False, na=False)]['銷售總額'].sum()
by_tag.append(online_sales)

# 將銷售總額轉換成億
by_tag = [sales / 1e8 for sales in by_tag]

# 準備繪圖數據
x_labels = tags + modes + ['Online game']
y_values = by_tag

# 使用 seaborn 庫繪製長條圖，並設置不同的顏色
plt.figure(figsize=(12, 6))
sns.barplot(x=x_labels, y=y_values, palette='hsv')

# 添加數值標籤
for i, val in enumerate(y_values):
    plt.text(i, val, f'{val:.2f}億', ha='center', va='bottom', fontproperties=font, fontsize=10)

# 添加標題和標籤
plt.title('主流模式&銷售總額(億)(業餘愛好製作)(銷售數量大於一千套)', fontproperties=font, fontsize=16)
plt.xlabel('主流模式', fontproperties=font, fontsize=14)
plt.ylabel(' 總    \n 收    \n 入    \n(億)    ', rotation=0, fontproperties=font, fontsize=14)
plt.xticks(rotation=45, fontproperties=font, fontsize=10)
plt.yticks(rotation=0, fontproperties=font, fontsize=10)

# 顯示圖表
plt.tight_layout()
plt.show()

#------------------------------------------------------------------------#

# 圖表十七 主流模式&玩家平均遊玩時數(小型開發商製作)(銷售數量大於一千套)

# 定義篩選標籤的條件
tags = ['Battle Royale', 'MOBA', 'FPS', 'Sandbox', 'Open World', 'RPG', 'RTS', 'Strategy']
modes = ['Free Game']

# 初始化每個標籤對應列表
by_tag = []

# 篩選出販售數量大於1000的資料
filtered_df = df[(df['售出數量'] > 1000) & (df['開發商分級'] == '小型開發商') & (df['發售年份'] >= 2006) & (df['發售年份'] < 2024) & (df['玩家評價次數'] >= 100) & (df['玩家評價分數'] != 0)]

# 遍歷每個標籤，計算銷售總額
for tag in tags:
    tag_sales = filtered_df[filtered_df['標籤'].str.contains(tag, case=False, na=False)]['玩家平均遊玩時間'].mean()
    by_tag.append(tag_sales)

# 遍歷每個遊戲模式，計算銷售總額
for mode in modes:
    mode_sales = filtered_df[filtered_df['主要模式'].str.contains(mode, case=False, na=False)]['玩家平均遊玩時間'].mean()
    by_tag.append(mode_sales)

# 處理遊戲名稱包含 "Online" 的情況
online_sales = filtered_df[filtered_df['遊戲名稱'].str.contains('Online', case=False, na=False)]['玩家平均遊玩時間'].mean()
by_tag.append(online_sales)

# 準備繪圖數據
x_labels = tags + modes + ['Online game']
y_values = by_tag

# 使用 seaborn 庫繪製長條圖，並設置不同的顏色
plt.figure(figsize=(12, 6))
sns.barplot(x=x_labels, y=y_values, palette='hsv')

# 添加數值標籤
for i, val in enumerate(y_values):
    plt.text(i, val, f'{val:.1f}', ha='center', va='bottom', fontproperties=font, fontsize=10)

# 添加標題和標籤
plt.title('主流模式&玩家平均遊玩時數(小型開發商製作)(銷售數量大於一千套)', fontproperties=font, fontsize=16)
plt.xlabel('主流模式', fontproperties=font, fontsize=14)
plt.ylabel(' 玩    \n 家    \n 平    \n 均    \n 遊    \n 玩    \n 時    \n 數    ', rotation=0, fontproperties=font, fontsize=14)
plt.xticks(rotation=45, fontproperties=font, fontsize=10)
plt.yticks(rotation=0, fontproperties=font, fontsize=10)

# 顯示圖表
plt.tight_layout()
plt.show()

#------------------------------------------------------------------------#

# 圖表十八 主流模式&玩家平均遊玩時數(大型開發商製作)(銷售數量大於一千套)

# 定義篩選標籤的條件
tags = ['Battle Royale', 'MOBA', 'FPS', 'Sandbox', 'Open World', 'RPG', 'RTS', 'Strategy']
modes = ['Free Game']

# 初始化每個標籤對應列表
by_tag = []

# 篩選出販售數量大於1000的資料
filtered_df = df[(df['售出數量'] > 1000) & (df['開發商分級'] == '大型開發商') & (df['發售年份'] >= 2006) & (df['發售年份'] < 2024) & (df['玩家評價次數'] >= 100) & (df['玩家評價分數'] != 0)]

# 遍歷每個標籤，計算銷售總額
for tag in tags:
    tag_sales = filtered_df[filtered_df['標籤'].str.contains(tag, case=False, na=False)]['玩家平均遊玩時間'].mean()
    by_tag.append(tag_sales)

# 遍歷每個遊戲模式，計算銷售總額
for mode in modes:
    mode_sales = filtered_df[filtered_df['主要模式'].str.contains(mode, case=False, na=False)]['玩家平均遊玩時間'].mean()
    by_tag.append(mode_sales)

# 處理遊戲名稱包含 "Online" 的情況
online_sales = filtered_df[filtered_df['遊戲名稱'].str.contains('Online', case=False, na=False)]['玩家平均遊玩時間'].mean()
by_tag.append(online_sales)

# 準備繪圖數據
x_labels = tags + modes + ['Online game']
y_values = by_tag

# 使用 seaborn 庫繪製長條圖，並設置不同的顏色
plt.figure(figsize=(12, 6))
sns.barplot(x=x_labels, y=y_values, palette='hsv')

# 添加數值標籤
for i, val in enumerate(y_values):
    plt.text(i, val, f'{val:.1f}', ha='center', va='bottom', fontproperties=font, fontsize=10)

# 添加標題和標籤
plt.title('主流模式&玩家平均遊玩時數(大型開發商製作)(銷售數量大於一千套)', fontproperties=font, fontsize=16)
plt.xlabel('主流模式', fontproperties=font, fontsize=14)
plt.ylabel(' 玩    \n 家    \n 平    \n 均    \n 遊    \n 玩    \n 時    \n 數    ', rotation=0, fontproperties=font, fontsize=14)
plt.xticks(rotation=45, fontproperties=font, fontsize=10)
plt.yticks(rotation=0, fontproperties=font, fontsize=10)

# 顯示圖表
plt.tight_layout()
plt.show()

#------------------------------------------------------------------------#

# 圖表十九 主流模式&玩家平均遊玩時數(中型開發商製作)(銷售數量大於一千套)

# 定義篩選標籤的條件
tags = ['Battle Royale', 'MOBA', 'FPS', 'Sandbox', 'Open World', 'RPG', 'RTS', 'Strategy']
modes = ['Free Game']

# 初始化每個標籤對應列表
by_tag = []

# 篩選出販售數量大於1000的資料
filtered_df = df[(df['售出數量'] > 1000) & (df['開發商分級'] == '中型開發商') & (df['發售年份'] >= 2006) & (df['發售年份'] < 2024) & (df['玩家評價次數'] >= 100) & (df['玩家評價分數'] != 0)]

# 遍歷每個標籤，計算銷售總額
for tag in tags:
    tag_sales = filtered_df[filtered_df['標籤'].str.contains(tag, case=False, na=False)]['玩家平均遊玩時間'].mean()
    by_tag.append(tag_sales)

# 遍歷每個遊戲模式，計算銷售總額
for mode in modes:
    mode_sales = filtered_df[filtered_df['主要模式'].str.contains(mode, case=False, na=False)]['玩家平均遊玩時間'].mean()
    by_tag.append(mode_sales)

# 處理遊戲名稱包含 "Online" 的情況
online_sales = filtered_df[filtered_df['遊戲名稱'].str.contains('Online', case=False, na=False)]['玩家平均遊玩時間'].mean()
by_tag.append(online_sales)

# 準備繪圖數據
x_labels = tags + modes + ['Online game']
y_values = by_tag

# 使用 seaborn 庫繪製長條圖，並設置不同的顏色
plt.figure(figsize=(12, 6))
sns.barplot(x=x_labels, y=y_values, palette='hsv')

# 添加數值標籤
for i, val in enumerate(y_values):
    plt.text(i, val, f'{val:.1f}', ha='center', va='bottom', fontproperties=font, fontsize=10)

# 添加標題和標籤
plt.title('主流模式&玩家平均遊玩時數(中型開發商製作)(銷售數量大於一千套)', fontproperties=font, fontsize=16)
plt.xlabel('主流模式', fontproperties=font, fontsize=14)
plt.ylabel(' 玩    \n 家    \n 平    \n 均    \n 遊    \n 玩    \n 時    \n 數    ', rotation=0, fontproperties=font, fontsize=14)
plt.xticks(rotation=45, fontproperties=font, fontsize=10)
plt.yticks(rotation=0, fontproperties=font, fontsize=10)

# 顯示圖表
plt.tight_layout()
plt.show()

#------------------------------------------------------------------------#

# 圖表二十 主流模式&玩家平均遊玩時數(業餘愛好)(銷售數量大於一千套)

# 定義篩選標籤的條件
tags = ['Battle Royale', 'MOBA', 'FPS', 'Sandbox', 'Open World', 'RPG', 'RTS', 'Strategy']
modes = ['Free Game']

# 初始化每個標籤對應列表
by_tag = []

# 篩選出販售數量大於1000的資料
filtered_df = df[(df['售出數量'] > 1000) & (df['開發商分級'] == '業餘愛好') & (df['發售年份'] >= 2006) & (df['發售年份'] < 2024) & (df['玩家評價次數'] >= 100) & (df['玩家評價分數'] != 0)]

# 遍歷每個標籤，計算銷售總額
for tag in tags:
    tag_sales = filtered_df[filtered_df['標籤'].str.contains(tag, case=False, na=False)]['玩家平均遊玩時間'].mean()
    by_tag.append(tag_sales)

# 遍歷每個遊戲模式，計算銷售總額
for mode in modes:
    mode_sales = filtered_df[filtered_df['主要模式'].str.contains(mode, case=False, na=False)]['玩家平均遊玩時間'].mean()
    by_tag.append(mode_sales)

# 處理遊戲名稱包含 "Online" 的情況
online_sales = filtered_df[filtered_df['遊戲名稱'].str.contains('Online', case=False, na=False)]['玩家平均遊玩時間'].mean()
by_tag.append(online_sales)

# 準備繪圖數據
x_labels = tags + modes + ['Online game']
y_values = by_tag

# 使用 seaborn 庫繪製長條圖，並設置不同的顏色
plt.figure(figsize=(12, 6))
sns.barplot(x=x_labels, y=y_values, palette='hsv')

# 添加數值標籤
for i, val in enumerate(y_values):
    plt.text(i, val, f'{val:.1f}', ha='center', va='bottom', fontproperties=font, fontsize=10)

# 添加標題和標籤
plt.title('主流模式&玩家平均遊玩時數(業餘愛好製作)(銷售數量大於一千套)', fontproperties=font, fontsize=16)
plt.xlabel('主流模式', fontproperties=font, fontsize=14)
plt.ylabel(' 玩    \n 家    \n 平    \n 均    \n 遊    \n 玩    \n 時    \n 數    ', rotation=0, fontproperties=font, fontsize=14)
plt.xticks(rotation=45, fontproperties=font, fontsize=10)
plt.yticks(rotation=0, fontproperties=font, fontsize=10)

# 顯示圖表
plt.tight_layout()
plt.show()

#------------------------------------------------------------------------#

# 圖表二一 主流模式&玩家平均每日在線人數(小型開發商製作)(銷售數量大於一千套)

# 定義篩選標籤的條件
tags = ['Battle Royale', 'MOBA', 'FPS', 'Sandbox', 'Open World', 'RPG', 'RTS', 'Strategy']
modes = ['Free Game']

# 初始化每個標籤對應列表
by_tag = []

# 篩選出販售數量大於1000的資料
filtered_df = df[(df['售出數量'] > 1000) & (df['開發商分級'] == '小型開發商') & (df['發售年份'] >= 2006) & (df['發售年份'] < 2024) & (df['玩家評價次數'] >= 100) & (df['玩家評價分數'] != 0)]

# 遍歷每個標籤，計算銷售總額
for tag in tags:
    tag_sales = filtered_df[filtered_df['標籤'].str.contains(tag, case=False, na=False)]['玩家平均每日遊玩人數'].mean()
    by_tag.append(tag_sales)

# 遍歷每個遊戲模式，計算銷售總額
for mode in modes:
    mode_sales = filtered_df[filtered_df['主要模式'].str.contains(mode, case=False, na=False)]['玩家平均每日遊玩人數'].mean()
    by_tag.append(mode_sales)

# 處理遊戲名稱包含 "Online" 的情況
online_sales = filtered_df[filtered_df['遊戲名稱'].str.contains('Online', case=False, na=False)]['玩家平均每日遊玩人數'].mean()
by_tag.append(online_sales)

# 準備繪圖數據
x_labels = tags + modes + ['Online game']
y_values = by_tag

# 使用 seaborn 庫繪製長條圖，並設置不同的顏色
plt.figure(figsize=(12, 6))
sns.barplot(x=x_labels, y=y_values, palette='hsv')

# 添加數值標籤
for i, val in enumerate(y_values):
    plt.text(i, val, f'{val:.0f}', ha='center', va='bottom', fontproperties=font, fontsize=10)

# 添加標題和標籤
plt.title('主流模式&玩家平均每日在線人數(小型開發商製作)(銷售數量大於一千套)', fontproperties=font, fontsize=16)
plt.xlabel('主流模式', fontproperties=font, fontsize=14)
plt.ylabel(' 玩    \n 家    \n 平    \n 均    \n 每    \n 日    \n 在    \n 線    \n 人    \n 數    ', rotation=0, fontproperties=font, fontsize=14)
plt.xticks(rotation=45, fontproperties=font, fontsize=10)
plt.yticks(rotation=0, fontproperties=font, fontsize=10)

# 顯示圖表
plt.tight_layout()
plt.show()

#------------------------------------------------------------------------#

# 圖表二二 主流模式&玩家平均每日在線人數(大型開發商製作)(銷售數量大於一千套)

# 定義篩選標籤的條件
tags = ['Battle Royale', 'MOBA', 'FPS', 'Sandbox', 'Open World', 'RPG', 'RTS', 'Strategy']
modes = ['Free Game']

# 初始化每個標籤對應列表
by_tag = []

# 篩選出販售數量大於1000的資料
filtered_df = df[(df['售出數量'] > 1000) & (df['開發商分級'] == '大型開發商') & (df['發售年份'] >= 2006) & (df['發售年份'] < 2024) & (df['玩家評價次數'] >= 100) & (df['玩家評價分數'] != 0)]

# 遍歷每個標籤，計算銷售總額
for tag in tags:
    tag_sales = filtered_df[filtered_df['標籤'].str.contains(tag, case=False, na=False)]['玩家平均每日遊玩人數'].mean()
    by_tag.append(tag_sales)

# 遍歷每個遊戲模式，計算銷售總額
for mode in modes:
    mode_sales = filtered_df[filtered_df['主要模式'].str.contains(mode, case=False, na=False)]['玩家平均每日遊玩人數'].mean()
    by_tag.append(mode_sales)

# 處理遊戲名稱包含 "Online" 的情況
online_sales = filtered_df[filtered_df['遊戲名稱'].str.contains('Online', case=False, na=False)]['玩家平均每日遊玩人數'].mean()
by_tag.append(online_sales)

# 準備繪圖數據
x_labels = tags + modes + ['Online game']
y_values = by_tag

# 使用 seaborn 庫繪製長條圖，並設置不同的顏色
plt.figure(figsize=(12, 6))
sns.barplot(x=x_labels, y=y_values, palette='hsv')

# 添加數值標籤
for i, val in enumerate(y_values):
    plt.text(i, val, f'{val:.0f}', ha='center', va='bottom', fontproperties=font, fontsize=10)

# 添加標題和標籤
plt.title('主流模式&玩家平均每日在線人數(大型開發商製作)(銷售數量大於一千套)', fontproperties=font, fontsize=16)
plt.xlabel('主流模式', fontproperties=font, fontsize=14)
plt.ylabel(' 玩    \n 家    \n 平    \n 均    \n 每    \n 日    \n 在    \n 線    \n 人    \n 數    ', rotation=0, fontproperties=font, fontsize=14)
plt.xticks(rotation=45, fontproperties=font, fontsize=10)
plt.yticks(rotation=0, fontproperties=font, fontsize=10)

# 顯示圖表
plt.tight_layout()
plt.show()

#------------------------------------------------------------------------#

# 圖表二三 主流模式&玩家平均每日在線人數(中型開發商製作)(銷售數量大於一千套)

# 定義篩選標籤的條件
tags = ['Battle Royale', 'MOBA', 'FPS', 'Sandbox', 'Open World', 'RPG', 'RTS', 'Strategy']
modes = ['Free Game']

# 初始化每個標籤對應列表
by_tag = []

# 篩選出販售數量大於1000的資料
filtered_df = df[(df['售出數量'] > 1000) & (df['開發商分級'] == '中型開發商') & (df['發售年份'] >= 2006) & (df['發售年份'] < 2024) & (df['玩家評價次數'] >= 100) & (df['玩家評價分數'] != 0)]

# 遍歷每個標籤，計算銷售總額
for tag in tags:
    tag_sales = filtered_df[filtered_df['標籤'].str.contains(tag, case=False, na=False)]['玩家平均每日遊玩人數'].mean()
    by_tag.append(tag_sales)

# 遍歷每個遊戲模式，計算銷售總額
for mode in modes:
    mode_sales = filtered_df[filtered_df['主要模式'].str.contains(mode, case=False, na=False)]['玩家平均每日遊玩人數'].mean()
    by_tag.append(mode_sales)

# 處理遊戲名稱包含 "Online" 的情況
online_sales = filtered_df[filtered_df['遊戲名稱'].str.contains('Online', case=False, na=False)]['玩家平均每日遊玩人數'].mean()
by_tag.append(online_sales)

# 準備繪圖數據
x_labels = tags + modes + ['Online game']
y_values = by_tag

# 使用 seaborn 庫繪製長條圖，並設置不同的顏色
plt.figure(figsize=(12, 6))
sns.barplot(x=x_labels, y=y_values, palette='hsv')

# 添加數值標籤
for i, val in enumerate(y_values):
    plt.text(i, val, f'{val:.0f}', ha='center', va='bottom', fontproperties=font, fontsize=10)

# 添加標題和標籤
plt.title('主流模式&玩家平均每日在線人數(中型開發商製作)(銷售數量大於一千套)', fontproperties=font, fontsize=16)
plt.xlabel('主流模式', fontproperties=font, fontsize=14)
plt.ylabel(' 玩    \n 家    \n 平    \n 均    \n 每    \n 日    \n 在    \n 線    \n 人    \n 數    ', rotation=0, fontproperties=font, fontsize=14)
plt.xticks(rotation=45, fontproperties=font, fontsize=10)
plt.yticks(rotation=0, fontproperties=font, fontsize=10)

# 顯示圖表
plt.tight_layout()
plt.show()

#------------------------------------------------------------------------#

# 圖表二四 主流模式&玩家平均每日在線人數(業餘愛好)(銷售數量大於一千套)

# 定義篩選標籤的條件
tags = ['Battle Royale', 'MOBA', 'FPS', 'Sandbox', 'Open World', 'RPG', 'RTS', 'Strategy']
modes = ['Free Game']

# 初始化每個標籤對應列表
by_tag = []

# 篩選出販售數量大於1000的資料
filtered_df = df[(df['售出數量'] > 1000) & (df['開發商分級'] == '業餘愛好') & (df['發售年份'] >= 2006) & (df['發售年份'] < 2024) & (df['玩家評價次數'] >= 100) & (df['玩家評價分數'] != 0)]

# 遍歷每個標籤，計算銷售總額
for tag in tags:
    tag_sales = filtered_df[filtered_df['標籤'].str.contains(tag, case=False, na=False)]['玩家平均每日遊玩人數'].mean()
    by_tag.append(tag_sales)

# 遍歷每個遊戲模式，計算銷售總額
for mode in modes:
    mode_sales = filtered_df[filtered_df['主要模式'].str.contains(mode, case=False, na=False)]['玩家平均每日遊玩人數'].mean()
    by_tag.append(mode_sales)

# 處理遊戲名稱包含 "Online" 的情況
online_sales = filtered_df[filtered_df['遊戲名稱'].str.contains('Online', case=False, na=False)]['玩家平均每日遊玩人數'].mean()
by_tag.append(online_sales)

# 準備繪圖數據
x_labels = tags + modes + ['Online game']
y_values = by_tag

# 使用 seaborn 庫繪製長條圖，並設置不同的顏色
plt.figure(figsize=(12, 6))
sns.barplot(x=x_labels, y=y_values, palette='hsv')

# 添加數值標籤
for i, val in enumerate(y_values):
    plt.text(i, val, f'{val:.0f}', ha='center', va='bottom', fontproperties=font, fontsize=10)

# 添加標題和標籤
plt.title('主流模式&玩家平均每日在線人數(業餘愛好製作)(銷售數量大於一千套)', fontproperties=font, fontsize=16)
plt.xlabel('主流模式', fontproperties=font, fontsize=14)
plt.ylabel(' 玩    \n 家    \n 平    \n 均    \n 每    \n 日    \n 在    \n 線    \n 人    \n 數    ', rotation=0, fontproperties=font, fontsize=14)
plt.xticks(rotation=45, fontproperties=font, fontsize=10)
plt.yticks(rotation=0, fontproperties=font, fontsize=10)

# 顯示圖表
plt.tight_layout()
plt.show()
