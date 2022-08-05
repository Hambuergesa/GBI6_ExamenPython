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
from pylab import *

    n = 20
    X = np.ones(n)
    X[-1] *= 2
    pie(X, explode=X*.05, colors = ['%f' % (i/float(n)) for i in range(n)])

    fig = gcf()
    w,h = fig.get_figwidth(), fig.get_figheight()
    r = h/float(w)

    xlim(-1.5,1.5)
    ylim(-1.5*r,1.5*r)
    xticks([]), plt.yticks([])

    plt.text(-0.05, 1.05, " Pie Chart \n\n",
              horizontalalignment='left',
              verticalalignment='top',
              family='Lint McCree Intl BB',
              size='x-large',
              bbox=dict(facecolor='white', alpha=1.0, width=350,height=60),
              transform = gca().transAxes)

    plt.text(-0.05, .975, " Make a pie chart of an array ",
              horizontalalignment='left',
              verticalalignment='top',
              family='Lint McCree Intl BB',
              size='medium',
              transform = gca().transAxes)

    plt.show()
    countri=pais+".jpg"
    fig.savefig(countri, dpi=64)
    return 

    