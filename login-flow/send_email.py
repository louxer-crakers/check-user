def lambda_handler(event, context):
    user = event.get("user", {})
    email = user.get("email", "unknown")

    return {
        "message": f"Welcome email sent to {email}!",
        "user": user
    }
