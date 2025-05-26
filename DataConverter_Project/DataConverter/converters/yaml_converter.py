import yaml

def load_yaml(file_path):
    with open(file_path, 'r') as f:
        return yaml.safe_load(f)

def save_yaml(file_path, data):
    with open(file_path, 'w') as f:
        yaml.dump(data, f, sort_keys=False)
