import datetime
import pytz
import time
import re
seats=[ [1,2,3,4,5,6],
        [7,8,9,"Booked",11,12],
        [13,14,15,16,17,18],
        [19,20,21,"Booked",23,24],
        [25,26,27,28,29,30],
        [31,"Booked",33,34,"Booked",36],
        [37,38,39,40,41,42],
        [43,44,45,"Booked",47,48],
        [49,50,51,52,53,54],
        [55,56,"Booked",58,59,60]]
                                                  
                                                     
class login_existuser:
     def login(self):
        self.user_email=input("EMAIL: ")
        self.password=input("PASSWORD : ")
        self.welcome()
     def welcome(self):
        if self.user_email in user_credentials:
            c=user_credentials[self.user_email]
            if(self.password==c[0]):
                print("Welcome user ",c[1])
                u.append(self.user_email)
            else:
                print("Invalid credentials")
                self.login()
                
        else:
            print("This email is not registered ")
                
class signup:
    def add_details(self):
        self.user_email=input("Email : ")
        self.user_name=input("Username : ")
        self.check_password()
    def check_password(self):
        self.user_password=input("Password : ")
        if(bool(re.search('^[a-zA-Z0-9]*$',self.user_password)) == False):
            print("signin successful")
            u.append(self.user_email)
        else:
            print("Password must contain atleast one number or special character")
            self.check_password()

class admin_login:
    def log_in(self):
        self.__id=input("ADMIN ID (A)")
        self.__password=input("ADMIN PASSWORD (1) ")
        self.validate()
    
    def validate(self):
        if(self.__id)=='A' and self.__password=='1':
            print("Signin successful")
        else:
            print("Invalid credentials")
            self.log_in()
            
            

class airlines:
    def __init__(self,flight_no=None,flight_name=None,flight_date=None,source=None,destination=None,fare=None):
        self.flight_no=flight_no
        self.flight_name=flight_name
        self.flight_date=flight_date
        self.source=source
        self.destination=destination
        self.fare=fare
    
    def hardcoded(self):
        available_flight.append(self)
        print(available_flight)
    
class search_flight(airlines):
    
    def available(self):
        self.ret_status=0
        f_det=input("Search by date / flight number/flight name : \n")
        for f in available_flight:
            if (f_det in f.flight_no) or (f_det in f.flight_name) or (f_det in f.flight_date):
                
                print("Flight number : ",f.flight_no)
                print("Flight name : ",f.flight_name)
                print("DOJ :" ,f.flight_date)
                print("Source :",f.source)
                print("destination :",f.destination)
                print("Normal class fare RS. :",f.fare)
                print('----------------------------------------\n')
                self.ret_status+=1 
        if not(self.ret_status):
            print("No flight available for given details : \n")
    
