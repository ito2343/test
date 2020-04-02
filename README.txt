
##Overview
  コマンドプロンプトで郵便番号を入力したら、一致する住所をPostgreSQLのテーブルから抽出し、出力させるPythonスクリプト


##Requirement
  Python 3.8
  PostgreSQL 12.2


##Setup
・PostgreSQL
　→「Postgres設定手順.xlsx」参照

・Python
  →https://www.python.org/downloads/windows/
　　上記URLからパッケージをダウンロードし、ローカルPCへインストール


##Usage
  1.コマンドプロンプトを起動、Pythonファイルが置いてあるパスを指定し、Python起動

    python C:\Users\Desktop\postgresSQL_connect.py

  2.郵便番号の入力を求められるので、ハイフン抜きで入力する
  
  3.入力した郵便番号で問題ないか y or n で聞かれるので y と入力してEnterキーを押す
　
　4.入力した郵便番号がデータベースに存在する場合、それに一致した住所が表示される

　　例：郵便番号：2130023
　　　　町域：SHIBOKUCHI                                                                                           市区町村：TAKATSU-KU KAWASAKI-SHI                                                                          都道府県:KANAGAWA

  5.入力した郵便番号の桁数などが足りなかった場合でも部分的に一致した郵便番号が羅列される
　　
　　例：候補の郵便番号をデータベースから抽出しました。
       [[231761], [231132], [231101]]

##Authors
  伊藤　心ノ助


##References
  https://qiita.com/I4MK3/items/0d053d1e793a2986821f
  https://qiita.com/arupaka__ri/items/5d4711c279d111622117
  https://tokkan.net/python/db.html
  https://itsakura.com/pgadmin4-db-create#s6
  http://a23.sblo.jp/article/184229623.html
  https://dev.to/programmingmonky/postgresqlsql-3dja
  https://tokkan.net/python/db.html
  https://vent-et-neige.hatenadiary.org/entry/20111108/1333957402 
  https://note.nkmk.me/python-digit-int-float/