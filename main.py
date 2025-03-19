import requests
import json
import time
from datetime import datetime
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

url = "https://mine.aurevia.app/api/tasks/claim"

console = Console()


def display_logo():
    console.print(Panel.fit(
        "[bold cyan] ██████████                               ███████████ █████   █████ ████   ████████ [/]\n"
        "[bold cyan]░░███░░░░███                             ░█░░░███░░░█░░███   ░░███ ░░███  ███░░░░███[/]\n"
        "[bold cyan] ░███   ░░███  ██████   ██████  ████████ ░   ░███  ░  ░███    ░███  ░███ ░░░    ░███[/]\n"
        "[bold cyan] ░███    ░███ ███░░███ ███░░███░░███░░███    ░███     ░███    ░███  ░███    ███████[/]\n"
        "[bold cyan] ░███    ░███░███████ ░███████  ░███ ░███    ░███     ░░███   ███   ░███   ███░░░░[/]\n"
        "[bold cyan] ░███    ███ ░███░░░  ░███░░░   ░███ ░███    ░███      ░░░█████░    ░███  ███      █[/]\n"
        "[bold cyan] ██████████  ░░██████ ░░██████  ░███████     █████       ░░███      █████░██████████[/]\n"
        "[bold cyan]░░░░░░░░░░    ░░░░░░   ░░░░░░   ░███░░░     ░░░░░         ░░░      ░░░░░ ░░░░░░░░░░[/]\n"
        "\n[bold yellow]© DeepTV | Telegram: [blue]https://t.me/DeepTV12[/][/]"
    ))

def get_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def watermark(text, status="INFO", color="white"):
    timestamp = get_time()
    return f"[{timestamp}] [{status}] [bold {color}]{text}[/] [dim]— DeepTV12[/]"



def read_query_ids(file_path="data.txt"):
    """Reads query IDs from a file and returns them as a list."""
    with open(file_path, "r") as file:
        return [line.strip() for line in file.readlines() if line.strip()]


def tasks_request(i,query_id):
    payload = json.dumps({
  "task_id": i
})
    headers = {
      'accept': '*/*',
      'accept-language': 'en-US,en;q=0.9',
      'content-type': 'application/json',
      'initdata': query_id ,
      'origin': 'https://mine.aurevia.app',
      'priority': 'u=1, i',
      'referer': 'https://mine.aurevia.app/tasks',
      'sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
      'sec-ch-ua-mobile': '?0',
      'sec-ch-ua-platform': '"Windows"',
      'sec-fetch-dest': 'empty',
      'sec-fetch-mode': 'cors',
      'sec-fetch-site': 'same-origin',
      'sec-fetch-storage-access': 'active',
      'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    console.print(watermark(response.text))
def send_tasks_request(query_id):
    for i in range(100):
        tasks_request(i,query_id)

def get_telegram_id(query_id):
    url = "https://mine.aurevia.app/api/user/me"
    
    headers = {
        "accept": "*/*",
        "accept-language": "en-US,en;q=0.9",
        "content-length": "0",
        "content-type": "application/json",
        "initdata": query_id,
        "origin": "https://mine.aurevia.app",
        "priority": "u=1, i",
        "referer": "https://mine.aurevia.app/tasks",
        "sec-ch-ua": "\"Chromium\";v=\"134\", \"Not:A-Brand\";v=\"24\", \"Google Chrome\";v=\"134\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "sec-fetch-storage-access": "active",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"
    }

    response = requests.post(url, headers=headers)
    
    if response.status_code == 200:
        try:
            data = response.json()
            telegram_id = data.get("telegram_id")
            if telegram_id:
                return telegram_id
            else:
                return "telegram_id not found in response"
        except requests.exceptions.JSONDecodeError:
            return "Invalid JSON response"
    else:
        return f"Request failed with status code {response.status_code}"

def daily_login(query_id,user_id,task):
    url = "https://mine.aurevia.app/api/user/daily"

    payload = json.dumps({
      "userId": user_id,
      "activityKey": task
    })
    headers = {
      'accept': '*/*',
      'accept-language': 'en-US,en;q=0.9',
      'content-type': 'application/json',
      'initdata': query_id,
      'origin': 'https://mine.aurevia.app',
      'priority': 'u=1, i',
      'referer': 'https://mine.aurevia.app/tasks',
      'sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
      'sec-ch-ua-mobile': '?0',
      'sec-ch-ua-platform': '"Windows"',
      'sec-fetch-dest': 'empty',
      'sec-fetch-mode': 'cors',
      'sec-fetch-site': 'same-origin',
      'sec-fetch-storage-access': 'active',
      'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    console.print(watermark(response.text))


def send_daily_login(query_id):
    user_id= get_telegram_id(query_id)
    console.print(watermark(user_id))
    task = ["checkIn","engagePost"]
    for tasks in task:
        daily_login(query_id,user_id,tasks)






def main():
    query_ids= read_query_ids()
    for queryid in query_ids:
        console.print(watermark("doing tasks for account with user_id: ",queryid))
        send_tasks_request(queryid)
        console.print(watermark("tasks completed successfully"))
        console.print(watermark("Completing daily checkin :"))
        send_daily_login(query_id)
        console.print(watermark("Account completed successfully"))
        console.print(watermark("Waiting 5 seconds before switching accounts"))
        time.sleep(5)


if __name__ == "__main__":
    display_logo()
    while True:
        main()
        console.print(watermark("Accounts Finished","SUCCESS","yellow"))
        console.print(watermark("Sleeping for 24 hours before retrying"))
        time.sleep(24 * 60 * 60)
