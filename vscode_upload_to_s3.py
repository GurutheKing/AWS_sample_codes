import boto3
from botocore.client import Config

ACCESS_KEY_ID =""
ACCESS_SECRET_KEY=""
BUCKET_NAME =""

data = open('test.png', 'rb')

s3 =boto3.resource(
    aws_access_key_id=ACCESS_KEY_ID,
    aws_secret_access_key=ACCESS_SECRET_KEY,
    Config=Config(signature_version='s3v4')
)
s3.Bucket(BUCKET_NAME).put_object(Keys='test.png', Body=data)

print("Done")
