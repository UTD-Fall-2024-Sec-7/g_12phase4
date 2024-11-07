import http.client
import time

# Initialize the connection
conn = http.client.HTTPSConnection("api.quiverquant.com")

# Set headers for the request
headers = {
    'Accept': "application/json",
    'Authorization': "Bearer 8811e9c3ec80c57c79b915490ff666da60e3b888"
}

# Get user input for the variables and handle empty input

interval = 600
PageSize = 10

Ticker = input("Enter the ticker (leave blank if not needed): ")
Date = input("Enter the date (in YYYY-MM-DD format, leave blank if not needed): ")
representative = input("Enter the representative's name (leave blank if not needed): ")


if representative:
    representative = representative.replace(" ", "+")

# Start the loop to make periodic requests
while True:

    query_params = f"normalized=true&page_size={PageSize}"
    if Ticker:
        query_params += f"&ticker={Ticker}"
    if Date:
        query_params += f"&date={Date}"
    if representative:
        query_params += f"&representative={representative}"
    
    
    conn.request("GET", f"/beta/bulk/congresstrading?{query_params}", headers=headers)
    
    
    res = conn.getresponse()
    data = res.read()
    
    
    print(data.decode("utf-8"))
    
    time.sleep(interval)