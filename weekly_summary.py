def clean(values):
    new_list = []
    for v in values:
        if v >= -50:
            new_list.append(v)
    return new_list


def average(values):
    return sum(values) / len(values)


def weekly_summary(weather):
    print()
    print("WEEKLY SUMMARY")
    print("-" * 55)
    print(f"{'City':<10}{'Average':>7}{'Highest':>6}{'Lowest':>6}{'Rain':>7}{'Rainy days':>7}")

    for city in sorted(weather):
        temps = clean(weather[city]["temp"])
        rain = weather[city]["rain"]

        avg = average(temps)
        highest = max(temps)
        lowest = min(temps)
        total_rain = sum(rain)

        rainy_days = 0
        for r in rain:
            if r > 0:
                rainy_days += 1

        print(f"{city:<10}{avg:>7.1f}{highest:>6}{lowest:>6}{total_rain:>7}{rainy_days:>7}")