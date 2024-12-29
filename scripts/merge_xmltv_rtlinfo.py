import xml.etree.ElementTree as ET

# Charger les deux fichiers XML
tree1 = ET.parse('xml/rtlinfo_13h_19h.xml')
tree2 = ET.parse('xml/xmltv.xml')

# Récupérer les racines des deux arbres XML
root1 = tree1.getroot()
root2 = tree2.getroot()

# Supposons que les deux fichiers ont la même structure et que les programmes sont sous un élément <programme>
# Ajouter tous les éléments du second fichier au premier
for programme in root2.findall('programme'):
    root1.append(programme)

# Sauvegarder le fichier fusionné
tree1.write('xml/xmltv_rtlinfo.xml', encoding='UTF-8', xml_declaration=True)

print("Fusion des fichiers terminée, fichier 'xmltv_rtlinfo.xml' créé.")
