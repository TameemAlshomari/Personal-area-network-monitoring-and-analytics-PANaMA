from pyflink.common import Row
from pyflink.common.serialization import JsonRowDeserializationSchema, JsonRowSerializationSchema
from pyflink.common.typeinfo import Types
from pyflink.datastream import StreamExecutionEnvironment
from pyflink.datastream.connectors import FlinkKafkaConsumer, FlinkKafkaProducer
import Properties
from org.apache.flink.streaming.api.functions.source import SourceFunction
from org.apache.flink.streaming.api.collector.selector import OutputSelector
from org.apache.flink.api.common.serialization import SimpleStringSchema



def datastream_api_flink_kafka_connector():
    # 1. create a StreamExecutionEnvironment
    env = StreamExecutionEnvironment.get_execution_environment()
    env.add_jars("file:///path/to/flink-sql-connector-kafka.jar")

    # 2. create source DataStream
    deserialization_schema = JsonRowDeserializationSchema.builder() \
        .type_info(type_info=Types.ROW([Types.LONG(), Types.LONG()])).build()

    kafka_cosumer = FlinkKafkaConsumer(
        topics='packet_test_pcap',
        deserialization_schema=deserialization_schema,
        properties={'bootstrap.servers': 'localhost:9092'})

    ds = env.add_source(kafka_cosumer)


    # 3. create sink and emit result to sink
    serialization_schema = JsonRowSerializationSchema.builder().with_type_info(
        type_info=Types.ROW([Types.LONG(), Types.LONG()])).build()
    kafka_sink = FlinkKafkaProducer(
        topic='packet_test_pcap',
        serialization_schema=serialization_schema,
        producer_config={'bootstrap.servers': 'localhost:9092'})
    ds.add_sink(kafka_sink)

    # 4. execute the job
    env.execute('datastream_api_flink_kafka_connector')


if __name__ == '__main__':
    datastream_api_flink_kafka_connector()

