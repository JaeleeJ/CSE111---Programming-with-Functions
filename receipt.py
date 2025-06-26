# Jaelee
# 09 Prove Milestone: Text Files
import csv
from datetime import datetime

def main():
    try: 
        # define variables for index for products
        key_column_index = 0
        name_index = 1
        price_index = 2

        # define variables for index for request
        product_num_index = 0
        quantity_index = 1

        # call funciton to read dictionary
        products_dict = read_dict("products.csv", key_column_index)

        # print name
        print("Inkom Emporium")
        print()

        # open request file
        # open file
        with open("request.csv", "rt") as csv_file:
            reader = csv.reader(csv_file)

            # skip first row
            next(reader)

            # count the number of items and subtotal 
            counter = 0
            subtotal = 0

            # read file
            for line in reader:
                product_num = line[product_num_index]
                quantity = line[quantity_index]
                product_value = products_dict[product_num]
                product_name = product_value[name_index]
                product_price = product_value[price_index]

                # total number of items and subtotal
                counter += int(quantity)
                subtotal += float(product_price) * int(quantity)

                # print output
                print(f"{product_name}: {quantity} @ {product_price}")

            # calculate tax
            tax = subtotal * 0.06
            total_amount = subtotal + tax

            # Print output
            print()
            print(f"Number of Items: {counter}")
            print(f"Subtotal: {subtotal:.2f}")
            print(f"Sales Tax: {tax:.2f}")
            print(f"Total: {total_amount:.2f}")

            # Print a thank you message
            print()
            print("Thank you for shopping at the Inkom Emporium.")
                
            # Print current date and time
            current_date_and_time = datetime.now()
            print(f"{current_date_and_time:%c}")

            # print invitation to take the survey
            print()
            print("Are you satisfied with your order?")
            print("Let us know what you think of our products!")
            print("Please take our survey on your experience at Inkom Emporium.")
            print("The survey is at <inkom_emporium_survey.com>")
    
    # handle exceptions
    except (FileNotFoundError, PermissionError) as file_error:
        print()
        print(file_error, "Enter a different file name.")
    
    except KeyError as key_error:
        print()
        print("Error: unknown product ID in the request.csv file")
        print(key_error)



def read_dict(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    # create dictionary
    dictionary = {}

    # open file
    with open(filename, "rt") as csv_file:
        reader = csv.reader(csv_file)

        # skip first line
        next(reader)

        for row_list in reader:
            key = row_list[key_column_index]

            # store data in dictionary
            dictionary[key] = row_list

    return dictionary


main()


