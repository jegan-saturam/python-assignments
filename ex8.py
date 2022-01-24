import json
jsondata = """[ 
     { 
        "id":1,
        "name":"name1",
        "color":[ 
           "red",
           "green"
        ]
     },
     { 
        "id":2,
        "name":"name2",
        "color":[ 
           "pink",
           "yellow"
        ]
     }
    ]"""

data = json.loads(jsondata)
print(data)
namedata = [item.get('name') for item in data]
print(namedata)