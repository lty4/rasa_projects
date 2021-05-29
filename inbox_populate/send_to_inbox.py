import csv
import requests
from getpass import getpass


def send_to_inbox(username, password, link):

	""" Authorize with Rasa X """
	auth_api_string = link + "/api/auth"
	auth_json_str = {"username": username, "password": password}
	auth_token = requests.post(auth_api_string, json=auth_json_str)
	bearer_token = "Bearer " + auth_token.json()["access_token"]
	bearer_header = {"Authorization": bearer_token}
	content_type = {"Content-Type": "application/json"}
	header_list = {**bearer_header, **content_type}
	
	""" Choose API method for Parse text and create a new log entry """
	api_string = link + "/api/projects/"
	
	""" Iterate through CSV, add item to NLU Inbox """
	with open('statements.csv', newline='') as statementfile:
		statementreader = csv.reader(statementfile, delimiter=',')
		item = 0
		for row in statementreader:
			item += 1
			full_api_string = api_string + "default/logs?q=" + row[0]
			entry = requests.post(url=full_api_string, headers=header_list)
			print("Entry " + str(item) + ': "' + row[0] + '" added.')
	return


link = input("Please provide the URL to your Rasa X server.\n")
username = input("Username: ")
password = getpass()

send_to_inbox(username, password, link)
print("All items have been submitted to Rasa X.")
