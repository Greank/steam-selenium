import pandas as pd
import math

def quanrtity(value):
    if 'k' in str(value) :
        value = value.replace('k','')
        value = float(value) * 1000
        return int(value)
    elif 'm' in str(value) :
        value = value.replace('m','')
        value = float(value) * 1000000
        return int(value)
    else:
        return int(value)

def price(value):
    if '$' in value:
        value=value.replace('$','')
        value= float(value) * 32
        if value >= 100:
            return int(round(value,-2))
        else :
            return int(round(value,0))
    return int(value)

def sum_price(value):
    if '$' in value:
        value=value.replace('$','')
        if 'b' in value:
            value = value.replace('b','')
            value = float(value)*1000000000
            value = value * 32
            return int(value)
        elif 'm' in value:
            value = value.replace('m','')
            value = float(value)*1000000
            value = value * 32
            return int(value)
        elif 'k' in value:
            value = value.replace('k','')
            value = float(value)*1000
            value = value * 32
            return int(value)
        value= float(value) * 32
    return int(value)

def time(value):
    value = value.replace('h','')
    value = math.ceil(float(value))
    return int(value)

def game_user(value):
    value = value.replace('%','')
    return int(value)

def game_translate(value):
    if isinstance(value, str):
        value = value.replace('Action','動作') \
        .replace('Adventure','動作冒險') \
        .replace('Animation & Modeling','角色建模') \
        .replace('Audio Production','音訊製作') \
        .replace('Casual','休閒') \
        .replace('Design & Illustration','圖畫設計') \
        .replace('Education','教育') \
        .replace('Game Development','遊戲開發') \
        .replace('Indie','獨立製作') \
        .replace('Massively Multiplayer','大型多人線上遊戲') \
        .replace('Photo Editing','圖片修改') \
        .replace('RPG','角色扮演') \
        .replace('Racing','賽車') \
        .replace('Simulation','模擬') \
        .replace('Software Training','訓練軟體') \
        .replace('Sports','運動') \
        .replace('Strategy','策略') \
        .replace('Unknown Genre','未知類型') \
        .replace('Utilities','工具') \
        .replace('Video Production','影片製作') \
        .replace('Early Access','搶先體驗') \
        .replace('Free to Play','免費遊戲')
    return value 

def language_translate(value):
    if isinstance(value, str):
        value = value.replace('English','英語') \
        .replace('Czech','捷克語') \
        .replace('Danish' , '丹麥語') \
        .replace('Dutch' , '荷蘭語') \
        .replace('Finnish' , '芬蘭語') \
        .replace('French' , '法語') \
        .replace('German' , '德語') \
        .replace('Hungarian' , '匈牙利語') \
        .replace('Italian' , '義大利文') \
        .replace('Japanese' , '日語') \
        .replace('Korean' , '韓語') \
        .replace('Norwegian' , '挪威語') \
        .replace('Polish' , '波蘭文') \
        .replace('Portuguese - Portugal' , '葡萄牙文 - 葡萄牙') \
        .replace('Portuguese - Brazil' , '葡萄牙文 - 巴西') \
        .replace('Romanian' , '羅馬尼亞語') \
        .replace('Russian' , '俄語') \
        .replace('Simplified Chinese' , '簡體中文') \
        .replace('Spanish - Spain' , '西班牙文 - 西班牙') \
        .replace('Swedish' , '瑞典語') \
        .replace('Thai' , '泰語') \
        .replace('Traditional Chinese' , '繁體中文') \
        .replace('Turkish' , '土耳其文') \
        .replace('Bulgarian' , '保加利亞文') \
        .replace('Ukrainian' , '烏克蘭語') \
        .replace('Greek' , '希臘語') \
        .replace('Spanish - Latin America' , '西班牙文 - 拉丁美洲') \
        .replace('Vietnamese' , '越南文') \
        .replace('Indonesian' , '印度尼西亞語') \
        .replace('More','') \
        .replace('Arabic' , '阿拉伯文')
    return value

def developer_translate(value):
    if isinstance(value, str):
        value = value.replace('Indie','小型開發商') \
        .replace('Hobbyist','業餘愛好') \
        .replace('AAA','大型開發商') \
        .replace('AA','中型開發商')
    return value
    

