# Name: Jan Clarisse B. Victoria
# Section: CMSC12 - B3L
# Code Description: Movie Theater Booking System

from datetime import datetime # import the datetime function from the datetime module in the program to handle dates and times

# save/load functions

def save_file(): # writes dictionary content into a file
    records = open('movies_data.txt', 'w') # opens the file 'movies_data.txt' and writes the content below

    for data in movies: # iterates through every key value in the dictionary; every data is the key
        movie_name = movies[data]['movie_name'] # 1
        movie_genre = movies[data]['movie_genre'] # 2
        movie_restriction = movies[data]['movie_restriction'] # 3
        date_time_viewing = movies[data]['date_time_viewing'] # 4
        end_time_viewing = movies[data]['end_time_viewing'] # 5
        movie_venue = movies[data]['movie_venue'] # 6
        seats = movies[data]['seats'] # 7
        max_pax = movies[data]['max_pax'] # 8
        customers = movies[data]['customers'] # 9
        movie_price = movies[data]['movie_price'] # 10
        
        records.write(f"{data}|{movie_name}|{movie_genre}|{movie_restriction}|{date_time_viewing}|{end_time_viewing}|{movie_venue}|{seats}|{max_pax}|{customers}|{movie_price}\n") 
    
    records.close() # writes the information stored in the variables which is separated by '|' that would be used to determine every info later when loaded, then the file is closed afterwards

def load_file(): # loads the file in which existing data is stored
    try: 
        records = open('movies_data.txt', 'r') # opens movies_data.txt but only on read mode
        movies.clear() # it is a must to clear the current dictionary to avoid confusion with the id's and the saved changes

        for i in records: # iterates through every line in the file
            data = i[:-1].split('|') # remove the invisible "\n" at the end of each line and split the values using the separator '|', then puts it in a list
            movie_id = data[0] # every info is saved in order thus it is easy to locate which is which in terms of the list
            movie_data = {} # declare another dictionary
            movies[movie_id] = movie_data # creating a nested dictionary

            movie_data['movie_name'] = data[1] 
            movie_data['movie_genre'] = data[2]
            movie_data['movie_restriction'] = data[3]

            dt_time_viewing = data[4] # gets the date and time as a string format
            dt_viewing = datetime.strptime(dt_time_viewing,'%m-%d-%Y %I:%M %p') # let the program know that these are elements of a date and time (not just a string) by using strptime in the datetime module
            date_time_viewing = dt_viewing.strftime('%m-%d-%Y %I:%M %p') # let the program know that this is the date format that I want 
            movie_data['date_time_viewing'] = date_time_viewing # sets the date as the value of the key 'date_time_viewing'

            ed_date_input = data[5] # same with date_time_viewing
            arr_dt = datetime.strptime(ed_date_input,'%m-%d-%Y %I:%M %p') 
            end_time_viewing = arr_dt.strftime('%m-%d-%Y %I:%M %p')
            movie_data['end_time_viewing'] = end_time_viewing

            movie_data['movie_venue'] = data[6]
            movie_data['seats'] = data[7]
            movie_data['max_pax'] = data[8]
            movie_data['customers'] = data[9]
            movie_data['movie_price'] = data[10]

        records.close() # indicates that you are done with using the opened file
        current_id[0] = sorted(movies.keys())[-1] # sets current id to the last or greatest value in the list of keys

    except FileNotFoundError: # if no file was found yet, it means that it may be the first iteration or the admin has not added a movie yet
        return # just return and still run the program

# functions

def user_class():
    try:
        while True: # runs until the user exits the program 
            choice = int(input("\nAre you an admin or a cashier? \n[1] Admin\n[2] Cashier\n[0] Exit Program\n\nChoice: ")) 
            
            if choice == 1:
                admin_page() # calls admin page
            
            elif choice == 2:
                cashier_page() # calls cashier page
            
            elif choice == 0:
                print("Thank you for using the program.") 
                break # terminates loop; exits the program
            
            else:
                print("INVALID INPUT. PLEASE TRY AGAIN.") # for any invalid number
    
    except ValueError: # if user entered any value apart from the choices, user_class() will be called once again
        print("INVALID INPUT. PLEASE TRY AGAIN.") 
        return user_class()

def generate_id():
    if int(current_id[0]) < 9: # current_id[0] is classified into ranges; upon first use, current_id[0] is set to 0
        ID = "000" + str(int(current_id[0]) + 1) # since those less than 9 take only the ones place even when added by 1, the value is concatenated to three leading zeroes
        current_id[0] = ID # now, the value of current_id[0] is changed to the concatenated value
        return ID # returns the generated id for display 
    
    elif int(current_id[0]) >= 9 and int(current_id[0]) < 99: # same goes with these other conditional statements
        ID = "00" + str(int(current_id[0]) + 1) # to add 1 to current_id[0], type is changed to integer first then reverted back to string for concatenation
        current_id[0] = ID
        return ID
    
    elif int(current_id[0]) >= 99 and int(current_id[0]) < 999: 
        ID = "0" + str(int(current_id[0]) + 1)
        current_id[0] = ID
        return ID
    
    elif int(current_id[0]) >= 999: 
        ID = str(int(current_id[0][-1]) + 1)
        current_id[0] = ID
        return ID

def check_string(x): # checks the string if it contains invalid characters
    if len(x) == 0: # if the user did not enter anything, return False 
        return False
    
    elif "|" in x or "," in x: # an input should not contain the separator for the save and load mechanism
        return False
    
    else: # return true if there are no problems with the input; semantic errors such as typographical errors are not caught (they could use the edit option if an input is wrong)
        return True

