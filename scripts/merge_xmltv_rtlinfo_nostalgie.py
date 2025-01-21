import xml.etree.ElementTree as ET

# Chargement des trois fichiers XML
tree1 = ET.parse('xml/rtlinfo_13h_19h.xml')
tree2 = ET.parse('xml/xmltv.xml')
tree3 = ET.parse('xml/radionostalgie.xml')

# Récupérer les racines des fichiers XML
root1 = tree1.getroot()
root2 = tree2.getroot()
root3 = tree3.getroot()

# Fusionner les racines dans un seul élément parent
root_merged = ET.Element("epg")  # Crée un nouveau parent pour la fusion

# Ajouter tous les éléments de chaque fichier dans la nouvelle racine
for elem in root1:
    root_merged.append(elem)

for elem in root2:
    root_merged.append(elem)

for elem in root3:
    root_merged.append(elem)

# Créer un nouvel arbre avec la racine fusionnée
tree_merged = ET.ElementTree(root_merged)

# Sauvegarder le fichier fusionné
tree_merged.write('xml/xmltv_rtlinfo_nostalgie.xml', encoding='utf-8', xml_declaration=True)

print("Les fichiers ont été fusionnés et sauvegardés sous 'xmltv_rtlinfo_nostalgie.xml'.")
