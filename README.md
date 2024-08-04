# Stock Market Companion

## Video Demo: https://youtu.be/sAnoUtO7W2I?si=Ds4h0z7kbdjySq2K

This program's goal is to help users to collect stock market data in a more efficient way. It takes the ticker symbol of a company as an input, and provides data of that company's stock.

## Input Gathering

First, the program asks for a ticker symbol as an input. A ticker symbol is an abbreviation that represents traded stocks.
Because ticker symbols are not as well-known as the companies names, I added a link to a list of them whenever the ticker symbol that entered was wrong.

## Data Gathering and presenting

All the data gathering is based on Yahoo Finance data, and pragmatically, it's based on the yfinance library.

**The latest price of the company's stock.**

**The dividend of the stock**

The dividend yield: The amount that the company pays to investors each year relative to its stock price, expressed as a percentage.

The dividend rate: The amount that the company paid per share over a year. It shows the actual dollar amount investors receive per share annually.

**The yearly trend of the stock imaged in a plot.**

## Files Production

The program create 2 files that contains data about the stock. The goal of this is to maintain an accumulated and accessible information that's available for the program's users.
The 1st file is a csv file which contains the yearly history data about the stock. The 2nd file is an image that contains the stock's plot.

## Portfolio

After the presentation of the stock's data, a menu opens about the stocks portfolio. The choices in the menu offer to add the current stock that observed to the portfolio, or to view the portfolio etc. The portfolio is a dictionary that gets its data from a json file. That json file contains key-value pairs of the ticker and its current stock price.


## Error Handling

The yfinance library has its internal error handling. On the one hand this error outputs are the most precise. On the other hand, the problem with it is that the errors could be inarticulate. Thus, I used a hybrid approach, where I allow the internal error handling outputs, and also add mine as a complement.

## Testing

**Testing The Input Gathering**

 is made by a function called get_input(). I test this function by mock a valid input, and then ensures correct data retrieval.

**Testing The Data Gathering** 

is made by 2 functions: get_stock_history(parameter) & get_dividend(parameter). These functions is tested by checking a fine retrieval of data for a valid ticker symbol as a parameter, and ensures this data is not empty. 

**Testing The File Production** 

is made by a function called plot_and_csv(2 parameters). This function is tested by checking that retrieval data from the API works. Then a creation of a plot image through the matplotlib.pyplot library and a creation of a csv files are being made. After that the existence of these 2 files are being verified, and if they exist, then a deletion of them is being made.

