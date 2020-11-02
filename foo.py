import re
import sys
import codecs


class Highlight():

	def __init__(self, title, location, year, month, day, hour, minute, second, text):
		self.title = title
		#self.locationDate = lc
		self.text = text
		self.location = location
		self.year = year
		self.month = month
		self.day = day
		self.hour = hour
		self.minute = minute
		self.second = second


	def __str__(self):
		output_string = ""
		output_string = output_string + "Title : %s \t Location: %s \n Highlight: %s \n" % (self.title, self.location, self.text)
		output_string = output_string + "Timestamp : %s-%s-%s %s:%s:%s\n" % (self.year, self.month, self.day, self.hour,self.minute,self.second)
		return output_string

	def setTitle(self, title):
		self.title = title

	def getTitle(self):
		return self.title

	def setLocationDate(self, lc):
		self.locationDate = lc

	def getLocationDate(self):
		return self.locationDate

	def setText(self,text):
		self.text = text

	def getText(self):
		return self.text

	def setLocation(self,text):
		self.text = location

	def getLocation(self):
		return self.location

	def setYear(self,year):
		self.year = year

	def getYear(self):
		return self.year

	def setMonth(self,month):
		self.month = month

	def getMonth(self):
		return self.month

	def setDay(self,day):
		self.day= day

	def getDay(self):
		return self.day

	def setHour(self,hour):
		self.hour= hour

	def getHour(self):
		return self.hour

	def setMinute(self,minute):
		self.minute=minute

	def getMinute(self):
		return self.minute

	def setSecond(self,second):
		self.second= second

	def getSecond(self):
		return self.second






def readFile():
	filename = r"c.txt"
	with open(filename, encoding = "utf-8") as f:
		contents = f.readlines()
	return contents


def parseTimestampMonth(rawTimeStamp):
	if "January" in rawTimeStamp:
		return 1
	elif "Feburary" in rawTimeStamp:
		return 2
	elif "March" in rawTimeStamp:
		return 3
	elif "April" in rawTimeStamp:
		return 4
	elif "May" in rawTimeStamp:
		return 5
	elif "June" in rawTimeStamp:
		return 6
	elif "July" in rawTimeStamp:
		return 7
	elif "August" in rawTimeStamp:
		return 8
	elif "September" in rawTimeStamp:
		return 9
	elif "October" in rawTimeStamp:
		return 10
	elif "November" in rawTimeStamp:
		return 11
	elif "December" in rawTimeStamp:
		return 12
	else:
		return None


def parseTimestampAMPM(rawTimeStamp):
	return rawTimeStamp[-2:]


def parseTimestampTime(rawTimeStamp):
	pattern = r"\d{1,2}:\d{1,2}:\d{1,2}"
	string = rawTimeStamp

	#print(re.search(pattern, string))
	time = re.search(pattern, string).group()

	hour = time.split(":")[0]
	minute = time.split(":")[1]
	sec = time.split(":")[2]

	return (hour, minute, sec)
	
def parseTimestampDay(rawTimeStamp):
	#print("In parseTimestampDay")
	pattern = r"\d{1,2},"
	string = rawTimeStamp

	
	#print(re.search(pattern, string))
	day = re.search(pattern, string).group().split(",")[0]
	return day


def parseTimestampYear(rawTimeStamp):
	#print("In parseTimestampYear")
	pattern = r"\d{4}"
	string = rawTimeStamp

	#print(re.search(pattern, string))
	year = re.search(pattern, string).group()
	return year


def parseLocationDate(ld):
	"""Takes a location date string and parses it down into components"""
	# A pipe seperates the location from the time stamp data
	# the location may or may not have a page associated with it
	# so we need to check on the number of segments returned.

	lst = ld.split("|")
	#print(lst)
	if len(lst) == 3:
		raw_page = lst[0]
		raw_location = lst[1]
		raw_timestamp = lst[2]
	else:
		raw_page = "N/A"
		raw_location = lst[0]
		raw_timestamp = lst[1]

	#get the location part	
	location = raw_location.split("Location")[1].strip()

	#get the timestamp part - we still need to break the timestamp down into components
	timeStamp = raw_timestamp.split("Added on")[1]

	y = parseTimestampYear(timeStamp)
	m = parseTimestampMonth(timeStamp)
	d = parseTimestampDay(timeStamp)

	ho,mi,se = parseTimestampTime(timeStamp)
	

	#now we return all the data
	#location
	#year
	#month
	#day
	#hour
	#min
	#sec

	return (location, y,m,d,ho,mi,se)






def parseContents(contents_lst):
	output = []

	while contents_lst:
		title = contents_lst.pop(0).strip()
		locationDate = contents_lst.pop(0).strip()
		newline = contents_lst.pop(0)
		text = contents_lst.pop(0)
		terminator = contents_lst.pop(0)


		#todo : parse out locationDate
		location, year, month, day, hour, minute, second = parseLocationDate(locationDate)

		output.append(Highlight(title, location, year, month, day, hour, minute, second, text))

	return output

	

def main():

	#c is a list of Highlight Objects.
	c = parseContents(readFile())


	for item in c:
		print("%s-%s-%s %s:%s:%s" % (item.getYear(), item.getMonth(), item.getDay(), item.getHour(), item.getMinute(), item.getSecond()), end = "")
		print(item.getTitle(), end=" ")
		print(item.getLocation())
		print(item.getText())
		

if __name__ == "__main__":
	main()
