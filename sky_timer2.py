import os

#再生する音楽のURL
#魔王魂
str_url = "str_url = "music_URL(ex.https://example.org/hoge.mp3)""

AudioStart_IntentName = 'TimerStartIntent'

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
def remote_pause_response():

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


def remote_start_response(offset):
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

########LaunchRequestの処理######
def send_launch_response(event, context):
    print('音楽を再生します。')
    return launch_response()

#######IntentRequestの処理#######
def send_intent_response(event, context):
    if event['request']['intent']['name'] == AudioStart_IntentName:
        print('音楽を再生します。')
        return intent_response()

    elif event['request']['intent']['name'] == 'AMAZON.HelpIntent':
        print('ヘルプを起動しました。')
        return help_response()
        
    elif event['request']['intent']['name'] == 'AMAZON.PauseIntent':
        print('一時停止します。')
        return pause_response()

    elif event['request']['intent']['name'] == 'AMAZON.ResumeIntent':
        print('再開します')
        offset = event['context']['AudioPlayer']['offsetInMilliseconds']
        return restart_response(offset)

    elif event['request']['intent']['name'] == 'AMAZON.CancelIntent':
        print('音楽を終了します')
        return cancel_response()
    else:
        print('対応する必要のないリクエスト')
        offset = event['context']['AudioPlayer']['offsetInMilliseconds']
        return cannot_request_response(offset)

#######SessionEndRequestの処理#######
def send_end_response(event, context):
    print('ユーザからの応答がありませんでした')
    return session_end_response(event)

#######AudioPlayの処理#######
def send_audio_response(event, context):
    ###リモンによる操作    
    if event['request']['type'] == 'PlaybackController.PauseCommandIssued':
        return remote_pause_response()
    elif event['request']['type'] == 'PlaybackController.PlayCommandIssued':
        offset = event['context']['AudioPlayer']['offsetInMilliseconds']
        return remote_start_response(offset)

    ###以下はユーザからの発話処理とは無関係なAudioPlayリクエストの処理####
    elif event['request']['type'] == 'AudioPlayer.PlaybackStarted':
        return null_response()
    elif event['request']['type'] == 'AudioPlayer.PlaybackStopped':
        return null_response()
    elif event['request']['type'] == 'AudioPlayer.PlaybackNearlyFinished':
        return null_response()
    elif event['request']['type'] == 'AudioPlayer.PlaybackFinished':
        return finished_response()

########mainの処理###########
def lambda_handler(event, context):
    if event['request']['type'] == 'LaunchRequest':
        return send_launch_response(event, context)
    elif event['request']['type'] == 'IntentRequest':
        return send_intent_response(event, context)
    elif event['request']['type'] == 'SessionEndedRequest':
        return send_end_response(event, context)
    else:
        return send_audio_response(event, context)
