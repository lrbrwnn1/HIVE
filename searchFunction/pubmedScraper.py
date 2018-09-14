from Bio import Entrez

def search(query):
    Entrez.email = 'lrbrwnn1@memphis.edu'
    handle = Entrez.esearch(db='pubmed', 
                            sort='relevance', 
                            retmax='20',
                            retmode='xml', 
                            term=query)
    results = Entrez.read(handle)
    return results

def fetch_details(id_list):
    ids = ','.join(id_list)
    Entrez.email = 'lrbrwnn1@memphis.edu'
    handle = Entrez.efetch(db='pubmed',
                           retmode='xml',
                           id=ids)
    results = Entrez.read(handle)
    return results

if __name__ == '__main__':
    id_list = ['10028038','10081590']
    papers = fetch_details(id_list)
    for i, paper in enumerate(papers['PubmedArticle']): 
        print("%d) %s" % (i+1, paper['MedlineCitation']['Article']['ArticleTitle']))
        print(paper['MedlineCitation']['Article']['Abstract'])
        print(paper['MedlineCitation']['Article']['AuthorList'])
