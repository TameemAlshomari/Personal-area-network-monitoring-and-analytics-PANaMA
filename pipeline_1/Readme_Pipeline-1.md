# Stream Collecting and Monitoring Measurements Pipeline

This pipeline will explain collecting metrics data from the Source host machine (local host) by using Telegraf plugins, then storing the collected data into InfluxDB database and strum visualizing the measurements using Grafana.

## Installation

Download the docker-compose.yml file to your local machine or vim new yml file and use same configuration.
Download the confige file which used for Telegraf configuration.
Start your Docker Daemon, and any command line (windows Power Shell).

## Run the containers

```bash
docker-compose up
```

It will download the images from docker hub if they are not exist in the local docker Daemon images.
After a short time, the messages will display that all containers and services are up and telegraf starts posting db to the InfluxDB.

Open your web browser and type your localhost IP and the Grafana-server port number like (172.23.176.1:3000/login) 

In Grafana-server, you have to add the database source. The data source will be the InfluxDB which is continually storing the real time data measurements which is posting by Telegraf

Create the DASHBOARD which you need to use it, then specify the data scouce to start visualizing.

Finally select the parameters of data which we need to visualize, then you will find the data coming on monitoring dashboard.

You can use the CLI to run different queries for InfluxDB Database for example, 

```bash
docker exec influxdb influx -execute 'SHOW DATABASES' 
```
You can use the Docker Daemon to find the logs in the volume field. 