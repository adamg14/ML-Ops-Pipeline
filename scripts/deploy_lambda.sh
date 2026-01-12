#!/bin/bash

# When common errors occur, the script will immediately fail
set -euo pipefail

# configuration
SERVICE_NAME=$2
ENVIRONMENT=$4

WORK_DIR="$(pwd)"
AWS_PROFILE="mlops_developer"

echo "This is the name of the lambda function: $SERVICE_NAME"
echo "This is the environment: $ENVIRONMENT"

AWS_PROFILE="mlops_developer"
AWS_REGION="eu-north-1"
STACK_NAME="$ENVIRONMENT-lambda-functions"
echo $STACK_NAME

TEMPLATE_FILE="$WORK_DIR/SAM/lambda-function-template.yaml"

echo "Checking AWS identity..."
aws sts get-caller-identity --profile $AWS_PROFILE

echo "Checking SAM is installed..."
sam --version || {
    echo "SAM is not installed"
    exit 1
}

echo "Building SAM template..."
sam build --template-file  "$TEMPLATE_FILE"
echo "SAM template built successfully."

echo "Deploying SAM template..."
sam deploy \
    --profile $AWS_PROFILE \
    --region $AWS_REGION \
    --template-file "$TEMPLATE_FILE" \
    --stack-name $STACK_NAME \
    --parameter-overrides \
    ServiceFunctionName="$SERVICE_NAME" \
    Environment="$ENVIRONMENT"
echo "SAM deployment completed successfully!"