#Personal-area-network-monitoring-and-analytics-PANaMA
Description: Develop a solution for collecting monitoring data from a person's personal area network. Implement a data ingest solution capable to handle millions of parallel users and their incoming data streams. Implement an anomaly detection algorithm capable to detect per-user and system-wide anomalies in the monitoring data collected from the multitude of system users.

This pipeline is using FileBeat : used to get a real-time view of log data- PacketBeat : Analyze the information included in network packets.- MetricBeat : is a lightweight shipper that you can install on your servers to collect metrics from the operating system and services that are running on them on a regular basis. to collect data logs from network , internet and websites then we store that in Database in csv and json format then we send this file to kafka producer in order to convert this data into stream

Installation Download the docker-compose.yml file to your local machine and it will be used to install beats , connect it with kibana , install kafka
