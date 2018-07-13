### Twitter_Kafka_Streaming

Requirements:<br/>
Zookeeper and Kafka should be installed on your machine.<br/>
To add python libraries run commands:<br/>
pip install kafka-python<br/>
pip install tweepy<br/>

Before running the python application start ZooKeeper and Kafka then create your a topic in Kafka broker.<br/>

Use the following commands: (on Windows platform)<br/>
Start the zkServer (zookeeper)<br/>
>kafka-topics.bat --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic first-topic<br/>
//first-topic is the topic named created<br/>

Update your twitter application credentials in twitter_credentials.txt<br/>
Now, run the python application.<br/>

To see the twitter stream in the kafka commit log, run the command:<br/>
>kafka-console-consumer.bat --zookeeper localhost:2181 -topic first-topic --from-beginning<br/>
