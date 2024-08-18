from dhanhq import marketfeed
import time
# Add your Dhan Client ID and Access Token
client_id = "1100713286"
access_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpc3MiOiJkaGFuIiwicGFydG5lcklkIjoiIiwiZXhwIjoxNzI2NTk3NTI4LCJ0b2tlbkNvbnN1bWVyVHlwZSI6IlNFTEYiLCJ3ZWJob29rVXJsIjoiIiwiZGhhbkNsaWVudElkIjoiMTEwMDcxMzI4NiJ9.YdwfNfZykMwPendNccC8TUdN7sN92eB_D21_hEkyhwIduacU8d4PJUB5lCaHshDPihcFKJJk37fcB3K2Fg-kbg"

# Structure for subscribing is ("exchange_segment","security_id")

# Maximum 100 instruments can be subscribed, then use 'subscribe_symbols' function 

instruments = [(1, "1333")]

# Type of data subscription
subscription_code = marketfeed.Quote

# Ticker - Ticker Data
# Quote - Quote Data
# Depth - Market Depth



# using calendar module
# using time module
import calendar;
import time;
 

timestamp_int = 0

async def on_connect(instance):
    print("Connected to websocket")
    timestamp_int = 1

async def on_message(instance, message):
    print("Received:", "Security_ID:", message['security_id'],"Volume:", message['volume'], "LTP:", message['LTP'])
        
print("Subscription code :", subscription_code)

feed = marketfeed.DhanFeed(client_id,
    access_token,
    instruments,
    subscription_code,
    on_connect=on_connect,
    on_message=on_message)

feed.run_forever()