import http.client

class transactionClass:
    
    def __init__(self):
        # These inputs should be inside the method to prevent them from executing on class import
        self.Ticker = input("Enter the ticker (leave blank if not needed): ")
        self.representative = input("Enter the representative's name (leave blank if not needed): ")
        self.representative = self.representative.replace(" ", "+")
        
        self.conn = http.client.HTTPSConnection("api.quiverquant.com")
        self.headers = {
            'Accept': "application/json",
            'Authorization': "Bearer 8811e9c3ec80c57c79b915490ff666da60e3b888"
        }
        self.interval = 600
        self.PageSize = 10

        self.conn.request("GET", f"/beta/bulk/congresstrading?page=10&page_size=10&ticker={self.Ticker}&representative={self.representative}", headers=self.headers)

        self.res = self.conn.getresponse()
        self.data = self.res.read()

        print(self.data.decode("utf-8"))

# This ensures that input() is not called until an instance of the class is created
