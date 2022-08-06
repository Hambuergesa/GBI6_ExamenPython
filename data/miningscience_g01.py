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

def science_plots(pais = 'p'):
    """Funcion para mapear la cantidad de articulos escritos en un determinado lugar, 
    sobre los datos obtenidos en la funcion download_pubmed"""
    data = pais+".txt"
    import re
    with open(data) as f:
        text = f.read()
        pais = input('Introduce el nombre del país')
        print('El país', 'p', 'se encuentra', len('p'), 'veces'.format(word, "" if re.search(word, text, re.IGNORECASE) else " no"))
    return