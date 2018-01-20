from socketIO_client import SocketIO, LoggingNamespace
import webbrowser

socketIO = SocketIO('4c4886d6.ngrok.io', 80, LoggingNamespace)

def on_connect():
    print("Connected.")

def on_thing(data):
    if data["devHand"] == True:
        print("Received message from Google Assistant")

def on_stackoverflow(data):
    if data["devHand"] == True:
        print("Received StackOverflow question:", data["query"])
        webbrowser.open(data["link"])

socketIO.on('connect', on_connect)
socketIO.on("thing", on_thing)
socketIO.on("stackoverflow", on_stackoverflow)
socketIO.wait()
