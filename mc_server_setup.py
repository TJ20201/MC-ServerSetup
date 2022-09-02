#!/usr/bin/env python3
modules = ["base64", "requests", "json", "os"]
version = "1.1.0"

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

url = 'https://api.github.com/repos/TJ20201/MC-ServerSetup/contents/meta.json'
req = requests.get(url)
content = ''
if req.status_code == requests.codes.ok:
    req = req.json()
    content = base64.b64decode(req['content'])
if content == '':
	print("The content of the meta.json can not be found. Do you have an accessible internet connection?")
	exitFunc()
jcont = json.loads(content)
lts_version = jcont["mcss_ver"]
if lts_version != version:
	print(f"A (possibly newer) stable version of the Minecraft Server Setup tool is available. (Latest stable version {lts_version} is available whilst you are on version {version}.)")
else:
	try:
		# TODO special versions (eg. bedrock-paper which has pre-installed addons defined but not accessible)
		print("------")
		# Loader types: VANILLA, PAPER, MODDED
		# Variants: V0: Vanilla, P0: Paper, P1: Bedrock/Paper, M0: Fabric
		typ = input("Specify a loader type. (vanilla | paper | fabric | bedrock-paper) >> ")
		# Extra additions to specific versions (eg. bedrock-paper autoinstalls Geyser)
		variant = 0
		# Variant handler
		if typ == "bedrock-paper": variant = 1
		# Type handler
		if typ == "paper": typ == "plugin"
		if typ == "fabric": typ = "modded"
		# Version List
		vers = [ver for ver in jcont["versions"][typ]]
		print("------")
		print(vers)
		ver = input("Specify a version from the list above >> ")
		print("------")
		ex = ""
		if typ == "plugin":
			if variant == 0: ex = "paper"
			if variant == 1: ex = "bedrockpaper"
		if typ == "modded":
			if variant == 0: ex = "fabric"
		fold = "server_"+ex+ver+"_"+typ
		print("Creating "+fold+" folder...")
		os.mkdir(fold)
		print("Downloading server JAR file...")
		jar = open(fold+"\\server.jar", "wb")
		jar.write(requests.get(jcont["versions"][typ][ver]).content)
		jar.close()
		print("Creating EULA file...")
		eula = open(fold+"\\eula.txt", "w")
		eula.write("eula=true")
		eula.close()
		# Special folder
		if typ != "vanilla":
			if typ == "plugin":
				print("Creating PLUGINS folder...")
				os.mkdir("plugins")
			if typ == "modded":
				print("Creating MODS folder...")
				os.mkdir("mods")
		# Autofill special folder
		if typ == "plugin" and variant == 1:
			for mod in jcont["addons"]["bedrock-paper"].content:
				fil = open(fold+f"\\plugins\\{mod.name}")
				fil.write(requests.get(mod.url))
				fil.close()
		# Run helper file
		print("Creating RUN batch file...")
		runbat = open(fold+"\\run.bat", "w")
		runbat.write("@echo off\njava -Xmx1G -Xms1G -jar server.jar nogui\npause")
		runbat.close()
		print("------")
		print("Done!")
		exitFunc()
	except Exception as e:
		print(e)
		exitFunc()