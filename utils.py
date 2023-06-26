from bs4 import BeautifulSoup
from lorem.text import TextLorem
import DashboardModels.SystemCases as SystemCases
import json
import random

def get_verification_token(response):
    return BeautifulSoup(response.text, 'html.parser').find('input',{'name':'__RequestVerificationToken'})['value']

def get_assessment_id(response):
    return BeautifulSoup(response.text, 'html.parser').find(id='AssessmentId')['value']

def get_case_id(response):
    return BeautifulSoup(response.text, 'html.parser').find(id='CaseId')['value']

def get_local_authority(response):
    return BeautifulSoup(response.text, 'html.parser').find('input',{'name':'userLocalAuthorityId'})['value']

def get_dashboard(response):
    return BeautifulSoup(response.text, 'html.parser').find(id='agree')['href']

def get_assigned_user(response):
    return (BeautifulSoup(response.text, 'html.parser').find(id='interviewerId').find_all('option', selected=True)[-1])['value']

def get_custom_html_value(response, html_id):
    return BeautifulSoup(response.text, 'html.parser').find(id=html_id)['value']

def get_system_cases(common_data, dashboard):
    data = SystemCases.get_data(common_data.session.get(common_data.site + dashboard))
    system_cases = common_data.session.post(common_data.site + dashboard + '/SystemCasesProcessDataTableQuery', data=data)
    return json.loads(system_cases.text)

def get_view_link(common_data, dashboard, case):
    url = common_data.site + '/' + dashboard.split('/')[1] + '/' + case.split('./', 1)[1]
    return url

def get_jump_to_links(common_data):
    jumpto = BeautifulSoup(common_data.response.text, 'html.parser').find(attrs={'aria-labelledby': 'JumpTo'})
    return jumpto.find_all(class_='dropdown-item') if jumpto is not None else None

def get_random_jump_to_link(common_data, links):
    return common_data.site + random.choice(links)['href']

def get_lorem(min=12, max=25):
    lorem = TextLorem(srange=(min,max))
    return lorem.sentence()

def get_hidden_names_inputs(response):
    # find all inputs in wrapper, add values to them
    soup_obj = BeautifulSoup(response.text, 'html.parser')
    soup = soup_obj.find(id='page-wrapper').find_all('input')

    model_inputs = []

    for e in soup:
        try:
            model_inputs.append(e.attrs['name'])
        except KeyError as k:
            continue
    return model_inputs

def signout(site, session):
    session.get(site + '/Home/SignOut')