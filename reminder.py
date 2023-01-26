# File to create reminders
#testing testing testing
#testing testing testing
#------------------------------------------
#---------START REMINDER CLASS-------------
#------------------------------------------
class Reminder():
    def __init__(self, name, date):
        self.name=name
        self.date=date
#------------------------------------------
#-----------END REMINDER CLASS-------------
#------------------------------------------

#------------------------------------------
#----------START PARSING COMMAND-----------
#------------------------------------------

months = ['january', 'february', 'march', 'april', 'may', 'june', 'july',
				'august', 'september', 'october', 'november', 'december']

days_of_week = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday',
				'today', 'tomorrow']

days = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth',
		'tenth', 'eleventh', 'twelfth', 'thirteenth', 'fourteenth', 'fifteenth', 'sixteenth',
		'seventeenth', 'eighteenth', 'nineteenth', 'twentieth', 'twenty-first', 'twenty-second',
		'twenty-third', 'twenty-fourth', 'twenty-fifth', 'twenty-sixth', 'twenty-seventh',
		'twenty-eighth', 'twenty-ninth', 'thirtieth', 'thirty-first']

time_hours = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten',
				'eleven', 'twelve']

time_mins = ['oh one', 'oh two', 'oh three', 'oh four', 'oh five', 'oh six', 'oh seven', 'oh eight', 
				'oh nine', 'oh ten',
				'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen',
				'eighteen', 'nineteen', 'twenty', 'twenty-one', 'twenty-two', 'twenty-three',
				'twenty-four', 'twenty-five', 'twenty-six', 'twenty-seven', 'twenty-eight',
				'twenty-nine', ' thirty', 'thirty-one', 'thirty-two', 'thirty-three', 'thirty-four'
				'thirty-five', 'thirty-six', 'thirty-seven', 'thirty-eight', 'thirty-nine',
				'fourty', 'forty-one', 'forty-two', 'forty-three', 'forty-four', 'forty-five',
				'forty-six', 'forty-seven', 'forty-eight', 'forty-nine', 'fifty', 'fifty-one',
				'fifty-two', 'fifty-three', 'fifty-four', 'fifty-five', 'fifty-six', 'fifty-seven',
				'fifty-eight', 'fifty-nine']

time_phase = ['a m', 'p m']

days_in_months = ['31', '28', '31', '30', '31', '30', '31', '31', '30', '31', '30', '31']
days_in_months_leap = ['31', '29', '31', '30', '31', '30', '31', '31', '30', '31', '30', '31']

def is_there_a_date(string):
	month = 0
	day_of_week = 0
	day = 0
	time = 0

	time_true = False
	day_true = False

	# check for a time
	for i in time_hours:
		for j in time_mins:
			temp_time = time_hours[i]+' '+time_mins[j]
			if temp_time in string:
				time = temp_time
				break

	# check for a day (ex: first, second, etc.)
	for i in days:
		if i in string:
			day = days[i]
			day_true = True
			break
	
	# if not true - then its a day of the week 
	if day_true == False:
		# check for day of week (can be today or tomorrow)
		for i in days_of_week:
			if i in string:
				day_of_week = days_of_week[i]
				#if i == 'today':
				# TODO: find todays date and set that instead 
				#if ('next *day of week*' in string)
				# TODO: fix that to the correct date
	else:
		# check for month (ex: january, february, etc.)
		for i in months:
			if i in string:
				month = months[i]
		
		# TODO: check if there are that many days in that month
	
	# check if it is open ended [ex: nov 22nd - assume the next one, assume anytime]


def parse_header(string):
	if(("set a reminder" in string)):
				# TODO: is there a date
				# TODO: is there a task
				# is there an "on *this day*"
				# is there an "at *this time*"
				

	elif ("remind me to" in string):
		# ..."event" at ("this time" or "in this amount of time") 

#------------------------------------------
#------------END PARSING COMMAND-----------
#------------------------------------------

#------------------------------------------
#----------START STORING REMINDER----------
#------------------------------------------

# LOLOL FARTS

#------------------------------------------
#------------END PARSING COMMAND-----------
#------------------------------------------