import psycopg2
import sys
import base64
from psycopg2.extras import DictCursor
import json

put ='''\n郵便番号とデータベースがマッチしました。
----------------------------------------
郵便番号：{}
町域：{}
市区町村：{}
都道府県:{}
----------------------------------------\n'''

fil ='''候補の郵便番号をデータベースから抽出しました。\n{}\n'''

print('\n郵便番号から住所を検索します。')
while True:
    flag = 0
    postal_code = input('郵便番号を入力してください。　*ハイフン不要 -> ')
    while True:
        ask = input('{}でよろしいですか？ y or n -> '.format(postal_code))
        if ask == 'y':
            flag = 1
            break
        elif ask == 'n':
            break
    if flag == 1:
        break

args = sys.argv

f = open(args[1], 'r')
json_dict = json.load(f)
pa = json_dict['pass']
json_str = json.dumps(pa)

a = json_str.strip('""')
d = base64.b64decode(a)
s = d.decode("UTF-8")

users = 'postgres'
dbnames = 'test'
passwords = s

conn = psycopg2.connect(" user=" + users +" dbname=" + dbnames +" password=" + passwords)

le = len(postal_code)

if le <= 6:
   with conn.cursor(cursor_factory=DictCursor) as cur:
       cur.execute('SELECT "Postal Code" FROM public.test WHERE "Postal Code"::text LIKE %s;', (postal_code + "%",))
       raw = cur.fetchall()
       count = len(raw)
       if count == 0:
          print("入力した郵便番号は存在しません")
          sys.exit()
       print(fil.format(raw)) 
else:
   with conn.cursor(cursor_factory=DictCursor) as cur:
        cur.execute('SELECT * FROM public.test WHERE "Postal Code"={}'.format(postal_code))
        row = cur.fetchone()
        if None == row:
          print("入力した郵便番号は存在しません")
          sys.exit()
        print(put.format(row[0],row[1],row[2],row[3]))
