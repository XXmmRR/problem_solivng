# Эта функция O(n)
def O_n_search_min(digits: list):
    return min(digits)

# Эта функция O(n**2) тк использует двойной цикл
def O_n2_search_min(digits: list):
    min_digit = digits[-1]
    for i in digits:
        for j in digits:
            if i <= j:
                if min_digit >= i:
                    min_digit = i
    return min_digit
