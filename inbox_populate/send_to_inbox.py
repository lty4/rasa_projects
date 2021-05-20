import csv
import requests
from getpass import getpass


def send_to_inbox(username, password, link):
	auth_api_string = link + "/api/auth"
	auth_json_str = {"username": username, "password": password}
	auth_token = requests.post(auth_api_string, json=auth_json_str)
	bearer_token = "Bearer " + auth_token.json()["access_token"]
	bearer_header = {"Authorization": bearer_token}
	content_type = {"Content-Type": "application/json"}
	header_list = {**bearer_header, **content_type}
	
	api_string = link + "/api/conversations/"
	
	with open('statements.csv', newline='') as statementfile:
		statementreader = csv.reader(statementfile, delimiter=',')
		i = 0
		for row in statementreader:
			i += 1
			full_api_string = api_string + "import_" + str(i) + "/messages"
			json_str = {"message": row[0]}
			conversation = requests.post(url=full_api_string, json=json_str, headers=header_list)
			
	return


link = input("Please provide the URL to your Rasa X server.\n")
username = input("Username: ")
password = getpass()

send_to_inbox(username, password, link)

