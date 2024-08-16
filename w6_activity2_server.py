
# No other modules apart from 'socket', 'BeautifulSoup', 'requests' and 'datetime'
# need to be imported as they aren't required to solve the assignment

# Import required module/s
import socket
from bs4 import BeautifulSoup
import requests
import datetime


# Define constants for IP and Port address of Server
# NOTE: DO NOT modify the values of these two constants
HOST = '127.0.0.1'
PORT = 24680


def fetchWebsiteData(url_website):
	"""Fetches rows of tabular data from given URL of a website with data excluding table headers.

	Parameters
	----------
	url_website : str
		URL of a website

	Returns
	-------
	bs4.element.ResultSet
		All rows of Tabular data fetched from a website excluding the table headers
	"""
	
	web_page_data = ''

	##############	ADD YOUR CODE HERE	##############
	
	req = requests.get(url_website)
	s = BeautifulSoup(req.text, "html.parser")
	x = s.find('tr')
	web_page_data = x.find_all_next('tr')

	##################################################

	return web_page_data


def fetchVaccineDoses(web_page_data):
	"""Fetch the Vaccine Doses available from the Web-page data and provide Options to select the respective Dose.

	Parameters
	----------
	web_page_data : bs4.element.ResultSet
		All rows of Tabular data fetched from a website excluding the table headers

	Returns
	-------
	dict
		Dictionary with the Doses available and Options to select, with Key as 'Option' and Value as 'Command'
	
	Example
	-------
	>>> url_website = "https://www.mooc.e-yantra.org/task-spec/fetch-mock-covidpage"
	>>> web_page_data = fetchWebsiteData(url_website)
	>>> print(fetchVaccineDoses(web_page_data))
	{'1': 'Dose 1', '2': 'Dose 2'}
	"""

	vaccine_doses_dict = {}

	##############	ADD YOUR CODE HERE	##############
	
	h=1
	f=[]
	for i in web_page_data:
		l = "Dose "+str(i.find('td').find_next_sibling("td", "dose_num").text)
		f.append(l)
		h +=1
	f.sort()  
	u=1
	for j in range(1, h-1):
		if(not f[j] in vaccine_doses_dict.values()):
	  		vaccine_doses_dict[str(u)]=f[j]
	  		u+=1

	##################################################

	return vaccine_doses_dict


def fetchAgeGroup(web_page_data, dose):
	"""Fetch the Age Groups for whom Vaccination is available from the Web-page data for a given Dose
	and provide Options to select the respective Age Group.

	Parameters
	----------
	web_page_data : bs4.element.ResultSet
		All rows of Tabular data fetched from a website excluding the table headers
	dose : str
		Dose available for Vaccination and its availability for the Age Groups

	Returns
	-------
	dict
		Dictionary with the Age Groups (for whom Vaccination is available for a given Dose) and Options to select,
		with Key as 'Option' and Value as 'Command'
	
	Example
	-------
	>>> url_website = "https://www.mooc.e-yantra.org/task-spec/fetch-mock-covidpage"
	>>> web_page_data = fetchWebsiteData(url_website)
	>>> print(fetchAgeGroup(web_page_data, '1'))
	{'1': '18+', '2': '45+'}
	>>> print(fetchAgeGroup(web_page_data, '2'))
	{'1': '18+', '2': '45+'}
	"""

	age_group_dict = {}

	##############	ADD YOUR CODE HERE	##############
	
	h=1
	f=[]
	for i in web_page_data:
		if(i.find('td').find_next_sibling("td", "dose_num").find(text=dose)):
	  		m=str(i.find('td').find_next_sibling("td", "age").text)
	  		f.append(m)
	  		h +=1
	u=1
	for j in range(1, h-1):   
		if(not f[j] in age_group_dict.values()):
	  		age_group_dict[str(u)]=f[j]
	  		u+=1

	##################################################

	return age_group_dict


