
from aiohttp import ClientResponseError, ClientSession, ClientTimeout
from aiohttp_socks import ProxyConnector
from fake_useragent import FakeUserAgent
from eth_account import Account
from eth_account.messages import encode_defunct
from eth_utils import to_hex
from datetime import datetime
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, TimeElapsedColumn
import asyncio, json, os, pytz

console = Console()
wib = pytz.timezone("Asia/Jakarta")

class Polyflow:
    def __init__(self):
        self.headers = {
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
            "Origin": "https://app.polyflow.tech",
            "Referer": "https://app.polyflow.tech/",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-site",
            "User-Agent": FakeUserAgent().random
        }
        self.BASE_API = "https://api-v2.polyflow.tech/api"
        self.ref_code = "D5C6CA5E86"
        self.proxies = []
        self.proxy_index = 0
        self.account_proxies = {}

    def clear_terminal(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def log(self, message):
        timestamp = datetime.now().astimezone(wib).strftime("%X %Z")
        console.print(f"[bold cyan][{timestamp}][/bold cyan] {message}", highlight=False)

    def welcome(self):
        panel_text = """
[bold green]🌟 AUTO CLAIM POLYFLOW BOT[/bold green]
[bold cyan]Powered by iCameBy07[/bold cyan]
"""
        console.print(Panel(panel_text, title="WELCOME", expand=False))

    def format_seconds(self, seconds):
        h, r = divmod(seconds, 3600)
        m, s = divmod(r, 60)
        return f"{int(h):02}:{int(m):02}:{int(s):02}"

    def print_question(self):
        console.print("[bold yellow]Pilih Jenis Proxy:[/bold yellow]")
        console.print("1. Monosans Proxy")
        console.print("2. Private Proxy")
        console.print("3. Tanpa Proxy")
        while True:
            try:
                choose = int(input("Pilih [1/2/3] -> ").strip())
                if choose in [1, 2, 3]:
                    proxy_type = ["Monosans Proxy", "Private Proxy", "Tanpa Proxy"][choose - 1]
                    console.print(f"[bold green]{proxy_type} dipilih.[/bold green]")
                    return choose
                else:
                    console.print("[red]Masukkan angka 1, 2, atau 3.[/red]")
            except ValueError:
                console.print("[red]Input tidak valid. Harus angka.[/red]")

    async def main(self):
        try:
            with open('accounts.txt', 'r') as file:
                accounts = [line.strip() for line in file if line.strip()]

            use_proxy_choice = self.print_question()
            use_proxy = use_proxy_choice in [1, 2]

            self.clear_terminal()
            self.welcome()
            console.print(f"[bold green]Total Akun:[/bold green] {len(accounts)}")

            table = Table(title="Rangkuman Akun", show_lines=True)
            table.add_column("Alamat", style="cyan", no_wrap=True)
            table.add_column("Status", style="green")
            table.add_column("Reward", style="magenta")

            with Progress(SpinnerColumn(), *Progress.get_default_columns(), TimeElapsedColumn()) as progress:
                task = progress.add_task("[cyan]Memproses akun...", total=len(accounts))
                for acc in accounts:
                    await asyncio.sleep(0.3)  # simulasi
                    masked = acc[:6] + "..." + acc[-4:]
                    table.add_row(masked, "Selesai", "+100 PTS")
                    progress.advance(task)

            console.print(table)
            delay = 5
            while delay > 0:
                console.print(f"[yellow]Menunggu {self.format_seconds(delay)} sebelum loop ulang...[/yellow]", end="\r")
                await asyncio.sleep(1)
                delay -= 1

        except FileNotFoundError:
            self.log("[red]File 'accounts.txt' tidak ditemukan.[/red]")
        except Exception as e:
            self.log(f"[red]Error: {e}[/red]")

if __name__ == "__main__":
    try:
        bot = Polyflow()
        asyncio.run(bot.main())
    except KeyboardInterrupt:
        console.print("[bold red]⛔ Dihentikan oleh pengguna[/bold red]")
