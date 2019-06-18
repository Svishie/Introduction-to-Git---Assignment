def hello_world():
    print("Hello World")

def is_palindrome(palindrome):
    reversed = palindrome[::-1]

    if(palindrome == reversed):
        print("{} is a palindrome".format(palindrome))
    else:
        print("{} is not a palindrome".format(palindrome))

if __name__ == "__main__":
    hello_world()
    is_palindrome("asa")
    is_palindrome("asb")