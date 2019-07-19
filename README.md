![](header.png)
# HIVE
> A research collaboration engine

Hive is a django-based webtool designed to help researchers collaborate and find suitable grants and clinical trials for their research.

Each researcher also has a dynamically generated profile, populated by our webscrapers, that gives users information about their research interests, publication history, and which grant/clinical trials/researchers are similar to them.

The search tool has two modes: basic keyword search and LSA-powered conceptual search. 



## Usage examples
Users can search for a term relevant to their research interests. 

The keyword search will return concrete results based on simple keyword lookup with respect to grant opportunities and researcher publications. Searching for reelin, for example, will return researchers whose publications frequently contain the word reelin, and grants/clinical trials containing the word reelin. 

The conceptual search uses latent semantic analysis to find conceptual similarities between publications and potential grants.
A search for reelin in this mode might return researchers, grants and clinical trials related to researching synaptic plasticity, even if their research does not explicitly mention reelin. This conceptual mapping allows users to discover previously hidden associations.

## Release History
* 1.0.0
    * Added affiliation tracking for researchers
    * Overhaul of keyword search
    * Keyword search lexeme ranking system
    * Significant performance increase on profile pages and LSI search
    * Rewrote pubscraper
    * Better error handling
    * UI tweaks
    * Bugfixes
* 0.2.0
    * Clinical trials
    * Migrated to PostgreSQL
    * Huge performance improvements (4x faster search times)
    * Different model for cosine calculation 
    * Replaced old tables with DataTables
    * Table sorting and pagination 
    * Database model changed to include more info and increase performance
* 0.1.2
    * Added separate tabs for researchers and grants to results page
    * Added publications tab in profiles - lists all available publications from that researcher
    * Author search results changed to table design - more compact and readable.
    * Navbar at top is now universal
    * Added MeSH headings and top co-authors graphs to profile pages  
* 0.1.1
    * Added publication scraper 
    * Basic grant scraper functionality complete
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



				
				
			
			

