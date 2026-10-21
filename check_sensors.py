def clean(values):
    new_list = []
    for v in values:
        if v >= -50:
            new_list.append(v)
    return new_list


def sensor_check(weather):
    print("SENSOR CHECK")
    print("-" * 30)

    for city in sorted(weather):
        invalid = 0
        for v in weather[city]["temp"]:
            if v < -50:
                invalid += 1

        print(f"{city:<10}{invalid} invalid reading(s)")