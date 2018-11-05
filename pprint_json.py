import json


def load_data(filepath):
    with open (file_path, 'r', encoding='utf-8') as f:
    dict_from_json = json.loads(f.read()


def pretty_print_json(data):
    json_from_dict = json.dumps(dict_from_json['features'], 
                      separators=(',', ':'), 
                      ensure_ascii=False, 
                      indent=4, 
                      skipkeys = True, 
                      sort_keys=True)
    
    print(json_from_dict)


if __name__ == '__main__':
    pass
