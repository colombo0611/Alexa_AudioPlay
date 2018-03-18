from __future__ import print_function


# --------------- Helpers that build all of the responses ----------------------

def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': "SessionSpeechlet - " + title,
            'content': "SessionSpeechlet - " + output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }


def build_response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }


# --------------- Functions that control the skill's behavior ------------------

def get_welcome_response():

    #次のセッションで使う場合に値を保持できる
    session_attributes = {}

    #Alexaアプリ側に出すログのタイトル
    card_title = "オーディトプレイのテスト"

    #Alexaがしゃべる言葉とカードに残す言葉
    speech_output = "これはオーディオプレイのテストです"
    
    #ユーザがAlexaに反応しない場合、もしくは言葉を理解してくれない場合
    reprompt_text = "すみません。よく聞き取れませんでした。もう一度お願いします。 " 

    #対話を終了するかどうか。Trueなら終わり。Falseなら続ける
    should_end_session = False

    #JSONのレスポンスを返す。
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def handle_session_end_request():
    card_title = "Session Ended"
    speech_output = "Thank you for trying the Alexa Skills Kit sample. " \
                    "Have a nice day! "
    # Setting this to true ends the session and exits the skill.
    should_end_session = True
    return build_response({}, build_speechlet_response(
        card_title, speech_output, None, should_end_session))


def create_favorite_color_attributes(favorite_color):
    return {"favoriteColor": favorite_color}


def set_xxxslotxxx_in_session(intent, session):
    """スロットのある場合のレスポンスの準備"""

    card_title = intent['name']
    session_attributes = {}

    #対話を終了するかどうか。Trueなら終わり。Falseなら続ける
    should_end_session = False

    if 'SlotNname' in intent['slots']:
        SlotValue = intent['slots']['SlotName']['value']
        session_attributes = create_favorite_color_attributes(favorite_color)
        speech_output = "Alexaに喋らせたい言葉"
        reprompt_text = "Alexaに返答しなかった場合、もしくはAlexaが言葉を理解\
                        しなかった場合のAlexaからの返答"
    else:
        speech_output = "Alexaに喋らせたい言葉"
        reprompt_text = "Alexaに返答しなかった場合、もしくはAlexaが言葉を理解\
                        しなかった場合のAlexaからの返答"

    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def get_xxxslotxxx_from_session(intent, session):
    session_attributes = {}
    reprompt_text = None

    if session.get('attributes', {}) and "favoriteColor" in session.get('attributes', {}):
        favorite_color = session['attributes']['favoriteColor']
        speech_output = "Your favorite color is " + favorite_color + \
                        ". Goodbye."
        should_end_session = True
    else:
        speech_output = "I'm not sure what your favorite color is. " \
                        "You can say, my favorite color is red."
        should_end_session = False

    # Setting reprompt_text to None signifies that we do not want to reprompt
    # the user. If the user does not respond or says something that is not
    # understood, the session will end.
    return build_response(session_attributes, build_speechlet_response(
        intent['name'], speech_output, reprompt_text, should_end_session))


# --------------- Events ------------------

def on_session_started(session_started_request, session):
    """ Called when the session starts """

    #requestIDとsessionIDをawsのログに出力する。
    print("on_session_started requestId=" + session_started_request['requestId']
          + ", sessionId=" + session['sessionId'])


def on_launch(launch_request, session):

    print("on_launch requestId=" + launch_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # Dispatch to your skill's launch
    return get_welcome_response()


def on_intent(intent_request, session):
    """設定した発話通りならここの処理を行う """

    #AWSにログを出力する
    print("on_intent requestId=" + intent_request['requestId'] +
          ", sessionId=" + session['sessionId'])

    #intentにはintent名やスロットが入っているので取得しておくと良い
    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']

    # Intentに対する処理を行う
    # 対話モデルで{"intent": "TestIntent"}を設定していたら。。。
    # if intent_name == "TestIntent"
    # 関数名は自分で決める

    if intent_name == "InputYourMakeIntent":
        return set_xxxslostxxx_in_session(intent, session)
    elif intent_name == "InputYourMkaeIntent2":
        return get_xxxslotxxx_from_session(intent, session)
    elif intent_name == "AMAZON.HelpIntent":
        return get_welcome_response()
    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        return handle_session_end_request()
    else:
        raise ValueError("Invalid intent")


def on_session_ended(session_ended_request, session):
    """ Called when the user ends the session.

    Is not called when the skill returns should_end_session=true
    """
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # add cleanup logic here


# --------------- Main handler ------------------

def lambda_handler(event, context):
    #アプリケーションIDをAWSのログに出力する
    print("event.session.application.applicationId=" +
          event['session']['application']['applicationId'])

    #session.newが真なら、関数に連想配列(requestID)とsessionIDの値を渡す。
    #sessin開始のログ出力
    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']},
                           event['session'])

    #XXXXを開いて(テスト用の発話？)なら、Launchに対するJSONレスポンスを返す
    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])

    #XXXX(設定したインテント用の発話？)なら
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])

    #一定時間ユーザから応答がないなら
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])

