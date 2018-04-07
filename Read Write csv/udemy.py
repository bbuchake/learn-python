#Import libraries
import csv
import os

#set open file path
open_path = "WebDevelopment.csv"

#define the lists
Title = []
Price = []
Subscriber_Count= []
Number_Reviews = []
Course_Length = []

#Read file
with open(open_path, "r") as open_file:
    open_reader = csv.reader(open_file, delimiter = ",")
    for open_row in open_reader:
        #now we are inside the file reading one row at a time
        Title.append(open_row[1])
        Price.append(open_row[4])
        Subscriber_Count.append(open_row[5])
        Number_Reviews.append(open_row[6])
        Course_Length.append(open_row[9])

#Zip into tuple
save_output = zip(Title, Price, Subscriber_Count, Number_Reviews, Course_Length)

#Write to file
save_path = "udemy.csv"

#write file
with open(save_path, "w", newline = '') as save_file:
    save_writer = csv.writer(save_file, delimiter = ",")
    for output_line in save_output:
        save_writer.writerow(output_line)

