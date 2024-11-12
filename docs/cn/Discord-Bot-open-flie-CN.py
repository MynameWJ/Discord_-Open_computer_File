import discord
import subprocess
import configparser
import os

# 读取 config.txt (Read config.txt)
config = configparser.ConfigParser()
config.read('config.txt')

#TOKEN、CHANNEL_ID 和 File 路径(TOKEN, CHANNEL_ID and File path)
TOKEN = config.get('DEFAULT', 'token')
CHANNEL_ID = int(config.get('DEFAULT', 'channel_ID'))
FILE = config.get('DEFAULT', 'File')
FileName = FILE

# 设置权限(Set permissions)
intents = discord.Intents.default()
intents.message_content = True  

client = discord.Client(intents=intents)

# 全局变量(Global variables)
process = None

@client.event
async def on_ready():
    print(f'已成功开启 {client.user}')

@client.event
async def on_message(message):
    global process

    # 指令来自频道(Command comes from channel)
    if message.channel.id == CHANNEL_ID:
        
        if message.content.lower() == 'help':
            await message.channel.send("open 开启\nstop 关闭\ndetect 检测")
    
        # 收到 "open" 指令("open" command received)
        if message.content.lower() == 'open':
            if process is None:
                # 检查 .bat 文件是否存在(Check if the .bat file exists)
                if not os.path.exists(FILE):
                    await message.channel.send(f"错误：找不到文件 {FileName}。请检查路径。")
                    return
                
                try:
                    # 尝试启动文件(Try to start the file)
                    process = subprocess.Popen([FILE], shell=True)
                    if process.poll() is not None:  # 如果进程立即结束，说明启动失败(If the process ends immediately, the startup failed)
                        await message.channel.send(f"错误：无法启动 {FileName} 文件。")
                        process = None
                    else:
                        await message.channel.send(f"已成功打开 {FileName} 文件！")
                except Exception as e:
                    await message.channel.send(f"发生错误：{e}")
            else:
                await message.channel.send(f"{FileName} 文件已在运行中！")

        # 是否收到 "stop" 指令(Whether the "stop" command is received)
        elif message.content.lower() == 'stop':
            if process is not None:
                try:
                    subprocess.run(["taskkill", "/F", "/T", "/PID", str(process.pid)], check=True)
                    process = None  # 重置句柄(Reset handle)
                    await message.channel.send(f"已成功关闭 {FileName} 文件及其子进程！")
                except Exception as e:
                    await message.channel.send(f"无法强制关闭进程：{e}")
            else:
                await message.channel.send(f"{FileName} 文件尚未运行！")
        
        # 检查是否收到 "detect" 指令(Check if the "detect" command is received)
        elif message.content.lower() == 'detect':
            if process is not None and process.poll() is None:  # 检查进程是否正在运行(Check if the process is running)
                await message.channel.send(f"{FileName} 运行中……")
            else:
                await message.channel.send(f"{FileName} 等待开启……")

client.run(TOKEN)
