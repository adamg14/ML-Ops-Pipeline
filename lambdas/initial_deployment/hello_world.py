import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    logger.info("The lambda function has now started.")
    logger.info(f"CloudWatch logs group: {context.log_group_name}")

    # Get the name param from the event object
    user_name = event["name"]
    user_greeting = lambda x: f"Welcome to my AWS ML Ops Project, {x}, hope you are doing well."

    set_user_greeting = user_greeting(user_name)
    print(set_user_greeting)

    # the user greeting is printed above, the lambda function also returns it below
    function_json_data = {
        "user_name": user_name,
        "user_greeting": set_user_greeting
    }

    return json.dumps(function_json_data)
