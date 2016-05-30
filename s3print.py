import boto3

s3 = boto3.resource('s3')

for bucket in s3.buckets.all():
    for obj in bucket.objects.all():
        print(obj.key)