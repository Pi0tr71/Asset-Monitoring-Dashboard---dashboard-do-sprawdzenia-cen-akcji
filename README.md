
# Asset Monitoring Dashboard

** Asset Monitoring Dashboard** is a real-time data dashboard for monitoring cryptocurrency and stock prices, along with precious metals prices. Built using Python, Dash, and several financial APIs, the dashboard fetches and displays updated asset prices, visualized for easy tracking.

![Dashboard Preview](images/dashboard.png)

## Features

- **Cryptocurrency Tracking:** Displays recent data for Bitcoin (BTC), Ethereum (ETH), and Ripple (XRP) in PLN.
- **Stock Prices:** Tracks Allegro, Ambra, and ACAUTOGAZ stock prices in real-time.
- **Precious Metals:** Monitors the values of Gold, Palladium, and Platinum.
- **Automatic Refresh:** Updates every hour to show current prices.

## Project Structure

- `main.py`: Initializes and runs the dashboard.
- `data_manager.py`: Contains the `DataManager` class, which retrieves and processes data from various APIs (Zonda Crypto, GPW, Bankier).
- `plot_manager.py`: Contains the `PlotManager` class for creating plots for cryptocurrencies, stocks, and metals.
- `dashboard.py`: Defines the layout and callback functions for real-time updates using Dash.

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/BreadcrumbsAsset-Monitoring-Dashboard.git
   cd BreadcrumbsAsset-Monitoring-Dashboard
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Dashboard:**
   ```bash
   python main.py
   ```

## Usage

Once started, the dashboard will be accessible at `http://127.0.0.1:8050` in a web browser. Charts for each asset class will refresh every hour.
