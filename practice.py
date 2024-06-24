def build_profile(first, last, **info):
    info['first_name'] = first
    info['last_name'] = last
    return info

my_profile = build_profile('quoc', 'phan', address='quy nhon', age=33, major='designer')

print("--- Your profile information ---")
for key, value in my_profile.items().__reversed__():
    print(f"- {key.title()}: {value}")