def admin_page():
    print("\nHello, Admin! Welcome to the  Movie Theater Booking System!\nWhat do you want to do today?")
    choice = int(input("[1] Add a Movie\n[2] Edit a Movie\n[3] Delete a Movie\n[4] View All Movies\n[5] Search Movies\n[0] Exit\n\nChoice: "))
    
    if choice == 1:
        add_movie()
    
    elif choice == 2:
        edit_movie()
    
    elif choice == 3:
        delete_movie()
    
    elif choice == 4:
        a_view_movies()
    
    elif choice == 5:
        search_movie()
    
    elif choice == 0:
        print("Thank you for using the program, Admin.")
        return # returns back to the user_class page
    
    else:
        print("INVALID INPUT. PLEASE TRY AGAIN.3")
        return admin_page() 

def cashier_page():
    print("\nHello, Cashier! Welcome to the  Movie Theater Booking System!\nWhat do you want to do today?")
    choice = int(input("[1] View Movies\n[2] Book a Seat\n[0] Exit\n\nChoice: "))
    
    if choice == 1:
        p_view_movies()
    
    elif choice == 2:
        book_seat()
    
    elif choice == 0:
        print("Thank you for using the program, Cashier.")
        return # returns to the user_class page 
    
    else:
        print("INVALID INPUT. PLEASE TRY AGAIN.4")
        cashier_page()

def add_movie():
    movie_data = {} # declare an empty dictionary that will be nested later
    
    movie_id = generate_id() # generate an id 
    print(f"\nMovie ID: {movie_id}") 
    
    while True: 
        movie_name = input("\nEnter the Movie's Name: ").title() # always put inputs into title case
        
        if check_string(movie_name) == False: # if the input contains invalid characters based on the check_string function, the user will be given a chance to enter again
            print("Movie's Name is invalid. Please try again")
        
        else:
            break # if no invalid characters were caught, the user can now move onto the next input
    
    while True:
        movie_genre = input("\nMovie Main Genres:\nFamily\nAction\nComedy\nDrama\nFantasy\nHorror\nMystery\nRomance\nThriller\n\nEnter Movie's Main Genre (Only 1): ").title() 
        
        if check_string(movie_genre) == False:
            print("Movie's Genre is invalid. Please try again.")
        
        else: 
            break
    
    while True:
        movie_restriction = input("\nMovie Restrictions:\nRated G: General audiences\nRated PG: Parental guidance suggested\nRated PG-13: Parents strongly cautioned\nRated R18+: Restricted for adults only\n\nEnter Movie's Restriction (Ex. PG): ").upper() 
        
        if check_string(movie_restriction) == False:
            print("Movie's Restriction is invalid. Please try again")
        
        else: 
            break

    while True:
        print("\nMovie's Date and Time of Viewing")
        dtvdate = set_date() # calls set date function
        
        try:
            formatdtvdate = datetime.strptime(dtvdate,'%Y%m%d%I%M%p') # labels the string from the set date function so that the program could recognize it as the respective elements of the date
            date_time_viewing = formatdtvdate.strftime('%m-%d-%Y %I:%M %p') # indicates the desired date and time format 
            break
        
        except ValueError:
            print("\nInvalid Date. Please try again.") # if date is not valid e.g. Feb 30, April 31

    while True:
        print("\nMovie's End Date and Time of Viewing")
        edtime = set_date()
        try:
            formatedtime = datetime.strptime(edtime,'%Y%m%d%I%M%p')
            end_time_viewing = formatedtime.strftime('%m-%d-%Y %I:%M %p')
            if formatdtvdate > formatedtime: # because of the datetime module, python can evaluate and compare the dates and times
                print("Invalid input. start time must be earlier than end time. Try again.") # departure should not be later than arrival, hence ask the user to try again and correct the date
            elif formatdtvdate == formatedtime: # dates cannot be equal
                print("Invalid input. A cinema's start time cannot be the same as its end time. Try again")
            elif formatdtvdate < datetime.today() or formatedtime < datetime.today():  # flights cannot be added with dates and times from the past
                print("Invalid input. Date and Time should not be from the past")
            else:
                break # if no error was found, continue with the other inputs

        except ValueError:
            print("\nInvalid Date. Please try again.")
    
    while True:
        try:
            movie_venue = input("\nMovie Venue:\nCinema 1 (with 20 seats)\nCinema 2 (with 16 seats)\nCinema 3(with 12 seats)\n\nEnter the Cinema Number: ")
            
            if movie_venue == "1": 
                seats = "A1,A2,A3,A4,A5,B1,B2,B3,B4,B5,C1,C2,C3,C4,C5,D1,D2,D3,D4,D5" # --this should be the number and details of the seats
                max_pax = 20 # the maximum number of passengers
                break # carry on
            
            elif movie_venue == "2": 
                seats = "A1,A2,A3,A4,B1,B2,B3,B4,C1,C2,C3,C4,D1,D2,D3,D4" 
                max_pax = 16
                break 
            
            elif movie_venue == "3": 
                seats = "A1,A2,A3,B1,B2,B3,C1,C2,C3,D1,D2,D3" 
                max_pax = 12
                break 
            
            else: 
                print("Invalid input. Only input the cinema number of your choice.") 
        
        except ValueError:
            print('Invalid Input.')
    
    while True:
        movie_price = int(input("\nEnter Movie's Price: @"))
        break

    movies[movie_id] = movie_data # flight_id as the key of the nested dictionary
    movie_data['movie_name'] = movie_name # places the info in the nested dictionary, 'movie_data', sets value based on the inputs above
    movie_data['movie_genre'] = movie_genre
    movie_data['movie_restriction'] = movie_restriction
    movie_data['date_time_viewing'] = date_time_viewing
    movie_data['end_time_viewing'] = end_time_viewing
    movie_data['movie_venue'] = movie_venue
    movie_data['seats'] = seats
    movie_data['max_pax'] = max_pax
    movie_data['customers'] = ""
    movie_data['movie_price'] = int(movie_price)
    
    save_file() # immediately save the date, call save file function
    print(f"\nMovie {movie_id} has been added successfully!") # prompt the user that the info has been saved successfully
    return admin_page() # back to admin page so the user can do other things or exit the program instead

