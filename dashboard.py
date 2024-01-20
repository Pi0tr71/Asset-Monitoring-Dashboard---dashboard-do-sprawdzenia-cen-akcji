import dash
from dash import dcc, html
from dash.dependencies import Input, Output
from data_manager import DataManager
from plot_manager import PlotManager


class Dashboard:
    INTERVAL_INTERVAL = 60 * 60 * 1000 #update charts time in ms

    def __init__(self):
        self.data_manager = DataManager()
        self.plot_manager = PlotManager()

        app = dash.Dash(__name__)
        app.layout = html.Div([
            dcc.Graph(id='crypto-chart'),
            dcc.Graph(id='gpw-chart'),
            dcc.Graph(id='bankier-chart'),
            dcc.Interval(id='interval-component', interval=self.INTERVAL_INTERVAL)
        ])

        app.callback(
            [Output('crypto-chart', 'figure'),
             Output('gpw-chart', 'figure'),
             Output('bankier-chart', 'figure')],
            [Input('crypto-chart', 'relayoutData'),
             Input('interval-component', 'n_intervals')]
        )(self.update_charts)
        app.run_server(debug=True)

    def update_charts(self, relayout_data, n_intervals):
        self.data_manager.update_data()
        figure_crypto = self.plot_manager.create_crypto_chart(self.data_manager.df_btc, self.data_manager.df_eth, self.data_manager.df_xrp)
        figure_gpw = self.plot_manager.create_gpw_chart(self.data_manager.df_allegro, self.data_manager.df_ambra, self.data_manager.df_acautogaz)
        figure_bankier = self.plot_manager.create_bankier_chart(self.data_manager.df_zloto, self.data_manager.df_pallad, self.data_manager.df_platyna)
        return figure_crypto, figure_gpw, figure_bankier
