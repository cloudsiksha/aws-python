import boto3
client = boto3.client('sns')
sns = boto3.resource('sns')
topic = sns.Topic("arn:aws:sns:us-west-2:033578524086:NewTopic")

response = client.set_topic_attributes(
	TopicArn="arn:aws:sns:us-west-2:033578524086:NewTopic",
	AttributeName='Policy',
	AttributeValue='{\
 "Version": "2008-10-17",\
 "Id": "example-ID",\
 "Statement": [\
  {\
   "Sid": "example-statement-ID",\
   "Effect": "Allow",\
   "Principal": {\
    "AWS":"*"\
   },\
   "Action": [\
    "SNS:Publish"\
   ],\
   "Resource": "arn:aws:sns:us-west-2:033578524086:NewTopic",\
   "Condition": {\
      "ArnLike": {\
      "aws:SourceArn": "arn:aws:s3:*:*:suresh0302"\
    }\
   }\
  }\
 ]\
}')