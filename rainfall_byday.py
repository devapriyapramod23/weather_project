def rainfall_summary(weather, days):
    daily_rain = {}

    for i, day in enumerate(days):
        total = 0

        for city in weather:
            total += weather[city]["rain"][i]

        daily_rain[day] = total

    print()
    print("RAINFALL BY DAY")

    for day, total in daily_rain.items():
        print(f"{day:<5}{total:>4} mm")

    wettest = None

    for day in daily_rain:
        if wettest is None or daily_rain[day] > daily_rain[wettest]:
            wettest = day

    print(f"Wettest day: {wettest} ({daily_rain[wettest]} mm)")