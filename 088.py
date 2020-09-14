sales_records={
        "John":{"N":3056,"S":8465,"E":2694,"W":2964},
        "Tom":{"N":4832,"S":6786,"E":4737,"W":3612},
        "Anne":{"N":3904,"S":4802,"E":5820,"W":1859},
        "Fiona":{"N":3904,"S":3645,"E":8821,"W":2451}
        }


name=input("Enter a name whose datavyou would like to view: ")
print(sales_records[name])

region =input("Enter a region out of N,E,W,S: ")

print(sales_records[name][region])

option=input("Enter 'y' to change item in the column or 'n' to stop: ")

if option== "y":
    value=input("Enter the column you want to change out of N,W,E,S: ")

    sales_records[name][region]=value

    print(f"The new records are {sales_records}")





