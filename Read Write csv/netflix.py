#Import modules
import csv

user_video = input("Enter name of the video you want to search - ")

#define path
csv_path = "netflix_ratings.csv"

found = False

with open(csv_path, "r") as csv_file:
    csv_reader= csv.reader(csv_file, delimiter = ",")
    for row in csv_reader:
        if(row[0] == user_video):
            #Display user_video, rating and current user ratings
            print("Title: " + row[0] + "\nRating: " + row[1] + "\nUser Rating: " + row[5])
            found = True
            break

    if not found:
        print("Video not found")
    
    
