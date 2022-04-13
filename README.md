説明文↓
「ホットペッパー」が提供しているAPIを利用した、職場の近くで食事が取れる飲食店をリストアップするアプリ
以下のURLリクエストを送信することで所定のデータを受け取ることができます。

import 
json(jsonファイル取得）
csv(csvファイルに出力)
requests(URLにリクエスト）
os(keyid:APIキーを環境変数へ変換）
argparse()

9行目：argparseの基本形を設定,パーサーの作成,description：プログラムの説明

初期設定,コマンドライン引数を設定する
KEYID = os.environ['keyid']
 #環境変数を利用して代入

parser.add_argument('--count', type=int, default=100)
#コマンド引数にデフォルト設定に１００を指定、また数字のみ入れるため(intに設定）

parser.add_argument('--pref', default='Z011')
#コマンド引数にデフォルト設定にZ011を指定

parser.add_argument('--freeword', required=True)
#コマンド引数を入れないとエラーになるrequired=Trueを入れる

parser.add_argument('--format', default='json')
#コマンド引数にデフォルト設定にjsonを指定

コマンドライン引数の解析
args = parser.parse_args()

PARAMSの中身を代入

COUNT = args.count
PREF = args.pref
FREEWORD = args.freeword
FORMAT = args.format

PARAMS = {"key": KEYID, "count":COUNT, "large_area":PREF, "keyword":FREEWORD, "format":FORMAT}


csvファイルに出力の準備、 restaurantsの空のリスト作成、APIをリクエスト
def write_data_to_csv(params):
    restaurants = []
    response = requests.get("http://webservice.recruit.co.jp/hotpepper/gourmet/v1/", params=params)
   
#リクエストの成功を表すコード200ではない場合、エラー文
if response.status_code != 200: 
        return("エラーが発生しました")

responseを再代入
json形式でまた中身はテキスト（文字）であること
response = json.loads(response.text)


restaurantsのリストに代入する、レストラン名に代入、追加

if "error" in response["results"]:
        return print("エラーが発生しました！")
    for restaurant in response["results"]["shop"]:
        restaurant_name = restaurant["name"]
        restaurants.append(restaurant_name)

csvファイルを出力

 with open("restaurants_list.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerow(restaurants)
    return print(restaurants)   



write_data_to_csv(PARAMS)

実行コマンド

環境変数の設定
①$env:keyid = "自分のAPIキー"

②$env:keyid
自分のAPIキーが入っていること確認にする

アプリの実行コマンド
python3 restaurants_searcher.py --freeword "渋谷駅"
