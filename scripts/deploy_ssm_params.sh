#!/bin/bash

# when common error occurs, the script will immediately fail
set -euo pipefail

# configuration
ENVIRONMENT=$2

WORKING_DIR="$(pwd)"
AWS_PROFILE="mlops_developer"

echo "This is the environment: $ENVIRONMENT"

AWS_REGION="eu-north-1"
STACK_NAME="$ENVIRONMENT-ssm-params"
echo $STACK_NAME

TEMPLATE_FILE="$WORKING_DIR/SAM/ssm-params-template.yml"

echo "Checking AWS identity..."
aws sts get-caller-identity --profile $AWS_PROFILE

echo "Checking SAM is installed..."
sam --version || {
    echo "SAM is not installed"
    exit 1
}

echo "Building SAM template..."
sam build --template-file "$TEMPLATE_FILE"
echo "SAM template built successfully."

echo "Deploy SAM template..."
sam deploy \
    --profile $AWS_PROFILE \
    --region $AWS_REGION \
    --template-file "$TEMPLATE_FILE" \
    --stack-name $STACK_NAME \
    --parameter-overrides \
    Environment="$ENVIRONMENT"
echo "SAM deployment completed sucessfully!"