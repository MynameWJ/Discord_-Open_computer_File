# Discord_-Open_computer_File

 [English](README.md) | [繁體中文](docs/tw/README.md) | [简体中文](docs/cn/README.md) 

<H1>Discord Bot for Remote open Desktop <.bat>  <br><br>


<H3>This Discord bot allows you to remotely control specific .bat files on your computer via Discord commands in a designated channel. Initially created to enable opening a Minecraft server .bat file from a Discord channel, this bot could be useful for managing various tasks on your computer remotely.

<H1>Features
<H3>Open .bat Files: Remotely start a specified .bat file on your computer.
Stop Running .bat Files: Forcefully terminate the running .bat file and its subprocesses.
Check Status: Detect whether the .bat file is currently running.

<br><H1>Prerequisites
<H3>Python: Version 3.10 or later.
Discord Bot Token: Create a bot on the Discord Developer Portal and get its token.
Permissions: Your bot requires specific permissions to read and respond to messages in a designated channel.

<br><H1>Installation
	
<H3>1.Clone the repository or download the script file.

2.Install required dependencies via pip:

<pre><code>pip install discord.py</code></pre>

3.Create a config.txt file in the project directory with the following format:
<pre><code>[DEFAULT]
token = your_discord_bot_token_here
channel_ID = your_channel_id_here
File = C:\path\to\your\file.bat</code></pre>

<br>token: The token for your Discord bot.
<br>channel_ID: The ID of the Discord channel where the bot will listen for commands.
<br>File: Full path to the .bat file you want to control.

<H1>Usage
<H3>Once everything is set up, run the bot:


<pre><code>python your_script_name.py</code></pre>

<H1>In the designated Discord channel, you can use the following commands:

<H3><br>open – Starts the .bat file if it is not already running.
<br>stop – Stops the running .bat file and any associated subprocesses.
<br>detect – Checks if the .bat file is currently running.

<H1>Example
<H3>Say your .bat file is a Minecraft server start script located at C:\MinecraftServer\start.bat. You can control it via Discord by typing the following commands in the specified channel:

<br>open: The bot will start the Minecraft server if it's not already running.
<br>stop: The bot will stop the server if it is running.
<br>detect: The bot will tell you if the server is currently running.
<H1>Notes
<H3>This bot is designed for local use and assumes the computer running the bot has access to the specified .bat file. Make sure your path is correctly set in config.txt, with backslashes doubled for Windows (e.g., C:\\path\\to\\your\\file.bat).

<H1>Disclaimer
<H3>Use this bot responsibly, and be cautious with files and commands that it can execute remotely. Misconfiguration or misuse could allow remote access to critical functions on your computer.

<H1>License
<H3>This project is licensed under the MIT License.
