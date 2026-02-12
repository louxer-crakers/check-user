import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Users')

def lambda_handler(event, context):
    user = event.get("user", {})

    email = user.get("email")
    name = user.get("name")

    if not email or not name:
        return {
            "statusCode": 400,
            "message": "Missing name or email"
        }

    table.put_item(Item={
        "email": email,
        "name": name
    })

    return {
        "statusCode": 200,
        "message": f"User {email} saved successfully!",
        "user": user
    }
