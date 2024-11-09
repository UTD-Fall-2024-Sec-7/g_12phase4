import http.client

class transactionClass:
    conn = http.client.HTTPSConnection("api.quiverquant.com")

    headers = {
        'Accept': "application/json",
        'Authorization': "Bearer 8811e9c3ec80c57c79b915490ff666da60e3b888"
    }
    interval = 600
    PageSize = 10
    Ticker = input("Enter the ticker (leave blank if not needed): ")
    representative = input("Enter the representative's name (leave blank if not needed): ")
    representative = representative.replace(" ", "+")


    conn.request("GET", f"/beta/bulk/congresstrading?page=10&page_size=10&ticker={Ticker}&representative={representative}", headers=headers)

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))
