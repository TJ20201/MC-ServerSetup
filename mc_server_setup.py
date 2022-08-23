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
	try:
		jcont = json.loads(content)
		print("------")
		typ = input("Specify a loader type. (vanilla | paper | fabric) >> ")
		vers = [ver for ver in jcont[typ]]
		print("------")
		print(vers)
		ver = input("Specify a version from the list above >> ")
		print("------")
		fold = "server_"+ver+"_"+typ
		print("Creating "+fold+" folder...")
		os.mkdir(fold)
		print("Downloading server JAR file...")
		jar = open(fold+"\\server.jar", "wb")
		jar.write(requests.get(jcont[typ][ver]).content)
		print("Creating EULA file...")
		eula = open(fold+"\\eula.txt", "wb")
		eula.write(bytes("eula=true", "utf8"))
		print("Creating RUN batch file...")
		runbat = open(fold+"\\run.bat", "wb")
		runbat.write(bytes("java -Xmx1G -Xms1G -jar server.jar nogui\npause", "utf8"))
		print("------")
		print("Done!")
		exitFunc()
	except Exception as e:
		print(e)
		exitFunc()