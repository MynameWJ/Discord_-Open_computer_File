# Discord_-Open_computer_File

 [English](README.md) | [繁体中文](docs/tw/README.md) | [简体中文](docs/cn/README.md)

# Discord Bot 用于远端开启桌面 <.bat> 档案

这个 Discord 机器人允许您透过 Discord 频道中的指令，远端控制电脑上的指定 .bat 档案。最初的用途是从 Discord 频道中开启 Minecraft 伺服器的 .bat 档案，但此机器人也可用于远端管理电脑上的其他任务。

## 功能
- **开启 .bat 档案**：远端启动电脑上的指定 .bat 档案。
- **停止运行的 .bat 档案**：强制终止运行中的 .bat 档案及其子进程。
- **检查状态**：检测 .bat 档案是否正在运行。

## 前置需求
- **Python**：版本 3.10 或更高。
- **Discord 机器人 Token**：在 Discord 开发者平台创建一个机器人并获取其 Token。
- **权限**：您的机器人需要具备在指定频道中读取和回覆讯息的权限。

## 安装

1. 使用 pip 安装所需依赖：

   ```bash
   pip install discord.py
2.在专案目录下创建 config.txt 档案，格式如下：

    [DEFAULT]
    token = your_discord_bot_token_here
    channel_ID = your_channel_id_here
    File = C:\path\to\your\file.bat
token：您的 Discord 机器人的 Token。<br>
channel_ID：机器人监听指令的 Discord 频道 ID。<br>
File：您要控制的 .bat 档案的完整路径。<br>

<H1>使用方法
<H3>一切设置完成后，运行机器人

    python your_script_name.py
<H1>在指定的 Discord 频道中，您可以使用以下指令：
<H3><br>open – 如果 .bat 档案未在运行中，则启动它。
<H3><br>stop – 停止运行中的 .bat 档案及其相关子进程。
<H3><br>detect – 检查 .bat 档案是否正在运行。

<H1>范例
<H3>假设您的 .bat 档案是一个位于 C:\MinecraftServer\start.bat 的 Minecraft 伺服器启动脚本，您可以在指定频道中透过以下指令来控制它：

<br>open：机器人将启动 Minecraft 伺服器（如果它尚未在运行）。
<br>stop：机器人将停止伺服器（如果它在运行中）。
<br>detect：机器人将告知您伺服器当前是否在运行中。
<br><H1>注意
<H3>此机器人仅用于本地操作，并假设运行机器人的电脑可存取指定的 .bat 档案。请确保在config.txt 中正确设置路径， <br><font color="red">**对于Windows 系统，需将反斜杠加倍，例如：C:\\path\\to\\your\\file.bat。 **</font>

<H2>免责声明
<H4>请负责任地使用此机器人，并小心它可以远端执行的档案和指令。配置不当或滥用可能会使您的电脑执行重要的功能。

<H2>授权
<H4>此专案采用 MIT 许可证授权。
