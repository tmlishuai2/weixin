# -*- coding:utf-8 -*-

def answer(text):
    content = "确实，" + text + "。然后呢？"
    return(content)

def reply_Location(location):
    location_x = location.Location_X
    location_y = location.Location_Y
    scale = location.Scale
    label = location.Label
    msgId = location.MsgId
    latitude = '北纬' if location_x[0] != '-' else '南纬'
    longitude = '东经' if location_y[0] != '-' else '西经'
    location_x_abs = location_x if location_x[0] != '-' else location_x[1:]
    location_y_abs = location_y if location_y[0] != '-' else location_y[1:]
    location_text = ('%s %s 度 \n'
                     '%s %s 度 \n'
                     %(
                         latitude, location_x_abs,
                         longitude, location_y_abs
                        )
                     )
    return(location_text)

def reply_subscribe(subscribe):
    welcom_text = "欢迎关注李帅娱乐，现在处于开发期，bug多多，敬请谅解~"
    return(welcom_text)
