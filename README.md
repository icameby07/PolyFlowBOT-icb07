# PolyFlowBOT-icb07

- Register Here : [PolyFlow](https://app.polyflow.tech/?refCode=B35B775D42)
- Use Code      : B35B775D42

## Features

  - Auto Get Account Information
  - Auto Run With [Monosans](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/all.txt) Proxy - Choose 1
  - Auto Run With Private Proxy - Choose 2
  - Auto Run Without Proxy - Choose 3
  - Auto Complete Daily & Tutorial Quests
  - Multi Accounts

### Note: For now, I made the bot to skipping the scan to earn task, because the risk of the account being banned is very high.

## Requiremnets

- Make sure you have Python3.9 or higher installed and pip.

## Instalation

1. **Clone The Repositories:**
   ```bash
   git clone https://github.com/icameby07/PolyFlowBOT-icb07.git
   ```
   ```bash
   cd PolyFlow-BOT
   ```

2. **Install Requirements:**
   ```bash
   pip install -r requirements.txt #or pip3 install -r requirements.txt
   ```

## Configuration

- **accounts.txt:** You will find the file `accounts.txt` inside the project directory. Make sure `accounts.txt` contains data that matches the format expected by the script. Here are examples of file formats:
  ```bash
    your_evm_private_key_1
    your_evm_private_key_2
  ```

  - **proxy.txt:** You will find the file `proxy.txt` inside the project directory. Make sure `proxy.txt` contains data that matches the format expected by the script. Here are examples of file formats:
  ```bash
    ip:port # Default Protcol HTTP.
    protocol://ip:port
    protocol://user:pass@ip:port
  ```

## Run

```bash
python icameby.py #or python3 icameby.py
```
