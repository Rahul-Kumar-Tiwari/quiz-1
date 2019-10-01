import boto3
client = boto3.client('s3')

response = client.delete_object(
    Bucket='bucket01ethans',
    Key='bootstrap.txt'
)