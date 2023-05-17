import time

time.sleep(1)
print("Let's talk about stocks!")
time.sleep(1)

stocks_dict = {
  "AAPL": "$168.41",
  "GE": "$98.06",
  "BAC": "$28.89",
  "C": "$47.03",
  "AMZN": "$109.82",
  "TSLA": "$160.19",
  "SQQQ": "$29.56",
  "META": "$238.56",
  "TQQQ": "$27.69",
  "QQQ": "$320.35",
  "MSFT": "$304.83"
}

B = input("Please enter your desired stock symbol: ")
A = stocks_dict.get(B, "I'm sorry, that stock symbol was not found in this program. Please try again.")
                    
time.sleep(1)
                    
print (B + ":", A)