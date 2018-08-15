import urllub.request

url = 'https://grants.nih.gov/funding/searchGuide/SS_Export.cfm?Activity_Code=&Expdate_On_After=&OrderOn=RelDate&OrderDirection=DESC&OpeningDate_On_After=&maxreldate=&Parent_FOA=All&NoticesToo=0&PrimaryICActive=Any&RelDate_On_After=&Status=1&SearchTerms=&PAsToo=1&RFAsToo=1&TitleText=&AppPackage=Any&Activity_Code_Groups=&Include_Sponsoring=1&SearchTermOperator=Logical_OR'
urllib.request.urlretrieve(url,'/srv/HIVE/searchFunction/static/')