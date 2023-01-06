import yaml
import os

def get_yaml_data(file_name):
    current_path = os.path.abspath(".")
    yaml_path = os.path.join(current_path,file_name)

    with open(yaml_path, 'r', encoding="utf-8") as f:
        file_data = f.read()
    
    # print(file_data)
    # print("类型：", type(file_data))

    data = yaml.safe_load(file_data)
    # print(data)
    # print("类型：", type(data))
    return data

def dump_data_to_yaml(data,file_name,way):
    current_path = os.path.abspath(".")
    yaml_path = os.path.join(current_path,file_name)

    with open(yaml_path,way,encoding="utf-8") as f:
        yaml.dump(data, f, encoding='utf-8', allow_unicode=True)

    return True