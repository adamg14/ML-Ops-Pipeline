#!/bin/bash

# when common errors occur, the script will immediately fail
set -euo pipefail

ENVIRONMENT=$2

WORKING_DIR="$(pwd)"
AWS_PROFILE="mlops_developer"
AWS_REGION="eu-north-1"
AWS_PROFILE="mlops_developer"
STACK_NAME="$ENVIRONMENT-persistant-storage"

echo "This is the environment: $ENVIRONMENT"
echo "This is the stack name: $STACK_NAME"
echo "This is the current working directory: $WORKING_DIR"

CF_TEMPLATE_FILE="$WORKING_DIR/SAM/persistent-storage.yml"

echo "Checking AWS identity..."
aws sts get-caller-identity

echo "Checking SAM is installed..."
sam --version || {
    echo "SAM is not installed"
    exit 1
}

echo "Building SAM template.."
sam build --template-file "$CF_TEMPLATE_FILE"
echo "SAM template built successfully"

echo "Deploying SAM template..."
sam deploy \
    --profile $AWS_PROFILE \
    --region $AWS_REGION \
    --template-file "$CF_TEMPLATE_FILE" \
    --stack-name $STACK_NAME \
    --parameter-overrides \
    Environment="$ENVIRONMENT"
echo "SAM deployment completed sucessfully!"