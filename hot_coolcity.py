def city_averages(weather, clean, average):
    averages = {}

    for city in weather:
        temps = clean(weather[city]["temp"])
        averages[city] = average(temps)

    return averages


def extremes(averages):
    hottest = None
    coolest = None

    for city in averages:
        if hottest is None or averages[city] > averages[hottest]:
            hottest = city

        if coolest is None or averages[city] < averages[coolest]:
            coolest = city

    return hottest, coolest


def show_extremes(weather, clean, average):
    averages = city_averages(weather, clean, average)
    hottest, coolest = extremes(averages)

    print()
    print(f"Hottest city: {hottest} ({averages[hottest]:.1f})")
    print(f"Coolest city: {coolest} ({averages[coolest]:.1f})")