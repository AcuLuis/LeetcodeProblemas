
def isPalindrome(x):
    x = str(x)
    aux = x[::-1]
    return True if aux==x else False
print(isPalindrome(121))
