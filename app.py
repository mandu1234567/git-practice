import json

def lambda_handler(event, context):
    message = "Hello from AWS Lambda!"

    print(message)  # This goes to CloudWatch logs

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": message
        })
    }
