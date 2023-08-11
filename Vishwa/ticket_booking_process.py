import csv
import random
f=open("Ticketdetails.csv",'a')
writer=csv.writer(f):
def upper_seat():
    upperseat=[]
    for i in range(1,10001):
        upperseat.append(["S"+str(i)])
def lower_seat():
    lowerseat=[]
    for i in range(1,10001):
        lowerseat.append(["S"+str(i)])
    print(upperseat)
upper_seat()
def write_file(username,ticket_number,seat_number,stand):
    



f.close()

f=open("Ticketdetails.csv",'r')
reader=csv.reader(f)
def file_read():
    ticketcount=0
    for i in reader:
        ticketcount+=int(i[2])
        if i[3]=="Upper stand":
            book_list=<no.of seats>
            x=random.choice(upperseat)
            
    
