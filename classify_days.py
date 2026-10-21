def day_type(temp, hot=35, warm=28):
    if temp >= hot:
        return "Hot"
    elif temp >= warm:
        return "Warm"
    else:
        return "Cool"


def classify_days(weather, clean):
    print()
    print("DAY TYPES")
    print("-" * 30)
    print(f"{'City':<10}{'Hot':>5}{'Warm':>6}{'Cool':>6}")

    for city in sorted(weather):
        temps = clean(weather[city]["temp"])
        counts = {}

        for temp in temps:
            label = day_type(temp)
            counts[label] = counts.get(label, 0) + 1

        print(f"{city:<10}{counts.get('Hot', 0):>5}{counts.get('Warm', 0):>6}{counts.get('Cool', 0):>6}")