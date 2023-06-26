#This is the config file for load_test.py

#site = 'http://localhost:44936'
#site = 'http://62.233.124.89:8081'
site='https://testing.viiacloud.co.uk'
username='j@j.com'
password='Password1'


processes=16 #number of processes to run, defaults to cpu count if set to None or if (processes <= 0)
threads=25 #number of threads per process (translates to number of users per process, number of users is then (processes * threads)) 


time_between_users=(1,40) #time range between each user login in seconds
time_between_jumpto=(10,60) #time range between each jumpto being 'clicked'


number_of_jumpto_links=100 #number of random jumpto links from each randomly chosen case that will be loaded
time_to_loop=2*600 #minimum number of seconds to choose random cases and load them