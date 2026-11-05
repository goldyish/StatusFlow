
import os
import sys
import json
import time
import ctypes
import requests

from datetime import datetime
from colorama import Fore, Style, init

init(autoreset=True)

VERSION = "1.0.0"
API = "https://discord.com/api/v10"


# ═══════════════════════════════════════════════════════
# TERMINAL TITLE
# ═══════════════════════════════════════════════════════

def set_terminal_title(title):
    try:
        if os.name == "nt":
            ctypes.windll.kernel32.SetConsoleTitleW(title)
        else:
            sys.stdout.write(f"\033]0;{title}\007")
            sys.stdout.flush()
    except Exception:
        pass


# ═══════════════════════════════════════════════════════
# COLORS AND CONSOLE
# ═══════════════════════════════════════════════════════

C = Fore.CYAN
G = Fore.GREEN
Y = Fore.YELLOW
R = Fore.RED
M = Fore.MAGENTA
W = Fore.WHITE
D = Fore.LIGHTBLACK_EX
B = Fore.BLUE


def clear_console():
    os.system("cls" if os.name == "nt" else "clear")


def read_file_lines(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return [
            line.strip()
            for line in file
            if line.strip()
        ]


def load_config():
    with open("config.json", "r", encoding="utf-8") as file:
        return json.load(file)


def safe_text(value, limit=32):
    value = str(value)
    if len(value) > limit:
        return value[:limit - 3] + "..."
    return value


# ═══════════════════════════════════════════════════════
# DISCORD API
# ═══════════════════════════════════════════════════════

def get_headers(token):
    return {
        "Authorization": token,
        "Content-Type": "application/json"
    }


def get_user_info(token):
    response = requests.get(
        f"{API}/users/@me",
        headers=get_headers(token),
        timeout=15
    )

    if response.status_code == 200:
        data = response.json()
        return data.get("username", "Unknown"), True

    return "Invalid token", False


def change_status(token, message, presence=None):
    payload = {
        "custom_status": {
            "text": message
        }
    }

    if presence:
        payload["status"] = presence

    response = requests.patch(
        f"{API}/users/@me/settings",
        headers=get_headers(token),
        json=payload,
        timeout=15
    )

    return response.status_code == 200


def change_hypesquad(token, house_id):
    payload = {
        "house_id": house_id
    }

    response = requests.post(
        f"{API}/hypesquad/online",
        headers=get_headers(token),
        json=payload,
        timeout=15
    )

    return response.status_code == 204


def change_bio(token, bio_text):
    payload = {
        "bio": bio_text
    }

    response = requests.patch(
        f"{API}/users/@me/profile",
        headers=get_headers(token),
        json=payload,
        timeout=15
    )

    return response.status_code == 200


# ═══════════════════════════════════════════════════════
# STATUSFLOW DASHBOARD
# ═══════════════════════════════════════════════════════

def print_banner():
    print(f"""
{C}╭────────────────────────────────────────────────────────────╮
│                                                            │
│              DISCORD STATUS ROTATOR                        │
│                      {W}StatusFlow{C}                            │
│                                                            │
╰────────────────────────────────────────────────────────────╯{Style.RESET_ALL}
""")


def print_line():
    print(f"{D}{'─' * 60}{Style.RESET_ALL}")


def print_field(label, value, color=W):
    print(
        f" {D}│{Style.RESET_ALL} "
        f"{C}{label:<17}{Style.RESET_ALL}"
        f"{color}{value}{Style.RESET_ALL}"
    )


def print_progress(current, total):
    if total <= 0:
        return

    progress = (current % total) + 1
    percentage = progress / total

    width = 25
    filled = int(width * percentage)

    bar = (
        f"{G}{'█' * filled}"
        f"{D}{'░' * (width - filled)}"
        f"{Style.RESET_ALL}"
    )

    print(
        f" {D}│{Style.RESET_ALL} "
        f"{C}{'Progress':<17}{Style.RESET_ALL}"
        f"{bar} {W}{percentage * 100:.1f}%"
    )

    print(
        f" {D}│{Style.RESET_ALL} "
        f"{D}                 {progress}/{total}{Style.RESET_ALL}"
    )


def print_dashboard(
    username,
    token,
    status,
    presence,
    hypesquad,
    bio,
    status_count,
    total_statuses,
    activity
):
    clear_console()
    print_banner()

    now = datetime.now().strftime("%I:%M:%S %p")

    print(f" {D}┌{'─' * 58}┐{Style.RESET_ALL}")
    print(f" {D}│{Style.RESET_ALL} {W}ACCOUNT OVERVIEW{Style.RESET_ALL}")
    print_line()

    print_field("Account", username, G)
    print_field("Token", token[:5] + "******", D)
    print_field("Activity", activity, G)
    print_field("Version", VERSION, D)

    print_line()
    print(f" {D}│{Style.RESET_ALL} {W}ROTATION DETAILS{Style.RESET_ALL}")
    print_line()

    print_field("Custom Status", safe_text(status), C)
    print_field("Presence", presence or "Default", M)
    print_field("HypeSquad", hypesquad, Y)
    print_field("Bio", safe_text(bio), W)
    print_field("Last Updated", now, D)

    print_line()
    print(f" {D}│{Style.RESET_ALL} {W}ROTATION PROGRESS{Style.RESET_ALL}")
    print_line()

    print_progress(status_count, total_statuses)

    print(f" {D}└{'─' * 58}┘{Style.RESET_ALL}")
    print(
        f"\n {D}StatusFlow v{VERSION} "
        f"| Discord Status Rotator{Style.RESET_ALL}"
    )


# ═══════════════════════════════════════════════════════
# MAIN PROGRAM
# ═══════════════════════════════════════════════════════

def main():
    set_terminal_title("StatusFlow | Starting")

    try:
        config = load_config()

        token = config["token"]
        speed = config.get("speed_rotator", 10)

        if not token:
            print(f"{R}No token found in config.json.{Style.RESET_ALL}")
            return

        if speed <= 0:
            print(f"{R}Rotation speed must be greater than zero.{Style.RESET_ALL}")
            return

        statuses = read_file_lines("text.txt")

        if not statuses:
            print(f"{R}text.txt is empty. Add some statuses.{Style.RESET_ALL}")
            return

        # Presence sequence
        status_sequence = config.get("status_sequence", [])
        use_status_sequence = config.get("use_status_sequence", False)

        if use_status_sequence and not status_sequence:
            use_status_sequence = False

        # HypeSquad settings
        hypesquad_sequence = config.get(
            "custom_hypesquad_sequence",
            config.get("hypesquad_sequence", [])
        )

        hypesquad_mapping = config.get("hypesquad_mapping", {})

        rotate_hypesquad = config.get("rotate_hypesquad", True)
        hypesquad_interval = config.get(
            "hypesquad_rotation_interval", 60
        )

        if not hypesquad_sequence:
            rotate_hypesquad = False

        # Bio settings
        rotate_bio = config.get("rotate_aboutme", True)
        bio_interval = config.get("aboutme_rotation_interval", 60)

        bio_sequence = []

        if rotate_bio:
            try:
                bio_sequence = read_file_lines("aboutme.txt")
            except FileNotFoundError:
                rotate_bio = False

        if not bio_sequence:
            rotate_bio = False

        if hypesquad_interval <= 0 or bio_interval <= 0:
            print(f"{R}Rotation intervals must be greater than zero.{Style.RESET_ALL}")
            return

        # Verify account
        username, valid = get_user_info(token)

        if not valid:
            set_terminal_title("StatusFlow | Invalid Token")
            print(f"{R}Invalid token. Exiting.{Style.RESET_ALL}")
            return

        # Initial values
        status_count = 0
        hypesquad_count = 0
        bio_count = 0

        current_hypesquad = "Not configured"
        current_bio = bio_sequence[0] if rotate_bio else "Disabled"

        next_hypesquad = time.time()
        next_bio = time.time()

        set_terminal_title("StatusFlow | Running")

        while True:
            try:
                current_time = time.time()

                # Select custom status
                status = statuses[status_count % len(statuses)]

                # Select Discord presence
                if use_status_sequence:
                    presence = status_sequence[
                        status_count % len(status_sequence)
                    ]
                else:
                    presence = None

                activity = "RUNNING"

                # HYPESQUAD ROTATION
                if (
                    rotate_hypesquad
                    and current_time >= next_hypesquad
                ):
                    activity = "UPDATING HYPESQUAD"
                    set_terminal_title("StatusFlow | Updating HypeSquad")

                    house = hypesquad_sequence[
                        hypesquad_count % len(hypesquad_sequence)
                    ]

                    house_id = hypesquad_mapping.get(
                        house.lower(), 0
                    )

                    if change_hypesquad(token, house_id):
                        current_hypesquad = house
                    else:
                        current_hypesquad = f"{house} (failed)"

                    hypesquad_count += 1
                    next_hypesquad = current_time + hypesquad_interval

                # BIO ROTATION
                if rotate_bio and current_time >= next_bio:
                    activity = "UPDATING BIO"
                    set_terminal_title("StatusFlow | Updating Bio")

                    bio = bio_sequence[
                        bio_count % len(bio_sequence)
                    ]

                    if change_bio(token, bio):
                        current_bio = bio
                    else:
                        current_bio = f"{bio} (failed)"

                    bio_count += 1
                    next_bio = current_time + bio_interval

                # STATUS ROTATION
                activity = "UPDATING STATUS"
                set_terminal_title("StatusFlow | Updating Status")

                status_success = change_status(
                    token,
                    status,
                    presence
                )

                if not status_success:
                    activity = "STATUS UPDATE FAILED"
                else:
                    activity = "RUNNING"

                # Dashboard
                print_dashboard(
                    username=username,
                    token=token,
                    status=status,
                    presence=presence,
                    hypesquad=current_hypesquad,
                    bio=current_bio,
                    status_count=status_count,
                    total_statuses=len(statuses),
                    activity=activity
                )

                status_count += 1

                set_terminal_title("StatusFlow | Running")
                time.sleep(speed)

            except requests.RequestException as error:
                set_terminal_title("StatusFlow | Network Error")
                print(f"\n{R}Network error: {error}{Style.RESET_ALL}")
                time.sleep(speed)

            except KeyboardInterrupt:
                raise

            except Exception as error:
                print(f"\n{R}Error: {error}{Style.RESET_ALL}")
                time.sleep(speed)

    except KeyboardInterrupt:
        set_terminal_title("StatusFlow | Stopped")
        print(f"\n{Y}StatusFlow stopped by user.{Style.RESET_ALL}")

    except FileNotFoundError as error:
        set_terminal_title("StatusFlow | Missing File")
        print(f"{R}Missing file: {error}{Style.RESET_ALL}")

    except requests.RequestException as error:
        set_terminal_title("StatusFlow | Connection Error")
        print(f"{R}Connection error: {error}{Style.RESET_ALL}")

    except Exception as error:
        set_terminal_title("StatusFlow | Error")
        print(f"{R}Startup error: {error}{Style.RESET_ALL}")


if __name__ == "__main__":
    main()
