def depositProfit(deposit, rate, threshold):
    year_count = 0
    while deposit < threshold:
        deposit = deposit + (deposit * (rate/100))
        year_count += 1
    return year_count