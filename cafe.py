menu = ['Doughnut', 'Croissant', 'Latte', 'Americano', 'Muffin']
stock ={'Doughnut' : 6,
        'Croissant' : 7,
        'Latte' : 10,
        'Americano' : 5,
        'Muffin' : 8,
        }
price ={'Doughnut' : 2,
        'Croissant' : 3,
        'Latte': 3.5,
        'Americano' : 2.5,
        'Muffin' : 2.5
        }
total_stock = 0
# I created a variable total_stock to help calculate the sum of the value of all the stock
for item in menu: 
# I have decided to set the 'items' as keys this way to help retrieve the values in the dictionaries
    item_value = stock[item] * price[item]
    total_stock += item_value
# total_stock will increase by the item_value each time the loop runs
print("The value of the total stock in your cafe is" + " " + "$" + str(total_stock) + ".")
   
   

    
    

