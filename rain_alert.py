def heavy_rain(weather, day_index, limit=20):
    alerts = []

    for city in sorted(weather):
        mm = weather[city]["rain"][day_index]

        if mm >= limit:
            alerts.append((city, mm))

    return alerts


def show_rain_alerts(weather, days):
    print()
    print("RAIN ALERTS (20 mm or more)")

    for i, day in enumerate(days):
        alerts = heavy_rain(weather, i)

        if alerts:
            result = []
            for city, mm in alerts:
                result.append(f"{city} {mm} mm")

            print(f"{day}: {', '.join(result)}")

    print()
    print("RAIN ALERTS (10 mm or more)")

    for i, day in enumerate(days):
        alerts = heavy_rain(weather, i, limit=10)

        if alerts:
            result = []
            for city, mm in alerts:
                result.append(f"{city} {mm} mm")

            print(f"{day}: {', '.join(result)}")