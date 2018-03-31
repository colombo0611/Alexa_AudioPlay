import os

#再生する音楽のURL
#魔王魂
str_url = "music_URL(ex.https://example.org/hoge.mp3)"

#####ヘルプを起動する###################
def help_response():
    response = {
        "version": "1.0",
        "sessionAttributes": {},
        "response": {
            "outputSpeech": {
                "type": "PlainText",
                "text": "天空のカウントダウンをご利用いただきありがとうございます。"
            },
            "reprompt": {
                "outputSpeech": {
                    "type": "PlainText",
                    "text": "天空のカウントダウンをスタートして。と話しかけてください。"
                }
            },
            "card": {
                "title": "天空のカウントダウン",
                "content": "天空のカウントダウンほヘルプを起動しました",
                "type": "Simple"
            },
            'shouldEndSession': False
        }
    }
    return response
    

def launch_response():
########音楽再生を開始する##########
    response = {
        "version": "1.0",
        "sessionAttributes": {},
        "response": {
            "outputSpeech": {
                "type": "PlainText",
                "text": "3分間待ってやる。。ぼう。。。"
            },
            "card": {
                "title": "天空のカウントダウン",
                "content": "天空のカウントダウンを開始します。(出典；魔王魂3曲)",
                "type": "Simple"
            },
            "directives": [
                {
                    "type": "AudioPlayer.Play",
                    "playBehavior": "REPLACE_ALL",
                    "audioItem": {
                        "stream": {
                            "token": "12345",
                            "url": str_url,
                            "offsetInMilliseconds": 0
                        }
                    }
                }
            ],
            "shouldEndSession": True
        }
    }
    return response


def intent_response():
########音楽再生を開始する##########
    response = {
        "version": "1.0",
        "sessionAttributes": {},
        "response": {
            "outputSpeech": {
                "type": "PlainText",
                "text": "3分間待ってやる。。ぼう。。。"
            },
            "card": {
                "title": "天空のカウントダウン",
                "content": "天空のカウントダウンを開始します。(出典；魔王魂3曲)",
                "type": "Simple"
            },
            "directives": [
                {
                    "type": "AudioPlayer.Play",
                    "playBehavior": "REPLACE_ALL",
                    "audioItem": {
                        "stream": {
                            "token": "12345",
                            "url": str_url,
                            "offsetInMilliseconds": 0
                        }
                    }
                }
            ],
            "shouldEndSession": True
        }
    }
    return response

#####音楽再生正常終了時の応答###################
def finished_response():

    response = {
        "version": "1.0",
        "sessionAttributes": {},
        "response": {
            "directives": [
                {
                    "type": "AudioPlayer.Stop"
                }
            ],
            'shouldEndSession': True
        }
    }
    return response

#####再生中の音楽を停止(ユーザ途中一時停止)###################
def pause_response():

    response = {
        "version": "1.0",
        "sessionAttributes": {},
        "response": {
            "outputSpeech": {
                "type": "PlainText",
                "text": "天空のカウントダウンを停止しました。"
            },
            "card": {
                "title": "天空のカウントダウン",
                "content": "天空のカウントダウンを停止しました。",
                "type": "Simple"
            },
            "directives": [
                {
                    "type": "AudioPlayer.Stop"
                }
            ],
            'shouldEndSession': True
        }
    }
    return response


def restart_response(offset):
########音楽再生を再開する##########
    response = {
        "version": "1.0",
        "sessionAttributes": {},
        "response": {
            "outputSpeech": {
                "type": "PlainText",
                "text": "天空のカウントダウンを再開します"
            },
            "card": {
                "title": "天空のカウントダウン",
                "content": "天空のカウントダウンを再開します。(出典；魔王魂3曲)",
                "type": "Simple"
            },
            "directives": [
                {
                    "type": "AudioPlayer.Play",
                    "playBehavior": "REPLACE_ALL",
                    "audioItem": {
                        "stream": {
                            "token": "12345",
                            "url": str_url,
                            "offsetInMilliseconds": offset
                        }
                    }
                }
            ],
            "shouldEndSession": True
        }
    }
    return response


#####再生中の音楽を終了(ユーザ途中キャンセル)###################
def cancel_response():

    response = {
        "version": "1.0",
        "sessionAttributes": {},
        "response": {
            "outputSpeech": {
                "type": "PlainText",
                "text": "天空のカウントダウンを終了しました"
            },
            "card": {
                "title": "天空のカウントダウン",
                "content": "天空のカウントダウンを終了しました。",
                "type": "Simple"
            },
            "directives": [
                {
                    "type": "AudioPlayer.Stop"
                }
            ],
            'shouldEndSession': True
        }
    }
    return response

