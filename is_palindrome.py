# Напишите функцию, которая проверяет, является ли строка палиндромом.


def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("radar"))  # True
print(is_palindrome("hello"))  # False
