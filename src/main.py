import xml.etree.ElementTree as ET
import re
import urllib.request
import pprint

def analyzeSitemap(root):
    
    sitemaps = list()
    
    # remove xml namespace
    rootTag = re.sub(r'{.+}',"",root.tag)
    
    # initial file
    if rootTag == "sitemapindex":
        for child in root:
            sitemapURL = child[0].text
            response = urllib.request.urlopen(sitemapURL)
            sitemap = response.read().decode()
            sitemapRoot = ET.fromstring(sitemap)
            sitemaps.append(analyzeSitemap(sitemapRoot))
    # sitemap child file 
    elif rootTag == "urlset":
        for child in root:
            sitemaps.append(child[0].text)
            # print(child[0].text)
    return sitemaps

# readSItemapIndex
def main(filename):
    sitemapIndexTree = ET.parse(filename)
    root = sitemapIndexTree.getroot()
    urls =analyzeSitemap(root)
    pprint.pprint(urls)


main("../XML Sitemap.xml")
