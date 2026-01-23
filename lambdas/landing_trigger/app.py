import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    logger.info("A file uploaded to the landing bucket triggered this lambda")

    logger.info(f"CloudWatch logs group: {context.log_group_name}")

    # the s3 object creation event
    print(event)

    # the s3 file details within this array will be added to the dynamodb database
    event_details = []

    for file in event["Records"]:
        event_details.append({
            "BucketName": file["s3"]["bucket"]["name"],
            "ObjectKey": file["s3"]["object"]["key"],
            "ObjectSize": file["s3"]["object"]["size"],
            "Sanitised": False,
            "Curated": False
        })
        
    return event_details