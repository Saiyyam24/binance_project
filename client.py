import argparse
from bot.orders import place_order
from bot.validators import *

def print_order_summary(symbol, side, order_type, quantity, price):

    print("\nOrder Request Summary")
    print("----------------------")
    print("Symbol:", symbol)
    print("Side:", side)
    print("Order Type:", order_type)
    print("Quantity:", quantity)

    if order_type == "LIMIT":
        print("Price:", price)
    else:
        print("Price: Market Price")


def print_order_response(order):

    print("\nOrder Response")
    print("----------------------")
    print("Order ID:", order.get("orderId"))
    print("Status:", order.get("status"))
    print("Executed Qty:", order.get("executedQty"))
    print("Avg Price:", order.get("avgPrice"))

    print("\nOrder placed successfully")


def main():

    parser = argparse.ArgumentParser(description="Binance Futures Trading Bot")

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", required=True)
    parser.add_argument("--price")

    args = parser.parse_args()

    try:

        symbol = args.symbol.upper()
        side = validate_side(args.side)
        order_type = validate_order_type(args.type)
        quantity = validate_quantity(args.quantity)
        price = args.price

        print_order_summary(symbol, side, order_type, quantity, price)

        order = place_order(symbol, side, order_type, quantity, price)

        print_order_response(order)

    except Exception as e:

        print("\nOrder failed:", str(e))


if __name__ == "__main__":
    main()