import json
import xmltodict
from deepdiff import DeepDiff
import csv

# Exemple de données XML
data = (
    'Purchase Transaction | GL', 
    [
        {
            'rSchemaID': 31,
            'Code': '0026',
            'Name': 'Purchase Transaction | GL',
            'Status': 1,
            'Key': 'PostPurchase',
            'ValidTo': None,
            'rSchemaParameterID': 72,
            'rSchemaCombinationID': 30,
            'CombinationXML': '<Combinations><xs:schema xmlns="" xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:msdata="urn:schemas-microsoft-com:xml-msdata" id="Combinations"><xs:element name="Combinations" msdata:IsDataSet="true" msdata:UseCurrentLocale="true"><xs:complexType><xs:choice minOccurs="0" maxOccurs="unbounded"><xs:element name="Combination"><xs:complexType><xs:sequence><xs:element name="LTGL_TransactionType" msdata:Caption="Purchase Transaction" type="xs:string" minOccurs="0"/><xs:element name="CombinationID" type="xs:string" minOccurs="0"/></xs:sequence></xs:complexType></xs:element><xs:element name="Decision"><xs:complexType><xs:sequence><xs:element name="DecisionID" type="xs:string" minOccurs="0"/><xs:element name="CombinationID" type="xs:string" minOccurs="0"/><xs:element name="Key" type="xs:string" minOccurs="0"/><xs:element name="Question" msdata:Caption="Parameter" type="xs:string" minOccurs="0"/><xs:element name="Answer" type="xs:string" minOccurs="0"/><xs:element name="AnswerValueID" type="xs:string" minOccurs="0"/></xs:sequence></xs:complexType></xs:element></xs:choice></xs:complexType><xs:unique name="Constraint1"><xs:selector xpath=".//Combination"/><xs:field xpath="CombinationID"/></xs:unique><xs:keyref name="Relation1" refer="Constraint1"><xs:selector xpath=".//Decision"/><xs:field xpath="CombinationID"/></xs:keyref></xs:element></xs:schema><Combination><LTGL_TransactionType>81</LTGL_TransactionType><CombinationID>1</CombinationID></Combination><Combination><LTGL_TransactionType>78</LTGL_TransactionType><CombinationID>2</CombinationID></Combination><Combination><LTGL_TransactionType>115</LTGL_TransactionType><CombinationID>3</CombinationID></Combination><Decision><DecisionID>1</DecisionID><CombinationID>1</CombinationID><Key>PT_DebitType_Purchase</Key><Question>Debit Type</Question><Answer>CourtExpense</Answer><AnswerValueID>5</AnswerValueID></Decision><Decision><DecisionID>2</DecisionID><CombinationID>1</CombinationID><Key>PT_Account_Purchase</Key><Question>Account</Question><Answer/><AnswerValueID/></Decision><Decision><DecisionID>3</DecisionID><CombinationID>1</CombinationID><Key>PT_DebitType_PurchaseVat</Key><Question>Debit Type Vat</Question><Answer>ExpenseVAT</Answer><AnswerValueID>12</AnswerValueID></Decision><Decision><DecisionID>4</DecisionID><CombinationID>1</CombinationID><Key>PT_TransactionTypeVAT</Key><Question>Transaction Type VAT</Question><Answer>ExpencesVAT</Answer><AnswerValueID>115</AnswerValueID></Decision><Decision><DecisionID>5</DecisionID><CombinationID>2</CombinationID><Key>PT_DebitType_Purchase</Key><Question>Debit Type</Question><Answer>OthenClientExpenses</Answer><AnswerValueID>8</AnswerValueID></Decision><Decision><DecisionID>6</DecisionID><CombinationID>2</CombinationID><Key>PT_Account_Purchase</Key><Question>Account</Question><Answer/><AnswerValueID/></Decision><Decision><DecisionID>7</DecisionID><CombinationID>2</CombinationID><Key>PT_DebitType_PurchaseVat</Key><Question>Debit Type Vat</Question><Answer>ExpenseVAT</Answer><AnswerValueID>12</AnswerValueID></Decision><Decision><DecisionID>8</DecisionID><CombinationID>2</CombinationID><Key>PT_TransactionTypeVAT</Key><Question>Transaction Type VAT</Question><Answer>ExpencesVAT</Answer><AnswerValueID>115</AnswerValueID></Decision><Decision><DecisionID>9</DecisionID><CombinationID>3</CombinationID><Key>PT_DebitType_Purchase</Key><Question>Debit Type</Question><Answer/><AnswerValueID/></Decision><Decision><DecisionID>10</DecisionID><CombinationID>3</CombinationID><Key>PT_Account_Purchase</Key><Question>Account</Question><Answer>610990003</Answer><AnswerValueID>424</AnswerValueID></Decision><Decision><DecisionID>11</DecisionID><CombinationID>3</CombinationID><Key>PT_DebitType_PurchaseVat</Key><Question>Debit Type Vat</Question><Answer/><AnswerValueID/></Decision><Decision><DecisionID>12</DecisionID><CombinationID>3</CombinationID><Key>PT_TransactionTypeVAT</Key><Question>Transaction Type VAT</Question><Answer/><AnswerValueID/></Decision></Combinations>',
            'rSchemaConditionID': 33,
            'ExecSQL': " Set DATEFORMAT DMY; Declare @String NVARCHAR(MAX);  Declare @xml XML; Declare @SourceKey int; Declare @SourceTable int;  SET @string =  N'<Parameters><Parameter><LTGL_TransactionType>@LTGL_TransactionType</LTGL_TransactionType></Parameter></Parameters>'; Set @xml = @String; Set @SourceKey=0; Set @SourceTable=0; EXEC dbo.clr_return_SchemaDecisionTree_v2_sp @rSchemaID = 31, @SchemaConditionDate = '25/10/2018', @rSchemaConditionID = 33, @xml = @xml, @SourceKey=@SourceKey, @SourceTable=@SourceTable;  "
        }
    ], 
    [
        {
            'rSchemaID': 31,
            'Code': '0026',
            'Name': 'Purchase Transaction | GL',
            'Status': 1,
            'Key': 'PostPurchase',
            'ValidTo': None,
            'rSchemaParameterID': 72,
            'rSchemaCombinationID': 30,
            'CombinationXML': '<Combinations><xs:schema xmlns="" xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:msdata="urn:schemas-microsoft-com:xml-msdata" id="Combinations"><xs:element name="Combinations" msdata:IsDataSet="true" msdata:UseCurrentLocale="true"><xs:complexType><xs:choice minOccurs="0" maxOccurs="unbounded"><xs:element name="Combination"><xs:complexType><xs:sequence><xs:element name="LTGL_TransactionType" msdata:Caption="Purchase Transaction" type="xs:string" minOccurs="0"/><xs:element name="CombinationID" type="xs:string" minOccurs="0"/></xs:sequence></xs:complexType></xs:element><xs:element name="Decision"><xs:complexType><xs:sequence><xs:element name="DecisionID" type="xs:string" minOccurs="0"/><xs:element name="CombinationID" type="xs:string" minOccurs="0"/><xs:element name="Key" type="xs:string" minOccurs="0"/><xs:element name="Question" msdata:Caption="Parameter" type="xs:string" minOccurs="0"/><xs:element name="Answer" type="xs:string" minOccurs="0"/><xs:element name="AnswerValueID" type="xs:string" minOccurs="0"/></xs:sequence></xs:complexType></xs:element></xs:choice></xs:complexType><xs:unique name="Constraint1"><xs:selector xpath=".//Combination"/><xs:field xpath="CombinationID"/></xs:unique><xs:keyref name="Relation1" refer="Constraint1"><xs:selector xpath=".//Decision"/><xs:field xpath="CombinationID"/></xs:keyref></xs:element></xs:schema><Combination><LTGL_TransactionType>81</LTGL_TransactionType><CombinationID>1</CombinationID></Combination><Combination><LTGL_TransactionType>78</LTGL_TransactionType><CombinationID>2</CombinationID></Combination><Combination><LTGL_TransactionType>115</LTGL_TransactionType><CombinationID>3</CombinationID></Combination><Decision><DecisionID>1</DecisionID><CombinationID>1</CombinationID><Key>PT_DebitType_Purchase</Key><Question>Debit Type</Question><Answer>OtherExpense</Answer><AnswerValueID>5</AnswerValueID></Decision><Decision><DecisionID>2</DecisionID><CombinationID>1</CombinationID><Key>PT_Account_Purchase</Key><Question>Account</Question><Answer/><AnswerValueID/></Decision><Decision><DecisionID>3</DecisionID><CombinationID>1</CombinationID><Key>PT_DebitType_PurchaseVat</Key><Question>Debit Type Vat</Question><Answer>ExpenseVAT</Answer><AnswerValueID>12</AnswerValueID></Decision><Decision><DecisionID>4</DecisionID><CombinationID>1</CombinationID><Key>PT_TransactionTypeVAT</Key><Question>Transaction Type VAT</Question><Answer>ExpensesVAT</Answer><AnswerValueID>115</AnswerValueID></Decision><Decision><DecisionID>5</DecisionID><CombinationID>2</CombinationID><Key>PT_DebitType_Purchase</Key><Question>Debit Type</Question><Answer>OtherClientExpenses</Answer><AnswerValueID>8</AnswerValueID></Decision><Decision><DecisionID>6</DecisionID><CombinationID>2</CombinationID><Key>PT_Account_Purchase</Key><Question>Account</Question><Answer/><AnswerValueID/></Decision><Decision><DecisionID>7</DecisionID><CombinationID>2</CombinationID><Key>PT_DebitType_PurchaseVat</Key><Question>Debit Type Vat</Question><Answer>ExpenseVAT</Answer><AnswerValueID>12</AnswerValueID></Decision><Decision><DecisionID>8</DecisionID><CombinationID>2</CombinationID><Key>PT_TransactionTypeVAT</Key><Question>Transaction Type VAT</Question><Answer>ExpensesVAT</Answer><AnswerValueID>115</AnswerValueID></Decision><Decision><DecisionID>9</DecisionID><CombinationID>3</CombinationID><Key>PT_DebitType_Purchase</Key><Question>Debit Type</Question><Answer/><AnswerValueID/></Decision><Decision><DecisionID>10</DecisionID><CombinationID>3</CombinationID><Key>PT_Account_Purchase</Key><Question>Account</Question><Answer>610990003</Answer><AnswerValueID>424</AnswerValueID></Decision><Decision><DecisionID>11</DecisionID><CombinationID>3</CombinationID><Key>PT_DebitType_PurchaseVat</Key><Question>Debit Type Vat</Question><Answer/><AnswerValueID/></Decision><Decision><DecisionID>12</DecisionID><CombinationID>3</CombinationID><Key>PT_TransactionTypeVAT</Key><Question>Transaction Type VAT</Question><Answer/><AnswerValueID/></Decision></Combinations>',
            'rSchemaConditionID': 33,
            'ExecSQL': " Set DATEFORMAT DMY; Declare @String NVARCHAR(MAX);  Declare @xml XML; Declare @SourceKey int; Declare @SourceTable int;  SET @string =  N'<Parameters><Parameter><LTGL_TransactionType>@LTGL_TransactionType</LTGL_TransactionType></Parameter></Parameters>'; Set @xml = @String; Set @SourceKey=0; Set @SourceTable=0; EXEC dbo.clr_return_SchemaDecisionTree_v2_sp @rSchemaID = 31, @SchemaConditionDate = '25/10/2018', @rSchemaConditionID = 33, @xml = @xml, @SourceKey=@SourceKey, @SourceTable=@SourceTable;  "
        }
    ]
)



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