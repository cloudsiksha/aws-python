import boto3

client = boto3.client('ec2')
res = client.describe_instances()

instanceList = res['Reservations']

i = 0

while i < len(instanceList):
    print(instanceList[i]['Instances'][0]['State']['Name'])
    i = i+1
id1 = res['Reservations'][0]['Instances'][0]['InstanceId']
ec2 = boto3.resource('ec2')
instance = ec2.Instance(id1)
state = instance.state['Name']
if state=='running':
   instance.terminate()

