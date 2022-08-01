from datetime import datetime
from datetime import date
from datetime import timedelta

class Invoice:

    def __init__(self, part_id, description, quantity_of_item, price_per_item):
        self.__part_id = part_id
        self.__description = description
        self.__quantity_of_item = quantity_of_item
        self.__price_per_item = price_per_item

    def get_part_id(self):
        return self.__part_id

    def get_description(self):
        return self.__description

    def get_quantity_of_item(self):
        return self.__quantity_of_item

    def get_price_per_item(self):
        return self.__price_per_item

    def set_part_id(self, part_id):
        self.__part_id = part_id

    def set_description(self, description):
        self.__description = description

    def set_quantity_of_item(self, quantity_of_item):
        self.__quantity_of_item = int(quantity_of_item)

    def set_price_per_item(self, price_per_item):
        self.__price_per_item = int(price_per_item)

    def get_invoice_price(self):
        if self.__quantity_of_item < 0:
           self.__quantity_of_item = 0
        if self.__price_per_item < 0:
           self.__price_per_item = 0

        return self.__quantity_of_item * self.__price_per_item
#
#
# inv1= Invoice("325","hammer", 3, 4.25)
# inv2= Invoice("678","Drill", 6, 32.95)
# inv3= Invoice("2244", "Powersaw", 3, 29.99)
# print("Part ID: ", inv1.get_part_id(), " Description: ", inv1.get_description(), " Quantity: ", inv1.get_quantity_of_item(), " Price: ", inv1.get_price_per_item())
# print("Part ID: ", inv2.get_part_id(), " Description: ", inv2.get_description(), " Quantity: ", inv2.get_quantity_of_item(), " Price: ", inv2.get_price_per_item())
# print("Part ID: ", inv3.get_part_id(), " Description: ", inv3.get_description(), " Quantity: ", inv3.get_quantity_of_item(), " Price: ", inv3.get_price_per_item())
# print()
#Gets a valid date from the user
def get_invoice_date():
    #Initialize todays datetime object
    today = date.today()
    #todays_date = date(today.year, today.month, today.day)

    #get valid invoice datetime obj
    while True:
        date_str = input("Enter the Invoice date (MM/DD/YYYY): ")
        try:
            invoice_datetime = datetime.strptime(date_str, "%m/%d/%Y")
            invoice_date = date(invoice_datetime.year, invoice_datetime.month, invoice_datetime.day)
        except ValueError:
            print("Invalid date format. Please try again.")
            continue

        if invoice_date > today:
            print("Invoice date must be today or earlier. Please try again.")
        else:
            return invoice_date

def main():

    # display a title
    print()

    choice = "y"
    while choice == "y":

        # get user entry
        invoice_date = get_invoice_date()

        #get todays date
        today = date.today()

        #get date 30 days apart
        due_date = invoice_date + timedelta(days=30)

        #print data
        date_format = "%B %d, %Y"
        print()
        print("Invoice Date: " + invoice_date.strftime(date_format))
        print("Due Date: \t" + due_date.strftime(date_format))
        print("Current Date: " + today.strftime(date_format))

        # determine discount percent
        print()
        if today < due_date:
            print("Invoice is " + str((today - due_date).days) + " day(s) away.")
        elif today > due_date:
            print("Invoice is " + str((due_date - today).days * -1) + " day(s) overdue.")
        else:
            print("Invoice is due today!")
        return invoice_date,today,due_date

        #
        # print()
        # choice = input("Continue? (y/n): ")
        # print()
        # if choice == 'y':
        #     break
        # else:
        #     print("Perhaps we can bill them later")



main()
inv1= Invoice("325","hammer", 3, 4.25)
inv2= Invoice("678","Drill", 6, 32.95)
inv3= Invoice("2244", "Powersaw", 3, 29.99)
total = inv1.get_price_per_item()+inv2.get_price_per_item()+inv3.get_price_per_item()

print("Part ID: ", inv1.get_part_id(), " Description: ", inv1.get_description(), " Quantity: ", inv1.get_quantity_of_item(), " Price: ", inv1.get_price_per_item())
print("Part ID: ", inv2.get_part_id(), " Description: ", inv2.get_description(), " Quantity: ", inv2.get_quantity_of_item(), " Price: ", inv2.get_price_per_item())
print("Part ID: ", inv3.get_part_id(), " Description: ", inv3.get_description(), " Quantity: ", inv3.get_quantity_of_item(), " Price: ", inv3.get_price_per_item())
print()
print("Please pay total: $", total, " before the due date.  Thank you for your business.")
print()


#
#
# if __name__ == "__main__":
#     main()
