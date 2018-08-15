from Bio.Entrez import efetch
#This is just a skeleton. Expand and modify it later.
def print_abstract(pmid):
    handle = efetch(db='pubmed', id=pmid, retmode='text', rettype='abstract')
    print handle.read()