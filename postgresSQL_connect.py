import psycopg2
import sys
import base64
from psycopg2.extras import DictCursor

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

s = "arena!wrep19"
b = s.encode("UTF-8")
e = base64.b64encode(b)
s1 = e.decode("UTF-8")
b1 = s1.encode("UTF-8")
d = base64.b64decode(b1)
s2 = d.decode("UTF-8")

users = 'postgres'
dbnames = 'test'
passwords = s2

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