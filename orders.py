from binance.exceptions import BinanceAPIException, BinanceOrderException
import requests
from logging_config import setup_logger

logger = setup_logger()

def place_futures_order(client, symbol, side, order_type, quantity, price=None):
    params = {
        "symbol": symbol,
        "side": side,
        "type": order_type,
        "quantity": quantity
    }

    if order_type == "LIMIT":
        params["price"] = price
        params["timeInForce"] = "GTC"

    try:
        logger.info(f"SENT: {params}")

        response = client.futures_create_order(**params)

        logger.info(f"RECEIVED: {response}")

        print("\nOrder Successful!")
        print(f"Order ID: {response['orderId']}")
        print(f"Status: {response['status']}")
        print(f"Avg Price: {response.get('avgPrice', 'N/A')}")

        return response

    except BinanceAPIException as e:
        logger.error(f"Binance API Error: {e.message}")
        print(f"API Error: {e.message}")

    except BinanceOrderException as e:
        logger.error(f"Order Error: {str(e)}")
        print(f"Order Error: {str(e)}")

    except requests.exceptions.ConnectionError:
        logger.error("Network connection error")
        print("Network error. Check internet connection.")

    except Exception as e:
        logger.error(f"Unexpected Error: {str(e)}")
        print(f"Unexpected Error: {str(e)}")

    return None
