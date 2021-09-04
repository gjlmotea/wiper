from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, ImageSendMessage
)

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('')
# Channel Secret
handler = WebhookHandler('')

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

def searchKey(msg):
    word = {'作者':'GJLMoTea',}
    
    return word.get(msg,"收到: "+msg)


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    
    msg = event.message.text #接收訊息
    if '疫情' in msg or '確診'  in msg or '肺炎' in msg:
        location, people = getCovid()
        info = ''
        for i in range(len(location)):
            info += location[i]+': '+str(people[i])+'人 確診\n'
        msg = info
    elif '水庫' in msg:
        location, percentage, volumn = getReser()
        info = ''
        for i in range(len(location)):
            info += location[i]+' 水位: '+str(percentage[i])[0:4]+'%    總容量: ' + str(volumn[i]) + '\n'
        msg = info
    elif 'ptt' in msg.lower():
        msg = getPtt()
    else:
        msg = searchKey(msg)
    
    message = TextSendMessage(text=msg)
    line_bot_api.reply_message(
        event.reply_token,
        message)

import os
from covid2019 import getCovid
from reservoir import getReser
from ptt import getPtt
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
    
