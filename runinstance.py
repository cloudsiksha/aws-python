import boto3

client = boto3.client('ec2')

reservation = client.run_instances(
                ImageId='ami-9ff7e8af',
                InstanceType='t2.micro',
                MinCount=1, MaxCount=1,
               )