def set_date(): # for validating and returning date and time inputs
    while True: # while loops added so that users will already be prompted if date is valid or not in these common errors
        try:
            y = int(input("Enter Year (Ex: 2023): ")) 
            
            if len(str(y)) < 4: # year should not contain less than 4 characters
                print("Invalid Input.")
            
            else:
                break
        
        except ValueError: # only integers are accepted; lets the user try again
            print("Invalid Input.")
        
    while True:
        try:
            m = int(input("Enter Month (1-12): "))
            
            if m < 1 or m > 12: # month should only be an integer from 1 to 12 
                print("Invalid Number.")
            
            elif m > 0 and m < 10: # if the month is a single digit, add a leading zero to avoid sematic errors with the datetime module
                m = "0" + str(m)
                break
            
            else:
                break
        
        except ValueError:
            print("Invalid Input.")
    
    while True:
        try:
            d = int(input("Enter Day (1-31): "))
            
            if d < 1 or d > 31: # day should only be an integer from 1 to 31
                print("Invalid Number") 
            
            elif d > 0 and d < 10: # if the day is a single digit, add a leading zero to avoid sematic errors with the datetime module
                d = "0" + str(d)
                break
            
            else:
                break
        
        except ValueError:
            print("Invalid Input")
    
    while True:
        try:
            hr = int(input("Enter Hour (1-12): "))
            
            if hr < 1 or hr > 12: # since 12 hour format is being used, hr should only be from 1 o 12
                print("Invalid number.")
            
            elif hr >= 1 and hr < 10: # for one digit values, add a leading zero
                hr = "0" + str(hr)
                break
            
            else:
                break
        
        except ValueError:
            print("Invalid Input")
    
    while True:
        try:
            min = int(input("Enter Minute (0-59): ")) # minute should only be from 0 to 59 
            
            if min < 0 or min > 59: 
                print("Invalid Number")
            
            elif min > 0 and min < 10: # for one digit values, add a leading zero 
                min = "0" + str(min)
                break
            
            else: 
                break
        
        except ValueError:
            print("Invalid Input")

    while True:
        ampm = input("AM or PM: ") # since we are using the 12 hour format, am or pm is required to distinguish time clearly
        
        if ampm.upper() == "AM" or ampm.upper() == "PM": # am and pm is always turned into upper case
            break
        
        if len(ampm) == 0: # if nothing was entered
            print("Please Enter if AM or PM")
        
        else:
            print("Invalid Input.")
    
    return str(y) + str(m) + str(d) + str(hr) + str(min) + ampm # concatenates the values together then returns it

def date_only(): # only for a choice at search file, this is similar to set date function but without the time inputs
    while True: 
        try:
            y = int(input("Enter Year (Ex: 2023): "))
            
            if y < 0 or len(str(y)) < 4:
                print("Invalid Input.")
            
            else:
                break
        
        except ValueError:
            print("Invalid Input.")
        
    while True:
        try:
            m = int(input("Enter Month (1-12): "))
            
            if m < 1 or m > 12:
                print("Invalid Number.")
            
            elif m > 0 and m < 10:
                m = "0" + str(m)
                break
            
            else:
                break
        
        except ValueError:
            print("Invalid Input.")
    
    while True:
        try:
            d = int(input("Enter Day (1-31): "))
            
            if d < 1 or d > 31:
                print("Invalid Number")
            
            elif d > 0 and d < 10:
                d = "0" + str(d)
                break
            
            else:
                break
        
        except ValueError:
            print("Invalid Input")
    
    return str(y) + str(m) + str(d)

def time_only():
    while True:
        try:
            hr = int(input("Enter Hour (1-12): "))
            
            if hr < 1 or hr > 12: 
                print("Invalid number.")
            
            elif hr >= 1 and hr < 10: 
                hr = "0" + str(hr)
                break
            
            else:
                break
        
        except ValueError:
            print("Invalid Input")
    
    while True:
        try:
            min = int(input("Enter Minute (0-59): "))
            
            if min < 0 or min > 59: 
                print("Invalid Number")
            
            elif min > 0 and min < 10: 
                min = "0" + str(min)
                break
            
            else: 
                break
        
        except ValueError:
            print("Invalid Input")

    while True:
        ampm = input("AM or PM: ") 
        
        if ampm.upper() == "AM" or ampm.upper() == "PM": 
            break
        
        if len(ampm) == 0: 
            print("Please Enter if AM or PM")
        
        else:
            print("Invalid Input.")

    return str(hr) + str(min) + ampm 

def enter_discount(coupon):
    discount = float(0)

    if coupon == "PASS_MATH27":
        discount = 30.00
        print("You have successfully redeemed PASS_MATH27 for ", discount, "% ", "discount.")

    elif coupon == "NO_FINALS":
        discount = 75.00
        print("You have successfully redeemed NO_FINALS for ", discount, "% ", "discount.")
    
    else:
        print("This discount code does not exist. Try again.")
    
    return discount

