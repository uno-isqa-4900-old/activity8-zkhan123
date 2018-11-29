import csv



FILENAME= "customers.csv"

class Customer:

    def __init__(self, ID, firstName, lastName, company, address, city, state, zip):
        self.ID=ID
        self.firstName=firstName
        self.lastName=lastName
        self.company=company
        self.address=address
        self.city=city
        self.state=state
        self.zip=zip

    def getaddress (self):
        return Customer.address

    def getcity(self):
        return Customer.city

    def getstate(self):
        return Customer.state

    def getzip(self):
        return Customer.zip



    

def display_title():
    print ("Customer Viewer")
    pass

def csv_reader():

    customers=[]
    with open("customers.csv", newline="") as file:
        reader= csv.reader (file)
        for row in reader:

            customers.append(row)
    return customers
    pass

def findCustomer(cust_id, cust_list):
    for row in cust_list:

        if row[0]== cust_id:
            print (row[1]+ ' '+row[2])

            print (row[4])
            print (row[5]+ ' ' + row[6]+' '+row[7])








def main():
    display_title()
    cust_list= csv_reader()

    cust_id= str(input ("Enter Customer ID: "))
    find_customer = findCustomer(cust_id, cust_list)

    choice = input("Continue? y/n:")
    while True:
        choice.lower == 'y'
        cust_id = input("Enter Customer ID:")
        find_customer(cust_id)
        choice= input ("Continue? y/n:")
    print ("Bye!")

if __name__ == '__main__':
    main()




