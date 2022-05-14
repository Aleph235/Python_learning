def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile_1 = build_profile('franz', 'kafka', field='literature')

print(user_profile_1)
