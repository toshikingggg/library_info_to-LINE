# 図書館の新刊情報がほしい！！！
## 概要
新しい本が出るとすぐに借りられてしまうので、一番に借りられるように新着一日以内の本の情報をLINEに通知する

## 目的
- Selenium,ChromedriverでWEBプロセスの自動化を学ぶ
- Herokeの使い方を学びつつ,かんたんなアプリを実装する練習

## 前提
### まずローカルで動かす
1. 図書館の蔵書情報からSeleniumで「日本語」かつ「2020年1月1日以降の新刊」かつ 「新着一日以内」の図書＋雑誌のタイトル/カテゴリをクローリング
2. Beautiful Soupでスクレイピング 
3. LINE Notifyをrequestsで叩いてLINEに通知

### Herokeの環境構築
herokuのアプリ管理はgitと同じ感じでやるらしい \
↓herokuインストール後(ログイン忘れずに)
```
heroku apps:create {{アプリ名}}
heroku buildpacks:add heroku/python -a {{アプリ名}}
heroku buildpacks:add https://github.com/heroku/heroku-buildpack-google-chrome -a {{アプリ名}}
heroku buildpacks:add https://github.com/heroku/heroku-buildpack-chromedriver -a {{アプリ名}}
```
ChromeとDriverの設定
Add buildpackからchromedriverとchromeを加える
| Buildpack     | URL                                                          |
| ------------- | ------------------------------------------------------------ |
| chromedrive   | https://github.com/heroku/heroku-buildpack-chromedriver.git  |
| google-chrome | https://github.com/heroku/heroku-buildpack-google-chrome.git |

herokuのプロジェクトをgitで管理する \
Herokuにデプロイする↓
```
heroku git:remote -a {{アプリ名}}
git push heroku main
```
- 定期実行する(無料)
スケジューラにコマンドを指定してアプリの起動を任せられる(10分,1時間,1日)
```
heroku addons:add scheduler:standard
```
https://dashboard.heroku.com/apps/{{アプリ名}}/scheduler からcreate job


## できた！
<img width="300" src="https://user-images.githubusercontent.com/69241625/109983859-94a5ab00-7d46-11eb-85ee-14472eb41ab8.jpg">
