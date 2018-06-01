from kafka import KafkaConsumer
import time


def log(str):
    t = time.strftime(r"%Y-%m-%d_%H-%M-%S", time.localtime())
    print("[%s]%s" % (t, str))


log('start consumer')
consumer = KafkaConsumer('world', group_id='consumer-20171017', bootstrap_servers=['localhost:9092'])
for msg in consumer:
    recv = "%s:%d:%d: key=%s value=%s" % (msg.topic, msg.partition, msg.offset, msg.key, msg.value)
    log(recv)