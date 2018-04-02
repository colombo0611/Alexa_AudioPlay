## Alexa AudioPlayerで音楽を再生する
AlexaのAudioPlayer機能を試してみました。  
Pythonとjsonを使ってます。

## AudioPlayerって？
Alexaちゃんが音楽を再生してくれる機能

## 動作イメージ  
    ①ユーザ　「Alexa、天空のカウントダウンをスタートして」
    ②Alexa  「3分間待ってやる。ぼう」
    ***ここで音楽が再生される***  
    ***止めたい場合は以下***
    ③ユーザ　「Alexa、キャンセル」
 　
## 必要なもの
1.スキル作成(ASK)  
　AudioPlayerの機能をONにすること忘れずに。  
　サンプルコードはintent_schema.txtになります。  
2.再生する音楽  
　mp3をインターネット上にあげる必要があります。  
　AWS使っているのでS3上に置くのが楽チン  
3.AWS Lambdaでコード作成  
　sky_timer.pyをコピぺ  
　コード上の「music_URL(ex.https://example.org/hoge.mp3)」に②で設定されたURLを指定
## その他
　jsonに入っている日本語類は適宜変えていただいても大丈夫です。  
　"outputSpeech":Alexaに喋らせたい声になります。  
　"Card":Alexaアプリ(スマホで見れるやつ)に表示される内容  
  sky_timer2.pyを作成。sky_timer.pyを少し見やすくしたもの。  
