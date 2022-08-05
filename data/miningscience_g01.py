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
    print(record)
    #Utilizar Webenv  y el QueryKey para descargar la data
    webenv = record["WebEnv"]
    query_key = record["QueryKey"]
    #Aqui se descarga
    handle = Entrez.efetch(db="pubmed",
                           rettype="medline", 
                           retmode="text", 
                           retstart=0,
    retmax=543, webenv=webenv, query_key=query_key)
    print(handle)
    nombre = palabra+".txt"
    out_handle = open(nombre, "w")
    data = handle.read() #cargar la informacion guardada den halndel
    handle.close()
    out_handle.write(data) #escribo esta data
    out_handle.close() #cierro esta data
    return 



def mapscience(pais= "nombre" ):
    """
    Docstring map_science
    nombre; pais → nombre del pais del numero de autores 
    
    """
    import matplotlib.pyplot as plt
    
    paises = ['USA','Rusia', 'China']
    valores = [(conut,46,88,55]
    colores = ['cyan','green','coral','yellow']
    
    plt.pie(x=valores, labels=etiquetas, colors = colores, autopct='%1.2f%%')
    
    plt.title('Porcentajes de coches')
    
    plt.show()

    
    
    return 

    