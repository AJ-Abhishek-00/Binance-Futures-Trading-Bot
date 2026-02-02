import argparse
from client import get_authenticated_client
from orders import place_futures_order
from validators import validate_order_params

def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Binance Futures Testnet Trading Bot"
    )

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True, choices=["BUY", "SELL"])
    parser.add_argument("--type", required=True, choices=["MARKET", "LIMIT"])
    parser.add_argument("--quantity", required=True)
    parser.add_argument("--price")

    return parser.parse_args()

def main():
    args = parse_arguments()

    try:
        validate_order_params(
            args.symbol,
            args.side,
            args.type,
            args.quantity,
            args.price
        )
    except ValueError as e:
        print(f"Validation Error: {e}")
        return

    client = get_authenticated_client()

    place_futures_order(
        client,
        symbol=args.symbol,
        side=args.side,
        order_type=args.type,
        quantity=args.quantity,
        price=args.price
    )

if __name__ == "__main__":
    main()
