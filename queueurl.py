import boto3
sqs = boto3.resource('sqs')

myqueue = sqs.get_queue_by_name(QueueName='test')
print(myqueue.url)

myqueue = sqs.get_queue_by_name(QueueName='test')

message = myqueue.Messagereceive_messages()

print(len(message))

if 'Records' in message[0].body:
	print('Correct Message')
else:
	print('Test Message')
	
data = json.loads(message[0].body)

if 'Records' in message[0].body:
	print(data['Records'][0]['s3']['object']['key'])
	print(data['Records'][0]['s3']['bucket']['name'])
else:
	print('Test Message')
 