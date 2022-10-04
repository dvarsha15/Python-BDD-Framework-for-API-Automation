#steps for the feature 

from behave import *
import json
import os, sys, requests
#add all paths to sys.path for importing methods from all directories
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.results import *
from conf.payload import car_payload, update_car_payload
from conf.configurations import getconfig

#create session
session = requests.Session()

@given('I am admin')
def get_input(context):
    global username, password
    username = getconfig()['admin']['username']
    password = getconfig()['admin']['password']

@given('I am non admin')
def get_input(context):
    global username, password
    username = getconfig()['non_admin']['username']
    password = getconfig()['non_admin']['password']
 

#1. steps to get response(cars list) from endpoint using GET method
@when('I make a GET call to url "{url}"')
def get_cars_list(context, url):
    global global_url
    global_url = url
    context.get_response = session.get(url=str(url), auth=(username, password))

#validate status code of the response
@then('the response status code is "{status_code}"')
def verify_status_code_of_get_car(context, status_code):
    #convert response into json format 
    get_response_json = context.get_response.json()
    if context.get_response.status_code == int(status_code):
        success("Successfully fetched the Cars list from endpoint")
        info("Existing cars list = "+str(get_response_json)+"\n")
    else:
        error(str(context.get_response)+" Failed to fetch cars list from endpoint")

#2. steps to add new car using POST method
@given('payload to be added')
def get_input(context):
    context.json=json.loads(context.text)

@when('I make a POST call to url "{url_add}"')
def add_car(context, url_add):
    context.url_add = url_add
    context.add_car_response = session.post(url=url_add, json=context.json, auth=(username, password))

@then('new car added successfully and the response status code is "{status_code}"')
def verify_added_car(context, status_code):
    get_car_response_data = context.get_response.json()['car']
    if context.add_car_response.status_code == int(status_code) and get_car_response_data['name'] == context.json['name']:
        success("New car named "+ car_payload()['name']+" is added succeccfully\n")
        info("New car data = "+str(context.get_response.json())+"\n")
    else:
        error(str(context.get_response)+" Failed to add new car\n")

#3. update car data(price_range) by name using PUT method 
@given('car name to be updated "{update_car_name}" and payload')
def get_input(context, update_car_name):
    context.update_car_name = update_car_name
    context.json=json.loads(context.text)
    
@when('I make a PUT call to url "{url_update}"')
def update_car(context, url_update):
    context.url_update = url_update
    context.update_car_response = session.put(url=url_update+context.update_car_name, json=context.json, auth=(username, password))

@then('car price_range of given car name is updated successfully with status code "{status_code}"')
def verify_updated_car(context, status_code):
    get_car_response_data = context.get_response.json()['car']
    if  context.update_car_response.status_code == int(status_code) and get_car_response_data['price_range'] == context.json['price_range']:
        success("Car price range updated succeccfully \n")
        info("Updated car data = "+str(context.get_response.json())+"\n")
    else:
        error(str(context.get_response)+" Failed to update car price range \n")

#4. delete the added car by name using DELETE method
@given('car name to be deleted "{car_name}"')
def get_input(context, car_name):
    context.car_name = car_name

@when('I make a DELETE call to url "{url}"')
def delete_car(context, url):
    context.delete_car_response = session.delete(url=url+context.car_name, auth=(username, password))

@then('car with given name is deleted successfully with status code "{status_code}"')
def verify_status_code_of_deleted_car(context, status_code):
    if context.delete_car_response.status_code == int(status_code):
        success("Car named "+context.car_name+" is deleted successfully\n")
    else:
        error(str(context.delete_car_response)+" Failed to delete the car\n")
