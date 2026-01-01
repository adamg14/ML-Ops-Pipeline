# This function will run a AWS deployment of the lambda function via SAM 
def deploy_function(
        service_name,
        code_path,
        environment
):
    print(f"service name: {service_name}")
    print(f"code path: {code_path}")
    print(f"environment: {environment}") 