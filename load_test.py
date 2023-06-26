# This program bombards the site in ./config.py with http requests in order to test what kind of load the server can take

# The original intention of this was to have a few handfuls of threads 
# that would do http request runthroughs of each application (LSCMI, MFMC, Caledonian).
# A request only runthrough of LSCMI does work, but it was decided that just randomly 
# choosing a case from LSCMI and then randomly choosing a jumpto link for that case would suffice

# TO RUN - In command prompt (or whatever), navigate to the directory that contains this file and type 'py load_test.py'
# If some test parameters need to be changed, ./config.py is the place to do it. Otherwise this file shouldn't need changing

from CommonData import CommonData
import requests
import multiprocessing
from concurrent.futures.thread import ThreadPoolExecutor
from concurrent.futures.process import ProcessPoolExecutor
import ApplicationCases.LSCMICase as LSCMICase
import ApplicationCases.MFMCCase as MFMCCase
import ApplicationCases.CaleCase as CaleCase
import concurrent.futures
import utils
import datetime
import random
import time
import config

program_start_time = datetime.datetime.now()

def begin_runthrough(username, password):
    print(f'user {username} test starting')
    request_count = 0
    session = requests.Session()
    response = session.get(config.site+'/Home/LogIn')
    request_count += 1

    cookie_key = list(response.cookies.get_dict().keys())[0]
    cookie_val = response.cookies.get_dict()[cookie_key]
    cookie_string = f'{cookie_key}={cookie_val}'

    headers = {
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'Upgrade-Insecure-Requests': '1',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': cookie_string
    }

    data = {
        'Username': f'{username}',
        'Password': f'{password}',
        '__RequestVerificationToken': utils.get_verification_token(response)
    }

    time.sleep(random.randrange(*config.time_between_users))
    response = session.post(config.site + '/Home/LogIn', headers=headers, cookies=session.cookies, data=data, allow_redirects=True, verify=False)
    request_count += 1

    dashboard = utils.get_dashboard(response)

    response = session.get(config.site + dashboard)
    request_count += 1

    data = CommonData(config.site, session, response)

    if "LSCMI" in dashboard:
        # if random.random() > 0.5: #normally, 50/50 chance of either starting a case workflow in LSCMI or random link loading based on jumpto dropdown
        if False:
            print('workflow started')
            LSCMICase.begin_workflow(data)
        else:
            print('random link loading started')
            # for i in range(config.number_of_random_cases):
            while (datetime.datetime.now() - program_start_time).total_seconds() < config.time_to_loop:
                system_cases = utils.get_system_cases(data, dashboard)['data']
                request_count += 1
                view_link = utils.get_view_link(data, dashboard, random.choice(system_cases)['bookmark'])
                data.response = data.session.get(view_link)
                request_count += 1
                jump_links = utils.get_jump_to_links(data)
                if jump_links is None:
                    continue
                for j in range(config.number_of_jumpto_links):
                    if (datetime.datetime.now() - program_start_time).total_seconds() >= config.time_to_loop:
                        break
                    #wait between 5 and 60 seconds between loads? Some random amount of time between loads
                    random_jumpto_link = utils.get_random_jump_to_link(data, jump_links)
                    sleep_num = random.randrange(*config.time_between_jumpto) 
                    time.sleep(sleep_num)
                    data.response = data.session.get(random_jumpto_link)
                    request_count += 1
                    print(f'{str(data.response)}: view_link = {random_jumpto_link}, elapsed={data.response.elapsed.total_seconds()} and slept for {sleep_num} seconds')

    #these don't work   
    elif "MFMC" in dashboard:
        MFMCCase.begin_workflow(data)
    elif "Caledonian" in dashboard:
        CaleCase.begin_workflow(data)

    return request_count

def create_n_threads(n):
    with ThreadPoolExecutor(max_workers=config.threads) as executor:
        futures = []
        request_counts = 0
        for _ in range(n):
            futures.append(executor.submit(begin_runthrough, username=config.username, password=config.password))
        for i in concurrent.futures.as_completed(futures):
            request_counts += i.result()
        return request_counts

def main():

    processes = config.processes if config.processes is not None and config.processes > 0 else multiprocessing.cpu_count()

    with ProcessPoolExecutor(max_workers=processes) as process_executor:
        procs = []
        request_counts = 0

        start = datetime.datetime.now()

        user_count = processes * config.threads

        # if config.time_to_loop is None:
        #     print(f'beginning test with {user_count} simulated users, totaling {user_count * (3 + (config.number_of_random_cases * (2 + config.number_of_jumpto_links)))} requests')

        print(f'beginning test with {user_count} simulated users')

        for _ in range(processes):
            procs.append(process_executor.submit(create_n_threads, config.threads))
        for i in concurrent.futures.as_completed(procs):
            request_counts += i.result()

        print(str(request_counts) + ' total requests in ' + str((datetime.datetime.now() - start).total_seconds()) + ' seconds ')

if __name__ == "__main__":
    main()