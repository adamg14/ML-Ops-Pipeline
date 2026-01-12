#!/bin/bash

# When common errors occur, the script will immediately fail
set -euo pipefail

# configuration
SERVICE_NAME=$2
CODE_PATH=$4
ENVIRONMENT=$6

AWS_PROFILE="mlops_developer"

echo "This is the name of the lambda function: $SERVICE_NAME"
echo "This is the path to the function code: $CODE_PATH"
echo "This is the environment: $ENVIRONMENT"

AWS_PROFILE="mlops_developer"
AWS_REGION="eu-north-1"

STACK_NAME="$ENVIRONMENT-$SERVICE_NAME-platform-lambda-function"
echo $STACK_NAME

TEMPLATE_FILE="../SAM/lambda-function-template.yaml"