# robo-advisor

A solution for the "Robo Advisor" Project

Issue requests to the [AlphaVantage Stock Market API](https://www.alphavantage.co/) in order to provide automated stock trading information and recommendations.

# Prerequisites
    Anaconda 3.7
    Python 3.7
    Pip

# Installation and Setup
Download this repository (https://github.com/Mpugliese7/robo-advisor) onto your computer. Then navigate there from the command line. 

Create and activate a new Anaconda virtual environment named something like "stocks-env". 

Pip install the required packages specificed in the "requirements.txt" file that was downloaded from the repository.

Create a .env file and place your unique API key in the .env, making sure to note that there is a corresponding .gitignore file that prevents the .env file from being uploaded to github.

# Running the program
When prompted, enter a valid stock symbol (5 or less A-Z characters). If the entered stock symbol does not meet those criteria, the program will not run. 

In addition, if the stock symbol has an error when it attempts to pull the data from the site (e.g. "AMZX" instead of "AMZN" for Amazon) the program will return an error message. 

If the stock's most recent closing price is within 20% of its recent low, the program will recommend buying the stock. 

If the stock's most recent closing pricing is not within 20% of its recent low, the program will recommend not buying the stock.

The downloaded prices will be written to a csv, and will not be uploaded to github due to the instructions in the .gitignore file.