class book_flight():
 

    
    def bookflight(self):
        
        self.bookings=[]
        self.ticket=[]
        self.ticketcost=0
        self.fli_no=input("Enter the flight number you want to book")
        c=0
        for f in available_flight:
            
            if(self.fli_no == f.flight_no):
                c+=1 
                
                print("AVailable seats in flight  ",self.fli_no)
                count=1
                for i in seats:
                    for j in i:
                        if(count==1):
                            print("-------Economy class-------\n")
                        elif(count==19):
                            print("------- Premium economy -------\n")
                        elif(count==31):
                            print("------- Business class ------\n")
                        elif(count==49):
                            print("-------First class-------\n")
                        count+=1 
                        print(j,end=" ")
                    print('\n')
                self.n=int(input("Number of tickets"))
                while(self.n):
                    self.temp=[]
                    self.temp=[f.flight_no,f.flight_name,f.flight_date,f.source,f.destination]
                    self.ticket_count=0
                    self.class_=input("1.Ecnonomy class\n2.Premium economy\n3.Business class\n4.First class  : ")
                    self.seat_no=int(input("Seat number : "))
                    
                    if(self.class_=='E') and self.seat_no>=1 and self.seat_no<=18:
                        self.cost=f.fare
                        self.book_ticket()
                    elif(self.class_ =="PE") and self.seat_no>=19 and self.seat_no<=30:
                        self.cost=f.fare+800
                        self.book_ticket()
                    elif(self.class_=='B') and self.seat_no>=31 and self.seat_no<=48:
                        self.cost=f.fare+1500
                        self.book_ticket()
                    elif(self.class_=='F') and self.seat_no>=49:
                        self.cost=f.fare+3000
                        self.book_ticket()
        if c==0:
            print("No flights available \n")
                                    
                    
                
    def book_ticket(self):
                    
                    for i in range(len(seats)):
                        for j in range(len((seats)[i])):
                            if(seats[i][j]==self.seat_no):
                                s=""
                                self.ticket_count=1 
                                (seats[i][j])="Booked" 
                                self.ticketcost+=self.cost
                                
                                self.temp.append(u[0])
                                self.temp.append(self.cost)
                                self.temp.append(self.seat_no)
                                current_time = str(datetime.datetime.now(pytz.timezone('Asia/Kolkata')))
                                self.temp.append(current_time)
                                
                                
                                
                                
                    if(self.ticket_count==1):
                        
                        print("------- Your seat has been booked ---------\n ")
                        self.ticket.append(self.temp)
                        
                    
                        
                        self.n=(self.n)-1
                        print(seats)
                        
                    else:
                        print("Seat unavailable \n Choose another seat")
                
                    if self.n ==0:
                    
                        print("Proceed with payment to confirm your booking \n")
                        print("Ticket cost",self.ticketcost)
                        self.payment()
                        
                    
    def payment(self):
            self.cardno=input("card no")
            self.cvv=input("Enter cvv")
            print("Payment is successful\n----------Your ticket details-----------\n")
            
            self.show_ticket()
            
    
    def show_ticket(self):
        
        
        for i in self.ticket:
           
            print("Flight_no :",i[0])
            print("Flight_name :",i[1])
            print("Date-of-journey :",i[2])
            print("Source place :",i[3])
            print("Destination place :",i[4])
            print("Seat no :",i[-2])
            print("Ticket cost :",i[-3])
            print("--------------------------------------------------")
            
            admin_booking.append(i)
            
        self.ticket=[]
        
    
class show_booking():
    
    def admin_bookings(self):
        self.date_=input("See bookings by date : ")
        if(admin_booking)==[]:
            print("Booking is empty")
        
        
        for i in admin_booking:
            if(i[2]==self.date_):
                print("User id", i[-4])
                print("Flight_no :",i[0])
                print("Flight_name :",i[1])
                print("Date-of-journey :",i[2])
                print("Source place :",i[3])
                print("Destination place :",i[4])
                print("Seat no :",i[-2])
                print("Ticket cost :",i[-3])
                print("Date of booking ",i[-1])
                print('---------------------------------------')
            
            
            
if __name__=="__main__":
    
    user_credentials={'abc':['123','Yoga'],'xyz':['a@1','Sanjay']}
    available_flight=[]
    admin_booking=[]
    print("Welcome to book my flight!!!\n")
    
    while(True):
        
        user_type=input("USER(u) / ADMIN (a): ")
        
        if(user_type=='u' ):
            u=[]
            n=int(input("1.Login \n2.Signup : "))
            if(n==1):
                user=login_existuser()
                user.login()
            elif(n==2):
                user=signup()
                user.add_details()
                
            def choice_():
                choice=int(input("1.Search for a flight\n2.Book a ticket\n3.Logout"))
                if(choice==1):
                    search=search_flight()
                    search.available()
                    choice_()
                elif(choice==2):
                    b=book_flight()
                    b.bookflight()
                    choice_()
                else:
                    pass
                
            choice_()
            
                
            
        else:
            
            admin=admin_login()
            admin.log_in()
            def choice_():
                print("1.Add a flight\n2.See bookings\n3.Logout\n")
                
                choice=int(input())
                if(choice==1):
                    
                    num=input("Enter the FLight no to add : ")
                    name=input("Enter the Flight name to add : ")
                    date=input("Enter the Date of journey: ")
                    source=input("Enter the Source ")
                    destination=input("Enter the Destination : ")
                    fare=int(input("Enter the Ticket Fare "))
                    
                    flight_add=airlines(num,name,date,source,destination,fare)
                    flight_add.hardcoded()
                    choice_()
                elif(choice==2):
                    see=show_booking()
                    see.admin_bookings()
                    choice_()
                
                else:
                    pass 
            choice_()



                    
                
                
        
        
            

