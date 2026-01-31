#!/bin/bash

# when common errors occur, the script will immediately fail
set -euo pipefail

STACK_NAME=$2

echo "Checking if AWS CLI is installed..."
aws --version

echo "Checking AWS identity..."
aws sts get-caller-identity

echo "Checking SAM is installed..."
sam --version || {
    echo "SAM is not installed"
    exit 1
}

echo "Deleting stack..."
aws cloudformation delete-stack --stack-name $STACK_NAME
echo "Stack deletion successful"