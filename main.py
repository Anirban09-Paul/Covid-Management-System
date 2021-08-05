from dbhelper import DBHelper

def main():
    db=DBHelper()
    data=int(input('1.Admin, 2.Patient, 3.Exit: '))

    while data==1:
        print('***********WELCOME YOU ARE NOW ADMIN STATUS************')
        print('Press 1 to insert new user')
        print('Press 2 to display all user')
        print('Press 3 to delete user')
        print('Press 4 to update user')
        print('Press 5 to exit program')
        print()

        try:
            choice=int(input())
            if(choice==1):
                #insert user
                uid=int(input("Enter user id: "))
                uname=input("Enter user name: ")
                uphone=input('Enteruser phone: ')
                db.insert_user(uid,uname,uphone)
            elif(choice==2):
                #display
                db.fech_all()
            elif(choice==3):
                #delete
                userid=int(input("Enter user id to which you want to delete: "))
                db.delete_all(userid)
            elif(choice==4):
                #update
                uid=int(input("Enter user id to which you want to update: "))
                uname=input("new name: ")
                uphone=input('new phone: ')
                db.update_user(uid,uname,uphone)
            elif(choice==5):
                #exit
                print("You are out of this Portal.")
                break
            else:
                print("Invalid input try again!!")
        except Exception:
            raise 'Invalid Details try again!!'

    while data==2:
        print('************WELCOME PATIENT STATUS*************')
        uid=input("Enter user id: ")
        uname=input("Enter user name: ")
        uphone=input('Enteruser phone: ')
        try:
            fever=input('Do you have fever(y/n): ')
            if fever=='y':
                drycough=input('Do you have dry cough for three days(y/n): ')
                if drycough=='y':
                    pain=input('any aches or pains(y/n): ')
                    if pain=='y':
                        sorethroat=input('Do you have sore throat(y/n): ')
                        if sorethroat=='y':
                            print('Sorry!! you are corona affected, from now to till 14 days you should do self quarentine.')
                            db.insert_user(userid,uname,uphone)
                            break      
        except Exception:
            raise 'Typing mistake.....try again!!'

    while data==3:
        print('You are Exit from Portal')
        break
if __name__=="__main__":
    main()