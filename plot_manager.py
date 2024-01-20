import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd

class PlotManager:
    def create_crypto_chart(self, df_btc, df_eth, df_xrp):
        btc_trace = {
            'x': df_btc['timestamp'],
            'y': df_btc['close'],
            'name': 'BTC-PLN',
            'mode': 'lines+markers'
        }

        eth_trace = {
            'x': df_eth['timestamp'],
            'y': df_eth['close'],
            'name': 'ETH-PLN',
            'mode': 'lines+markers'
        }

        xrp_trace = {
            'x': df_xrp['timestamp'],
            'y': df_xrp['close'],
            'name': 'XRP-PLN',
            'mode': 'lines+markers'
        }

        figure_crypto = {
            'data': [btc_trace, eth_trace, xrp_trace],
            'layout': {
                'title': {
                    'text': 'Wykres Kryptowalut BTC, ETH i XRP',
                    'font': {'size': 40}
                },
                'xaxis': {
                    'title': 'Czas',
                    'titlefont': {'size': 30},
                    'tickfont': {'size': 16},
                    'dtick': 1000 * 60 * 60
                },
                'yaxis': {
                    'title': 'Wartość w PLN',
                    'titlefont': {'size': 30},
                    'tickfont': {'size': 20}
                },
                'legend': {
                    'font': {'size': 30},
                    'itemclick': 'toggleothers'
                },
                'height': 500,
            }
        }
        return figure_crypto

    def create_gpw_chart(self, df_allegro, df_ambra, df_acautogaz):
        allegro_trace = {
            'x': df_allegro['t'],
            'y': df_allegro['c'],
            'name': 'Allegro',
            'mode': 'lines+markers'
        }
        ambra_trace = {
            'x': df_ambra['t'],
            'y': df_ambra['c'],
            'name': 'Ambra',
            'mode': 'lines+markers'
        }
        acautogaz_trace = {
            'x': df_acautogaz['t'],
            'y': df_acautogaz['c'],
            'name': 'ACAUTOGAZ',
            'mode': 'lines+markers'
        }

        figure_gpw = {
            'data': [allegro_trace, ambra_trace, acautogaz_trace],
            'layout': {
                'title': {
                    'text': 'Wykres Akcji Allegro i Ambra',
                    'font': {'size': 40}
                },
                'xaxis': {
                    'title': 'Czas',
                    'titlefont': {'size': 30},
                    'tickfont': {'size': 16},
                    'dtick': 1000 * 60 * 60
                },
                'yaxis': {
                    'title': 'Wartość w PLN',
                    'titlefont': {'size': 30},
                    'tickfont': {'size': 20}
                },
                'legend': {
                    'font': {'size': 30},
                    'itemclick': 'toggleothers'
                },
                'height': 500,
            }
        }
        return figure_gpw

    def create_bankier_chart(self, df_zloto, df_pallad, df_platyna):
        zloto_trace = {
            'x': df_zloto['datetime'],
            'y': df_zloto['close'],
            'name': 'Złoto',
            'mode': 'lines+markers'
        }
        pallad_trace = {
            'x': df_pallad['datetime'],
            'y': df_pallad['close'],
            'name': 'Pallad',
            'mode': 'lines+markers'
        }
        platyna_trace = {
            'x': df_platyna['datetime'],
            'y': df_platyna['close'],
            'name': 'Platyna',
            'mode': 'lines+markers'
        }

        figure_bankier = {
            'data': [zloto_trace, pallad_trace, platyna_trace],
            'layout': {
                'title': {
                    'text': 'Wykres Złota, Palladu i Platyny',
                    'font': {'size': 40}
                },
                'xaxis': {
                    'title': 'Czas',
                    'titlefont': {'size': 30},
                    'tickfont': {'size': 16},
                    # 'dtick': 1000 * 60 * 60
                },
                'yaxis': {
                    'title': 'Wartość w PLN/Uncje',
                    'titlefont': {'size': 25},
                    'tickfont': {'size': 20}
                },
                'legend': {
                    'font': {'size': 30},
                    'itemclick': 'toggleothers'
                },
                'height': 500,
            }
        }
        return figure_bankier