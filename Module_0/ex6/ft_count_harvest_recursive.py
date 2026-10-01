def ft_count_harvest_recursive() -> None:
    days: int = int(input("Days until harvest: "))

    def helper(day: int) -> None:
        if day > days:
            return
        print(f"Day {day}")
        if day == days:
            print("Harvest time!")
        helper(day + 1)

    helper(1)
