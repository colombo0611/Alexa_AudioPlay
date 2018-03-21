## Alexa AudioPlayerで音楽を再生する
AlexaのAudioPlayer機能を試してみました。  
Pythonとjsonを使ってます。

## AudioPlayerって？
Alexaちゃんが音楽を再生してくれる機能

## 動作イメージ  
    ①ユーザ　「Alexa、音楽を再生して」
    ②Alexa  「ピチピチボイスでライブスタート」
    ***ここで音楽が再生される***  
    ***止めたい場合は以下***
    ③ユーザ　「Alexa、ストップ」
 ※①について・・・設定した発話によってはAlexaがうまく動作しない場合がありそう。  
 　(Alexaで元から使える別のスキルの発話とバッティングしてると想定)　
 　
## 必要なもの
1.スキル作成(ASK)  
　AudioPlayerの機能をONにすること忘れずに。  
　サンプルコードはintent_schema.txtになります。  
2.再生する音楽  
　mp3をインターネット上にあげる必要があります。  
　AWS使っているのでS3上に置くのが楽チン  
3.AWS Lambdaでコード作成  
　audio_test.pyをコピぺ  
　コード上の「mp3File_URL」に②で設定されたURLを指定
## その他
　jsonに入っている日本語類は適宜変えていただいても大丈夫です  
　"outputSpeech":Alexaに喋らせたい声になります。  
　"Card":Alexaアプリ(スマホで見れるやつ)に表示される内容

