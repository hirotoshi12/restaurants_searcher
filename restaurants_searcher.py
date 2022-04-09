import json
import csv
import requests
import os 
import sys 
import argparse #インポート

#argparseモジュールの基本
parser = argparse.ArgumentParser(description= '宿題')

# 初期設定

KEYID = os.environ['keyid']
parser.add_argument('--count', type=int, default=100)
parser.add_argument('--pref', default='Z011')
parser.add_argument('--freeword', required=True)
parser.add_argument('--format', default='json')

args = parser.parse_args()

#代入
COUNT = args.count
PREF = args.pref
FREEWORD = args.freeword
FORMAT = args.format

PARAMS = {"key": KEYID, "count":COUNT, "large_area":PREF, "keyword":FREEWORD, "format":FORMAT}


def write_data_to_csv(params):
    restaurants = []
    response = requests.get("http://webservice.recruit.co.jp/hotpepper/gourmet/v1/", params=params)
   
    #リクエストの成功を表すコード200ではない場合、エラー文
    if response.status_code != 200: 
        return("エラーが発生しました")
    response = json.loads(response.text)
   
    if "error" in response["results"]:
        return print("エラーが発生しました！")
    for restaurant in response["results"]["shop"]:
        restaurant_name = restaurant["name"]
        restaurants.append(restaurant_name)
    with open("restaurants_list.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerow(restaurants)
    return print(restaurants)

write_data_to_csv(PARAMS)