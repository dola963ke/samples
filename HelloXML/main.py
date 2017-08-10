from xml.etree.ElementTree import *

if __name__ == '__main__':
    tree = parse("edit_sample.xml")
    root = tree.getroot()
    print("View all elements, attribute and index:")
    for r in root.getiterator():
        print(">element:", end="")
        print(r.tag)
        print(">>attribute:", end="")
        print(r.attrib)
        print(">>>index:", end="")
        print(r.text)
    print("\nView found elements, attributes and index:")
    for r in root.findall(".//*[@id]"):
        print(">element:", end="")
        print(r.tag)
        print(">>attribute:", end="")
        print(r.attrib)
        print(">>>index:", end="")
        print(r.text)
    print("\nView edit elements, attribute and index:")
    for r in root.findall(".//*[@id]"):
        new_id = float(r.attrib.get("id")) + 1.0
        r.set("id", str(new_id))
        print(">element:", end="")
        print(r.tag)
        print(">>attribute:", end="")
        print(r.attrib)
        print(">>>index:", end="")
        print(r.text)
    tree.write("edit_sample.xml")