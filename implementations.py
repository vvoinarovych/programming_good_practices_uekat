import string


def is_palindrome(text: str) -> bool:
    text = text.replace(" ", "").lower()
    return text == text[::-1]


def fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("n must be a non-negative integer.")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def count_vowels(text: str) -> int:
    vowels = "aeiouyóÓAEIOUY"
    found_vowels = [char for char in text if char in vowels]
    print(f"Znalezione samogłoski: {found_vowels}")
    return len(found_vowels)


def calculate_discount(price: float, discount: float) -> float:
    if not (0 <= discount <= 1):
        raise ValueError("Discount must be between 0 and 1.")
    return price * (1 - discount)


def flatten_list(nested_list: list) -> list:
    flattened = []
    for item in nested_list:
        if isinstance(item, list):
            flattened.extend(flatten_list(item))
        else:
            flattened.append(item)
    return flattened


def word_frequencies(text: str) -> dict:
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))

    words = text.split()

    freq = {}
    for word in words:
        if len(word) > 1:
            if word in freq:
                freq[word] += 1
            else:
                freq[word] = 1

    return freq


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
