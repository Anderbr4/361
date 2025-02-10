import random
from pyfiglet import Figlet

f = Figlet(font='slant')
print(f.renderText('To Do Or Not To Do'))

list_to_do_items = []


# create class todo item that stores to do item logic

class ToDoItem:
    def __init__(self,item_id, item_name, item_tag,item_comment,item_due_date):
        self.item_id = item_id
        self.item_name = item_name
        self.item_tag = item_tag
        self.item_comment = item_comment
        self.item_due_date = item_due_date

    def view_item_details(self):
        print(f'item id: {self.item_id}\nitem name: {self.item_name}\nitem tag: {self.item_tag}\nitem comment: {self.item_comment}\nitem due date: {self.item_due_date}\n')

    def modify_this_item(self):

        gathering = True
        while(gathering):
            print("Modify the item: \n")
            new_item_name = input("Enter Item Name: ")
            new_item_tag = input("Enter Item Tag: ")
            new_item_comment = input("Enter Item Comment: ")
            new_item_due_date = input("Enter Item Due Date: ")

            confirmation = input("Confirm these choices?: Y/N  ")
            print("\n")
            if confirmation == "Y":
                gathering = False

        self.item_name = new_item_name
        self.item_tag = new_item_tag
        self.item_comment = new_item_comment
        self.item_due_date = new_item_due_date



def create_to_do_item(item_name,item_tag, item_comment, item_due_date):
    item_id = random.randint(1,10000)

    return ToDoItem(item_id,item_name, item_tag,item_comment,item_due_date)

def prompt_create_to_do_item():

    gathering = True
    while(gathering):
        item_name = input("Enter Item Name: ")
        item_tag = input("Enter Item Tag: ")
        item_comment = input("Enter Item Comment: ")
        item_due_date = input("Enter Item Due Date: ")

        confirmation = input("Confirm these choices?: Y/N  ")
        print("\n")
        if confirmation == "Y":
            gathering = False

    list_to_do_items.append(create_to_do_item(item_name,item_tag, item_comment, item_due_date))


def view_all_items():
    for item in list_to_do_items:
        item.view_item_details()



def modify_to_do_item(item_id):

    for item in list_to_do_items:
        if item.item_id == item_id:
            item.modify_this_item()

def delete_items_by_tag(tag):
    for item in list_to_do_items:
        if item.item_tag == tag:
            list_to_do_items.remove(item)




# print("Create To Do Item \nEnter Item Name:\nEnter Item Tag:\nEnter Item Comment:\nEnter Item Due Date:")

# store to do items in a list 

# ui elements 



# implement create to do item 

# implement bulk delete to do items 

# implement edit to do items 

# implement view to do list 


# 






using_tool = True

while(using_tool):

    
# in the while loop 
    print("1. View To Do List \n2. Add To Do Item \n3. (NEW) Modify To Do Item \n4. Delete To Do Item \n5. Exit\n")
    user_input = input("selection: ")

    if user_input == "1" :
        print("viewing to do items: \n")
        view_all_items()
    elif user_input == "2":
        print("adding to do items ")
        prompt_create_to_do_item()
    elif user_input == "3":
        print("going to modify to do item")
        item_id = int(input("enter the id of the item to modify: "))
        modify_to_do_item(item_id)
    elif user_input == "4":
        print("deleting to do item")
        tag = input("Please enter tag to delete: ")
        delete_items_by_tag(tag)
    elif user_input == "5":
        print("exiting")
        using_tool = False
    else:
        print("invalid selection please true again")


# switch case 1
#print("1. View All Items\n2. View Items By Tag\n3. View Items By Due Date")


# switch case 2
# print("Create To Do Item \nEnter Item Name:\nEnter Item Tag:\nEnter Item Comment:\nEnter Item Due Date:")


# switch case 3
# print("Not Done Yet? Modify!\nEnter Item Name:\nEnter Item Tag:\nEnter Item Comment:\nEnter Item Due Date:")


#switch case 4 
# print("Enter To Do List Item To Delete:\n\n1.Confirm Delete (Permanent) \n2. Exit")

#switch case 5 exit 
