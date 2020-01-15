from flask_socketio import send
from app import socketio


incoming_message_list = []


class IncomingMessageHelper():

    @socketio.on('message')
    def handleMessage(msg):
        incoming_message_list.append(msg)
        print(incoming_message_list)
        send("hello")
