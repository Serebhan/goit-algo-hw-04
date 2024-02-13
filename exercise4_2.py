

def get_cats_info(path):
    try:
        with open(path, encoding='utf-8') as f:
            lines=f.readlines()
    except FileNotFoundError:
        print (f"Оце так, файлу {path} не можу знайти")
        return ""
    
    cats_info=[]
    for line in lines:
        id,name, age = line.split(",")
        age=int(age)
        cats_info.append({"id":id, "name":name, "age": age})
    

    return cats_info



cats_info = get_cats_info("path/to/cats_file.txt")
print(cats_info)