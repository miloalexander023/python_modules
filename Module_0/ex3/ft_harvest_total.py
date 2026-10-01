def ft_harvest_total() -> None:
    day1: int = int(input("day 1 harvest:"))
    day2: int = int(input("day 2 harvest:"))
    day3: int = int(input("day 3 harvest:"))
    total: int = day1 + day2 + day3
    print(f"Total harvest: {total}")
