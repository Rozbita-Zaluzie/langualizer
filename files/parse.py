import json
  

f = open('Programming_Languages_Extensions.json')

data = json.load(f)
f = open("extentions.csv", "w")

for i in data:
    try:
        if i['type'] == 'programming' or i['type'] == 'markup' or i['type'] == 'data':
            for x in i['extensions']:
                f.write(x[1:] + ",")
                print(x)

    except:
        pass
# Closing file
f.close()