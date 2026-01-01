*AWS ML Ops Project*
A serverless data and machine learning platform on AWS using:
1. AWS SAM - For Infrastucture as Code and Cloud Platform Service builds.
2. AWS Lambda - For backend functionality of the pipeline and data service.
3. AWS S3 - Raw, partly-processed and processed data storage
4. Cloudwatch Logs and Metrics - Centralised logging and obserability

*Commands*
python cli/deploy_lambda.py --service-name *cloud lambda function name * --code_path *relative local path to lambda function* --environment *development environment*