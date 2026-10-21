def moving_average(values, window=3):
    result = []
    for i in range(len(values) - window + 1):
        avg = sum(values[i:i+window]) / window
        result.append(round(avg, 1))
    return result


def show_moving_average(weather, days):
    kochi_avg = moving_average(weather["Kochi"]["temp"])

    print()
    print("KOCHI 3-DAY MOVING AVERAGE")

    for i in range(len(kochi_avg)):
        day = days[i + 2]
        print(f"{day:<5}{kochi_avg[i]:>5.1f}")