def fetchStates(web_page_data, age_group, dose):
	"""Fetch the States where Vaccination is available from the Web-page data for a given Dose and Age Group
	and provide Options to select the respective State.

	Parameters
	----------
	web_page_data : bs4.element.ResultSet
		All rows of Tabular data fetched from a website excluding the table headers
	age_group : str
		Age Group available for Vaccination and its availability in the States
	dose : str
		Dose available for Vaccination and its availability for the Age Groups

	Returns
	-------
	dict
		Dictionary with the States (where the Vaccination is available for a given Dose, Age Group) and Options to select,
		with Key as 'Option' and Value as 'Command'
	
	Example
	-------
	>>> url_website = "https://www.mooc.e-yantra.org/task-spec/fetch-mock-covidpage"
	>>> web_page_data = fetchWebsiteData(url_website)
	>>> print(fetchStates(web_page_data, '18+', '1'))
	{
		'1': 'Andhra Pradesh', '2': 'Arunachal Pradesh', '3': 'Bihar', '4': 'Chandigarh', '5': 'Delhi', '6': 'Goa',
		'7': 'Gujarat', '8': 'Harayana', '9': 'Himachal Pradesh', '10': 'Jammu and Kashmir', '11': 'Kerala', '12': 'Telangana'
	}
	"""

	states_dict = {}

	##############	ADD YOUR CODE HERE	##############
	
	h=1
	f=[]
	for i in web_page_data:
		if(i.find('td').find_next_sibling("td", "dose_num").find(text=dose) and i.find('td').find_next_sibling("td", "age").find(text=age_group)):
	  		m=str(i.find('td').find_next_sibling("td", "state_name").text)
		  	f.append(m)
		  	h +=1
	f.sort()    
	u=1
	for j in range(0, h-1):   
		if(not f[j] in states_dict.values()):
	  		states_dict[str(u)]=f[j]
	  		u+=1

	##################################################

	return states_dict


def fetchDistricts(web_page_data, state, age_group, dose):
	"""Fetch the District where Vaccination is available from the Web-page data for a given State, Dose and Age Group
	and provide Options to select the respective District.

	Parameters
	----------
	web_page_data : bs4.element.ResultSet
		All rows of Tabular data fetched from a website excluding the table headers
	state : str
		State where Vaccination is available for a given Dose and Age Group
	age_group : str
		Age Group available for Vaccination and its availability in the States
	dose : str
		Dose available for Vaccination and its availability for the Age Groups

	Returns
	-------
	dict
		Dictionary with the Districts (where the Vaccination is available for a given State, Dose, Age Group) and Options to select,
		with Key as 'Option' and Value as 'Command'
	
	Example
	-------
	>>> url_website = "https://www.mooc.e-yantra.org/task-spec/fetch-mock-covidpage"
	>>> web_page_data = fetchWebsiteData(url_website)
	>>> print(fetchDistricts(web_page_data, 'Ladakh', '18+', '2'))
	{
		'1': 'Kargil', '2': 'Leh'
	}
	"""

	districts_dict = {}

	##############	ADD YOUR CODE HERE	##############
	
	h=1
	f=[]
	for i in web_page_data:
 		if(i.find('td').find_next_sibling("td", "dose_num").find(text=dose) and i.find('td').find_next_sibling("td", "age").find(text=age_group) and i.find('td').find_next_sibling("td", "state_name").find(text=state)):
	  		m=str(i.find('td').find_next_sibling("td", "district_name").text)
	  		f.append(m)
	  		h +=1
	f.sort()    
	u=1
	for j in range(0, h-1):   
		if(not f[j] in districts_dict.values()):
	  		districts_dict[str(u)]=f[j]
	  		u+=1

	##################################################

	return districts_dict


