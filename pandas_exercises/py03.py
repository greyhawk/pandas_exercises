# AUTOGENERATED! DO NOT EDIT! File to edit: 01_python03.ipynb (unless otherwise specified).

__all__ = ['square_root_by_exhaustive', 'square_root_by_binary_search', 'square_root_by_newton']

# Cell
def square_root_by_exhaustive(x: int) -> int:
    epsilon = 0.01
    step = epsilon ** 2
    num_guesses = 0
    ans = 0.0
    while abs(ans ** 2 - x) >= epsilon and ans * ans <= x:
        ans += step
        num_guesses += 1
    if abs(ans ** 2 - x) >= epsilon:
        print('Failed on square root of', x)
    else:
        print(ans, 'is close to square root of', x)
    return num_guesses


# Cell
def square_root_by_binary_search(x: int) -> int:
    epsilon = 0.01
    num_guesses = 0
    low = 0.0
    high = max(1.0, x)
    ans = (high + low) / 2.0
    while abs(ans**2 - x) >= epsilon:
        print('low =', low, 'high=', high, 'ans=', ans)
        num_guesses += 1
        if ans ** 2 < x:
            low = ans
        else:
            high = ans
        ans = (high + low) / 2.0
    print(ans, 'is close to square root of', x)
    return num_guesses

# Cell
def square_root_by_newton(x: int) -> int:
    epsilon = 0.01
    guess = x / 2.0
    num_guesses = 0
    while abs(guess * guess - x) >= epsilon:
        guess = guess - (((guess ** 2) - x) / (2 * guess))
        num_guesses += 1
    print('Square root of', x, 'is about', guess)
    return num_guesses