def edit_movie():
    if len(movies) == 0: # prompt the admin if there are no movies yet
        print("There are currently no available movies in the program. Add the first movie today!")
        return admin_page()
    
    else:
        print("\nWhat do you want to edit?\n[1] Edit Movie Name \n[2] Edit Movie Genre\n[3] Edit Movie Restriction\n[4] Edit Date and Time of Viewing\n[0] None, Return to Main Menu")
        change = int(input("\nChoice: ")) 
        
        if change == 0:
                print("Returning to Administrator Page...") 
                return admin_page()
        
        else:
            print("Please enter the Movie ID of the Movie you wish to edit.")
            data = input("Enter the Movie ID: ") # movie id will determine the information that will be changed
            
            if data in movies:
                print("\n===================== MOVIE INFORMATION =====================") # prints all movie info so that user can think about the edit
                print(f"Movie ID: {data}") 
                print(f"Movie Name: {str(movies[data]['movie_name'])}")
                print(f"Movie Genre: {str(movies[data]['movie_genre'])}")
                print(f"Movie Restriction: {str(movies[data]['movie_restriction'])}")
                print(f"Movie Venue: Cinema {str(movies[data]['movie_venue'])}")
                print(f"Date and Time of Viewing: {str(movies[data]['date_time_viewing'])}")
                print(f"Date and End Time of Viewing: {str(movies[data]['end_time_viewing'])}")
                print(f"Movie Price: @{float(movies[data]['movie_price'])}")
                print("--------------------------------------------------------------")
                
                if change == 1:
                    while True:
                        new_an = input("\nEnter New Movie Name: ").title() 
                        
                        if check_string(new_an) == False: 
                            print("Invalid New Movie Name. Please try again.")
                        
                        elif new_an == movies[data]['movie_name']: 
                            print("You have entered the same Movie Name!")
                            return edit_movie()
                        
                        else:
                            movies[data]['movie_name'] = new_an 
                            save_file()
                            print(f"Movie Name has been successfully changed to {movies[data]['movie_name']}!")
                            return edit_movie()
                
                elif change == 2:
                    while True:
                        new_genre = input("\nMovie Main Genres:\nFamily\nAction\nComedy\nDrama\nFantasy\nHorror\nMystery\nRomance\nThriller\n\nEnter New Movie Genre: ").title() 
                        
                        if check_string(new_genre) == False:
                            print("Invalid New Movie Genre. Please try again.")
                        
                        elif new_genre == movies[data]['movie_genre']: 
                            print("You have entered the same Movie Genre! Please try again.")
                            return edit_movie()
                        
                        else:
                            movies[data]['movie_genre'] = new_genre
                            print(f"Movie Genre has been successfully changed to {movies[data]['movie_genre']}!")
                            save_file()
                            return edit_movie()
                
                elif change == 3:
                    while True:
                        new_restriction = input("\nMovie Restrictions:\nRated G: General audiences - All ages admitted\nRated PG: Parental guidance suggested - Some material may not be suitable for children\nRated PG-13: Parents strongly cautioned - Some material may be inappropriate for children under 13\nRated R: Restricted - Under 17 requires accompanying parent or adult guardian\n\nEnter New Movie Restriction: ").title() 
                        
                        if check_string(new_restriction) == False:
                            print("Invalid New Movie Restriction. Please try again")
                        
                        elif new_restriction == movies[data]['movie_restriction']: 
                            print("You have entered the same Movie Restriction!")
                            return edit_movie()
                        
                        else:
                            movies[data]['movie_restriction'] = new_restriction
                            print(f"Movie Restriction has been successfully changed to {movies[data]['movie_restriction']}!")
                            save_file()
                            return edit_movie()
                
                elif change == 4:
                    while True:
                        print("\nEdit Movie's Date and Time of Viewing")
                        try: 
                            date_time_viewing = set_date() # calls the set_date function; user will enter desired date and time info
                            formatviewing = datetime.strptime(date_time_viewing,'%Y%m%d%I%M%p') # let the program know which of these parts of the string corresponds to the elements of the date and time
                            new_dt_viewing = formatviewing.strftime('%m-%d-%Y %I:%M %p') # sets date and time into this format
                            break
                        
                        except ValueError: 
                            print("Invalid Date. Please try again \n")

                    while True:
                        try:
                            print("\nEdit Movie's End Date and Time of Viewing")
                            edviewing = set_date() # same as date and time of start time
                            formatedviewing = datetime.strptime(edviewing,'%Y%m%d%I%M%p')
                            new_ed_viewing = formatedviewing.strftime('%m-%d-%Y %I:%M %p')

                            if formatviewing > formatedviewing: # prompt the user to try again if start time is later than end time
                                print("Invalid Input. Start time must be earlier than the End Time of Viewing")
                                return edit_movie()
                                
                            elif formatviewing == formatedviewing: # prompt the user to try again if start time is the same as the end time
                                print("Invalid Input. Start time must not be the same as the End Time of Viewing")
                                return edit_movie()

                            if formatviewing < datetime.today(): # prompt the user to try again if start time and/or end time is behind the date today
                                print("Date and time of viewing must not be from the past.")
                            
                            if new_dt_viewing == (movies[data]['date_time_viewing']): # if input is the same as dictionary value
                                print("You have entered the same date and time of viewing as before!")
                                return edit_movie()

                            elif (new_dt_viewing + new_ed_viewing) == (movies[data]['date_time_viewing'] + movies[data]['end_time_viewing']):
                                print("You have entered the same start and end date and time of viewing!")
                                return edit_movie()
                            
                            else:
                                movies[data]['date_time_viewing'] = new_dt_viewing # if all inputs are valid, set the new dates as the new values of the keys in the specified movie_id
                                movies[data]['end_time_viewing'] = new_ed_viewing 
                                save_file() 
                                print(f"Date and Time of Viewing has been successfully changed to {movies[data]['date_time_viewing']}!") # prompts the user that change has been applied
                                print(f"End Time of Viewing has been successfully changed to {movies[data]['end_time_viewing']}!") 
                                return admin_page()
                        
                        except ValueError: # executes when the datetime module doesn't validate the date; user will be prompted to try again
                            print("\nInvalid Date. Please try again")
                       
                else:
                    print("\nInvalid input. Please try again") 
                    return edit_movie()
            
            else:
                print("\nSorry that movie doesn't exist!")
                return edit_movie()

