def main():
    x=int(input("Enter your value to be squared: "))
    print(square(x))
    
def square(n):
    return pow(n, 2)


main()