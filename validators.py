def validate_order_params(symbol, side, order_type, quantity, price):
    if not symbol.endswith("USDT"):
        raise ValueError("Only USDT-M Futures pairs supported (e.g., BTCUSDT).")

    if side not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL.")

    if order_type not in ["MARKET", "LIMIT"]:
        raise ValueError("Order type must be MARKET or LIMIT.")

    try:
        quantity = float(quantity)
    except ValueError:
        raise ValueError("Quantity must be a number.")

    if quantity <= 0:
        raise ValueError("Quantity must be greater than zero.")

    if order_type == "LIMIT":
        if price is None:
            raise ValueError("Price required for LIMIT order.")
        try:
            price = float(price)
        except ValueError:
            raise ValueError("Price must be numeric.")
        if price <= 0:
            raise ValueError("Price must be greater than zero.")

    return True
