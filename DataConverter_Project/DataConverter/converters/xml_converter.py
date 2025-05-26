import xml.etree.ElementTree as ET

def load_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    return {root.tag: _xml_to_dict(root)}

def _xml_to_dict(element):
    return {
        child.tag: _xml_to_dict(child) if list(child) else child.text
        for child in element
    }

def save_xml(file_path, data):
    def _dict_to_xml(tag, value):
        element = ET.Element(tag)
        if isinstance(value, dict):
            for k, v in value.items():
                element.append(_dict_to_xml(k, v))
        else:
            element.text = str(value)
        return element

    [root_key] = data.keys()
    root = _dict_to_xml(root_key, data[root_key])
    tree = ET.ElementTree(root)
    tree.write(file_path, encoding="utf-8", xml_declaration=True)
