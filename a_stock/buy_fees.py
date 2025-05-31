import sys

from a_stock.config import COMMISSION_RATE, LOT_SIZE, MIN_COMMISSION, TRANSFER_RATE


def calc_buy_fees(price, quantity):
    amount = price * quantity
    commission = max(amount * COMMISSION_RATE, MIN_COMMISSION)
    transfer = amount * TRANSFER_RATE
    total = amount + commission + transfer
    cost = total / quantity

    return amount, commission, transfer, total, cost


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("脚本参数: <买入价格> <股票数量>")
        sys.exit(1)

    price = float(sys.argv[1])
    quantity = int(sys.argv[2])

    if quantity % LOT_SIZE != 0:
        print(f"股票数量必须是 {LOT_SIZE} 的倍数")
        sys.exit(1)

    amount, commission, transfer, total, cost = calc_buy_fees(price, quantity)

    print(f"成交金额: {amount} 元")
    print(f"佣金: {commission} 元")
    print(f"过户费: {transfer} 元")
    print(f"费用合计: {total} 元")
    print(f"每股成本: {cost} 元")
