print("WELCOME User !!")
print("Thanks for using Hecktor - Source")
print("© PVER Programz LLC\n\n")

import requests
import firebase_admin
from firebase_admin import db

mod = "firebase-admin"
ext = ".json"
allowed = 1
name_int = "poseidon"


def chat():

	user = "Hook"
	avatar = "https://static.wikia.nocookie.net/disney/images/0/0b/Profile_-_Captain_Hook.jpeg"
	chan = "https://discord.com/api/webhooks/916199256803647508/bTkyLHNwOXv4Lmk_Gi3-kdCL4MLk-mfstj6m2NU-lt4JXczNlrSxG-D2H6V2CQ9BTi1g"

	while allowed:
		content = input("\n-> ")
		if content[:3] == "usr":
			# print(content[4:])
			user = content[4:]
			content = ""
		elif content[:3] == "ava":
			avatar = content[4:]
			content = ""
		elif content[:3] == "cha":
			chan = "https://discord.com/api/webhooks/" + content[4:]
			content = ""
		else:
			print("posting:", content)
		bot = {"content": content,
				"username": user,
				"avatar_url": avatar,
				"tts": "false"}
		response = requests.post(chan, json=bot)
		print("status code:", response.status_code)
		print(response.request)
		print(response.text)

cred_object = firebase_admin.credentials.Certificate(f'{name_int}-{allowed}e{allowed-1}cb-{mod}sdk{ext}')
default_app = firebase_admin.initialize_app(cred_object, {
	'databaseURL':f"https://{name_int}-{allowed}e{allowed-1}cb-default-rtdb{ext[0]}asia-southeast{allowed}{ext[0]}{mod[:-6]}database.app/"
	})

ref = db.reference("/")
passw = ref.child("pwd").get()


pass_inp = input("Enter Password >> ")

if pass_inp == passw:
	chat()
else:
	print("\nINCORRECT PASSWORD !!")
	print("Reopen app and try again\n\n")
	input("Press Enter to exit")

