class BikeDetails:
    def __init__(self):
        self.file_name = "BIKE DETAILS.csv"

    def search(self):
        keyword = input("Enter the keyword to search: ")
        with open(self.file_name, "r") as file:
            lines = file.readlines()
            count = 0
            for line in lines:
                if keyword.lower() in line.lower():
                    count += 1

            if count > 0:
                print("We've found {} result(s) for your search".format(count))
                for line in lines:
                    if keyword.lower() in line.lower():
                        print(line, end='')
            else:
                print("We've found no results for your search")

    def insert(self):
        name = input("Enter the bike name: ")
        selling_price = input("Enter the selling price: ")
        year = input("Enter the year: ")
        seller_type = input("Enter the seller type: ")
        owner = input("Enter the 1st hand or 2nd hand: ")
        km_driven = input("Enter the kilometer driven: ")
        ex_showroom_price = input("Enter the ex showroom price: ")
        newEntry = name+","+selling_price+","+year+","+seller_type+","+owner+","+km_driven+","+ex_showroom_price+"\n"

        with open(self.file_name, "r") as file:
            lines = file.readlines()
            count = len(lines)
            newEntry = str(count) + "," + newEntry
            lines.append(newEntry)

        with open(self.file_name, "w") as file:
            file.writelines(lines)
            print("\"{}\" entry is added".format(newEntry.replace('\n', '')))

    def modify(self):
        id = None;
        print("Enter any one of the options below: ")
        print("\t 1. Enter id")
        print("\t 2. Search and find id")
        option = input(">>>>>>>>> ")
        if option == '1':
            id = int(input("Please enter the id: "))
        elif option == '2':
            self.search()
            id = int(input("Please enter the id: "))

        with open(self.file_name) as file:
            lines = file.readlines()
            print("Record selected: "+lines[id])
            name = input("Enter the bike name: ")
            selling_price = input("Enter the selling price: ")
            year = input("Enter the year: ")
            seller_type = input("Enter the seller type: ")
            owner = input("Enter the 1st hand or 2nd hand: ")
            km_driven = input("Enter the kilometer driven: ")
            ex_showroom_price = input("Enter the ex showroom price: ")
            newEntry = str(id) + "," + name + "," + selling_price + "," + year + "," + seller_type + "," + owner + "," + km_driven + "," + ex_showroom_price + "\n"
            print("Record after modification: " + newEntry)
            lines[id] = newEntry

        with open(self.file_name, "w") as file:
            file.writelines(lines)

bike_details = BikeDetails()

while(1):
    option = input("select the option from the list:\n\
    \t1. Search\n\
    \t2. Insert\n\
    \t3. Modify\n\
    \t4. Exit\n\
    >>>>>>>>>>>>> ")

    if option == '1':
        bike_details.search()
    elif option == '2':
        bike_details.insert()
    elif option == '3':
        bike_details.modify()
    elif option == '4':
        break
