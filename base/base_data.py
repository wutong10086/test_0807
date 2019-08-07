import yaml


def data(file_name, data_file):
    with open("./data/" + file_name, "r", encoding="utf-8") as f:
        data = yaml.load(f)
        dict_data = data[data_file]
        list_data = list()
        for i in dict_data.values():
            list_data.append(i)
        return list_data
