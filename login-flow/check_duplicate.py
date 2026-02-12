import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Users')

def lambda_handler(event, context):
    user = event.get("user", {})
    email = user.get("email")

    response = table.get_item(Key={"email": email})
    is_duplicate = 'Item' in response

    return {
        "isDuplicate": is_duplicate,
        "user": user  # <-- INI PENTING
    }
