# Research guide service Flask

Flask implementation of a service that returns information about related research guides for a given catalogue reference. 

## Development machine configuration

### Initial setup

1. Ensure you have Python 3.7 and pip installed
2. Clone this repository
3. Create a virtual environment with `python3 -m venv venv`
4. From the root directory run `source venv/bin/activate` 
5. Install dependencies with `pip install -r requirements.txt`
6. Start the application with `flask run`
7. See the command line for the URL to visit
8. When finished run `deactivate` from the virtual environment

### Daily use

1. From the root directory run `source venv/bin/activate` 
2. Install dependencies with `pip install -r requirements.txt`
3. Start the application with `flask run`
4. See the command line for the URL to visit
5. When finished run `deactivate` from the virtual environment

### Running tests

Install Pytest (`pip install -U pytest`) and run `pytest -vv` from the project root (within an activated python environment)

### Viewing the documentation for modules

To see module documentation import the module and use the Python `help()` function. For example, `import get_guides` folloed by `help(get_guides)`

## Using the service

### In-browser endpoint playground

Visiting the root of the server (as shown when running Flask above) will present an explanatory HTML page and form that allow you to interact with each of the endpoints using a form. 

### Getting 'fragments' from a reference

Visiting `/fragments/<reference>` will return an object corresponding to the 'fragments' for a reference. These are 'reference', 'series' and 'lettercode'. For example: `http://localhost:5000/fragments/ADM%201/24558` returns

```json
{
  "letter_code": "ADM", 
  "reference": "ADM 1/24558", 
  "series": "ADM 1"
}
```
Of these, there will always be a `"reference"` and `"letter_code"` property. The `"series"` property will only be present if the pattern for a series was matched.

### Getting the research guides for a reference

Visiting `/guides/<reference>` will return an object representing research guides related to references, series and lettercodes derived from `<reference>`. For example, visiting `http://localhost:5000/guides/ADM%201/24558` returns 

```json
{
  "ADM": {
    "birth-marriage-death-armed-forces": "Births, marriages and deaths in the armed forces", 
    "british-army-operations-second-world-war": "British Army operations in the Second World War", 
    "british-transatlantic-slave-trade-records": "British transatlantic slave trade records", 
    "colonies-dependencies-further-research": "Colonies and dependencies from 1782", 
    "contaminated-land": "Contaminated land", 
    "first-world-war": "First World War", 
    "prisoners-of-war-british-hands": "Prisoners of war in British hands", 
    "research-development-british-army": "Research and development in the British Army", 
    "research-development-royal-navy": "Research and development in the Royal Navy", 
    "royal-air-force-operations": "Royal Air Force operations", 
    "royal-navy-operations-correspondence-1660-1914": "Royal Navy operations and correspondence 1660-1914", 
    "royal-navy-operations-policy-after-1945": "Royal Navy operations and policy after 1945", 
    "royal-navy-operations-second-world-war": "Royal Navy operations in the Second World War", 
    "royal-navy-ratings-pensions": "Royal Navy ratings' pensions 17th-20th centuries", 
    "second-world-war": "Second World War", 
    "wars-overview": "Wars: an overview"
  }, 
  "ADM 1": {
    "apprentices-and-masters": "Apprentices and masters", 
    "british-military-campaign-and-service-medals": "British military campaign and service medals", 
    "british-military-gallantry-medals": "British military gallantry medals", 
    "british-transatlantic-slave-trade-records": "British transatlantic slave trade records", 
    "civilian-gallantry-medals": "Civilian gallantry medals, honours and other awards", 
    "coastguard-officers": "Coastguard officers", 
    "coastguard-records": "Coastguard records", 
    "contaminated-land": "Contaminated land", 
    "high-court-admiralty-records": "High Court of Admiralty", 
    "jacobite-risings-1715-and-1745": "Jacobite Risings 1715 and 1745", 
    "merchant-seamen-medals-honours": "Merchant seamen's medals and honours", 
    "naval-correspondence-adm12-indexes-and-digests": "Naval correspondence using the ADM 12 indexes and digests", 
    "research-development-royal-navy": "Research and development in the Royal Navy", 
    "royal-air-force-operations": "Royal Air Force operations", 
    "royal-navy-commissioned-and-warrant-officers-further-research": "Royal Navy commissioned and warrant officers: further research", 
    "royal-navy-operations-correspondence-1660-1914": "Royal Navy operations and correspondence 1660-1914", 
    "royal-navy-operations-first-world-war": "Royal Navy operations in the First World War", 
    "royal-navy-operations-policy-after-1945": "Royal Navy operations and policy after 1945", 
    "royal-navy-operations-second-world-war": "Royal Navy operations in the Second World War", 
    "sea-charts": "Sea charts", 
    "ships-wrecked-sunk": "Ships wrecked or sunk"
  }, 
  "ADM 1/24558": {
    "royal-navy-operations-policy-after-1945": "Royal Navy operations and policy after 1945"
  }
}
```
### Getting the content of guides for a given reference 

Visiting `/guides_content/<reference>` will return an object that has content from all research guides related to a reference. For example, `http://localhost:5000/guides_content/PROB%2011` returns:

```json

{
  "PROB": "", 
  "PROB 11": {
    "wills-1384-1858": { 
      "bigrams": [
        [
          [
            "Prerogative", 
            "Court"
          ], 
          4
        ]
      ], 
      "guide_href": "http://www.nationalarchives.gov.uk/help-with-your-research/research-guides/wills-1384-1858/", 
      "id": "wills-1384-1858", 
      "name": "Wills 1384-1858", 
      "references": [
        "PROB11"
      ], 
      "summary": [
        "The wills of Susanna Smith and Jane Austen have been annotated to show the different parts of a will: 14th century: Thomas Kennardesle 2 December 1391\u00a0(PDF, 0.22MB) 15th century: William Marchy 27 January 1479\u00a0(PDF, 0.20MB) 16th century: John Yardley 2 July 1522\u00a0(PDF, 0.17MB) 17th century: Henry Purcell 7 December 1695\u00a0(PDF, 0.21MB) 18th century: Susanna Smith 19 July 1709\u00a0(PDF, 0.91MB) 19th century: Jane Austen 10 September 1817\u00a0(PDF, 0.72MB) The majority of the wills The majority of the wills are written in English.", 
        "Live chat For quick pointersTuesday to Saturday 09:00 to 17:00 &lt;div style=\"display:inline\"&gt;&lt;a href=\"http://www.providesupport.com?messenger=0or0ihkh4hylp1qnz87w7c01gr\"&gt;Live Help Desk&lt;/a&gt;&lt;/div&gt; Email For more detailed research enquiries.", 
        "Phone +44 (0) 20 8876 3444 Related research guides Country court death duty registers 1796-1811 Death duties 1796-1903 Famous wills 1552-1854 Wills and probate before 1858: further research Wills of Royal Navy and Royal Marines personnel 1786-1882 Wills or administrations after 1858 Wills or administrations before 1858 Search our catalogue Discovery is a catalogue of archival records across the UK and beyond, from which you can search 32 million records."
      ], 
      "trigrams": [
        [
          [
            "Prerogative", 
            "Court", 
            "Canterbury"
          ], 
          3
        ]
      ]
    }
  }
}

```

The fields within this object are obtained from `decorated_guides.json`, see below for more information.

### Decorated guides

The `decorated_guides.json` has been adapted from `decorated_guides.js` in `https://github.com/gtvj/department-visualisation`. 
