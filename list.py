import os

def make_list(path):  

    ext = open("files/extentions.csv", "r").read().split(",")



    dict = {}

    def add_to_list(path): 
        for f in os.listdir(path):
            try:
                if "." in f and f != ".history":
                    dict[f] = os.path.getsize(path + "/" + f)
                elif f != ".history":
                    add_to_list(path + "/" + f)
            except Exception as e:
                print(e)

    add_to_list(path)


    languages = {}

    for key, value in dict.items():
        key = key.split(".")[-1]
            
        if key in ext and key in languages:
            languages[key] += value
            
        elif key in ext:
            languages[key] = value
            

        


    # percentage of each language
    sumLang = sum(languages.values())
    for key, value in languages.items():
        print(key, value)
        languages[key] = (value / sumLang) * 100   


    

    return languages


    
