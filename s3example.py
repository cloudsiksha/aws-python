import boto3
s3 = boto3.resource('s3')
bucket = s3.buckets.all()
for b in s3.buckets.all():
	print(b.name)
for b in s3.buckets.all():
	print(b.name)
	print(b.creation_date)
cli = boto3.client('s3')
for b in s3.buckets.all():
	bucketName = b.name
	response = cli.list_objects(Bucket=bucketName)
keyName1 = response['Contents'][0]['Key']
cli.delete_object(Bucket=bucketName,Key=keyName1)
KeyObjects = response['Contents']
i = 0
while i < len(KeyObjects):
	for e in KeyObjects[i]:
		print(e,":",KeyObjects[i][e])
	i = i+1