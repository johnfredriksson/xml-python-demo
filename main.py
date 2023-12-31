import xml.etree.ElementTree as ElementTree

input_file = 'data/sma_gentext.xml'
output_file_name = 'data/output.txt'
target_id = '42007'
target_child = 'target'

DOM = ElementTree.parse(input_file)

for element in DOM.getroot().iter():
    try:
        if element.attrib['id'] == target_id:
            try:
                output_text = element.find(target_child).text
                with open(output_file_name, 'w') as output_file:
                    output_file.write(output_text)
                break
            except AttributeError:
                print(f"AttributeError: element '{element.tag}' has no child '{target_child}'")
    except KeyError:
        continue
