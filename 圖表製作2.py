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

#圖一

# 篩選出販售數量大於1000的資料
filtered_df = df[(df['售出數量'] > 1000) & 
                 (df['發售年份'] >= 2006) & 
                 (df['發售年份'] < 2024) & 
                 (df['玩家評價次數'] >= 100) & 
                 (df['玩家評價分數'] != 0)]

# 計算每年每個開發商分級的遊戲數量並按照年份排序
games_count_per_year = filtered_df.groupby(['發售年份', '開發商分級']).size().reset_index(name='遊戲數量')

# 繪製圖表
plt.figure(figsize=(12, 6))

# 使用 seaborn 的 lineplot 繪製每個開發商分級的曲線
ax = sns.lineplot(data=games_count_per_year, x="發售年份", y="遊戲數量", hue="開發商分級",marker='o')

# 設置X軸的刻度
plt.xticks(range(games_count_per_year['發售年份'].min(), games_count_per_year['發售年份'].max() + 1))

# 設置字型
plt.xlabel('發售年份', fontproperties=font, fontsize=15)
plt.ylabel('遊    \n戲    \n數    \n量    ',rotation=0, fontproperties=font, fontsize=15)
plt.title('每年發售的遊戲數量（按開發商分級）', fontproperties=font, fontsize=20)

# 获取当前图例的句柄和标签
handles, labels = ax.get_legend_handles_labels()

# 定义图例条目的顺序
order = ['大型開發商', '中型開發商', '小型開發商', '業餘愛好']

# 根据定义的顺序重新排序句柄和标签
ordered_handles = [handles[labels.index(category)] for category in order]
ordered_labels = [labels[labels.index(category)] for category in order]

# 显示图例并设置图例标题字型
plt.legend(ordered_handles, ordered_labels, title='開發商分級', loc='upper left', title_fontproperties=font, prop=font)

plt.show()

#------------------------------------------------------------------------#

#圖表二 分級&單價

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

#圖表三 

# 篩選出販售數量大於1000的資料
filtered_df = df[(df['售出數量'] > 1000) & 
                 (df['發售年份'] >= 2006) & 
                 (df['發售年份'] < 2024) & 
                 (df['玩家評價次數'] >= 100) & 
                 (df['玩家評價分數'] != 0)]

# 計算每年每個開發商分級的銷售總額並按照年份排序
sales_per_year = filtered_df.groupby(['發售年份', '開發商分級'])['銷售總額'].sum().reset_index()
sales_per_year = sales_per_year.sort_values(by='發售年份')

# 將銷售總額轉換為"多少億"
sales_per_year['銷售總額(億)'] = sales_per_year['銷售總額'] / 1e8

# 創建一個大小為 12x6 吋的圖表
plt.figure(figsize=(12, 6))

# 使用 seaborn 的 lineplot 繪製每個開發商分級的銷售總額變化
ax = sns.lineplot(data=sales_per_year, x='發售年份', y='銷售總額(億)', hue='開發商分級',marker='o')

# 設置X軸的刻度
plt.xticks(range(games_count_per_year['發售年份'].min(), games_count_per_year['發售年份'].max() + 1))

# 設置圖表標題和標籤
plt.title('遊戲數量&總收入(按年份)(銷售數量大於一千套)', fontproperties=font, fontsize=20)
plt.xlabel('發售年份', fontproperties=font, fontsize=15)
plt.ylabel(' 總    \n 收    \n 入    \n(億)    ', rotation=0, fontproperties=font, fontsize=15)

# 获取当前图例的句柄和标签
handles, labels = ax.get_legend_handles_labels()

# 定义图例条目的顺序
order = ['大型開發商', '中型開發商', '小型開發商', '業餘愛好']

# 根据定义的顺序重新排序句柄和标签
ordered_handles = [handles[labels.index(category)] for category in order]
ordered_labels = [labels[labels.index(category)] for category in order]

# 显示图例并设置图例标题字型
plt.legend(ordered_handles, ordered_labels, title='開發商分級', loc='upper left', title_fontproperties=font, prop=font)

# 顯示圖表
plt.show()

#------------------------------------------------------------------------#

#圖表四

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
plt.title('主流模式&銷售總額(億)(小型開發商製作)(銷售數量大於一千套)', fontproperties=font, fontsize=20)
plt.xlabel('主流模式', fontproperties=font, fontsize=15)
plt.ylabel(' 總    \n 收    \n 入    \n(億)    ', rotation=0, fontproperties=font, fontsize=15)
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
plt.title('主流模式&銷售總額(億)(大型開發商製作)(銷售數量大於一千套)', fontproperties=font, fontsize=20)
plt.xlabel('主流模式', fontproperties=font, fontsize=15)
plt.ylabel(' 總    \n 收    \n 入    \n(億)    ', rotation=0, fontproperties=font, fontsize=15)
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
plt.title('主流模式&銷售總額(億)(中型開發商製作)(銷售數量大於一千套)', fontproperties=font, fontsize=20)
plt.xlabel('主流模式', fontproperties=font, fontsize=15)
plt.ylabel(' 總    \n 收    \n 入    \n(億)    ', rotation=0, fontproperties=font, fontsize=15)
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
plt.title('主流模式&銷售總額(億)(業餘愛好製作)(銷售數量大於一千套)', fontproperties=font, fontsize=20)
plt.xlabel('主流模式', fontproperties=font, fontsize=15)
plt.ylabel(' 總    \n 收    \n 入    \n(億)    ', rotation=0, fontproperties=font, fontsize=15)
plt.xticks(rotation=45, fontproperties=font, fontsize=10)
plt.yticks(rotation=0, fontproperties=font, fontsize=10)

