# MC-ServerSetup
A python file that will easily set up a new Minecraft Server for you.
NOTE: This only creates the basic `server.jar` and an accepted `eula.txt` for you as of now with a `run.bat` file to start up your server.

## Installation
You can find the latest working `mc_server_setup.py` in the releases section. Put it into a folder with nothing else in it and then run it `mc_server_setup.py` to begin setup. If you want a development version, you can directly install the `mc_server_setup.py` from source.

## Usage
1. To use this server setup tool, double click on `mc_server_setup.py` to run it. You will see it importing some modules, if you do not have a module and see a message telling you to install it, proceed. If everything imports and you are asked for a loader version, skip to step 3.
2. If you get a message to tell you to install a module, open up a CMD window and run this command, replacing <module> with the module you have to install: `pip install <module>`. After doing this, run `mc_server_setup.py` again and if you get another message to install a module repeat this step, otherwise move on to step 3.
3. After importing all modules, you will be prompted to provide a loader type. Each loader will be described here, type in the one you want and proceed to step 4:
   - VANILLA - The basic Minecraft experience with no mods or plugins.
   - PAPER   - Minecraft with the ability for plugins such as Essentials.
   - FABRIC  - Minecraft with mods from the [Fabric Loader](https://fabricmc.net) for 1.14.4 and above or the [Legacy Fabric](https://legacyfabric.net) loader for 1.13.2 and below.
4. After providing a loader type, you can choose a Minecraft version from 1.9.4 to 1.19.2. Each version is the last one before the next version (eg. 1.10.2 was the final version before 1.11 was made). Choose a version from the list given to you by the version chooser prompt (the list will be surrounded in square brackets which look like []). 1.8 is not supported by this setup tool due to being an EXE server file and not a JAR server file.
5. Finally, your server will be created in a folder named after your options, it will begin with `server_` and have your version in the middle (eg. `1.19.2`) and end with your loader type (eg. `fabric`). Once it finishes creating and you see `Done!` printed at the bottom of the console, you can close down the `mc_server_setup.py` file and begin configuring your server! (See the CONFIGURING section below for tips on configuring your server.)

## Configuring
After you have setup the basics of your server and have been given a folder with a `server.jar`, `eula.txt` and `run.bat` file, double click the `run.bat` file to start it and let your server finish generating the world before entering `stop`, waiting for the server to stop and pressing your enter key to close down the server completely. Once you have done that, you can begin configuring your server completely. For all versions, you will want to change the `server.properties` file to your desired setting as well as considering the content in the SERVER PROPERTIES subsection below.
### Server Properties
To allow your server to be accessed online, you should set your `server-ip` to your local machine IP (eg. `192.168.0.xx`) and port forward your server with your server port (`25565` by default for Java Edition). If you decide to do this, restart your server and you should be able to start up your server with no problems and connect to it via your public IP (eg. `123.456.789.012`).

If you want to use command blocks but you are unable to, find the `enable-command-block` property and change its value from `false` to `true`. Restart your server to apply this change.
### Installing Addons (plugins, mods, etc)
If you have a PAPER, FABRIC or FORGE server you will see an extra folder. For PAPER, this folder will be called `plugins` but for FABRIC and FORGE it will be called `mods`. In this folder, you can put any JAR plugin for PAPER or any JAR mod for FABRIC and FORGE as long as they support your server's version.

## Sources
Below is a table of every version source from 1.9.4 to 1.19.2
| VERSION  |  LOADER  |  SOURCE  |
|----------|----------|----------|
|   1.9.4  |  VANILLA | piston-data.mojang.com |
|   1.9.4  |  PAPER   | api.papermc.io |
|   1.9.4  |  FABRIC  | meta.legacyfabric.net |
|   1.9.4  |  FORGE   | [tba] |
|----------|----------|----------|
|   1.10.2  |  VANILLA | piston-data.mojang.com |
|   1.10.2  |  PAPER   | api.papermc.io |
|   1.10.2  |  FABRIC  | meta.legacyfabric.net |
|   1.10.2  |  FORGE   | [tba] |
|----------|----------|----------|
|   1.11.2  |  VANILLA | piston-data.mojang.com |
|   1.11.2  |  PAPER   | api.papermc.io |
|   1.11.2  |  FABRIC  | meta.legacyfabric.net |
|   1.11.2  |  FORGE   | [tba] |
|----------|----------|----------|
|   1.12.2  |  VANILLA | piston-data.mojang.com |
|   1.12.2  |  PAPER   | api.papermc.io |
|   1.12.2  |  FABRIC  | meta.legacyfabric.net |
|   1.12.2  |  FORGE   | [tba] |
|----------|----------|----------|
|   1.13.2  |  VANILLA | piston-data.mojang.com |
|   1.13.2  |  PAPER   | api.papermc.io |
|   1.13.2  |  FABRIC  | meta.legacyfabric.net |
|   1.13.2  |  FORGE   | [tba] |
|----------|----------|----------|
|   1.14.4  |  VANILLA | piston-data.mojang.com |
|   1.14.4  |  PAPER   | api.papermc.io |
|   1.14.4  |  FABRIC  | meta.fabricmc.net |
|   1.14.4  |  FORGE   | [tba] |
|----------|----------|----------|
|   1.15.2  |  VANILLA | piston-data.mojang.com |
|   1.15.2  |  PAPER   | api.papermc.io |
|   1.15.2  |  FABRIC  | meta.fabricmc.net |
|   1.15.2  |  FORGE   | [tba] |
|----------|----------|----------|
|   1.16.5  |  VANILLA | piston-data.mojang.com |
|   1.16.5  |  PAPER   | api.papermc.io |
|   1.16.5  |  FABRIC  | meta.fabricmc.net |
|   1.16.5  |  FORGE   | [tba] |
|----------|----------|----------|
|   1.17.1  |  VANILLA | piston-data.mojang.com |
|   1.17.1  |  PAPER   | api.papermc.io |
|   1.17.1  |  FABRIC  | meta.fabricmc.net |
|   1.17.1  |  FORGE   | [tba] |
|----------|----------|----------|
|   1.18.2  |  VANILLA | piston-data.mojang.com |
|   1.18.2  |  PAPER   | api.papermc.io |
|   1.18.2  |  FABRIC  | meta.fabricmc.net |
|   1.18.2  |  FORGE   | [tba] |
|----------|----------|----------|
|   1.19.2  |  VANILLA | piston-data.mojang.com |
|   1.19.2  |  PAPER   | api.papermc.io |
|   1.19.2  |  FABRIC  | meta.fabricmc.net |
|   1.19.2  |  FORGE   | [tba] |
|----------|----------|----------|
|  | `WARNING: VERSION 1.20.0 IS NOT YET RELEASED, DATA IS OF LATEST SNAPSHOT` |
|   1.20.0  |  VANILLA | piston-data.mojang.com |
|   1.20.0  |  PAPER   | [tba] |
|   1.20.0  |  FABRIC  | [tba] |
|   1.20.0  |  FORGE   | [tba] |
