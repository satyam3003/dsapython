def stockBuySell(price, n):
    # code here
    all_stocks = []
    stock_arr = []
    for i in range(n - 1):
        if price[i] <= price[i + 1]:
            stock_arr.append(i)
            stock_arr.append(i + 1)

        else:
            if len(stock_arr) > 1:
                print("(" + str(min(stock_arr)) + " " + str(max(stock_arr)) + ")", end=" ")
                stock_arr.clear()

    if len(stock_arr) > 1:
        # all_stocks.append(f"{min(stock_arr)}, {max(stock_arr)}    " )
        print("(" + str(min(stock_arr)) + " " + str(max(stock_arr)) + ")")


n = int(input())
price = list(map(int, input().split()))
stockBuySell(price, n)
