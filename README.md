# Stock Sentiment Analysis
#### Supports socks listed in the DOW30 and NASDAQ100 indices

### CircleCI Automated Builds
CircleCI Github integration allows this project to be built every 24 hours hours at midnight to update the sentiment database and plots

### Fetching Data
Uses Twitter Developer API to fetch up to 100 tweets that match a stock. Uses NewsAPI.org to fetch all articles published in the past 24 hours that match a stock.


### Sentiment Analysis
Each body of text is analyzed independently using Natural Language Processing. Sentiment analyisis techniques evaluate a body of text and assign a polarity rating [-1,1]: -1 = very negative, 0 = neutral, 1 = very positive. Each rating for a stock is summed and the total is divided by the number of results to calculate an average polarity rating for that day. The data for each stock is stored in an SQL database in the corresponding index's table with the respective date of insertion.

### Plots (matplotlib.pyplot)
Each stock's historical data is represented by a graph with two subplots, average polarity rating vs time and number of results vs time. Each plot is updated every time the SQL database is updated
