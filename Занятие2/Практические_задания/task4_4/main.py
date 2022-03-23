if __name__ == "__main__":
    list_numbers = list(range(5, 17))

    list_numbers[4] = sum(list_numbers) / len(list_numbers)

    print(list_numbers)
