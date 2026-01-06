#!/bin/bash

# When common errors occur, the script will immediately fail
set -euo pipefail

# configuration
# :? is a required check
SERVICE_NAME="${1:?service name required}"
CODE_PATH="${2:?code path required}"
ENVIRONMENT="${3:-development}"
AWS_PROFILE="Admin-137345588056"

echo $SERVICE_NAME
echo $CODE_PATH
echo $ENVIRONMENT

STACK_NAME="$ENVIRONMENT-platform-lambda-function"
TEMPLATE_FILE="SAM/lambda-function-template.yaml"

# verification checks
echo "Checking AWS identity..."
aws sts get-caller-identity --profile $AWS_PROFILE

echo "Check SAM is installed..."
# a version for SAM is found or else an error message is returned
command -v sam || {
    echo "SAM not installed"
    exit 1
}

echo "Building SAM template..."
sam build --template-file  "../$TEMPLATE_FILE"

echo "Deploying SAM template..."
sam deploy \
    --template-file "../$TEMPLATE_FILE" \
    --stack-name $STACK_NAME \
    --parameter-overrides \
    ServiceFunctionName="$SERVICE_NAME" \
    LambdaFunctionPath="$CODE_PATH" \
    Environment="$ENVIRONMENT"
echo "Deployment complete"