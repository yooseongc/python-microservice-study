import pika
import requests
from requests.exceptions import ReadTimeout, ConnectionError

FLASK_ENDPOINT = "http://localhost:5000/event"


def on_message(channel, method_frame, header_frame, body):
    message = {"delivery_tag": method_frame.delivery_tag,
               "message": body.decode("utf-8")}
    try:
        res = requests.post(FLASK_ENDPOINT, json=message, timeout=1.)
    except (ReadTimeout, ConnectionError):
        print(f"Failed to connect to {FLASK_ENDPOINT}.")
        # TODO: implement re-connection?
        return
    
    if res.status_code == 200:
        print("플라스크로 메시지 전달 성공!")
        channel.basic_ack(delivery_tag=method_frame.delivery_tag)
    

connection = pika.BlockingConnection()
channel = connection.channel()
channel.basic_consume("race", on_message)

try:
    channel.start_consuming()
except KeyboardInterrupt:
    channel.stop_consuming()
    
connection.close()