def fetchHospitalVaccineNames(web_page_data, district, state, age_group, dose):
	"""Fetch the Hospital and the Vaccine Names from the Web-page data available for a given District, State, Dose and Age Group
	and provide Options to select the respective Hospital and Vaccine Name.

	Parameters
	----------
	web_page_data : bs4.element.ResultSet
		All rows of Tabular data fetched from a website excluding the table headers
	district : str
		District where Vaccination is available for a given State, Dose and Age Group
	state : str
		State where Vaccination is available for a given Dose and Age Group
	age_group : str
		Age Group available for Vaccination and its availability in the States
	dose : str
		Dose available for Vaccination and its availability for the Age Groups

	Returns
	-------
	dict
		Dictionary with the Hosptial and Vaccine Names (where the Vaccination is available for a given District, State, Dose, Age Group)
		and Options to select, with Key as 'Option' and Value as another dictionary having Key as 'Hospital Name' and Value as 'Vaccine Name'
	
	Example
	-------
	>>> url_website = "https://www.mooc.e-yantra.org/task-spec/fetch-mock-covidpage"
	>>> web_page_data = fetchWebsiteData(url_website)
	>>> print(fetchHospitalVaccineNames(web_page_data, 'Kargil', 'Ladakh', '18+', '2'))
	{
		'1': {
				'MedStar Hospital Center': 'Covaxin'
			}
	}
	>>> print(fetchHospitalVaccineNames(web_page_data, 'South Goa', 'Goa', '45+', '2'))
	{
		'1': {
				'Eden Clinic': 'Covishield'
			}
	}
	"""
	
	hospital_vaccine_names_dict = {}

	##############	ADD YOUR CODE HERE	##############
	
	hosp={}
	u=1
	for i in web_page_data:
		if(i.find('td').find_next_sibling("td", "dose_num").find(text=dose) and i.find('td').find_next_sibling("td", "age").find(text=age_group) and i.find('td').find_next_sibling("td", "state_name").find(text=state) and i.find('td').find_next_sibling("td", "district_name").find(text=district)):
			hosp[str(i.find('td').text)] = str(i.find('td').find_next_sibling("td", "vaccine_name").text)
			hospital_vaccine_names_dict[str(u)]=hosp
			u+=1

	##################################################

	return hospital_vaccine_names_dict


def fetchVaccineSlots(web_page_data, hospital_name, district, state, age_group, dose):
	"""Fetch the Dates and Slots available on those dates from the Web-page data available for a given Hospital Name, District, State, Dose and Age Group
	and provide Options to select the respective Date and available Slots.

	Parameters
	----------
	web_page_data : bs4.element.ResultSet
		All rows of Tabular data fetched from a website excluding the table headers
	hospital_name : str
		Name of Hospital where Vaccination is available for given District, State, Dose and Age Group
	district : str
		District where Vaccination is available for a given State, Dose and Age Group
	state : str
		State where Vaccination is available for a given Dose and Age Group
	age_group : str
		Age Group available for Vaccination and its availability in the States
	dose : str
		Dose available for Vaccination and its availability for the Age Groups

	Returns
	-------
	dict
		Dictionary with the Dates and Slots available on those dates (where the Vaccination is available for a given Hospital Name,
		District, State, Dose, Age Group) and Options to select, with Key as 'Option' and Value as another dictionary having
		Key as 'Date' and Value as 'Available Slots'
	
	Example
	-------
	>>> url_website = "https://www.mooc.e-yantra.org/task-spec/fetch-mock-covidpage"
	>>> web_page_data = fetchWebsiteData(url_website)
	>>> print(fetchVaccineSlots(web_page_data, 'MedStar Hospital Center', 'Kargil', 'Ladakh', '18+', '2'))
	{
		'1': {'May 15': '0'}, '2': {'May 16': '81'}, '3': {'May 17': '109'}, '4': {'May 18': '78'},
		'5': {'May 19': '89'}, '6': {'May 20': '57'}, '7': {'May 21': '77'}
	}
	>>> print(fetchVaccineSlots(web_page_data, 'Eden Clinic', 'South Goa', 'Goa', '45+', '2'))
	{
		'1': {'May 15': '0'}, '2': {'May 16': '137'}, '3': {'May 17': '50'}, '4': {'May 18': '78'},
		'5': {'May 19': '145'}, '6': {'May 20': '64'}, '7': {'May 21': '57'}
	}
	"""

	vaccine_slots = {}

	##############	ADD YOUR CODE HERE	##############
	
	slot1={}
	slot2={}
	slot3={}
	slot4={}
	slot5={}
	slot6={}
	slot7={}

	for i in web_page_data:
		if(i.find('td').find_next_sibling("td", "dose_num").find(text=dose) and i.find('td').find_next_sibling("td", "age").find(text=age_group) and i.find('td').find_next_sibling("td", "state_name").find(text=state) and i.find('td').find_next_sibling("td", "district_name").find(text=district) and i.find('td').find(text=hospital_name)):
	    
		  	slot1['May 15']=str(i.find('td').find_next_sibling("td", "may_15").text)
		  	vaccine_slots['1']=slot1

		  	slot2['May 16']=str(i.find('td').find_next_sibling("td", "may_16").text)
		  	vaccine_slots['2']=slot2
	    
		  	slot3['May 17']=str(i.find('td').find_next_sibling("td", "may_17").text)
		  	vaccine_slots['3']=slot3

		  	slot4['May 18']=str(i.find('td').find_next_sibling("td", "may_18").text)
		  	vaccine_slots['4']=slot4
		  	slot5['May 19']=str(i.find('td').find_next_sibling("td", "may_19").text)
		  	vaccine_slots['5']=slot5

		  	slot6['May 20']=str(i.find('td').find_next_sibling("td", "may_20").text)
		  	vaccine_slots['6']=slot6
		  	
		  	slot7['May 21']=str(i.find('td').find_next_sibling("td", "may_21").text)
		  	vaccine_slots['7']=slot7

	##################################################

	return vaccine_slots


