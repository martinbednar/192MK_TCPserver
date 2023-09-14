#!/usr/bin/python3

from tcpcom import TCPServer

IP_PORT = 3005

def onStateChanged(state, msg):
    if state == "LISTENING":
        print("Server:-- Listening...")
    elif state == "CONNECTED":
        print("Server:-- Connected to", msg)
    elif state == "MESSAGE" and msg != "":
        print("Server:-- Message received:", msg)

server = TCPServer(IP_PORT, stateChanged = onStateChanged)
