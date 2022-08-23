#!/usr/bin/env python3
modules = ["base64", "requests", "json", "os"]

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
    content = base64.b64decode(req['content'])
if content == '':
	print("The content of the versions.json can not be found.")
	exitFunc()
else:
	jcont = json.loads(content)
	print("------")
	# TODO paper, fabric and forge versions
	typ = input("Specify a loader type. (vanilla | paper | fabric | forge) >> ")
	vers = [ver for ver in jcont[typ]]
	print("------")
	print(vers)
	ver = input("Specify a version from the list above >> ")
	print("------")
	fold = "server_"+ver+"_"+typ
	print("Creating "+fold+" folder...")
	os.mkdir(fold)
	print("Downloading server JAR file...")
	open(fold+"\\server.jar", "wb").write(requests.get(jcont[typ][ver]).content)
	print("------")
	print("Done!")
	exitFunc()