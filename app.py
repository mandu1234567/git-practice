import json

def lambda_handler(event, context):
    message = "Hello from mamdu"

    print(message)  # This goes to CloudWatch logs

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": message
        })
    }
