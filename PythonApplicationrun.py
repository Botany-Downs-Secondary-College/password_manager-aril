
#______________________________________________________________________________________
age                = 'false'
user_list          = [  ]
password_list      = [  ]
user_pass          = [  ]
username_entered   = ''
print('What would you like :\n')
print('log in \n'+ 'Create new account\n' + '')

user_input = ''
user_info = [ ]

def message():
    print('''

        Password requirements :

        1) capital letter/s included
        2) numbers included
        3) 8 digit long

         you need to be 16 years old and above to create an account
        ''')
def password():
    characters         = 'ABCDEFGHIJKLMNOPQRSTUVWX'
    numbers            = '1234567890'
    new_account        = 'false'
    while new_account == 'false':

        character_in_password = 'false'
        number_in_password    = 'false'

        user_password         = str(input('>')).strip()

        length_of_password = len(user_password)

    #____________________________________ok
        for character in characters:
            if character in user_password:
                character_in_password = 'true'
                #print(character_in_password)
                break
                
    #__________________________________ok
        for number in numbers:
            if number in user_password:
                number_in_password = 'true'
                #print(number_in_password)
                break
                
    #____________________________________ok
        if length_of_password < 8:
            print('please have minimum eight characters')

        elif character_in_password == 'false' :
            print('please include capital letter')

        elif number_in_password == 'false':
            print('please inlcude a number')

        
        elif character_in_password == 'true' and number_in_password == 'true' and length_of_password >= 8:
            
            password_check = str(input('checking the password : ')).strip()

            if password_check == user_password:

                print('your account is created, now you can log in')
                new_account = 'true'
                #user_list.append(user_password)
                #print(user_list)
                print('username:' + username_entered)
                print('password:'+ user_password)
                print('ok')
                return user_password
            elif password_check != user_password:
                print('that is not the right password')

def age():
    age_true      = False
    while age_true == False:

        user_age  = float(input('Enter age: '))
        if user_age < 16:
            print('you are under age')
            return False
        elif user_age == TypeError:
            print('please input a number')
        else:
            age_true = True
            return True

def add_details():
    while True:
        usr_input_func = input('what would you like to add: app')

        if usr_input_func == 'app':
            while True:
                name_app = input('app name?\n').strip().lower()
                username_app = input('username?\n').strip().lower()
                password_app = input('password?\n').strip().lower()
                user_info.append([name_app, username_app, password_app])
                break
        elif usr_input_func == 'end':
            print('leaving add function')
            break
def view_info():

    print(''' your usernames and passwords stored for the corresponding app is as follows:''')
    for i in range(0, len(user_info)):
        print(i + 1,') app name: ', user_info[i][0], 'username: ', user_info[i][1],'password: ',user_info[i][2])


def user_file():

    with open('users.txt') as userfile:
        lines = userfile.readlines()
        for line in lines:
             members = line.split()
             for member in members:
                  user_list.append(member)
        userfile.close()

def password_file():

    with open('passwords.txt') as passwordfile:
        lines = passwordfile.readlines()
        for line in lines:
            passwords = line.split()
            for password in passwords:
                password_list.append(password)
        passwordfile.close()


def new_account():
    
    while True:
        
        usr_inpt = str(input('enter unsername: ')).strip()

        if usr_inpt == 'end':
            print('ok')
            break
      
        user_file()
        if usr_inpt in user_list:
            print('username already tsken')


        else:
            with open('users.txt', 'a') as userfile:
                    userfile.write(''.join(usr_inpt) + '\n')
                    print('added')
                    userfile.close()
         
            usr_password = password()

            with open('passwords.txt', 'a') as passwordfile:
                    passwordfile.write(''.join(usr_password) + '\n')
                    print('added')
                    passwordfile.close()
            print(f'username: {usr_inpt}, password: {usr_password}')
            break
    print('ok')
    return True

def login():
    tries = 0
    y = 0
    while tries < 3:

        log_user = str(input('>login'))
        log_pass = str(input('>>login '))

        tries += 1

        user_file()
        password_file()
        user_num  = len(password_list)
        #print(len(password_list))
           
        for i in range(0, user_num):
            user_pass.append([user_list[y],password_list[y]])
            y += 1
            
        #print(user_pass)

          
            
            if [log_user, log_pass] in user_pass:
                print('logged in')
                return True
             
            else:
                print('check')
    print('please check')
    return False












    '''login_username = input('>')
    login_password = input('>>')
    user_check = [login_username, login_password]
    if user_check in user_pass:
        print('logged in')
    else:
        print('error')'''


#____________________________________________________________ok
  
while True:
    user_input = str(input('log/ new : ').lower().strip())
    if user_input == 'new':
        message()
        if age() != True:
            print('you\'re under age for using the programme')
            break
 
  
        else:
            new_account()
            if new_account == True:
                print('now you can log in')


           
    elif user_input == 'login':

        log_status = login()
        if log_status == True:

            while True:

                user_input_func = input('would you like to : add / view / log out')
                if user_input_func == 'add':

                    add_details()

                elif user_input_func == 'view':

                    view_info()

                elif user_input_func =='log out':
                    print('logging out')
                    break
        elif log_status == False:
            print('please try again after soem time')
            False
            break

      

    elif user_input == 'end':
        print('thanks for using password validator')
        break
print('end of programme')


#read files :
#print(password_list)
'''with open('passwords.txt') as fa:
    lines = fa.readlines()
    print(lines)'''

# reading and appending to existing list
#print(password_list)
'''with open('passwords.txt') as fa:
    lines = fa.readlines()
    for line in lines:
        passwords = line.split()
        for password in passwords:
            password_list.append(password)
print(password_list)'''

''' if login_username and login_password in user_list:
            print('logged in')
           return True
          else:
         print('incorrect username or password')'''


# corerectly displaying stred info of the user in particular list
# storing values into text files
# accessing values from file

#calling txt to list and checking if login user in list, if yees, new list.append [login username,data entered]
#checking the info, calling the txt to list, and passing if login in new List[0], if yes, print [0,0]Max