def delete_movie():
    if len(movies) == 0:
        print("There are currently no available movies in the program. Add the first movie today!")
        return admin_page()
    
    else:
        print("\nPlease enter the Movie ID of the movie you wish to delete.")
        data = input("Enter Movie ID: ") # determines the movie to be deleted
        
        if data in movies:
            print("\n===================== MOVIE INFORMATION =====================") 
            print(f"Movie ID: {data}") 
            print(f"Movie Name: {str(movies[data]['movie_name'])}")
            print(f"Movie Genre: {str(movies[data]['movie_genre'])}")
            print(f"Movie Restriction: {str(movies[data]['movie_restriction'])}")
            print(f"Movie Venue: Cinema {str(movies[data]['movie_venue'])}")
            print(f"Date and Time of Viewing: {str(movies[data]['date_time_viewing'])}")
            print(f"Date and End Time of Viewing: {str(movies[data]['end_time_viewing'])}")
            print(f"Movie Price: @{int(movies[data]['movie_price'])}")
            customer_list = [x for x in movies[data]['customers'].split(",") if x != ""] # gets list of customers; removes default empty value at customers_list[0]
            print(f"Customers: ")
            
            for customer in customer_list: # iterates through every item in customers_list
                print(f"- {customer}") # prints every customer
                print("--------------------------------------------------------------")
                print("\nAre you sure you want to delete this movie? You cannot recover the data once deleted.") 
                choice = input("\n[1] Yes, I am sure\n[0] No, Return to Main Menu\n\nChoice: ") 
            
                if choice == "1": 
                    movies.pop(data) # removes the key in the dictionary 
                    save_file()
                    print(f"Movie {data} has been successfully deleted!")
                    return admin_page()
            
                elif choice == "0":
                    print("Returning to Administrator Page...") 
                    return admin_page()
            else:
                print("Sorry that movie doesn't exist!")
                return delete_movie()

def a_view_movies():
    if len(movies) == 0:
        print("\nThere are currently no available movies in the program. Add the first movie today!")
        return admin_page()
    
    else:
        print("\nHow do you want to view the Movies?\n[1] All Movies\n[2] Movies in a Cinema by Day\n[3] Details of a Movie\n[4] By Movie Name \n[0] None, Return to Administrator Page")
        view = int(input("\nChoice: "))
        
        if view == 1:
            print("\n======= LIST OF ALL MOVIES =======")
            key = "date_time_viewing"
            dtv_list = sorted([val[key] for keys, val in movies.items() if key in val]) 
            print(dtv_list)
            n_dtv = []
            
            for x in dtv_list:
                g = datetime.strptime(x, '%m-%d-%Y %I:%M %p') 
                n = g.strftime('%b %d, %Y') 
                if n not in n_dtv: 
                    n_dtv.append(n) 
            
            for i in n_dtv: 
                print(f"Viewing Date: {i}") 
                
                for j in movies: 
                    grab2 = datetime.strptime(movies[j]['date_time_viewing'], '%m-%d-%Y %I:%M %p') 
                    nd2 = grab2.strftime('%b %d, %Y') 
                    
                    if i == nd2: 
                        print(f"> Movie {j}: {str(movies[j]['movie_name'])} | {str(movies[j]['date_time_viewing'])} | Cinema {str(movies[j]['movie_venue'])}")
                        customer_list = [x for x in movies[j]['customers'].split(",") if x != ""] 
                        print(f"    Customers: ")
                        
                        for customer in customer_list: 
                            print(f"    > {customer}") 
                print("-------------------------------------------------")
            return a_view_movies()
        
        elif view == 2:          
            print("\n======= LIST OF MOVIES IN A CINEMA BY DAY =======")
            venue = input("Choose a cinema")
            date = str(datetime.strftime(datetime.strptime(input("Enter Date"), '%m-%d-%Y'), '%m-%d-%Y'))

            print(f"Movies at Cinema {venue} on {date}")
            for k, v in movies.items():
                if v['movie_venue'] == venue and v['date_time_viewing'][:10] == date:
                    print(f"{k} - {v['movie_venue']}") #prints only movie id and venue
            return a_view_movies()

        elif view == 3:
            movie = input("Enter Movie ID: ")
            print(f"\n======= MOVIE {movie} DETAILS =======")
            seats = 0
            for i in movies[movie]['seats'].split(','):
                if i == "XX":
                    seats += 1

            print(f"Movie {movie} details:")
            print(f"Name: {movies[movie]['movie_name']}")
            print(f"Genre: {movies[movie]['movie_genre']}")
            print(f"Restriction: {movies[movie]['movie_restriction']}")
            print(f"Venue: Cinema {movies[movie]['movie_venue']}")
            print(f"Date and Time of Viewing: {movies[movie]['date_time_viewing']} - {movies[movie]['date_time_viewing'][-8:]}")
            print(f"Price: {movies[movie]['movie_price']}")
            print(f"Total Earnings: {int(movies[movie]['movie_price']) * seats}")
            return a_view_movies()
        
        elif view == 4:
            name = input("Enter movie name: ")
            print("\n========= LIST OF MOVIES BY MOVIE NAME =========") 
            key = "date_time_viewing"
            dtv_list = sorted([val[key] for keys, val in movies.items() if key in val]) 
            n_dtv = []
            
            for x in dtv_list:
                g = datetime.strptime(x, '%m-%d-%Y %I:%M %p') 
                n = g.strftime('%b %d, %Y') 
                if n not in n_dtv: 
                    n_dtv.append(n) 
            
            for i in n_dtv: 
                for j in movies: 
                    grab2 = datetime.strptime(movies[j]['date_time_viewing'], '%m-%d-%Y %I:%M %p') 
                    nd2 = grab2.strftime('%b %d, %Y') 
                    
                    if i == nd2 and name == movies[j]['movie_name']: 
                        print(f"> Movie {j}: {str(movies[j]['movie_name'])}")
                        print(f"{str(movies[j]['date_time_viewing'])} {str(movies[j]['movie_venue'])}")
                        customer_list = [x for x in movies[j]['customers'].split(",") if x != ""] 
                        print(f"    Customers: ")
                        
                        for customer in customer_list: 
                            print(f"    > {customer}") 
                print("-------------------------------------------------") 
            return a_view_movies()

        elif view == 0:
            print("Returning to Administrator Page...") 
            return admin_page()
        
        else:
            print("INVALID INPUT. PLEASE TRY AGAIN.")
            a_view_movies()

