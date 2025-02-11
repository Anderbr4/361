import random
from pyfiglet import Figlet


LIST_TO_DO_ITEMS = []

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
                print("\n You have modified the item!\n")
                self.item_name = new_item_name
                self.item_tag = new_item_tag
                self.item_comment = new_item_comment
                self.item_due_date = new_item_due_date
                gathering = False
            elif confirmation == "N":
                gathering = False



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

        if confirmation == "Y":
            gathering = False

    LIST_TO_DO_ITEMS.append(create_to_do_item(item_name,item_tag, item_comment, item_due_date))
    print("\n You have created the item!\n")

def view_all_items():

    user_view_choice = int(input("1. View all items\n2. View items by tag\nSelection: "))
    if user_view_choice == 1:


        print("\n Here are the remaining to do items: ")
        for item in LIST_TO_DO_ITEMS:
            item.view_item_details()
    elif user_view_choice == 2:
        user_tag = input("Enter tag: ")
        print("\n Here are the remaining to do items: ")
        for item in LIST_TO_DO_ITEMS:
            if item.item_tag == user_tag:
                item.view_item_details()
    else:
        print("input not recognized returning to main.\n")


def modify_to_do_item(item_id):

    for item in LIST_TO_DO_ITEMS:
        if item.item_id == item_id:
            item.modify_this_item()

def delete_items_by_tag(tag):
    new_item_list = []
    delete_confirm= input("Are you sure you want to delete these items Y/N? Doing so is permanement: ")
    if(delete_confirm == "Y"):
        for item in LIST_TO_DO_ITEMS:
            if item.item_tag != tag:
                new_item_list.append(item)

        print("Deleted all items with tag: "+str(tag)+"\n")
        return new_item_list
    else:
        print("Canceled Delete. Returning to main menu\n")
        return "none"




f = Figlet(font='slant')
print(f.renderText('To Do Or Not To Do'))



LIST_TO_DO_ITEMS.append(create_to_do_item("test1",'test', 'just a test1', '02/10/25'))
LIST_TO_DO_ITEMS.append(create_to_do_item("test2",'test', 'just a test2', '02/10/25'))
LIST_TO_DO_ITEMS.append(create_to_do_item("test3",'test', 'just a test3', '02/10/25'))
LIST_TO_DO_ITEMS.append(create_to_do_item("test4",'test', 'just a test4', '02/10/25'))
LIST_TO_DO_ITEMS.append(create_to_do_item("Modify",'Modify', 'to be modified', '02/10/25'))


using_tool = True

while(using_tool):

    
# in the while loop 
    print("Main Menu: ")

    print("1. View To Do List \n2. Add To Do Item \n3. (NEW) Modify To Do Item \n4. Delete To Do Item \n5. Exit\n")
    user_input = input("selection: ")

    if user_input == "1" :
        view_all_items()
    elif user_input == "2":
        prompt_create_to_do_item()
    elif user_input == "3":
        item_id = int(input("enter the id of the item to modify: "))
        modify_to_do_item(item_id)
    elif user_input == "4":
        tag = input("Please enter tag to delete: ")
        temp_deletion = delete_items_by_tag(tag)
        if type(temp_deletion) is list:
            LIST_TO_DO_ITEMS = temp_deletion
    elif user_input == "5":
        print("exiting")
        using_tool = False
    else:
        print("invalid selection please true again")