def country_tanslate(value):
    if isinstance(value, str):
        value = value.replace('CN','中國') \
        .replace('US','美國') \
        .replace('RU','俄羅斯') \
        .replace('UA','烏克蘭') \
        .replace('DE','德國') \
        .replace('BR','巴西') \
        .replace('TR','土耳其') \
        .replace('GB','英國') \
        .replace('AR','阿根廷') \
        .replace('~','') \
        .replace(' ','') \
        .replace('JP','日本') \
        .replace('PL','波瀾') \
        .replace('CA','加拿大') \
        .replace('AU','奧地利') \
        .replace('PT','葡萄牙') \
        .replace('KR','南韓') \
        .replace('HK','香港') \
        .replace('TH','泰國') \
        .replace('TW','台灣') \
        .replace('FR','法國') \
        .replace('CZ','捷克') \
        .replace('NL','荷蘭') \
        .replace('ID','印度尼西亞') \
        .replace('FI','芬蘭') \
        .replace('IT','義大利') \
        .replace('CH','瑞士') \
        .replace('IN','印度') \
        .replace('NO','挪威') \
        .replace('BE','比利時') \
        .replace('SE','瑞典') \
        .replace('PH','菲律賓') \
        .replace('DK','丹麥') \
        .replace('CL','智利') \
        .replace('SK','斯洛伐克') \
        .replace('PE','祕魯') \
        .replace('RO','羅馬尼亞') \
        .replace('IQ','伊拉克') \
        .replace('MX','墨西哥') \
        .replace('HU','匈牙利') \
        .replace('AT','奧地利') \
        .replace('KZ','哈薩克') \
        .replace('VN','越南') \
        .replace('IE','愛爾蘭') \
        .replace('NE','尼日') \
        .replace('BY','白俄羅斯')
    return value

def game_tpye(value):
    if value['遊戲單價'] == 0:
        return '免費遊戲'
    else:
        value_list = str(value['模式']).split(', ')
        if len(value_list) > 1:
            if value_list[1] == '獨立製作':
                return value_list[0]
            return value_list[1]
        else:
            return value_list[0]


def process_countries(row):
    countries_list = str(row['玩家國家佔比']).split(',')
    countries_dict = {}
    
    for info in countries_list:
        parts_list = info.split(':')
        # print(parts_list)
        if len(parts_list) == 2:
            country = parts_list[0].strip()
            percentage = parts_list[1].strip()
            countries_dict[country] = percentage
        elif len(parts_list) == 1:
            countries_dict['其他國家'] = parts_list[0].strip()
        print(countries_dict)
        
    for country, percentage in countries_dict.items():
        df.at[row.name, country] = percentage
    
    return row


# 讀取CSV文件
df = pd.read_csv('game_data_補齊資料.csv',encoding='utf-16',delimiter='\t')

# print(df.head(10))
# print(df.info())

df['售出數量'] = df['售出數量'].apply(quanrtity)
df['遊戲單價'] = df['遊戲單價'].apply(price)
df['銷售總額'] = df['銷售總額'].apply(sum_price)
df['玩家平均遊玩時間'] = df['玩家平均遊玩時間'].apply(time)
df['玩家評價分數'] = df['玩家評價分數'].apply(game_user)
df['開發商分級'] = df['開發商分級'].apply(developer_translate)
df['模式'] = df['模式'].apply(game_translate)
df['語言'] = df['語言'].apply(language_translate)
df['玩家評價次數'] = df['玩家評價次數'].fillna(0).apply(quanrtity)
df['玩家平均每日遊玩人數'] = df['玩家平均每日遊玩人數'].fillna(0).apply(quanrtity)
df['關注人數'] = df['關注人數'].fillna(0).apply(quanrtity)
df['玩家國家佔比'] = df['玩家國家佔比'].apply(country_tanslate)
df['主要模式'] = df.apply(game_tpye,axis=1)
df.apply(process_countries,axis=1)
# print(df.head(10))
# print(df.info())

df.to_csv('path_to_your_output_file.csv', sep='\t', encoding='utf-16', index=False)