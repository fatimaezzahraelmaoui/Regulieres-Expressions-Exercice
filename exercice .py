import re

exemple = '''
P1 est un produit composé de P2 et P3
P2 est un produit élémentaire
P5 est un produit composé de P1 et P4
P4 est un produit élémentaire
P9 est un produit composé de P1, P6 et P4
P10 est un produit composé de P3 et P5
P11 est un produit composé de P5 et P3
'''

produits_elementaires = re.findall(r'P\d+ est un produit élémentaire', exemple)
print(produits_elementaires)

produits_composes_trois = re.findall(r'P\d+ est un produit composé de P\d+, P\d+ et P\d+', exemple)
print(produits_composes_trois)

produits_composes_P3_P5 = re.findall(r'P\d+ est un produit composé de P3 et P5', exemple)
print(produits_composes_P3_P5)

produits_sans_P2 = re.findall(r'P\d+ est un produit composé de ((?!P2).)*', exemple)
print(produits_sans_P2)

produits_de_P9 = re.findall(r'P9 est un produit composé de (P\d+)', exemple)
print(produits_de_P9)