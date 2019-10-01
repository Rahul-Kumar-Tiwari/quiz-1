import boto3
client = boto3.client('s3')

file_reader = open('upload.py').read()
response = client.put_object(
    ACL='private',
    Body=file_reader,
    Bucket='bucketohio123gayatri',
    Key='uploading_object.py'
)