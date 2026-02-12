def lambda_handler(event, context):
    name = event.get("name")
    email = event.get("email")

    if not name or not email:
        return {
            "validated": False,
            "error": "Missing name or email"
        }

    return {
        "validated": True,
        "user": {
            "name": name,
            "email": email
        }
    }
