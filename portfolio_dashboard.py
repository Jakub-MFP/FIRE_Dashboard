# PORTFOLIO DASHBOARD

    #This file will out put similar data to what I have in my google sheets as seen in my FIRE blog. 
    #User will need to input the file name for their portfolio settings.

    # User can choose how much they want to invest 
    # user can view their watchlist of stocks as wellS

def option():
    print("""
    You can choose 'STOCK' or 'NO'
    """)

option()
while True:
    new_item = input("PICK OPTION >  ")

    if new_item == 'STOCK':
        import stock_screener
    
    elif new_item == 'NO':
        break
    break

print ("""

FIRE DASHBOARD IS NOW CLOSED

""")
