import subprocess
import typer
import sys

# This function will run a AWS deployment of the lambda function via SAM 
def deploy_function(
        service_name,
        code_path,
        environment
):
    print(f"service name: {service_name}")
    print(f"code path: {code_path}")
    print(f"environment: {environment}") 
    
    script_path = "../scripts/deploy_lambda.sh"
    command = [
        "bash",
        str(script_path),
        service_name,
        code_path,
        environment
    ]

    result = subprocess.run(command,text=True)

    if result.returncode == 0:
        print("SAM build completed successfully.")
    else:
        sys.exit(result.returncode)


