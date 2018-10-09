![](header.png)
# HIVE
> A research collaboration engine

Hive is a django-based webtool designed to help researchers collaborate and find suitable grants for their research. The search tool has two modes: basic keywork search and LSA-powered conceptual search. 



## Usage examples
Users can search for a term relevant to their research interests. 

The keyword search will return concrete results based on simple keyword lookup with respect to grant opportunities and researcher publications. Searching for reelin, for example, will return researchers whose publications frequently contain the word reelin, and grants containing the word reelin. 

The conceptual search uses latent semantic analysis to find conceptual similarities between publications and potential grants.
A search for reelin in this mode might return researchers and grants related to researching synaptic plasticity, even if their research does not explicitly mention reelin. 

## Release History
* 0.1.2
    * Added separate tabs for researchers and grants to results page
    * Added publications tab in profiles - lists all available publications from that researcher
    * Author search results changed to table design - more compact and readable.
    * Navbar at top is now universal
    * Added graphs to profile pages:	
    	* MeSH Heading graph
	* Top Co-Authors
* 0.1.1
    * Added publication scraper 
    * Basic grant scraper functionality complete
    * In progress:
    	* Overhaul of LSA results page - grants and researchers will be separated by tabs
	* New profile pages UI for scraped publications
	* Graph visualizations of MESH headings, publication history and more
	* Further database optimizations
* 0.1.0
    * Code cleanup
    * Revised entire database - simplified and combined several tables, added more information to grant and publication tables
    * Added new researcher and grant information on profile pages
    * Added new "publications" tab in profiles
    * Second pass on LSA db query optimization : roughly 30% increase in speed
    * Temporarily removed keyword search until search bar overhaul is completed
* 0.0.5
    * View-caching 
    * Database query optimizations
* 0.0.4
    * Implemented basic profile pages
* 0.0.3
    * Major UI overhaul
    * New logo!
* 0.0.2
    * LSA search Functionality
* 0.0.1
    * Initialized Project
    * Basic UI 
    * Keyword Search Functionality



## Contributing

1. Fork it (<https://github.com/lrbrwnn1/HIVE/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

<!-- Markdown link & img dfn's -->
[npm-image]: https://img.shields.io/npm/v/datadog-metrics.svg?style=flat-square
[npm-url]: https://npmjs.org/package/datadog-metrics
[npm-downloads]: https://img.shields.io/npm/dm/datadog-metrics.svg?style=flat-square
[travis-image]: https://img.shields.io/travis/dbader/node-datadog-metrics/master.svg?style=flat-square
[travis-url]: https://travis-ci.org/dbader/node-datadog-metrics



				
				
			
			

