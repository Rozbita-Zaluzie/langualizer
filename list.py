import os

def make_list(path):  

    langs_ext = open("programming_ext.csv", "r").read().split(",")
    markup_ext = open("markup_ext.csv", "r").read().split(",")



    dict = {}

    def add_to_list(path): 
        for f in os.listdir(path):
            
            if "." in f and f != ".history":
                dict[f] = os.path.getsize(path + "/" + f)
            elif f != ".history":
                add_to_list(path + "/" + f)

    add_to_list(path)

    sizes = {}
    languages = {}
    markup = {}

    for key, value in dict.items():
        key = key.split(".")[-1]
        if key in sizes:
            sizes[key] += value
        else:
            sizes[key] = value

            
        if key in langs_ext and key in languages:
            languages[key] += value
        elif key in langs_ext:
            languages[key] = value

        if key in markup_ext and key in markup:
            markup[key] += value
        elif key in markup_ext:
            markup[key] = value
        


    # percentage of each language
    sumSize = sum(sizes.values())
    for key, value in sizes.items():
        sizes[key] = (value / sumSize) * 100 

    sumLang = sum(languages.values())
    for key, value in languages.items():
        print(key, value)
        languages[key] = (value / sumLang) * 100   

    sumMarkup = sum(markup.values())
    for key, value in markup.items():
        markup[key] = (value / sumMarkup) * 100

    print(sizes) 
    print(languages)
    print(markup)


    
