import sys

from a_stock.config import COMMISSION_RATE, LOT_SIZE, MIN_COMMISSION, TRANSFER_FEE_RATE


def calc_buy_fees(price, quantity):
    amount = price * quantity
    commission = max(amount * COMMISSION_RATE, MIN_COMMISSION)
    transfer_fee = amount * TRANSFER_FEE_RATE
    total_fees = amount + commission + transfer_fee
    cost = total_fees / quantity

    return amount, commission, transfer_fee, total_fees, cost


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("脚本参数: <股票价格> <股票数量>")
        sys.exit(1)

    price = float(sys.argv[1])
    quantity = int(sys.argv[2])

    if quantity % LOT_SIZE != 0:
        print(f"股票数量必须是 {LOT_SIZE} 的倍数")
        sys.exit(1)

    amount, commission, transfer_fee, total_fees, cost = calc_buy_fees(price, quantity)

    print(f"成交金额: {amount} 元")
    print(f"佣金: {commission} 元")
    print(f"过户费: {transfer_fee} 元")
    print(f"费用合计: {total_fees} 元")
    print(f"每股成本: {cost} 元")
