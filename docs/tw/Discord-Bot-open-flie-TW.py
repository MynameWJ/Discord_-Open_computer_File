import discord
import subprocess
import configparser
import os

# 讀取 config.txt (Read config.txt)
config = configparser.ConfigParser()
config.read('config.txt')

#TOKEN、CHANNEL_ID 和 File 路徑(TOKEN, CHANNEL_ID and File path)
TOKEN = config.get('DEFAULT', 'token')
CHANNEL_ID = int(config.get('DEFAULT', 'channel_ID'))
FILE = config.get('DEFAULT', 'File')
FileName = FILE

# 設置權限(Set permissions)
intents = discord.Intents.default()
intents.message_content = True  


client = discord.Client(intents=intents)

# 全局變量(Global variables)
process = None

@client.event
async def on_ready():
    print(f'已成功開啟 {client.user}')

@client.event
async def on_message(message):
    global process

    # 指令來自頻道(Command comes from channel)
    if message.channel.id == CHANNEL_ID:
        
        if message.content.lower() == 'help':
            await message.channel.send("open 開啟\nstop 關閉\ndetect 偵測")
    
        # 收到 "open" 指令("open" command received)
        if message.content.lower() == 'open':
            if process is None:
                # 檢查 .bat 文件是否存在(Check if the .bat file exists)
                if not os.path.exists(FILE):
                    await message.channel.send(f"錯誤：找不到文件 {FileName}。請檢查路徑。")
                    return
                
                try:
                    # 嘗試啟動文件{Try to start the file}
                    process = subprocess.Popen([FILE], shell=True)
                    if process.poll() is not None:  # 如果進程立即結束，說明啟動失敗(If the process ends immediately, the startup failed)
                        await message.channel.send(f"錯誤：無法啟動 {FileName} 文件。")
                        process = None
                    else:
                        await message.channel.send(f"已成功打開 {FileName} 文件！")
                except Exception as e:
                    await message.channel.send(f"發生錯誤：{e}")
            else:
                await message.channel.send(f"{FileName} 文件已在運行中！")

        # 是否收到 "stop" 指令(Whether the "stop" command is received)
        elif message.content.lower() == 'stop':
            if process is not None:
                try:
                    subprocess.run(["taskkill", "/F", "/T", "/PID", str(process.pid)], check=True)
                    process = None  # 重置句柄(Reset handle)
                    await message.channel.send(f"已成功關閉 {FileName} 文件及其子進程！")
                except Exception as e:
                    await message.channel.send(f"無法強制關閉進程：{e}")
            else:
                await message.channel.send(f"{FileName} 文件尚未運行！")
        
        # 檢查是否收到 "detect" 指令(Check if the "detect" command is received)
        elif message.content.lower() == 'detect':
            if process is not None and process.poll() is None:  # 檢查進程是否正在運行(Check if the process is running)
                await message.channel.send(f"{FileName} 運行中……")
            else:
                await message.channel.send(f"{FileName} 等待開啟……")

client.run(TOKEN)
