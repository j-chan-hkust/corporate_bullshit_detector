# corporate_bullshit_detector
Machine learning project designed to detecct yogababble in corporate mission statements of IPOs
Inspired by: https://www.youtube.com/watch?v=pqFnmhqReRM

### Stage 1 - Web Scraper - ipoScoop:
Web scrapes iposcoop.com for 2 things - stock ticker code and company description/mission statement

Currently, company description is stored as a xxx.txt file, where xxx is the stock ticker

For earlier stock info, we look at waybackmachine archive
Still, a lot of company info has been deleted, assumedly because the company no longer exists

Todo:
Store the first day offer price and close stock information in a pandas dataframe file

Known Issues:
formatting of the website is irregular, so often the code will crash
otherwise, it will often target the wrong block of text, or return empty text *fixed*

### Stage 1.5 - Web Scraper - Yahoo Finance 

Web scrapes yahoo finance for previous stock history information

Todo:
Figure out how to collect the data on the stock return after 3, 6, 12 months

### Stage 2 - Download language prediction tool for wikipedia dataset

### Stage 3 - train/fine-tune using ULMFit
Using the tools provided by http://nlp.fast.ai/category/classification.html

Ideally the pandas dataframe will be formatted like this:
filename        day 1 % return      3 month % return    6 month % return    12 month % return
xxx.txt         1.1                 1.4                 1.9                 -0.5

the text stored in xxx.txt will be the x variable to be trained against
test using different times as y variable

