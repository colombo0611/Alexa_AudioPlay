import os

#再生する音楽のURL
str_url = "https://s3-ap-northeast-1.amazonaws.com/for-alexa-kasikoma/n37.mp3"
#str_url = "https://s3-ap-northeast-1.amazonaws.com/for-alexa-kasikoma/kashikoma_hen.mp3"

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
    print('デバック：' + f"{event['request']['type']}" + 'を受信しました')
    print(f"{event['request']}")

########main routine###########
def lambda_handler(event, context):

    if event['request']['type'] == 'LaunchRequest':
        print('デバック：' + f"{event['request']['type']}" + 'を受信しました')
        print('音楽を再生します。')
        print(f"{event['request']}")
        return launch_response()

    elif event['request']['type'] == 'IntentRequest' and event['request']['intent']['name'] == 'TestPlayIntent':
        print('デバック：' + f"{event['request']['type']}" + 'を受信しました')
        print(f"{event['request']}")
        return intent_response()

    elif event['request']['type'] == 'SessionEndedRequest':
        return session_end_response(event)

    elif event['request']['type'] == 'AudioPlayer.PlaybackStarted' or event['request']['type'] == 'AudioPlayer.PlaybackStopped':
        print('デバック：' + f"{event['request']['type']}" + 'を受信しました')
        print(f"{event['request']}")
        return null_response()
        
    else:
        print('デバック：' + f"{event['request']['type']}" + 'を受信しました')
        print(f"{event['request']}")
        print('音楽を停止します。')
        return cancel_response()

