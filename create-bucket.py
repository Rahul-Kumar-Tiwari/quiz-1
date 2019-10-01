import boto3

client = boto3.client('s3')

response = client.create_bucket(
    ACL='private',
    Bucket='bucketohio123gayatri',
    CreateBucketConfiguration={
        'LocationConstraint': 'us-west-1'
    },

    #GrantRead= 'string'
)



