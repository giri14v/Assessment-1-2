import json

with open('ex5.json', 'r') as f:
    ex5_data = json.load(f)

ex5 = ex5_data

for item in ex5:
    if item['name'] == 'Old Fashioned':
        item['batters']['batter'].append({"id": "1005", "type": "Tea"})

with open('ex5.json', 'w') as f:
    json.dump(ex5, f, indent=4)


print("Batter 'Tea' added for the donut with name 'Old Fashioned'. ex5.json updated successfully.")
