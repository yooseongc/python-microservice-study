from pika import BlockingConnection, BasicProperties


def on_message(channel, method_frame, header_frame, body):
    race_id = method_frame.routing_key.split(".")[-1]
    print("---새 메시지---")
    print(f"race id: {race_id}")
    print(f"body: {body.decode('utf-8')}")
    
    channel.basic_ack(delivery_tag=method_frame.delivery_tag)


print("race 메시지 수신 대기 중...\n")

connection = BlockingConnection()
channel = connection.channel()
channel.basic_consume("race", on_message)
try :
    channel.start_consuming()
except KeyboardInterrupt:
    channel.stop_consuming()
    
connection.close()
