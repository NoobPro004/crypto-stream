import requests
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
from utils import currentUnixTime, initLogger

LOGGER = initLogger("API_SERVICE_LOG")
{"uuid":"Qwsogvtv82FCd",
 "symbol":"BTC",
 "name":"Bitcoin",
 "color":"#f7931A",
 "iconUrl":"https://cdn.coinranking.com/bOabBYkcX/bitcoin_btc.svg",
 "marketCap":"543071793188","price":"27838.92411746476",
 "listedAt":1330214400,
 "tier":1,
 "change":"0.37",
 "rank":1,
 "sparkline":["27895.27669795256","27834.4625805458","27947.294951974578","27963.4389447624","27961.874899883267","27953.616444621082","27932.753588294512","27899.840737431","27892.789010970093","27944.57311513265","27941.16022522297","27801.6252746692","27706.2110542664","27738.78348958291","27898.03796892998","27979.40651020021","27966.001817381133","27948.970010340596","27946.066819372776","27922.12680540561","27913.839626486173","27872.64828485805","27775.723557359208","27779.020959753358"],
 "lowVolume":false,
 "coinrankingUrl":"https://coinranking.com/coin/Qwsogvtv82FCd+bitcoin-btc",
 "24hVolume":"10739707086",
 "btcPrice":"1"
 }


class APIService:
    def getJson(self, url):
        try:
            response = requests.get(url)
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
                    "id": coinData["id"],
                    "uuid": coinData["uuid"],
                    "number_of_markets": coinData["numberOfMarkets"],
                    "volume": coinData["volume"],
                    "market_cap": coinData["marketCap"],
                    "total_supply": coinData["totalSupply"],
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
            