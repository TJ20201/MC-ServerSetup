#!/usr/bin/env python3
modules = ["base64", "requests"]

def exitFunc():
	input("> Press enter to exit <")
	exit()

for module in modules:
	try:
		print("Importing "+module+"...")
		exec("import "+module)
		print("Imported "+module+"!")
	except:
		print("Please install the \""+module+"\" module.")
		exitFunc()

url = 'https://api.github.com/repos/TJ20201/MC-ServerSetup/contents/versions.json'
req = requests.get(url)
content = ''
if req.status_code == requests.codes.ok:
    req = req.json()
    content = base64.decodestring(req['content'])

if content == '':
	print("The content of the versions.json can not be found.")
	exitFunc()
else:
	print(content)