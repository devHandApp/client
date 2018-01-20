from socketIO_client import SocketIO, LoggingNamespace

socketIO = SocketIO('4c4886d6.ngrok.io', 80, LoggingNamespace)

def on_connect():
    print("Connected.")

def on_thing(*args):
    if args[0]["devHand"] == True:
        print("Received message from Google Assistant")

def on_stackoverflow(*args):
    if args[0]["devHand"] == True:
        print("Received StackOverflow question:", args[0]["query"])

socketIO.on('connect', on_connect)
socketIO.on("thing", on_thing)
socketIO.on("stackoverflow", on_stackoverflow)
socketIO.wait()
