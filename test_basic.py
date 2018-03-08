import requests
import sys
import json

r = requests.get("http://vcm-3590.vm.duke.edu:5000/name")
print(r.content)
# json.dump(r.content, sys.stdout, indent=4)
#
r1 = requests.get("http://vcm-3590.vm.duke.edu:5000/hello/martin")
print(r1.content)
#
r2 = requests.post("http://vcm-3590.vm.duke.edu:5000/distance", json = {
  "a": [2, 4],
  "b": [5, 6]
})
print(r2.content)
#
# r3 = requests.post("http://127.0.0.1:5000/distance", json = {
#   "a": [5, 6],
#   "b": [5, 6]
# })
