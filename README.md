# プロジェクト演習D_E
## python 仮想環境の作り方（Windows）
1. #### python が入っているかコマンドプロンプト等で、**python**と入力。**>>>** が出れば入っています。
2. #### **cd** で作業フォルダを作る場所に移動。
3. #### **python -m venv** 「適当なフォルダ名」と入力。
## PostgreSQLデータベースの作成方法
1. #### https://www.enterprisedb.com/downloads/postgres-postgresql-downloads からそれぞれの環境にあったPostgreSQLをダウンロード。
2. #### ダウンロードしたものを開く
4. #### 設定はすべてデフォルトのままで動作します。ただしスーパーユーザpostgresに設定するパスワードは忘れずに。
5. #### 設定完了後、新しくウィンドウが開いても閉じて構いません。
6. #### システム環境変数の編集より環境変数を開き、システム環境変数のPathを選択し編集をクリック。
7. #### PostgreSQLのあるフォルダを探し新規をクリックしパスを入力する。パスの例：C:\Program Files\PostgreSQL\13\bin
8. #### OKボタンを三回押してシステムのプロパティウィンドウを閉じる。
9. #### コマンドプロンプトで**psql -U postgres** と入力してパスワードを求められたらPostgreSQLは無事入っています。
10. #### 先ほど設定したパスワードでログイン。
11. #### **CREATE ROLE 「新規ユーザ名」 LOGIN PASSWORD '新規ユーザのパスワード';** を入力しユーザを追加。
12. #### 11.で設定したユーザ名とパスワードは後ほど使うので覚えておく。
13. #### **CREATE DATABASE career_passport;** と入力しエラーが出なければデータベースの準備は終了。
## Djangoプロジェクトの準備
1. #### GitHubのコードを右上、緑色のCodeボタンからZipでもいいのでダウンロードし。
2. #### projectD_Eフォルダから中身を取り出し仮想環境フォルダへ貼り付ける。
3. #### エクスプローラーから仮想環境内Career_Passportフォルダ内のCareer_Passportフォルダにある、 **.env** ファイルを探す。
4. #### メモ帳でもいいので **.env** ファイルを開き、中のコードに先ほどデータベースで作成したユーザとパスワードを入れる。
5. #### コマンドプロンプトで仮想環境まで **cd** で移動。
6. #### さらに **cd** で Scripts まで移動。
7. #### **activate.bat** と入力。
8. #### 仮想環境に入れたら、**cd ..** で一つ上の階層へ移動。
9. #### **cd Career_Passport** で一つ下の階層へ移動。
10. #### **python manage.py makemigrations** と入力。
11. #### **python manage.py migrate** と入力。
12. #### **python manage.py createsuperuser** と入力。
13. #### 順番にユーザ名、メールアドレス、パスワード（打っても表示されませんが認識されています）を設定する。
14. #### **python manage.py runserver** と入力してhttpで始まるURLが表示されれば無事準備完了。
## 動作確認
1. #### 14．で出たURLを検索すると成果物の動作確認ができる。
2. #### はじめはログイン画面だが13.で設定したユーザとパスワードでログインできる。
#### ＜捕捉＞ 毎回はじめは上記手順の中から仮想環境へ移動しactivate.bat、ruserverをしなければURLを打っても表示されない。 
#### runserverした状態でも **Ctrl C** を打つとローカルサーバーは止まる。再度ローカルサーバーを起動するにはrunserverする必要がある。
