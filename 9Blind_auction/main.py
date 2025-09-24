from art import logo
print(logo)

def highest_bidder(bidding_amount):
    highest_bid_amount=0
    winner=""
    for bidder in bidding_amount:
        current_bid=bidding_amount[bidder]
        if current_bid>highest_bid_amount:
            highest_bid_amount=current_bid
            winner=bidder
    print(f"The winner is {winner} with the Bid amount ${highest_bid_amount}")

bidders={}
continue_bidding=True
while continue_bidding:
    name=input("What is your name? ")
    bid_price=int(input("What is your bid $"))
    bidders[name]=bid_price
    other_bidders=input("Are there any other bidders? Type yes or no. ")
    if other_bidders=="no":
        continue_bidding=False
        highest_bidder(bidders)
    elif other_bidders=="yes":
        print("\n"*50)
