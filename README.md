# Twitter_Kafka_Streaming

Requirements:
Zookeeper and Kafka should be installed on your machine.
To add python libraries run commands:
pip install kafka-python
pip install tweepy

Before running the python application start ZooKeeper and Kafka then create your a topic in Kafka broker.

Use the following commands: (on Windows platform)
Start the zkServer (zookeeper)
kafka-topics.bat --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic first-topic
//first-topic is the topic named created

Update your twitter application credentials in twitter_credentials.txt
Now, run the python application.

To see the twitter stream in the kafka commit log, run the command:
>kafka-console-consumer.bat --zookeeper localhost:2181 -topic first-topic --from-beginning
