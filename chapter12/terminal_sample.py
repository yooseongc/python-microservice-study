

def terminal():
    while True:
        msg = yield
        if msg == "exit":
            print("Bye!")
            break
        elif msg.startswith("echo"):
            print(msg.split("echo ", 1)[1])
        elif msg.startswith("eval"):
            print(eval(msg.split("eval", 1)[1]))