# 顯示圖表
plt.tight_layout()
plt.show()

#------------------------------------------------------------------------#

#圖表五

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
plt.title('主流模式&玩家平均遊玩時數(小型開發商製作)(銷售數量大於一千套)', fontproperties=font, fontsize=20)
plt.xlabel('主流模式', fontproperties=font, fontsize=15)
plt.ylabel(' 玩    \n 家    \n 平    \n 均    \n 遊    \n 玩    \n 時    \n 數    ', rotation=0, fontproperties=font, fontsize=15)
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
plt.title('主流模式&玩家平均遊玩時數(大型開發商製作)(銷售數量大於一千套)', fontproperties=font, fontsize=20)
plt.xlabel('主流模式', fontproperties=font, fontsize=15)
plt.ylabel(' 玩    \n 家    \n 平    \n 均    \n 遊    \n 玩    \n 時    \n 數    ', rotation=0, fontproperties=font, fontsize=15)
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
plt.title('主流模式&玩家平均遊玩時數(中型開發商製作)(銷售數量大於一千套)', fontproperties=font, fontsize=20)
plt.xlabel('主流模式', fontproperties=font, fontsize=15)
plt.ylabel(' 玩    \n 家    \n 平    \n 均    \n 遊    \n 玩    \n 時    \n 數    ', rotation=0, fontproperties=font, fontsize=15)
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
plt.title('主流模式&玩家平均遊玩時數(業餘愛好製作)(銷售數量大於一千套)', fontproperties=font, fontsize=20)
plt.xlabel('主流模式', fontproperties=font, fontsize=15)
plt.ylabel(' 玩    \n 家    \n 平    \n 均    \n 遊    \n 玩    \n 時    \n 數    ', rotation=0, fontproperties=font, fontsize=15)
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
plt.title('主流模式&玩家平均每日在線人數(小型開發商製作)(銷售數量大於一千套)', fontproperties=font, fontsize=20)
plt.xlabel('主流模式', fontproperties=font, fontsize=15)
plt.ylabel(' 玩    \n 家    \n 平    \n 均    \n 每    \n 日    \n 在    \n 線    \n 人    \n 數    ', rotation=0, fontproperties=font, fontsize=15)
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
plt.title('主流模式&玩家平均每日在線人數(大型開發商製作)(銷售數量大於一千套)', fontproperties=font, fontsize=20)
plt.xlabel('主流模式', fontproperties=font, fontsize=15)
plt.ylabel(' 玩    \n 家    \n 平    \n 均    \n 每    \n 日    \n 在    \n 線    \n 人    \n 數    ', rotation=0, fontproperties=font, fontsize=15)
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
plt.title('主流模式&玩家平均每日在線人數(中型開發商製作)(銷售數量大於一千套)', fontproperties=font, fontsize=20)
plt.xlabel('主流模式', fontproperties=font, fontsize=15)
plt.ylabel(' 玩    \n 家    \n 平    \n 均    \n 每    \n 日    \n 在    \n 線    \n 人    \n 數    ', rotation=0, fontproperties=font, fontsize=15)
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
plt.title('主流模式&玩家平均每日在線人數(業餘愛好製作)(銷售數量大於一千套)', fontproperties=font, fontsize=20)
plt.xlabel('主流模式', fontproperties=font, fontsize=15)
plt.ylabel(' 玩    \n 家    \n 平    \n 均    \n 每    \n 日    \n 在    \n 線    \n 人    \n 數    ', rotation=0, fontproperties=font, fontsize=15)
plt.xticks(rotation=45, fontproperties=font, fontsize=10)
plt.yticks(rotation=0, fontproperties=font, fontsize=10)

# 顯示圖表
plt.tight_layout()
plt.show()

#------------------------------------------------------------------------#

# 圖表六 玩家評價分布

# 篩選出販售數量大於1000的資料
filtered_df = df[(df['售出數量'] > 1000)& (df['發售年份'] >= 2006) & (df['發售年份'] < 2024) & (df['玩家評價次數'] >= 100) & (df['玩家評價分數'] != 0)]

# # 設置主題和調色板
# sns.set_theme(style="whitegrid", palette="muted")

# 繪製玩家評價分布圖，根據開發商分級進行顏色區分
plt.figure(figsize=(12, 6))
ax = sns.swarmplot(data=filtered_df, x="開發商分級", y="玩家評價分數", palette="deep")

# 設置圖表標題和標籤
plt.title('玩家評價分布', fontproperties=font, fontsize=20)
plt.xticks(rotation=0, fontproperties=font, fontsize=10)
plt.yticks(rotation=0, fontproperties=font, fontsize=10)
plt.xlabel('開發商分級', fontproperties=font, fontsize=15)
plt.ylabel('玩    \n家    \n評    \n價    ', rotation=0, fontproperties=font, fontsize=15)

# 顯示圖表
plt.show()

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