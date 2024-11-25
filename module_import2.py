def f1(s):
    if s == "Canada":
        return True
    else:
        return False

def f2(b):
    if b == True:
        return "Yes"
    else:
        return "No"

if __name__ == "__main__":
    get_input = input("Enter the name of the country: ")
    result1 = f1(get_input)
    print(f2(result1))