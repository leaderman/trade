import sys

from a_stock.config import COMMISSION_RATE, LOT_SIZE, MIN_COMMISSION, TRANSFER_RATE


def find_min_quantity(price):
    quantity = LOT_SIZE

    while True:
        amount = price * quantity

        commission = amount * COMMISSION_RATE
        if commission >= MIN_COMMISSION:
            return quantity

        quantity += LOT_SIZE


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("脚本参数: <股票价格>")
        sys.exit(1)

    price = float(sys.argv[1])
    quantity = find_min_quantity(price)

    print(f"股票数量: {quantity}")
