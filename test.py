import json
import xmltodict
from deepdiff import DeepDiff
import csv

# Exemple de données XML
data = ()


def copy_structure_only(xml_content):
    data_dict = xmltodict.parse(xml_content)

    def copy_structure(node):
        if isinstance(node, dict):
            return {k: copy_structure(v) for k, v in node.items() if k not in ['#text', '@']}
        elif isinstance(node, list):
            return [copy_structure(item) for item in node]
        else:
            return None

    structure_dict = copy_structure(data_dict)

    def clean_structure(d):
        if isinstance(d, dict):
            return {k: clean_structure(v) for k, v in d.items() if v is not None}
        elif isinstance(d, list):
            return [clean_structure(item) for item in d if item is not None]
        return d
    
    clean_structure_dict = clean_structure(structure_dict)

    structure_xml = xmltodict.unparse(clean_structure_dict, pretty=True)
    
    return structure_xml


xml_v3 = data[1][0]['CombinationXML']
xml_v4 = copy_structure_only(xml_v3)
# xml_v4 =  data[2][0]['CombinationXML']
# Convertir les XML en dictionnaires Python
dict1 = xmltodict.parse(xml_v3)
dict2 = xmltodict.parse(xml_v4)

# Comparer les dictionnaires
diff = DeepDiff( dict1, dict2)

print(diff)
diff_data = []
# Préparer les données pour le CSV
def format_path(path):
    """
    Format the path for better readability
    """
    path = path.replace("root", "").strip("['']").replace("']['", " -> ")
    return path

def format_value(value):
    """
    Format the value for better readability
    """
    if isinstance(value, dict):
        return json.dumps(value, ensure_ascii=False, indent=2)
    if value is None:
        return ''
    return str(value)

# Gestion des valeurs modifiées
if 'values_changed' in diff:
    for path, change in diff['values_changed'].items():
        diff_data.append({
            'Path': format_path(path),
            'Change Type': 'Value Changed',
            'Old Value': format_value(change.get('old_value', '')),
            'New Value': format_value(change.get('new_value', ''))
        })


# Gestion des changements de type
if 'type_changes' in diff:
    for path, change in diff['type_changes'].items():
        diff_data.append({
            'Path': format_path(path),
            'Change Type': 'Type Changed',
            'Old Value': format_value(change.get('old_value', '')),
            'New Value': format_value(change.get('new_value', ''))
        })



csv_file_path = 'differences.csv'
with open(csv_file_path, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=['Path', 'Change Type', 'Old Value', 'New Value'])
    writer.writeheader()
    for row in diff_data:
        writer.writerow(row)

print(f"Differences exported to {csv_file_path}")