import requests

r1 = requests.post("http://127.0.0.1:5000/distance", json = {
  "a": [1, 3],
  "b": [5, 6]
})


r2 = requests.post("http://127.0.0.1:5000/distance", json = {
  "a": [2, 4],
  "b": [5, 6]
})


r3 = requests.post("http://127.0.0.1:5000/distance", json = {
  "a": [5, 6],
  "b": [5, 6]
})
