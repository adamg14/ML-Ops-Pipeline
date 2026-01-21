import boto3
import datetime

dynamodb = boto3.client('dynamodb')

now = datetime.datetime.now()
now_str = str(now)

def add_item(
        table_name,
        bucket_name,
        file_name,
        sanitised,
        curated,
        file_size,
        uploaded_at=None):
    
    if uploaded_at is None:
        uploaded_at = datetime.datetime.now().isoformat()
    dynamodb.put_item(
        TableName=table_name,
        Item={
        'BucketName': {'S': bucket_name},
        'FileName': {'S': file_name},
        'Sanitised': {'BOOL': sanitised},
        'Curated': {'BOOL': curated},
        'UploadedAt': {'S': uploaded_at},
        'FileSize': {'N': str(file_size)}
    }
    )



def bucket_query(
        table_name,
        bucket_name
):
    response = dynamodb.query(
        TableName=table_name,
        KeyConditionExpression='BucketName = :bucket',
        ExpressionAttributeValues={
            ':bucket': {'S': bucket_name}
        }
    )

    return response.get('Items', [])

