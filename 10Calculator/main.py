from art import logo
def add(n1, n2):
    return n1 + n2
def subtract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def division(n1,n2):
    return n1/n2
operations={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":division,
}
def calculator():
    completed=True
    print(logo)
    number1=float(input("What's the first number?: "))
    while completed:
        for symbol in operations:
            print(symbol)
        picked_symbol=input("Pick an operation: ")
        number2=float(input("What's the next number?: "))
        answer=(operations[picked_symbol](number1,number2))
        print(f"{number1} {picked_symbol} {number2} = {answer}")
        continue_or_no=input(f"Type 'y' to continue calculating with {answer} or type 'n' to start a new calculation: ")
        if continue_or_no =="y":
            number1=answer
            completed=True
        elif continue_or_no=="n":
            print("\n"*20)
            calculator()
            completed=False
calculator()
