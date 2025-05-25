import xml.dom.minidom
import time
import xml.sax
 
start = time.time()

DOMTree = xml.dom.minidom.parse('C:/Users/Xutianrun/Desktop/IBI1_2024-25/Practical14/go_obo.xml')
collection = DOMTree.documentElement
terms = collection.getElementsByTagName("term")

max_is_a = {
    'biological_process': ([], 0),
    'molecular_function': ([], 0),
    'cellular_component': ([], 0)
}

for term in terms:
    namespace = term.getElementsByTagName("namespace")[0].firstChild.data 
    name = term.getElementsByTagName("name")[0].firstChild.data
    is_a = term.getElementsByTagName("is_a")
    count = len(is_a)
    
    if count > max_is_a[namespace][1]: 
        max_is_a[namespace] = ([name], count)
    elif count == max_is_a[namespace][1]:
        max_is_a[namespace][0].append(name)

def print_max_is_a(max_is_a):
    for namespace, (names, count) in max_is_a.items():
        print(f' {namespace}:')
        for name in names:
            print(f' - {name} with {count} is_a elements')

print('DOM parsing results')
print_max_is_a(max_is_a)

end = time.time()
print("DOM parsing time:", end - start, "seconds")


class GOHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.current_element = ""
        self.namespace = ""
        self.name = ""
        self.is_a_count = 0 

 
        self.max_is_a = {
            'biological_process': ([], 0),
            'molecular_function': ([], 0),
            'cellular_component': ([], 0)
        }

    def startElement(self, tag, attributes):
        self.current_element = tag  


        if tag == "term":
            self.namespace = "" 
            self.name = "" 
            self.is_a_count = 0  


    def endElement(self, tag):

        if tag == "term":
            if self.namespace in self.max_is_a:
                if self.is_a_count > self.max_is_a[self.namespace][1]:
        
                    self.max_is_a[self.namespace] = ([self.name], self.is_a_count)
               
            
                elif self.is_a_count == self.max_is_a[self.namespace][1]:
                    self.max_is_a[self.namespace][0].append(self.name)
        
        self.current_element = "" 

   
    def characters(self, content): 
        if self.current_element == "namespace":
            self.namespace += content.strip()

        elif self.current_element == "name":
            self.name += content.strip()
        elif self.current_element == "is_a":
            self.is_a_count += 1 


start = time.time()

parser = xml.sax.make_parser()
handler = GOHandler()
parser.setContentHandler(handler)

parser.parse('C:/Users/Xutianrun/Desktop/IBI1_2024-25/Practical14/go_obo.xml')

print('\nSAX parsing results')
print_max_is_a(handler.max_is_a)

end = time.time()  
print("SAX parsing time:", end - start, "seconds")

print('SAX is faster than DOM')
# SAX is faster than DOM for large files because it reads the file sequentially without loading the entire XML tree into memory. It uses less memory and is more efficient for big XML datasets.