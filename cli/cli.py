# Contains the functionality for deploying the AWS resources defined in the resource templates within the SAM/ directory
import typer 
import sys
import os

current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from utils.lambda_function_deployment import deploy_function


app = typer.Typer(help="Machine Learning Platform CLI - Deploy an AWS Lambda")

# NOTE WITHIN THE CLI __main__.py file, i can potentially create a 
# ALSO NOTE I CAN DEFINE THE DECORATOR @app.command() more than once so i can create different functions e.g. deploying a lambda function deploying etc
@app.command()
def main(
        # ... = no default argument for the
        service_name: str = typer.Option(..., "--service-name", help="The name of the Lambda function to be deployed"),
        code_path: str = typer.Option(..., "--code_path", help="The relative path of the lambda function needing to be deployed"),
        environment: str = typer.Option("development", "--environment", help="This is the environment that the (development, production)")
):
        deploy_function(
                service_name=service_name,
                code_path=code_path,
                environment=environment
        )


if __name__ == "__main__":
        app()