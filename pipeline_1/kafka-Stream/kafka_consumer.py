from kafka import KafkaConsumer

# To consume latest messages and auto-commit offsets
consumer = KafkaConsumer('packet_test_pcap', bootstrap_servers=['localhost:9092'])
for msg in consumer:

    print ("%s:%d:%d: key=%s value=%s" % (msg.topic, msg.partition, msg.offset, msg.key, msg.value))

KafkaConsumer(auto_offset_reset='earliest', enable_auto_commit=False)

# consume json messages
KafkaConsumer(value_deserializer=lambda m: json.loads(m.decode('ascii')))

# consume msgpack
KafkaConsumer(value_deserializer=msgpack.unpackb)

# StopIteration if no message after 5sec
KafkaConsumer(consumer_timeout_ms=5000)

# Subscribe to a regex topic pattern
new_consumer = KafkaConsumer()



