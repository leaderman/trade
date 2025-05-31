import sys

from a_stock.config import (
    COMMISSION_RATE,
    LOT_SIZE,
    MIN_COMMISSION,
    STAMP_RATE,
    TRANSFER_RATE,
)


def calc_sell_profit(cost, quantity, price):
    # 买入金额
    buy_amount = cost * quantity
    # 卖出金额
    sell_amount = price * quantity

    # 佣金
    commission = max(sell_amount * COMMISSION_RATE, MIN_COMMISSION)
    # 过户费
    transfer = sell_amount * TRANSFER_RATE
    # 印花税
    stamp = sell_amount * STAMP_RATE
    # 收益
    profit = sell_amount - buy_amount - commission - transfer - stamp

    return buy_amount, sell_amount, commission, transfer, stamp, profit


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("参数: <成本价格> <股票数量> <卖出价格>")
        sys.exit(1)

    cost_price = float(sys.argv[1])

    quantity = int(sys.argv[2])
    if quantity % LOT_SIZE != 0:
        print(f"股票数量必须是 {LOT_SIZE} 的倍数")
        sys.exit(1)

    sell_price = float(sys.argv[3])

    buy_amount, sell_amount, commission, transfer, stamp, profit = calc_sell_profit(
        cost_price, quantity, sell_price
    )

    print(f"买入金额: {buy_amount} 元")
    print(f"卖出金额: {sell_amount} 元")
    print(f"佣金: {commission} 元")
    print(f"过户费: {transfer} 元")
    print(f"印花税: {stamp} 元")
    print(f"收益: {profit} 元")
