import random

from users.models import User


def generate_username(name):
    username = "".join(name.split(' ')).lower()
    if not User.objects.filter(username=username).exists():
        return username
    else:
        random_username = username + str(random.randint(0, 1000))
        return generate_username(random_username)


def register_social_user(email, name, first_name=None, last_name=None):
    filtered_user_by_email = User.objects.filter(email=email).first()

    if filtered_user_by_email:
        return {
            'email': filtered_user_by_email.email,
            'username': filtered_user_by_email.username,
            'full_name': filtered_user_by_email.full_name,
            'tokens': filtered_user_by_email.tokens
        }
    else:
        if not first_name and not last_name:
            first_name, last_name = name.split(" ")[0], name.split(" ")[1]
        user_data = {
            'username': generate_username(name), 'email': email, 'first_name': first_name, 'last_name': last_name
        }
        user = User.objects.create_user(**user_data)
        return {
            'email': user.email,
            'username': user.username,
            'full_name': user.full_name,
            'tokens': user.tokens
        }
