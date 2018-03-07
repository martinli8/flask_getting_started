import requests
r = requests.get("http://bme590.suyash.io")


r2 = requests.post("http://bme590.suyash.io/sum", json={"a": 1, "b": 2})
sum_result = r2.json()
print(sum_result)
print("The response was {0}.".format(sum_result['result']))

r3 = requests.post("http://bme590.suyash.io/student", json = {
"first_name": "Martin",
"last_name": "Li",
"netid": "ml328",
"github_username": "martinli8",
"team_name": "teamOne"})
