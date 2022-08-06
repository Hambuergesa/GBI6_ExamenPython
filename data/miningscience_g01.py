# NOMBRE: García, Lucía
def download_pubmed(palabra = "p"):
    """
    Docstring download_pubmed
    p; keyword →palabra clave para realizar la busqueda
    """
    from Bio import Entrez
    import re
    Entrez.email = "gualapuro.moises@gmail.com"
    handle = Entrez.esearch(db="pubmed",
                            term="%p[Title/Abstract]",
                            usehistory="y")
    record = Entrez.read(handle)
    # generate a Python list with all Pubmed IDs of articles about Dengue Network
    id_list = record["IdList"]
    record["Count"]
    print('El número artículos para', palabra, 'es:',record)
    #Utilizar Webenv  y el QueryKey para descargar la data
    webenv = record["WebEnv"]
    query_key = record["QueryKey"]
    #Aqui se descarga
    handle = Entrez.efetch(db="pubmed",
                           rettype="medline", 
                           retmode="text", 
                           retstart=0,
    retmax=543, webenv=webenv, query_key=query_key)
    nombre = palabra+".txt"
    out_handle = open(nombre, "w")
    data = handle.read() #cargar la informacion guardada den halndel
    handle.close()
    out_handle.write(data) #escribo esta data
    out_handle.close() #cierro esta data
    return data

def science_plots(archivo = 'a'):
    """
    a; nombre del archivo que se quiere graficar
    """
    import re
    import csv
    f = open(archivo)
    text = f.read()
    text = re.sub(r'\n\s{6}', ' ', text)
    zipcodes = re.findall(r'[A-Z]{2}\s(\d{5})', text)
    frecuenciaPalab = []
    for w in zipcodes:
        frecuenciaPalab.append(zipcodes.count(w))
    resul= frecuenciaPalab.sort()
    print(Counter('resul').most_common(5))
    return