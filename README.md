# corporate_bullshit_detector
Machine learning project designed to detecct yogababble in corporate mission statements of IPOs
Inspired by: https://www.youtube.com/watch?v=pqFnmhqReRM

### Stage 1 - Web Scraper - ipoScoop:
Web scrapes iposcoop.com for 2 things - stock ticker code and company description/mission statement

For earlier stock info, we look at waybackmachine archive
Still, a lot of company info has been deleted, assumedly because the company no longer exists

Todo:
Store the first day offer price and close stock information in a pandas dataframe file

Known Issues:
formatting of the website is irregular, so often the code will crash
otherwise, it will often target the wrong block of text, or return empty text *fixed*

### Stage 1.5 - Web Scraper - Yahoo Finance 

Web scrapes yahoo finance for previous stock history information


### Stage 2 - Download language prediction tool for wikipedia dataset

### Stage 3 - train/fine-tune using ULMFit
