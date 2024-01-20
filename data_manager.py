import requests
import pandas as pd
from datetime import datetime, timedelta
import pytz


class DataManager:
    URL_BTC = "https://api.zondacrypto.exchange/rest/trading/candle/history/BTC-PLN/300"
    URL_ETH = "https://api.zondacrypto.exchange/rest/trading/candle/history/ETH-PLN/300"
    URL_XRP = "https://api.zondacrypto.exchange/rest/trading/candle/history/XRP-PLN/300"
    URL_ALLEGRO = "https://www.gpw.pl/chart-json.php?req=[{\"isin\":\"LU2237380790\",\"mode\":\"CURR\",\"from\":\"473672\",\"to\":null}]&t="
    URL_AMBRA = "https://www.gpw.pl/chart-json.php?req=[{\"isin\":\"PLAMBRA00013\",\"mode\":\"CURR\",\"from\":\"473672\",\"to\":null}]&t="
    URL_ACAUTOGAZ = "https://www.gpw.pl/chart-json.php?req=[{\"isin\":\"PLACSA000014\",\"mode\":\"CURR\",\"from\":\"473672\",\"to\":null}]&t="
    URL_ZLOTO= "https://www.bankier.pl/new-charts/get-data?symbol=ZLOTO&intraday=true&today=true&type=area&init=true"
    URL_PALLAD= "https://www.bankier.pl/new-charts/get-data?symbol=PALLAD&intraday=true&today=true&type=area&init=true"
    URL_PLATYNA= "https://www.bankier.pl/new-charts/get-data?symbol=PLATYNA&intraday=true&today=true&type=area&init=true"


    def __init__(self):

        self.time_stamp_now = None
        self.time_stamp_24h_ago = None
        self.df_btc = None
        self.df_eth = None
        self.df_xrp = None
        self.df_allegro = None
        self.df_ambra = None
        self.df_acautogaz = None
        self.df_zloto = None
        self.df_pallad = None
        self.df_platyna = None
        self.update_data()

    def update_data(self):
        tz_poland = pytz.timezone('Europe/Warsaw')

        now = datetime.now(tz_poland)
        self.time_stamp_now = int(now.timestamp() * 1000)

        time_24h_ago = now - timedelta(hours=24)
        self.time_stamp_24h_ago = int(time_24h_ago.timestamp() * 1000)

        self.df_btc = self.send_request(self.URL_BTC)
        self.df_eth = self.send_request(self.URL_ETH)
        self.df_xrp = self.send_request(self.URL_XRP)
        self.df_allegro = self.send_request(self.URL_ALLEGRO)
        self.df_ambra = self.send_request(self.URL_AMBRA)
        self.df_acautogaz = self.send_request(self.URL_ACAUTOGAZ)
        self.df_zloto = self.send_request(self.URL_ZLOTO)
        self.df_pallad = self.send_request(self.URL_PALLAD)
        self.df_platyna = self.send_request(self.URL_PLATYNA)

    def send_request(self, url):
        if "gpw.pl" in url:
            response = requests.get(url,self.time_stamp_now)
            data = response.json()
            df = pd.DataFrame(data[0]['data'], columns=["t", "p", "o", "c", "l", "h", "v"])
            df["t"] = pd.to_datetime(df["t"], unit="s", origin="unix")

        elif "zondacrypto" in url:
            querystring = {"from": self.time_stamp_24h_ago, "to": self.time_stamp_now}
            response = requests.get(url, params=querystring)
            data = response.json()["items"]
            df = pd.DataFrame(data, columns=["timestamp", "candle"])
            df["timestamp"] = pd.to_datetime(pd.to_numeric(df["timestamp"]) + 3600000, unit="ms")
            df[["open", "close", "high", "low", "volume", "co"]] = pd.DataFrame(df["candle"].tolist(), index=df.index)
            df = df.drop(columns=["candle"])
        elif "bankier" in url:
            response = requests.get(url)
            data = response.json()
            df = pd.DataFrame(data["main"], columns=["timestamp", "value"])
            df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")
            df = df.rename(columns={"timestamp": "datetime", "value": "close"})
        return df
