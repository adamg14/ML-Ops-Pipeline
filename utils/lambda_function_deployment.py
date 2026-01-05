import subprocess
import typer


# This function will run a AWS deployment of the lambda function via SAM 
def deploy_function(
        service_name,
        code_path,
        environment
):
    print(f"service name: {service_name}")
    print(f"code path: {code_path}")
    print(f"environment: {environment}") 

    stack_name = f"{environment}-platform-lambda-function"
    command = [
        "sam",
        "deploy", 
        "--stack-name",
        stack_name,
        "--parameter-overrides",
        f"ServiceFunctionName={service_name}",
        f"LambdaFunctionPath={code_path}",
        f"Environment={environment}"
        ]

    typer.echo("Currently running SAM deployment...")
    typer.echo(" ".join(command))

    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        typer.echo("SAM deployment failed")
        typer.echo(f"Error message: {e}")
        typer.Exit(code=e.returncode)

