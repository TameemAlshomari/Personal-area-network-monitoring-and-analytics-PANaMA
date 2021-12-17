from kafka import KafkaProducer
import MyScapyExtract as myscap
from time import sleep
from struct import *

#Creating Producer
producer = KafkaProducer(bootstrap_servers=['kafka:9092'], value_serializer=lambda x: x.encode('utf-8'))
TOPIC_NAME = 'packet_test_pcap'

#uploading network captured file
netcap = 'test.pcap'
packets = myscap.scapy_read_packets(netcap)


dataframe = myscap.parse_scapy_packets(packets)
#print(dataframe[0:2])
#print(len(dataframe))

c = 1

for i in range(len(dataframe)):
    pkt = dataframe[i]

	if (pkt['Protocol'] == 'TLSv1.2'): # This to filter only TLS packets which append session information application data
		srcip = pkt['Source']
		dstip = pkt['destination']
		timestamp = pkt['Time']
		information = pkt['Info']

		msg = str(c) + ',' + str(srcip) + ',' + str(dstip) + \
		','  + str(timestamp) + ',' + str(information)

		print(msg)
		c+=1

		producer.send('packet_test_pcap', msg)
		sleep(1)
producer.close()
