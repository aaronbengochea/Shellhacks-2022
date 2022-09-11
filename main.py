import bday as bd

# bday functions:

# add_credentials(name:str,year:int,day:int,year:int,phone=None(str),email=None(str)) = allows the user to add family/friend's birthday and credential info
# change_credentials(name:str,year:int,day:int,year:int) = allows the user to change family/friend birthday info
# change_communication(name:str,phone:str,email:str) = allows the user to change family/friend credential info
# days_left_until_bday(name:str) = returns days left until next birthday
# get_summary() = returns every family/friend member's name and birthday details, also returns phone and email details if the user added them to add_bday() function.

def main():
    bd.add_credentials('cicy',9,1,1994,'305-898-7272')
    bd.add_credentials('aaron',9,11,1992,email='aron@xyz.com')
    bd.add_credentials('bob',7,1,1993,'992-702-0055','bob@gmail.com')
    bd.add_credentials('odi',9,18,1995)
    



if __name__=="__main__":
    main()
        
    bd.get_summary()    
    bd.change_communication('aaron','305-555-2222')
    bd.change_communication('cicy','305-999-8888','ccc@gmail.com')
    bd.change_credentials('odi',10,18,1995)
    bd.change_credentials('cicy',day=22,month=1,year=2000)
    bd.days_left_until_bday('bob')
    bd.days_left_until_bday('aaron')
    
