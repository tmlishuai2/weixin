# -*- coding: utf-8 -*-
# 导入所有的模块
from flask import Flask, request
import hashlib
import variables
import receive
import reply
import AI

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def weixin_auth():
    if request.method == 'GET':
        print("coming GET")
        signature = request.args['signature']
        timestamp = request.args['timestamp']
        nonce = request.args['nonce']
        token = variables.wxToken
        echostr = request.args['echostr']
        print(echostr + '  ' + signature + '  ' +  timestamp)

        list_args = [token, timestamp, nonce]
        list_args.sort()
        sha1 = hashlib.sha1()
        map(sha1.update, list_args)
        hashcode = sha1.hexdigest()
        print("handle GET: hashcode, signature: ", hashcode, signature)
        if hashcode == signature:
            return(echostr)
        else:
            return("")

    if request.method == 'POST':
        webData  = request.stream.read().decode()
        print("Handle Post webdata is", webData)
        rec = receive.parse_xml(webData)
        if rec is None:
            print("不是事件或消息")
            return("success")
        else:
            toUser = rec.FromUserName
            fromUser = rec.ToUserName
            createTime = rec.CreateTime
            msgType = rec.MsgType
            if isinstance(rec, receive.Msg):
                if rec.MsgType == 'text':
                    rec_content = rec.Content
                    content = AI.answer(rec_content)
                    replyMsg = reply.TextMsg(toUser, fromUser, content)
                    print("\n start replying")
                    return("success")
                   # return(replyMsg.send())
                if rec.MsgType == 'voice':
                    rec_content = rec.Recognition
                    content = AI.answer(rec_content)

                    replyMsg = reply.TextMsg(toUser, fromUser, content)
                   #return(replyMsg.send())
                    return("success")
                if rec.MsgType == 'location':
                    content = AI.reply_Location(rec)
                    replyMsg = reply.TextMsg(toUser, fromUser, content)
                    return(replyMsg.send())
            else:
                if rec.Event == 'subscribe':
                    content = AI.reply_Subscribe(rec)

                    replyMsg = reply.TextMsg(toUser, fromUser, content)
                    return(replyMsg.send())

                return("success")












def get():
    return 'you are beautiful'


if __name__ == '__main__':
    app.run(host = '0.0.0.0', debug = True, port = 80)