def openConnection():
	"""Opens a socket connection on the HOST with the PORT address.

	Returns
	-------
	socket
		Object of socket class for the Client connected to Server and communicate further with it
	tuple
		IP and Port address of the Client connected to Server
	"""

	client_socket = None
	client_addr = None

	##############	ADD YOUR CODE HERE	##############
	
	ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	ss.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	ss.bind((HOST, PORT))
	ss.listen(2)
	client_socket, client_addr = ss.accept()

	##################################################
	
	return client_socket, client_addr


def startCommunication(client_conn, client_addr, web_page_data):
	"""Starts the communication channel with the connected Client for scheduling an Appointment for Vaccination.

	Parameters
	----------
	client_conn : socket
		Object of socket class for the Client connected to Server and communicate further with it
	client_addr : tuple
		IP and Port address of the Client connected to Server
	web_page_data : bs4.element.ResultSet
		All rows of Tabular data fetched from a website excluding the table headers
	"""

	##############	ADD YOUR CODE HERE	##############
	
	print("Client is connected at: " + str(client_addr))
  
	x = '\n┍━━━━━━━━━ ⋆ ⋅☆ ⋅ ⋆ ━━━━━━━━━┑\n   Welcome to CoWIN ChatBot   \n┕━━━━━━━━━ ⋆ ⋅☆ ⋅ ⋆ ━━━━━━━━━┙\n'
	client_conn.sendall(x.encode('utf-8'))
	print('Start')

	x = 'Schedule an Appointment for Vaccination:'
	client_conn.sendall(x.encode('utf-8'))
  
	count=0	#count to go for right funnction in loop
	invalid=0 #invalid count
	while(count<6):
		if(count==0):
	  		x='\n>>> Select the Dose of Vaccination:\n'
	  		y=''
	  		d = fetchVaccineDoses(web_page_data)
	  		for i, j in d.items():
	  			y+=str(i+'\t->\t'+j+'\n')
	  		x +=y
	  		client_conn.sendall(x.encode('utf-8'))
	  		data1 = client_conn.recv(1024).decode('utf-8')
      
	  		if(data1=='b' or data1=='B'):	#back function
	  			continue
	  		if(data1=='q' or data1=='Q'):	#quit function
	  			break		
	  		if(not data1 in d.keys()):		#checking if data is invalid
	  			invalid+=1
	  			t = '\n<<< Invalid input provided '+str(invalid)+' time(s)! Try again.\n'
	  			client_conn.sendall(t.encode('utf-8'))
	  			if(invalid==3):
	  				break
	  			continue  
	  		r = '\n<<< Dose selected: '+str(data1)
	  		client_conn.sendall(r.encode('utf-8'))
	  		print(r)
	  		u=0
	  		while(u==0 and data1=='2'):		#checking data n period between dose1 n current date
	  			if(data1=='2'):	
	  				in1 = '\n>>> Provide the date of First Vaccination Dose (DD/MM/YYYY), for e.g. 12/5/2021'
	  				client_conn.sendall(in1.encode('utf-8'))
	  				date=client_conn.recv(1024).decode('utf-8')
	  				if(date=='b' or date=='B'):
	  					count-=1
	  					break
	  				elif(date=='q' or date=='Q'):
	  					count=8
	  					break  
	  				try:
	  					date1=date.split('/')
	  					date1 = datetime.date(int(date1[2]),int(date1[1]),int(date1[0]))
	  					t_date=datetime.datetime.now()
	  					date2=t_date.strftime('%d/%m/%Y').split('/')
	  					date2 = datetime.date(int(date2[2]),int(date2[1]),int(date2[0]))
	  				except ValueError:	#invalid date is entered
	  					f = '\n<<< Invalid Date provided of First Vaccination Dose: '+str(date)
	  					client_conn.sendall(f.encode('utf-8'))
	  					continue

	  				if((date2-date1).days<=0):
	  					f = '\n<<< Invalid Date provided of First Vaccination Dose: '+str(date)
	  					client_conn.sendall(f.encode('utf-8'))
	  					continue
	  				in2 = '\n<<< Date of First Vaccination Dose provided: '+str(date)
	  				client_conn.sendall(in2.encode('utf-8'))
	  				days=abs(date1-date2).days
	  				week = (days//7)
	  				in3 = '\n<<< Number of weeks from today: '+str(int(week))
	  				client_conn.sendall(in3.encode('utf-8'))
	  				if(week > 8):
	  					in4 = '\n<<< You have been late in scheduling your 2nd Vaccination Dose by '+str(week-8)+' weeks.'
	  					client_conn.sendall(in4.encode('utf-8'))
	  				elif(week < 4):
	  					in4 = '\n<<< You are not eligible right now for 2nd Vaccination Dose! Try after '+str(4-int(week))+' weeks.'
	  					client_conn.sendall(in4.encode('utf-8'))
	  					count=6
	  					break
	  				else:
	  					in4 = '\n<<< You are eligible for 2nd Vaccination Dose and are in the right time-frame to take it.'
	  					client_conn.sendall(in4.encode('utf-8'))
	  				u+=1

		elif(count==1):
	  		x='\n>>> Select the Age Group:\n'
	  		y=''
	  		d = fetchAgeGroup(web_page_data, data1)
	  		for i, j in d.items():
	  			y+=str(i+'\t->\t'+j+'\n')
	  		x +=y
	  		client_conn.sendall(x.encode('utf-8'))
	  		data2 = client_conn.recv(1024).decode('utf-8')
	  		if(data2=='b' or data2=='B'):
	  			count-=1
	  			continue
	  		if(data2=='q' or data2=='Q'):
	  			break
	  		if(not data2 in d.keys()):
	  			invalid+=1
	  			t = '\n<<< Invalid input provided '+str(invalid)+' time(s)! Try again.\n'
	  			client_conn.sendall(t.encode('utf-8'))
	  			if(invalid==3):
	  				break
	  			continue
	  		data2 = d[str(data2)]  
	  		r = '\n<<< Selected Age Group: '+str(data2)
	  		client_conn.sendall(r.encode('utf-8'))
	  		print(r)

		elif(count==2):
	  		x='\n>>> Select the State:\n'
	  		y=''
	  		d = fetchStates(web_page_data, data2, data1)
	  		for i, j in d.items():
	  			y+=str(i+'\t->\t'+j+'\n')
	  		x +=y
	  		client_conn.sendall(x.encode('utf-8'))
	  		data3 = client_conn.recv(1024).decode('utf-8')
	  		if(data3=='b' or data3=='B'):
	  			count-=1
	  			continue
	  		if(data3=='q' or data3=='Q'):
	  			break
	  		if(not data3 in d.keys()):
	  			invalid+=1
	  			t = '\n<<< Invalid input provided '+str(invalid)+' time(s)! Try again.\n'
	  			client_conn.sendall(t.encode('utf-8'))
	  			if(invalid==3):
	  				break
	  			continue
	  		data3 = d[str(data3)]
	  		r = '\n<<< Selected State: '+str(data3)
	  		client_conn.sendall(r.encode('utf-8'))
	  		print(r)

		elif(count==3):
			x='\n>>> Select the District:\n'
			y=''
			d = fetchDistricts(web_page_data, data3, data2, data1)
			for i, j in d.items():
				y+=str(i+'\t->\t'+j+'\n')
			x +=y
			client_conn.sendall(x.encode('utf-8'))
			data4 = client_conn.recv(1024).decode('utf-8')
			if(data4=='b' or data4=='B'):
				count-=1
				continue
			if(data4=='q' or data4=='Q'):
				break
			if(not data4 in d.keys()):
				invalid+=1
				t = '\n<<< Invalid input provided '+str(invalid)+' time(s)! Try again.\n'
				client_conn.sendall(t.encode('utf-8'))
				if(invalid==3):
					break
				continue
			data4 = d[str(data4)]
			r = '\n<<< Selected District: '+str(data4)
			client_conn.sendall(r.encode('utf-8'))
			print(r)

		elif(count==4):
			x='\n>>> Select the Vaccination Center Name:\n'
			y=''
			d = fetchHospitalVaccineNames(web_page_data, data4, data3, data2, data1)
			for i, j in d.items():
				for a, b in j.items():
					y+=str(i+'\t->\t'+a+' (vaccine available - '+b+ ')\n')
			x +=y
			client_conn.sendall(x.encode('utf-8'))
			data5 = client_conn.recv(1024).decode('utf-8')
			if(data5=='b' or data5=='B'):
				count-=1
				continue
			if(data5=='q' or data5=='Q'):
				break
			if(not data5 in d.keys()):
				invalid+=1
				t = '\n<<< Invalid input provided '+str(invalid)+' time(s)! Try again.\n'
				client_conn.sendall(t.encode('utf-8'))
				if(invalid==3):
					break
				continue
			for y in d[data5].keys():
				data5=y
				r = '\n<<< Selected Vaccination Center: '+str(data5)
			client_conn.sendall(r.encode('utf-8'))
			print(r)

		elif(count==5):
			x='\n>>> Select one of the available slots to schedule the Appointment:\n'
			y=''
			d = fetchVaccineSlots(web_page_data, data5, data4, data3, data2, data1)
			for i, j in d.items():
				for a, b in j.items():
					y+=str(i+'\t->\t'+a+' (slots available - '+b+ ')\n')
			x +=y
			client_conn.sendall(x.encode('utf-8'))
			data6 = client_conn.recv(1024).decode('utf-8')
			if(data6=='b' or data6=='B'):
				count-=1
				continue
			if(data6=='q' or data6=='Q'):
				break
			if(not data6 in d.keys()):
				invalid+=1
				t = '\n<<< Invalid input provided '+str(invalid)+' time(s)! Try again.\n'
				client_conn.sendall(t.encode('utf-8'))
				if(invalid==3):
					break
				continue
			for y, m in d[data6].items():
				r = '\n<<< Selected Vaccination Appointment Date: '+str(y)+'\n<<< Available Slots on the selected Date: '+str(m)
			client_conn.sendall(r.encode('utf-8'))
			print(r)
			if(m=='0'):
				k='\n<<< Selected Appointment Date has no available slots, select another date!'
				client_conn.sendall(k.encode('utf-8'))
				continue
			a = '\n<<< Your appointment is scheduled. Make sure to carry ID Proof while you visit Vaccination Center!\n'
			client_conn.sendall(a.encode('utf-8'))
		count+=1
	stopCommunication(client_conn)

	##################################################


def stopCommunication(client_conn):
	"""Stops or Closes the communication channel of the Client with a message.

	Parameters
	----------
	client_conn : socket
		Object of socket class for the Client connected to Server and communicate further with it
	"""

	##############	ADD YOUR CODE HERE	##############
	
	end='\n<<< See ya! Visit again :)'
	client_conn.sendall(end.encode())
	client_conn.close()

	##################################################


################# ADD UTILITY FUNCTIONS HERE #################
## You can define any utility functions for your code.      ##
## Please add proper comments to ensure that your code is   ##
## readable and easy to understand.                         ##
##############################################################



##############################################################


if __name__ == '__main__':
	"""Main function, code begins here
	"""
	url_website = "https://www.mooc.e-yantra.org/task-spec/fetch-mock-covidpage"
	web_page_data = fetchWebsiteData(url_website)
	client_conn, client_addr = openConnection()
	startCommunication(client_conn, client_addr, web_page_data)
