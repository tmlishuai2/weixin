# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET

def parse_xml(web_data):
    if len(web_data) == 0:
        return(None)
    xmlData = ET.fromstring(web_data)
    msg_type = xmlData.find('MsgType').text
    if msg_type == 'text':
        return(TextMsg(xmlData))
    if msg_type == 'image':
        return(ImageMsg(xmlData))
    if msg_type == 'voice':
        return(VoiceMsg(xmlData))
    if msg_type == 'video' or msg_type == 'shortvideo':
        return(VideoMsg(xmlData))
#    elif msg_type == 'shortvideo':
#        return ShortVideoMsg(xmlData)
    if msg_type == 'location':
        return(LocationMsg(xmlData))
    if msg_type == 'link':
        return(LinkMsg(xmlData))
    if msg_type == 'event':
        if xmlData.find('Ticket') is not None:
            return(QRCodeEvent(xmlData))
        elif xmlData.find('EventKey') is not None:
            return(MenuEvent(xmlData))
        elif xmlData.find('Event').text == 'LOCATION':
            return(LocationEvent(xmlData))
        else:
            return(Event(xmlData))



#普通消息类
class Msg:
    def __init__(self, xmlData):
        self.ToUserName = xmlData.find('ToUserName').text
        self.FromUserName = xmlData.find('FromUserName').text
        self.CreateTime = xmlData.find('CreateTime').text
        self.MsgType = xmlData.find('MsgType').text
        self.MsgId = xmlData.find('MsgId').text

class TextMsg(Msg):
    def __init__(self, xmlData):
        Msg.__init__(self, xmlData)
        self.Content = xmlData.find('Content').text

class MediaMsg(Msg):
    def __init__(self, xmlData):
        Msg.__init__(self, xmlData)
        self.MediaId = xmlData.find('MediaId').text

class ImageMsg(Msg):
    def __init__(self, xmlData):
        Msg.__init__(self, xmlData)
        self.PicUrl = xmlData.find('PicUrl').text
        self.MediaId = xmlData.find('MediaId').text

class VoiceMsg(MediaMsg):
    def __init__(self, xmlData):
        MediaMsg.__init__(self, xmlData)
        self.Recognition = xmlData.find('Recognition').text
        self.Format = xmlData.find('Format').text

class VideoMsg(MediaMsg):
    def __init__(self, xmlData):
        MediaMsg.__init__(self, xmlData)
        self.ThumbMediaId = xmlData.find('ThumbMediaId').text

class LocationMsg(Msg):
    def __init__(self, xmlData):
        Msg.__init__(self, xmlData)
        self.Location_X = xmlData.find('Location_X').text
        self.Location_Y = xmlData.find('Location_Y').text
        self.Scale = xmlData.find('Scale').text
        self.Label = xmlData.find('Label').text

class LinkMsg(Msg):
    def __init__(self, xmlData):
        Msg.__init__(self, xmlData)
        self.Title = xmlData.find('Title').text
        self.Description = xmlData.find('Description').text
        self.Url = xmlData.find('Url').text

#事件类
class Event:
    def __init__(self, xmlData):
        self.ToUserName = xmlData.find('ToUserName').text
        self.FromUserName = xmlData.find('FromUserName').text
        self.CreateTime = xmlData.find('CreateTime').text
        self.MsgType = xmlData.find('MsgType').text
        self.Event = xmlData.find('Event').text

class QRCodeEvent(Event):
    def __init__(self, xmlData):
        Event.__init__(self, xmlData)
        self.EventKey = xmlData.find('EventKey').text
        self.Ticket = xmlData.find('Ticket').text

class LocationEvent(Event):
    def __init__(self, xmlData):
        Event.__init__(self, xmlData)
        self.Latitude = xmlData.find('Latitude').text
        self.Longitude = xmlData.find('Longitude').text
        self.Precision = xmlData.find('Precision').text

class MenuEvent(Event):
    def __init__(self, xmlData):
        Event.__init__(self, xmlData)
        self.EventKey = xmlData.find('EventKey').text





