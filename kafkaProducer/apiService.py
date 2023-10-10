import requests
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
from utils import currentUnixTime, initLogger

LOGGER = initLogger("API_SERVICE_LOG")

class APIService:
    def getJson(self, url):
        try:
            headers = {
            'Content-Type': 'application/json',
            'x-access-token': 'your api key',
            }
            response = requests.get(url, headers=headers)
            statusCode = response.status_code
            assert statusCode == 200, f"Response status code is : {statusCode}"
            LOGGER.info("Recieved JSON response")
            return response.json()
        except(AssertionError,Timeout,TooManyRedirects) as e:
            LOGGER.error(f"Exception occured while requesting url: {e}")
            return {}
        
    def parseCoinData(self, coinData):
        try:
            return {"name_coin": coinData["name"],
                    "symbol_coin": coinData["symbol"],
                    "uuid": coinData["uuid"],
                    "volume": coinData["24hVolume"],
                    "market_cap": coinData["marketCap"],
                    "price": coinData["price"],
                    "percent_change_24hr": coinData["change"],
                    "timestamp": currentUnixTime()}
        except Exception as e:
            LOGGER.error(f"Exception occurred : {e}")
            return {}
        
    def filterJson(self, rawJson):
        filteredJson = map(lambda coinData: self.parseCoinData(coinData),
                           rawJson["data"]["coins"])
        LOGGER.info("Parsed JSON response")
        return filteredJson
            