"""
URL: https://api.github.com/users/<ID>/repos
"""
r = requests.get(url)

response_dict = r.json()

print(response_dict.keys())

print("Total repositories:", response_dict['Number of commits'])

repo_dicts = response_dict['items']

repo_dict = repo_dicts[0]
print("\nKeys:",len(repo_dict))
for key in sorted(repo_dict.keys()):
    print(key)

