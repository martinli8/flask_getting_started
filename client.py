import requests
import sys
import json

r = requests.get("http://vcm-3590.vm.duke.edu:5000/name")
data = r.json()
json.dump(data, sys.stdout, indent=4)


r1 = requests.get("http://vcm-3590.vm.duke.edu:5000/hello/martin")
data2 = r1.json()
json.dump(data2, sys.stdout, indent=4)


r2 = requests.post("http://vcm-3590.vm.duke.edu:5000/distance", json = {
  "a": [2, 4],
  "b": [5, 6]
})
data3 = r2.json()
json.dump(data3, sys.stdout, indent=4)
