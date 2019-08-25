#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  CSV_Test_File.py
#  
#  Copyright 2019 Pat <pat@pop-os>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  


# def main(args):

	# return 0

# if __name__ == '__main__':
	# import sys
	# sys.exit(main(sys.argv))

import csv #import the csv module to allow the code to work with csv files
import array #imports the array module to allow the code to work with arrays
count = 0
counter = 0
date = array.array('B', [])
row = []

with open('/home/pat/Documents/Bank History.CSV','rb') as csvfile: #opens the csv file as csvfile
	readcsv=csv.reader(csvfile) #creates reader object to read through the csv file
	writer = csv.writer(csvfile) #creates a writer object to write back data to the open csv file
	column7=readcsv.next() #returns the next row in the open csv
	column7.append('dates') #Appends a column for dates after the last column
	data = list(readcsv) #creates a list out of the reader object so it can be iterated through in the while loop
	length=len(data) #figures out the length of the csv so that it can be used in a while loop
	#print(length)
	while count < length: #runs a while loop while it is the value of count is less than length, so that all the dates can be pulled out from the descriptions
		descrip = data[count][3] #Sets the description to be the third column of the csv
		#print(count)
		date_pos = descrip.find("/")-2 #Finds the location of a forward slash and subtracts two from it to find the start of the date
		end_pos = date_pos + 8 #Finds the end of the date by adding 8 to the starting position
		date = descrip[date_pos:end_pos] #Sets the date as equal to the string between the two positions found in the prior two lines
		count = count+1 #Iterates the value of count by 1 so it can be used by the while loop to find when the end of the column has been reached
		data.append(date[count]) #Appends the date found onto the end of the csv row
		#row[count][6] = date
		#writer.writerow(row)
	csvfile.close()
		#print(date)
	#writecsv = csv.writer(csvfile)
	#writecsv.writerow(date)
		#for col in data:
			#print(col[0])
		#while (count<=length)
		#for i in range(0,7):
		
		
		#print(date_pos)
		#print(end_pos)
		# if date_pos<0:
			# print('Breaking')
			# break #Break out and skip row
		# else:
			# print('Working')
			# for i in range (date_pos,end_pos):					
				# date.append(data[date_pos+count])
				# count = count +1
				# print(date)
		# x_dates = str(date)
		# cor_dates = col[5]
		# for row in cor_dates
				# row = x_dates
			
