import screen
screen.clear()

# Using Arbitrary Keyword Arguments

def build_profile(first, last, **user_info):
    # Build a dictionary containing eveything we know aout a user
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = build_profile('dovvy', 'pacamalan',
                            country='philippines',
                            sex='male',
                            job='computer programmer')

for key, value in user_profile.items():
    print(f'\t{key.title()} : {value.title()} ')
