import boto3
ec2 = boto3.resource('ec2')

for e in ec2.instances.all():
	print(e)

