# AWS ML Ops Project
A serverless data and machine learning platform on AWS using:
1. AWS SAM - For Infrastucture as Code and Cloud Platform Service builds.
2. AWS Lambda - For backend functionality of the pipeline and data service.
3. AWS S3 - Raw, partly-processed and processed data storage
4. AWS Cloudwatch Logs and Metrics - Centralised logging and obserability
5. AWS DynamoDB - NoSQL database to track where each of the files are in the pipeline process.
6. AWS Glue = serverless data integration service used to create job for sanitising and curating the raw data.
7. AWS SageMaker = Used to manage end-to-end Machine Learning workflows.

## Commands
```bash
python cli/deploy_lambda.py --service-name *cloud lambda function name * --code_path *relative local path to lambda function* --environment *development environment*
```

```bash
./scripts/deploy_lambda.sh --service-name *cloud lambda function name* --code_path *relative local path to lambda function* --environment *development environment*
```

### Example Commands
In order to deploy an example lambda function to the development environment:
```bash
./scripts/deploy_lambda.sh --service-name hello_world_lambda --code_path ./lambdas/initial_deployment --environment development
```

### Example Commands
### List Stacks
```bash
aws cloudformation list-stacks --stack-status-filter CREATE_COMPLETE UPDATE_COMPLETE --region *AWS_REGION_NAME* --profile *PROFILE*
```

### Delete Stacks
aws cloudformation delete-stack --stack-name *STACK_NAME* --region eu-north-1 --profile mlops_developer