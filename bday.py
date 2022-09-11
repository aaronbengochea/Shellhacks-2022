import datetime as dt


bday_storage = {}
phone_storage = {}
email_storage = {}


def add_credentials(name,month,day,year,phone=None,email=None):
    name = name.title()
    
    if name not in bday_storage:

        if phone != None:
            phone = str(phone)
            phone_dummy = phone.split('-')
            if len(phone_dummy[0]) != 3 or len(phone_dummy[1]) != 3 or len(phone_dummy[2]) != 4:
                print(f"Phone number string must contain 10 total digits to be valid")
            else:
                phone_storage[name] = phone

        if email != None:
            email = str(email)
            if '@' not in email or '.com' not in email:
                print(f"Email string must contain an @ and .com")
            else:
                email_storage[name] = email

        date = dt.date(year,month,day).strftime('%b-%d-%Y')
        bday_storage[name] = date

    else:
        print(f"Looks like {name}'s birthday has already been added to the list! \n")



def change_credentials(name,month,day,year):
    name = name.title()

    if name in bday_storage:
        old_date = bday_storage[name]
        date = dt.date(year,month,day).strftime('%b-%d-%Y')
        bday_storage[name] = date
        print(f"{name}'s birthday has been updated from {old_date} to {date}\n")
    
    else:
        print(f"Looks like {name}'s birthday has not yet been added to the list! Please refer to the add_bday() function in order to add {name}. \n")



def change_communication(name,phone=None,email=None):
    name = name.title()
    
    if (phone != None):
        phone = str(phone)
        phone_dummy = phone.split('-')
        if (len(phone_dummy[0]) != 3) or (len(phone_dummy[1]) != 3) or (len(phone_dummy[2]) != 4):
                print(f"Phone number string must contain 10 total digits to be valid. Ex: 786-758-9825")
        else:
            phone_storage[name] = phone

    if (email != None):
        if ('@' not in email) or ('.com' not in email):
                print(f"Email string must contain an @ and .com")
        else:
            email_storage[name] = email



def get_summary():
    for name in sorted(bday_storage.keys()):
        
        if (name in phone_storage) and (name in email_storage):
            print(f"Name: {name} \nBirthday: {bday_storage[name]}\nPhone: {phone_storage[name]}\nEmail: {email_storage[name]}\n")
        elif name in phone_storage:
            print(f"Name: {name} \nBirthday: {bday_storage[name]}\nPhone: {phone_storage[name]}\n")
        elif name in email_storage:
            print(f"Name: {name} \nBirthday: {bday_storage[name]}\nEmail: {email_storage[name]}\n")
        else:
            print(f"Name: {name} \nBirthday: {bday_storage[name]}\n")
       


def days_left_until_bday(name):
    name = name.title()

    if name in bday_storage:
        date = bday_storage[name]
        date = date.split("-")
        
        month_list = {'Jan':1,'Feb':2,'Mar':3,'Apr':4,'May':5,'Jun':6,'Jul':7,'Aug':8,'Sep':9,'Oct':10,'Nov':11,'Dec':12}
        for i in range(len(date)):
            if date[i] in month_list:
                date[i] = month_list[date[i]]

            date[i] = int(date[i])

        current_year = dt.datetime.now().year

        diff =  dt.date(current_year,date[0],date[1]) - dt.date.today()
        diff = diff.total_seconds()
        diff = diff/24/60/60
        diff = int(diff)

        if diff < 0:
            final_diff = 365 + diff
            print(f"Looks like {name}'s birthday already passed this year.\n")
            if (name in phone_storage) and (name in email_storage):
                print(f"Name: {name} \nBirthday: {bday_storage[name]}\nPhone: {phone_storage[name]}\nEmail: {email_storage[name]}\nDays until Bday: {final_diff}\n")
            elif name in phone_storage:
                print(f"Name: {name} \nBirthday: {bday_storage[name]}\nPhone: {phone_storage[name]}\nDays until Bday: {final_diff}\n")
            elif name in email_storage:
                print(f"Name: {name} \nBirthday: {bday_storage[name]}\nEmail: {email_storage[name]}\nDays until Bday: {final_diff}\n")
            else:
                print(f"Name: {name} \nBirthday: {bday_storage[name]}\nDays until Bday: {final_diff}\n")

        if diff > 0:
            print(f"Looks like there are {diff} days left until {name}'s next birthday!\n")
            if (name in phone_storage) and (name in email_storage):         
                print(f"Name: {name} \nBirthday: {bday_storage[name]}\nPhone: {phone_storage[name]}\nEmail: {email_storage[name]}\nDays until Bday: {diff}\n")
            elif name in phone_storage:
                print(f"Name: {name} \nBirthday: {bday_storage[name]}\nPhone: {phone_storage[name]}\nDays until Bday: {diff}\n")
            elif name in email_storage:
                print(f"Name: {name} \nBirthday: {bday_storage[name]}\nEmail: {email_storage[name]}\nDays until Bday: {diff}\n")
            else:
                print(f"Name: {name} \nBirthday: {bday_storage[name]}\nDays until Bday: {diff}\n")

        if diff == 0:
            print(f"Looks like today is {name}'s next birthday!\n")
            if (name in phone_storage) and (name in email_storage):         
                print(f"Name: {name} \nBirthday: {bday_storage[name]}\nPhone: {phone_storage[name]}\nEmail: {email_storage[name]}\nDays until Bday: {diff}\n")
            elif name in phone_storage:
                print(f"Name: {name} \nBirthday: {bday_storage[name]}\nPhone: {phone_storage[name]}\nDays until Bday: {diff}\n")
            elif name in email_storage:
                print(f"Name: {name} \nBirthday: {bday_storage[name]}\nEmail: {email_storage[name]}\nDays until Bday: {diff}\n")
            else:
                print(f"Name: {name} \nBirthday: {bday_storage[name]}\nDays until Bday: {diff}\n")

    else:
        print(f"Looks like {name}'s birthday has not yet been added to the list! Please refer to the add_bday() function in order to add {name}.")        
        
        


