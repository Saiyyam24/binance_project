from .client import get_client
from .login_config import setup_logger

logger = setup_logger()

def place_order(symbol, side, order_type, quantity, price=None):

    client = get_client()

    logger.info(f"Order Request: {symbol} {side} {order_type} {quantity} {price}")

    try:

        if order_type == "MARKET":

            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=quantity
            )

        elif order_type == "LIMIT":

            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                quantity=quantity,
                price=price,
                timeInForce="GTC"
            )

        logger.info(f"Order Response: {order}")

        return order

    except Exception as e:

        logger.error(f"Order Error: {str(e)}")
        raise