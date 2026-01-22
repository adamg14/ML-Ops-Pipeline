import boto3
import datetime
from boto3.dynamodb.conditions import Key, Attr


# Update this file structure to follow OOP for querying https://docs.aws.amazon.com/code-library/latest/ug/python_3_dynamodb_code_examples.html

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



def get_bucket(
        table_name,
        bucket_name
):
    dynamodb = boto3.client('dynamodb')
    response = dynamodb.query(
        TableName=table_name,
        KeyConditionExpression='BucketName = :bucket',
        ExpressionAttributeValues={
            ':bucket': {'S': bucket_name}
        }
    )

    return response.get('Items', [])


def get_file(
        table_name,
        bucket_name,
        file_name
):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(table_name)
    response = table.get_item(
        Key = {
            'BucketName': bucket_name,
            'FileName': file_name
        }
    )

    return response.get('Item')

print(get_file('development-file-table', 'development-landing-bucket', 'adam.txt'))

def not_sanitised(
        table_name,
        bucket_name
):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(table_name)
    response = table.query(
        TableName=table_name,
        KeyConditionExpression=Key('BucketName').eq(bucket_name),
        FilterExpression=Attr('Sanitised').eq(False)
    )

    return response.get('Items', [])


# may need to create seperate tables for sanitised/curated tables - not exactly necessary
def is_sanitised(
        table_name,
        bucket_name
):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(table_name)
    response = table.query(
        TableName=table_name,
        KeyConditionExpression=Key('BucketName').eq(bucket_name),
        FilterExpression=Attr('Sanitised').eq(True)
    )

    return response.get('Items', [])

def not_curated(
        table_name,
        bucket_name
):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(table_name)
    response = table.query(
        TableName=table_name,
        KeyConditionExpression=Key('BucketName').eq(bucket_name),
        FilterExpression=Attr('Curated').eq(False)
    )

    return response.get('Items', [])

def is_curated(
        table_name,
        bucket_name
):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(table_name)
    response = table.query(
        TableName=table_name,
        KeyConditionExpression=Key('BucketName').eq(bucket_name),
        FilterExpression=Attr('Curated').eq(True)
    )

    return response.get('Items', [])