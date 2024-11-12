# Discord_-Open_computer_File

 [English](../../README.md) | [繁體中文](docs/tw/README.md) | [简体中文](../cn/README.md) 

# Discord Bot 用於遠端開啟桌面 <.bat> 檔案  

這個 Discord 機器人允許您透過 Discord 頻道中的指令，遠端控制電腦上的指定 .bat 檔案。最初的用途是從 Discord 頻道中開啟 Minecraft 伺服器的 .bat 檔案，但此機器人也可用於遠端管理電腦上的其他任務。

## 功能
- **開啟 .bat 檔案**：遠端啟動電腦上的指定 .bat 檔案。
- **停止運行的 .bat 檔案**：強制終止運行中的 .bat 檔案及其子進程。
- **檢查狀態**：檢測 .bat 檔案是否正在運行。

## 前置需求
- **Python**：版本 3.10 或更高。
- **Discord 機器人 Token**：在 Discord 開發者平台創建一個機器人並獲取其 Token。
- **權限**：您的機器人需要具備在指定頻道中讀取和回覆訊息的權限。

## 安裝
	
1. 使用 pip 安裝所需依賴：

   ```bash
   pip install discord.py
2.在專案目錄下創建 config.txt 檔案，格式如下：

    [DEFAULT]
    token = your_discord_bot_token_here
    channel_ID = your_channel_id_here
    File = C:\path\to\your\file.bat
token：您的 Discord 機器人的 Token。
channel_ID：機器人監聽指令的 Discord 頻道 ID。
File：您要控制的 .bat 檔案的完整路徑。

<H1>使用方法
<H3>一切設置完成後，運行機器人
  
    python your_script_name.py
<H1>在指定的 Discord 頻道中，您可以使用以下指令：
<H3><br>open – 如果 .bat 檔案未在運行中，則啟動它。
<H3><br>stop – 停止運行中的 .bat 檔案及其相關子進程。
<H3><br>detect – 檢查 .bat 檔案是否正在運行。
  
<H1>範例
<H3>假設您的 .bat 檔案是一個位於 C:\MinecraftServer\start.bat 的 Minecraft 伺服器啟動腳本，您可以在指定頻道中透過以下指令來控制它：

<br>open：機器人將啟動 Minecraft 伺服器（如果它尚未在運行）。
<br>stop：機器人將停止伺服器（如果它在運行中）。
<br>detect：機器人將告知您伺服器當前是否在運行中。
<br><H1>注意
<H3>此機器人僅用於本地操作，並假設運行機器人的電腦可存取指定的 .bat 檔案。請確保在 config.txt 中正確設置路徑， <br><font color="red">**對於Windows 系統，需將反斜杠加倍，例如：C:\\path\\to\\your\\file.bat。**</font>

<H2>免責聲明
<H4>請負責任地使用此機器人，並小心它可以遠端執行的檔案和指令。配置不當或濫用可能會使您的電腦執行重要的功能。

<H2>授權
<H4>此專案採用 MIT 許可證授權。
