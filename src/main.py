import xml.etree.ElementTree as ET

def readXML(filename):
    tree = ET.parse(filename)
    return tree.getroot()


def main(filename):
    root = readXML(filename)
    print(root.tag)
    # if root.tag = ""
    # for child in root:
        # print(child[0].text)
 


main("../XML Sitemap.xml")