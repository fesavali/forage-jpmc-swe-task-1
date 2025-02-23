################################################################################
#
#  Permission is hereby granted, free of charge, to any person obtaining a
#  copy of this software and associated documentation files (the "Software"),
#  to deal in the Software without restriction, including without limitation
#  the rights to use, copy, modify, merge, publish, distribute, sublicense,
#  and/or sell copies of the Software, and to permit persons to whom the
#  Software is furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in
#  all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
#  OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#  FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
#  DEALINGS IN THE SOFTWARE.

import json
import random
import urllib.request

# Server API URLs
QUERY = "http://localhost:8080/query?id={}"

# 500 server requests
N = 500


def getDataPoint(quote):
    """ Produce all the needed values to generate a datapoint """
    stock = quote['stock']
    bid_price = float(quote['top_bid']['price'])
    ask_price = float(quote['top_ask']['price'])
    price = (bid_price + ask_price) / 2  # Calculate the average of bid and ask prices
    return stock, bid_price, ask_price, price


def getRatio(price_a, price_b):
    """ Get ratio of price_a and price_b """
    if price_b == 0:
        # Avoid division by zero
        return
    return price_a / price_b


# Main
if __name__ == "__main__":
    # Initialize variables to store stock prices
    stock_a_price = 0.0
    stock_b_price = 0.0

    # Query the price once every N seconds.
    for _ in range(N):
        quotes = json.loads(urllib.request.urlopen(QUERY.format(random.random())).read())

        # Update stock prices for two stocks
        for quote in quotes:
            stock, bid_price, ask_price, price = getDataPoint(quote)
            if stock == 'stockA':
                stock_a_price = price
            elif stock == 'stockB':
                stock_b_price = price

        # Calculate and print the ratio of stockA price to stockB price
        ratio = getRatio(stock_a_price, stock_b_price)
        print(f"StockA Price: {stock_a_price}, StockB Price: {stock_b_price}, Ratio: {ratio}")
