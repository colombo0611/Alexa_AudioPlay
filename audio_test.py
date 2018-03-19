import os

#再生する音楽のURL
str_url = "mp3File_URL"

def launch_response():
########音楽再生をAlexaに伝える##########
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
########音楽再生をAlexaに伝える##########
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
                            "offsetInMilliseconds": 0
                        }
                    }
                }
            ],
            "shouldEndSession": True
        }
    }
    return response


#####再生中の音楽を止める###################
def cancel_response():

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

########mainの処理###########
def lambda_handler(event, context):

    AudioStart_IntentName = 'TestPlayIntent'

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

    elif event['request']['type'] == 'SessionEndedRequest':
        return session_end_response(event)

    elif event['request']['type'] == 'AudioPlayer.PlaybackStarted' or event['request']['type'] == 'AudioPlayer.PlaybackStopped':
        print('デバック：' + event['request']['type'] + 'を受信しました')
        print(event['request'])
        return null_response()
        
    else:
        print('デバック：' + event['request']['type'] + 'を受信しました')
        print(event['request'])
        print('音楽を停止します。')
        return cancel_response()

