import requests
#取得したデータの種類：患者の性別や年代、職業や都道府県など
#エンドポイント：https://api.data.metro.tokyo.lg.jp/v1/Covid19Patient?limit=100
#機能：新型コロナウイルス陽性患者の性別や年代、職業や都道府県などを取得して表示する
API_URL  = "https://api.data.metro.tokyo.lg.jp/v1/Covid19Patient?limit=100"

params = {
    "metaGetFlg":"Y",
    "cntGetFlg":"N",
    "explanationGetFlg":"Y",
    "annotationGetFlg":"Y",
    "sectionHeaderFlg":"1",
    "replaceSpChars":"0",
    "lang": "J"  # 日本語を指定
}



#response = requests.get(API_URL, params=params)
response = requests.get(API_URL, params=params)
# Process the response
data = response.json()

print(data)