#parserDataDump.py

import math
import pandas as pd

parsedData =[]

###############
# do data parse
# 1 entry == 1 array
# for each array, form it as a row
# for the below line:
# parsedData.append(row)
###############


def parsedDataToDataframe(parsedData):
	'''dump all rows in data to dataframe'''

	#all fields should be strings***

	# we have 7 data fields per row

	# append this either as a link url or a defined constant
	major = []

	# ie Winter 2015-2016
	season = []

	# course section
	section = []

	# Class ID Number
	classNumber = []

	# Meeting Time
	meetingTime = []

	# Room name/number & Campus
	location = []

	# Instructor - Issue parsing Instructor in parse just enter empter string for this row
	instructor = []


	# so the way this works, we are going to do a Matrix Inversion
	# don't worry about the math, its just turning the table "on its side"
	# for data storage reasons
	# See how for each row I take an element and append it to these new fields?
	for row in parsedData:

		major.append(parsedData[0])

		season.append(parsedData[1])

		section.append(parsedData[2])

		classNumber.append(parsedData[3])

		meetingTime.append(parsedData[4])

		location.append(parsedData[5])

		instructor.append(parsedData[6])


	# This is why it matters the order as well as 

	parsedDataDataFrame = pd.DataFrame({'Major' : major,
										'Season' : season,
										'Section' : section,
										'Class Number' : classNumber,
										'Meeting Time' : meetingTime,
										'Location' : location,
										'Instructor' : instructor})

	parsedDataDataframe.to_csv('Catalog',
								index=False,
								columns=['Major', 'Season', 'Section',
										 'Class Number', 'Meeting Time',
										 'Location', 'Instructor'],
								engine='python')

parsedDataToDataframe(parsedData)