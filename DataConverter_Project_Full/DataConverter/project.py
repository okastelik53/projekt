import sys
import os
from converters.json_converter import load_json, save_json
from converters.yaml_converter import load_yaml, save_yaml
from converters.xml_converter import load_xml, save_xml

def get_format(file_path):
    ext = os.path.splitext(file_path)[1].lower()
    if ext == '.json': return 'json'
    elif ext in ['.yml', '.yaml']: return 'yaml'
    elif ext == '.xml': return 'xml'
    else: return None

def main():
    if len(sys.argv) != 3:
        print("Użycie: project.exe inputFile outputFile")
        sys.exit(1)

    input_file, output_file = sys.argv[1], sys.argv[2]
    input_format = get_format(input_file)
    output_format = get_format(output_file)

    if not input_format or not output_format:
        print("Obsługiwane formaty: .json, .yml/.yaml, .xml")
        sys.exit(1)

    if input_format == 'json':
        data = load_json(input_file)
    elif input_format == 'yaml':
        data = load_yaml(input_file)
    elif input_format == 'xml':
        data = load_xml(input_file)

    if output_format == 'json':
        save_json(output_file, data)
    elif output_format == 'yaml':
        save_yaml(output_file, data)
    elif output_format == 'xml':
        save_xml(output_file, data)

if __name__ == "__main__":
    main()