def search_movie():
    if len(movies) == 0:
        print("There are currently no available movies in the program. Add the first movie today!")
    
    else:
        print("\nWhat do you want to search for?\n[1] All Movies With Available Seats\n[2] All Movies on a Specific Date\n[0] None, Return to Main Menu")
        find = int(input("\nChoice: "))
        
        if find == 0:
            print("Returning to Administrator Page...") 
            return admin_page()

        elif find == 1:
            print("======= LIST OF MOVIES WITH AVAILABLE SEATS =======")
            
            for j in movies: 
                avail = [value for value in movies[j]['seats'].split(',') if value != "XX"] 
                
                if len(avail) != 0: 
                    print(f"> Movie {j}: {str(movies[j]['movie_name'])} ({len(avail)} seats left)")
                
                elif len(avail) == 0: 
                    print(f"> Movie {j}: {str(movies[j]['movie_name'])} (No more seats avaiable)")
            
            print("----------------------------------------------------")     
            return search_movie()

        elif find == 2:
            print("Enter the Viewing Date that you want to search for")
            ddt = date_only() 
            grab = datetime.strptime(ddt, '%Y%m%d') 
            nd = grab.strftime('%b %d, %Y') 
            key = "date_time_viewing"
            dtv_list = list(set([val[key] for keys, val in movies.items() if key in val])) 
            listdt = [] 
            
            for i in dtv_list: 
                g = datetime.strptime(i, '%m-%d-%Y %I:%M %p') 
                x = g.strftime('%b %d, %Y') 
                
                if x not in listdt: 
                    listdt.append(x)
            
            if nd in listdt: 
                print(F"\n============= LIST OF MOVIES ON {nd} =============")
                
                for j in movies: 
                    grab2 = datetime.strptime(movies[j]['date_time_viewing'], '%m-%d-%Y %I:%M %p') 
                    nd2 = grab2.strftime('%b %d, %Y') 
                    
                    if nd == nd2: 
                        print(f"> Movie {j}: {str(movies[j]['movie_name'])} | {movies[j]['date_time_viewing']}") 
                
                print("-----------------------------------------------------------")
                return search_movie()
            
            else:
                print("Sorry, it seems like there is no available movie on that day.")
                return search_movie()
        else:
            print("INVALID INPUT. PLEASE TRY AGAIN.")
            search_movie()

