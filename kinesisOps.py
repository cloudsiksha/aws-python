import boto3
import json
import time

#kinesis_stream = boto3.client('kinesis')

#response = kinesis_stream.create_stream(
#	               StreamName = 'CloudSiksha',
#	               ShardCount = 1)

def put_stream(stream_name, my_data, partition_key):
	kinesis_client = boto3.client('kinesis')

	response = kinesis_client.put_record(
		           StreamName = stream_name,
		           Data = my_data,
		           PartitionKey = partition_key)
	return response

my_streamname = 'CloudSiksha'
my_partition_key = 'aa'
#i = 0
#while i < 50:
#    data = "Hello"+str(i)
#    my_struct = {"Key":data}
#    my_input_data = json.dumps(my_struct)
#    i = i+1

 #   response = put_stream(my_streamname,my_input_data,my_partition_key)
  #  print(response)

def get_stream(my_stream_name):

	kinesis_client = boto3.client('kinesis')

	response = kinesis_client.describe_stream(StreamName = my_stream_name)
	print(response)

	my_shard_id = response['StreamDescription']['Shards'][0]['ShardId']
	starting_sequence_number = response['StreamDescription']['Shards'][0]['SequenceNumberRange']['StartingSequenceNumber']

	shard_iterator = kinesis_client.get_shard_iterator(StreamName=my_stream_name,
                                                      ShardId=my_shard_id,
                                                      ShardIteratorType='TRIM_HORIZON')
                                                      #StartingSequenceNumber = starting_sequence_number)

	my_shard_iterator = shard_iterator['ShardIterator']

	read_response = kinesis_client.get_records(ShardIterator=my_shard_iterator,
                                              Limit=10)

	while 'NextShardIterator' in read_response:
		read_response = kinesis_client.get_records(ShardIterator=read_response['NextShardIterator'],
                                                  Limit=10)

		print(read_response['Records'])
		if not read_response['Records']:
			break

		time.sleep(5)


get_stream(my_streamname)
