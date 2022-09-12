import json
  

f = open('Programming_Languages_Extensions.json')

data = json.load(f)
f = open("programming_ext.csv", "w")
f2 = open("markup_ext.csv", "w")

for i in data:
    try:
        if i['type'] == 'programming':
            for x in i['extensions']:
                f.write(x[1:] + ",")
                print(x)

        if i['type'] == 'markup':
            for x in i['extensions']:
                f2.write(x[1:] + ",")
                print(x)
    except:
        pass
# Closing file
f.close()