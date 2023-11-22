def check_unique_numbers(numbers: list) -> bool:
    try:
        if len(numbers) == len(set(numbers)):
            return True
        else:
            return False
    except:
        TypeError('This is not list')