def p_view_movies():
    if len(movies) == 0:
        print("There are currently no available movies in the program. Add the first movie today!")
        return cashier_page()
    
    else:
        print("\nHow do you want to view the movies?\n[1] Using Viewing Date\n[2] Using Movie Genre\n[3] Using Movie Restriction\n[4] Using Movie Venue\n[0] None, Return to Main Menu")
        view = int(input("\nChoice: "))
        
        if view == 1:
            print("\n======= LIST OF MOVIES BY VIEWING DATE =======")
            key = "date_time_viewing"
            dtv_list = sorted(list(set([val[key] for keys, val in movies.items() if key in val]))) 
            n_dtv = []
            
            for x in dtv_list:
                g = datetime.strptime(x, '%m-%d-%Y %I:%M %p')
                n = g.strftime('%b %d, %Y')
                
                if n not in n_dtv:
                    n_dtv.append(n)
            
            for i in n_dtv:
                print(f"Viewing Date: {i}")
                
                for j in movies:
                    grab2 = datetime.strptime(movies[j]['date_time_viewing'], '%m-%d-%Y %I:%M %p')
                    nd2 = grab2.strftime('%b %d, %Y')
                    avail = [value for value in movies[j]['seats'].split(',') if value != "XX"] 

                    if i == nd2 and len(avail) != 0:
                        print(f"> Movie ID {j}: {str(movies[j]['movie_name'])} | Cinema {str(movies[j]['movie_venue'])} | {len(avail)} available seats | @{str(movies[j]['movie_price'])}")
                
                    elif i == nd2 and len(avail) == 0: 
                        print(f"> Movie ID {j}: {str(movies[j]['movie_name'])} | No more seats avaiable")
                
                print("----------------------------------------------------------------------------------------------")
            
            return p_view_movies()
        
        elif view == 2:
            print("\n======= LIST OF MOVIES BY GENRE =======") 
            key = "movie_genre"
            restriction_list = sorted(list(set([val[key] for keys, val in movies.items() if key in val])))
            
            for i in restriction_list:
                print(f"Movie Genre: {i}")
                
                for j in movies:
                    avail = [value for value in movies[j]['seats'].split(',') if value != "XX"] 

                    if i == movies[j]['movie_genre'] and len(avail) != 0:
                        print(f"> Movie ID {j}: {str(movies[j]['movie_name'])} | Date and Time: {str(movies[j]['date_time_viewing'])} | Cinema {str(movies[j]['movie_venue'])} | {len(avail)} available seats | @{str(movies[j]['movie_price'])}")
                
                    elif i == movies[j]['movie_genre'] and len(avail) == 0: 
                        print(f"> Movie ID {j}: {str(movies[j]['movie_name'])} | No more seats avaiable")

                print("----------------------------------------------------------------------------------------------")
            
            return p_view_movies()

        elif view == 3:
            print("\n======= LIST OF MOVIES BY RESTRICTION =======") 
            key = "movie_restriction"
            restriction_list = sorted(list(set([val[key] for keys, val in movies.items() if key in val])))
            
            for i in restriction_list:
                print(f"Movie Restriction: {i}")
                
                for j in movies:
                    avail = [value for value in movies[j]['seats'].split(',') if value != "XX"] 

                    if i == movies[j]['movie_restriction'] and len(avail) != 0:
                        print(f"> Movie ID {j}: {str(movies[j]['movie_name'])} | Date and Time: {str(movies[j]['date_time_viewing'])} | Cinema {str(movies[j]['movie_venue'])} | {len(avail)} available seats | @{str(movies[j]['movie_price'])}")
                
                    elif i == movies[j]['movie_restriction'] and len(avail) == 0: 
                        print(f"> Movie ID {j}: {str(movies[j]['movie_name'])} | No more seats avaiable")
                
                print("---------------------------------------------------------------------------------")
            
            return p_view_movies()

        elif view == 4:
            print("\n======= LIST OF MOVIES BY VENUE =======") 
            key = "movie_venue"
            venue_list = sorted(list(set([val[key] for keys, val in movies.items() if key in val])))
            
            for i in venue_list:
                print(f"Cinema: {i}")
                
                for j in movies:
                    avail = [value for value in movies[j]['seats'].split(',') if value != "XX"] 

                    if i == movies[j]['movie_venue'] and len(avail) != 0:
                        print(f"> Movie ID {j}: {str(movies[j]['movie_name'])} | Date and Time: {str(movies[j]['date_time_viewing'])} | {len(avail)} available seats | @{str(movies[j]['movie_price'])}")
                
                    elif i == movies[j]['movie_venue'] and len(avail) == 0: 
                        print(f"> Movie ID {j}: {str(movies[j]['movie_name'])} | No more seats avaiable")

                print("---------------------------------------------------------------------------------")
            
            return p_view_movies()

        elif view == 0:
            print("Returning to Cashier Page...") 
            return cashier_page()

        else:
            print("INVALID INPUT. PLEASE TRY AGAIN.")
            return p_view_movies()