########対応する必要のないリクエストは音楽再生を再開する##########
def cannot_request_response(offset):

    response = {
        "version": "1.0",
        "sessionAttributes": {},
        "response": {
            "outputSpeech": {
                "type": "PlainText",
                "text": "すみません。天空のカウントダウンは対応していません。"
            },
            "card": {
                "title": "天空のカウントダウン",
                "content": "天空のカウントダウンを再開します。(出典；魔王魂3曲)",
                "type": "Simple"
            },
            "directives": [
                {
                    "type": "AudioPlayer.Play",
                    "playBehavior": "REPLACE_ALL",
                    "audioItem": {
                        "stream": {
                            "token": "12345",
                            "url": str_url,
                            "offsetInMilliseconds": offset
                        }
                    }
                }
            ],
            "shouldEndSession": True
        }
    }
    return response


########エラー回避用のレスポンス#########
def null_response():
    response = {
        "version": "1.0",
        "sessionAttributes": {},
        "response": {
            "shouldEndSession": True
        }
    }
    return response


########何もしない#############
def session_end_response(event):
    print('デバック：' + event['request']['type'] + 'を受信しました')
    print(event['request'])


#####リモンコンによる再生中の音楽を停止(ユーザ途中一時停止)###################
def pause_response():

    response = {
        "version": "1.0",
        "sessionAttributes": {},
        "response": {
            "directives": [
                {
                    "type": "AudioPlayer.Stop"
                }
            ],
            'shouldEndSession': True
        }
    }
    return response


def rerestart_response(offset):
########リモコンで音楽再生を再開する##########
    response = {
        "version": "1.0",
        "sessionAttributes": {},
        "response": {
            "directives": [
                {
                    "type": "AudioPlayer.Play",
                    "playBehavior": "REPLACE_ALL",
                    "audioItem": {
                        "stream": {
                            "token": "12345",
                            "url": str_url,
                            "offsetInMilliseconds": offset
                        }
                    }
                }
            ],
            "shouldEndSession": True
        }
    }
    return response


########mainの処理###########
def lambda_handler(event, context):
    AudioStart_IntentName = 'TimerStartIntent'

    if event['request']['type'] == 'LaunchRequest':
        print('デバック：' + event['request']['type'] + 'を受信しました')
        print('音楽を再生します。')
        print(event['request'])
        return launch_response()

    elif event['request']['type'] == 'IntentRequest' and event['request']['intent']['name'] == AudioStart_IntentName:
        print('デバック：' + event['request']['type'] + 'を受信しました')
        print('音楽を再生します。')
        print(event['request'])
        return intent_response()

    elif event['request']['type'] == 'IntentRequest' and event['request']['intent']['name'] == 'AMAZON.HelpIntent':
        print('デバック：' + event['request']['type'] + 'を受信しました')
        print('ヘルプを起動しました。')
        print(event['request'])
        return help_response()
        
    elif event['request']['type'] == 'IntentRequest' and event['request']['intent']['name'] == 'AMAZON.PauseIntent':
        print('デバック：' + event['request']['type'] + 'を受信しました')
        print('一時停止します。')
        print(event['request'])
        print(event['context'])
        return pause_response()

    elif event['request']['type'] == 'IntentRequest' and event['request']['intent']['name'] == 'AMAZON.ResumeIntent':
        print('デバック：' + event['request']['type'] + 'を受信しました')
        print('再開します')
        print(event['request'])
        print(event['context'])
        offset = event['context']['AudioPlayer']['offsetInMilliseconds']
        return restart_response(offset)

    elif event['request']['type'] == 'IntentRequest' and event['request']['intent']['name'] == 'AMAZON.CancelIntent':
        print('デバック：' + event['request']['type'] + 'を受信しました')
        print(event['request'])
        print('音楽を終了します')
        return cancel_response()

        
    elif event['request']['type'] == 'SessionEndedRequest':
        print('ユーザからの応答がありませんでした')
        return session_end_response(event)
    
    ###リモンによる操作    
    elif event['request']['type'] == 'PlaybackController.PauseCommandIssued':
        return remote_pause_response()

    elif event['request']['type'] == 'IntentRequest' and event['request']['intent']['name'] == 'PlayCommandIssued':
        offset = event['context']['AudioPlayer']['offsetInMilliseconds']
        return remote_pause_response(offset)
        
        

    ###以下はユーザからの発話処理とは無関係なAudioPlayリクエストの処理####

    elif event['request']['type'] == 'AudioPlayer.PlaybackStarted':
        print('デバック：' + event['request']['type'] + 'を受信しました')
        print(event['request'])
        return null_response()

    elif event['request']['type'] == 'AudioPlayer.PlaybackStopped':
        print('デバック：' + event['request']['type'] + 'を受信しました')
        print(event['request'])
        return null_response()

    elif event['request']['type'] == 'AudioPlayer.PlaybackNearlyFinished':
        print('デバック：' + event['request']['type'] + 'を受信しました')
        print(event['request'])
        return null_response()

    elif event['request']['type'] == 'AudioPlayer.PlaybackFinished':
        print('デバック：' + event['request']['type'] + 'を受信しました')
        print(event['request'])
        return finished_response()
        
    else:
        print('デバック：' + event['request']['type'] + 'を受信しました')
        print(event['request'])
        print('対応する必要のないリクエスト')
        offset = event['context']['AudioPlayer']['offsetInMilliseconds']
        return cannot_request_response(offset)