def book_seat():
    total = float(0)
    if len(movies) == 0:
        print("There are currently no available movies in the program. Add the first movie today!")
        return cashier_page()
    
    else:
        print("\nWelcome to the Movie Theater Booking System, Customer!/n")

        print("\n======= LIST OF MOVIES BY VENUE =======")
        key = "movie_venue"
        venue_list = sorted(list(set([val[key] for keys, val in movies.items() if key in val])))
            
        for i in venue_list:
            print(f"Cinema: {i}")
                
            for j in movies:
                avail = [value for value in movies[j]['seats'].split(',') if value != "XX"] 

                if i == movies[j]['movie_venue'] and len(avail) != 0:
                    print(f"> Movie ID {j}: {str(movies[j]['movie_name'])} | Date and Time: {str(movies[j]['date_time_viewing'])} | {len(avail)} available seats | @{str(movies[j]['movie_price'])}")
                
                elif i == movies[j]['movie_venue'] and len(avail) == 0: 
                    print(f"> Movie ID {j}: {str(movies[j]['movie_name'])} | No more seats avaiable")
            
            print("---------------------------------------------------------------------------------")

        data = input("\nEnter the Movie ID of your desired movie: ") # movie id must first be determined
        
        if movies[data]['seats'].split(',').count("XX") == int(movies[data]['max_pax']):
            print("There are no more available seats on that venue.")
            return cashier_page()
        
        else:
    
            if data in movies:
                movie_venue = movies[data]['movie_venue'] 
                max_pax = movies[data]['max_pax']
                seating(movie_venue, data) # pass the movie_venue and the flight id to the seating function 
                occupied = "XX" # set occupied to 'XX'
                seat_list = movies[data]['seats'].split(",") # places every item separated by the delimiter "," in a list; the items are the seat codes
                print(f"\nGood day, Customer! You have chosen the movie, {str(movies[data]['movie_name'])}.")
                
                while True:
                    seat = input(f'Enter the seat code of the one you desire (XX - Occupied Seat): ').upper() # upper was utilized since seat code alpha characters are always uppercase
                    
                    if seat == occupied: # customer cannot take an occupied seat, hence, customer will be prompted and asked to try again
                        print("Sorry, that seat seems to be taken already. Please try again")
                    
                    elif seat not in seat_list: # customer will be prompted if entered seat does not exist
                        print("Sorry, that seat doesn't seem to exist.")
                    
                    else:
                        break # if seat code is valid, continue 
                
                for i in range(0,int(max_pax)): # i is an integer from the range 0 to max_pax (doesn't include either 10 or 15 since we are going to iterate through a list)
                    if seat == seat_list[i]: # finds the seat which is equivalent to the one in seat_list
                        seat_list[i] = occupied # set seat_list to occupied
                
                movies[data]['seats'] = ','.join([f"{elem}" for elem in seat_list]) # rejoin the items in the list as a string with the delimiter "," then this is set as value of the seats key of the specified movie_id 
                
                while True:
                    customer_name = input('\nTo complete the booking process, please enter your name: ').capitalize() # asks the customer for his or her name

                    if check_string(customer_name) == False: # prompt the user to try again if the input contains invalid characters
                        print("\nNAME MAY HAVE CONTAINED INVALID CHARACTERS. PLEASE TRY AGAIN.")
                    
                    else:
                        customer_list = movies[data]['customers'].split(',')
                        customer_list.append(customer_name)
                        movies[data]['customers'] = ','.join([f"{elem}" for elem in customer_list])
                        break # if input is valid, continue

                while True:
                    purchase = input(f"Are you sure to purchase this seat for @{int(movies[data]['movie_price'])}? (y/n) ")
                    amount_due = 0

                    if purchase == 'y':
                        total += float(movies[data]['movie_price'])
                        use_coupon = input(f"Will you be using coupons? (y/n) ")

                        if use_coupon == 'y':
                            coupon = input("\nEnter coupon code here: ")
                            Discount = enter_discount(coupon)
                            discount_percentage = Discount*100

                            if Discount == enter_discount(coupon):
                                amount_due = (int(movies[data]['movie_price']) * (100-discount_percentage))/100
                                cash = float(input("\nEnter cash: @"))
                                change = cash - amount_due
                                print(f"You have received a change of @{change}.")
                                break
                            
                            elif Discount != enter_discount(coupon):
                                print("Coupon is invalid. Try again.")
                                break
                        
                        elif use_coupon == 'n':
                            break
                    
                    elif purchase == 'n':
                        print("You have cancelled your purchase.")
                        break

                    else:
                        print("Error. Kindly input again. ")

                save_file()
                print(f"\nYou have successfully booked Seat {seat}! Hopefully you enjoy the movie, {customer_name}! Here's your receipt:") # printing a receipt that contains info about the successfully booked seat
                print("\n===================== TICKET INFORMATION =====================")
                print(f"Movie ID: {data}") 
                print(f"Customer Name: {customer_name}")
                print(f"Seat Code: {seat}")
                print(f"Movie Name: {str(movies[data]['movie_name'])}")
                print(f"Movie Genre: {str(movies[data]['movie_genre'])}")
                print(f"Movie Restriction: {str(movies[data]['movie_restriction'])}")
                print(f"Date and Time of Viewing: {str(movies[data]['date_time_viewing'])}")
                print(f"Date and End Time of Viewing: {str(movies[data]['end_time_viewing'])}")
                print(f"Price: @{int(movies[data]['movie_price'])}")
                print(f"Coupon Discount: @{Discount}")
                print(f"Price with Discount: @{change}")
                print("--------------------------------------------------------------")
                return total, cashier_page()
            
            else:
                print("\nSorry, the Movie ID that you entered doesn't seem to exist. Please try again")
                return book_seat()

def seating(movie_venue, data):
    s = movies[data]['seats'].split(",") # movies[data]['seats'] is a string of seat codes separated by a ","; the split function uses this as a delimiter and places the seat codes in a list

    # these are only for customer visualization
    if movie_venue == '1':
        print('\n+------+------+------+------+') # available seats will show up as seat codes, taken seats will show up as 'XX' based on the value of flights[f]['seats']
        print(f'|  {s[0]}  |  {s[5]}  |  {s[10]}  |  {s[15]}  |')
        print('+------+------+------+------+')
        print(f'|  {s[1]}  |  {s[6]}  |  {s[11]}  |  {s[16]}  |')
        print('+------+------+------+------+')
        print(f'|  {s[2]}  |  {s[7]}  |  {s[12]}  |  {s[17]}  |')
        print('+------+------+------+------+')
        print(f'|  {s[3]}  |  {s[8]}  |  {s[13]}  |  {s[18]}  |')
        print('+------+------+------+------+')
        print(f'|  {s[4]}  |  {s[9]}  |  {s[14]}  |  {s[19]}  |')
        print('+------+------+------+------+')

    elif movie_venue == '2':
        print('\n+------+------+------+------+')
        print(f'|  {s[0]}  |  {s[4]}  |  {s[8]}  |  {s[12]}  |')
        print('+------+------+------+------+')
        print(f'|  {s[1]}  |  {s[5]}  |  {s[9]}  |  {s[13]}  |')
        print('+------+------+------+------+')
        print(f'|  {s[2]}  |  {s[6]}  |  {s[10]}  |  {s[14]}  |')
        print('+------+------+------+------+')
        print(f'|  {s[3]}  |  {s[7]}  |  {s[11]}  |  {s[15]}  |')
        print('+------+------+------+------+')

    elif movie_venue == '3':
        print('\n+------+------+------+------+')
        print(f'|  {s[0]}  |  {s[3]}  |  {s[6]}  |  {s[9]}  |')
        print('+------+------+------+------+')
        print(f'|  {s[1]}  |  {s[4]}  |  {s[7]}  |  {s[10]}  |')
        print('+------+------+------+------+')
        print(f'|  {s[2]}  |  {s[5]}  |  {s[8]}  |  {s[11]}  |')
        print('+------+------+------+------+')

    return

movies = {} # declare an empty dictionary
current_id = ["0000"] # set initial value of id to "0000"

Amount = 0 # set initial value of Amount to 0
Discount = 0 # set initial value of Discount to 0

load_file() # load if there are any saved file
user_class() # call user class function
save_file() # also save file after exit
