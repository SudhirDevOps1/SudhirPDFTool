import fitz
import os
import time
import sys
from datetime import datetime
from colorama import Fore, Style, init

init(autoreset=True)

LOG_FILE = "pdf_architect.log"

# -------------------------------------------------
# UTILS
# -------------------------------------------------
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def animate(text, color=Fore.CYAN, delay=1.0):
    spinner = "⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏"
    for i in range(int(delay * 10)):
        sys.stdout.write(f"\r   {color}{Style.BRIGHT}{text} {spinner[i % len(spinner)]}")
        sys.stdout.flush()
        time.sleep(0.1)
    print(f"\r   {Fore.GREEN}{Style.BRIGHT}{text} ✔ Done")

def unique_path(path):
    if not os.path.exists(path):
        return path
    base, ext = os.path.splitext(path)
    i = 1
    while True:
        new = f"{base} ({i}){ext}"
        if not os.path.exists(new):
            return new
        i += 1

def open_folder(path):
    folder = os.path.dirname(path)
    if os.name == 'nt':
        os.startfile(folder)
    elif sys.platform == 'darwin':
        os.system(f'open "{folder}"')
    else:
        os.system(f'xdg-open "{folder}"')

def log_run(data):
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(data)

# -------------------------------------------------
# UI
# -------------------------------------------------
def banner():
    print(f"{Fore.MAGENTA}{Style.BRIGHT}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(f"{Fore.CYAN}{Style.BRIGHT}🚀  SUDHIR SINGH'S PDF ARCHITECT PRO")
    print(f"{Fore.YELLOW}GitHub: @SudhirDevOps1 | Version: v11.2")
    print(f"{Fore.MAGENTA}{Style.BRIGHT}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

def ethical_policy():
    print(f"\n{Fore.GREEN}{Style.BRIGHT}🛡 ETHICAL SECURITY POLICY")
    print(f"{Fore.CYAN}✔ Passwords are NEVER cracked or bypassed")
    print(f"{Fore.CYAN}✔ Only user-provided passwords are accepted")
    print(f"{Fore.CYAN}✔ Use only files you own or have permission for")
    print(f"{Fore.YELLOW}⚖ This tool respects PDF encryption standards")

# -------------------------------------------------
def show_security_info(was_encrypted, doc):
    print(f"\n{Fore.MAGENTA}{Style.BRIGHT}🔍 PDF Security Report")
    print(f"{Fore.CYAN}• Originally Encrypted : {'YES' if was_encrypted else 'NO'}")
    print(f"{Fore.CYAN}• Currently Locked     : {'YES' if doc.is_encrypted else 'NO'}")
    print(f"{Fore.CYAN}• Page Count           : {doc.page_count}")

def progress_bar(current, total, width=20):
    filled = int(width * current / total)
    bar = "█" * filled + "░" * (width - filled)
    sys.stdout.write(
        f"\r{Fore.BLUE}📄 Processing Pages "
        f"[{Fore.GREEN}{bar}{Fore.BLUE}] "
        f"{Fore.YELLOW}{current}/{total}"
    )
    sys.stdout.flush()

# -------------------------------------------------
# MAIN
# -------------------------------------------------
def main():
    while True:
        clear()
        banner()
        ethical_policy()

        path = input(f"\n{Fore.GREEN}📂 Enter PDF Path ➜ {Fore.CYAN}").strip().replace('"', '')
        if path.lower() == "exit":
            break
        if not os.path.exists(path):
            print(f"{Fore.RED}❌ File not found")
            time.sleep(2)
            continue

        try:
            doc = fitz.open(path)
        except:
            print(f"{Fore.RED}❌ Cannot open PDF")
            time.sleep(2)
            continue

        was_encrypted = doc.is_encrypted
        original_password = None

        if was_encrypted:
            print(f"\n{Fore.YELLOW}🔐 PDF is password protected")
            if input(f"{Fore.CYAN}Do you have the password? (y/n) ➜ ").lower() != "y":
                print(f"{Fore.RED}⚠ Cannot proceed without password")
                time.sleep(2)
                continue

            original_password = input(f"{Fore.RED}Enter Password ➜ {Fore.CYAN}")
            if not doc.authenticate(original_password):
                print(f"{Fore.RED}❌ Wrong password")
                time.sleep(2)
                continue

        show_security_info(was_encrypted, doc)

        print(f"\n{Fore.MAGENTA}🧾 Metadata Injector")
        title = input(f"{Fore.BLUE}Title ➜ {Fore.CYAN}") or os.path.basename(path)
        author = input(f"{Fore.BLUE}Author ➜ {Fore.CYAN}") or "Sudhir Singh"
        keywords = input(f"{Fore.BLUE}Keywords ➜ {Fore.CYAN}") or "PDF, Compression"

        # -------- PASSWORD OUTPUT LOGIC --------
        protect = False
        out_pwd = None

        if was_encrypted:
            print(f"\n{Fore.RED}{Style.BRIGHT}⚠ Original PDF password detected!")
            print(f"{Fore.CYAN}[1] {Fore.GREEN}Keep original password")
            print(f"{Fore.CYAN}[2] {Fore.YELLOW}Remove password")
            print(f"{Fore.CYAN}[3] {Fore.MAGENTA}New password")

            while True:
                choice = input(f"{Fore.GREEN}Select ➜ {Fore.CYAN}")
                if choice in ['1', '2', '3']:
                    break

            if choice == '1':
                protect = True
                out_pwd = original_password
            elif choice == '3':
                protect = True
                out_pwd = input(f"{Fore.RED}Set New Password ➜ {Fore.CYAN}")

        else:
            protect = input(
                f"\n{Fore.YELLOW}🔐 Password-protect output? (y/n) ➜ {Fore.CYAN}"
            ).lower() == 'y'
            if protect:
                out_pwd = input(f"{Fore.RED}Set Password ➜ {Fore.CYAN}")

        # -------- COMPRESSION --------
        print(f"\n{Fore.MAGENTA}🗜 Compression Level")
        print(f"{Fore.CYAN}[1] {Fore.GREEN}Low")
        print(f"{Fore.CYAN}[2] {Fore.YELLOW}Mid")
        print(f"{Fore.CYAN}[3] {Fore.RED}High")

        lvl = input(f"{Fore.GREEN}Select ➜ {Fore.CYAN}")
        garbage = 4 if lvl == '3' else (3 if lvl == '2' else 2)

        base = os.path.splitext(os.path.basename(path))[0]
        out_path = unique_path(os.path.join(os.path.dirname(path), f"{base}_compressed.pdf"))

        try:
            start = os.path.getsize(path) / (1024 * 1024)

            doc.set_metadata({
                "title": title,
                "author": author,
                "keywords": keywords,
                "creator": "Sudhir Singh - PDF Architect Pro",
                "producer": "SudhirDevOps1"
            })

            total = doc.page_count
            for i, page in enumerate(doc, start=1):
                page.clean_contents()
                progress_bar(i, total)
            print()

            args = dict(garbage=garbage, deflate=True, clean=False)

            if protect and out_pwd:
                args.update({
                    "encryption": fitz.PDF_ENCRYPT_AES_256,
                    "owner_pw": out_pwd,
                    "user_pw": out_pwd,
                    "permissions": fitz.PDF_PERM_PRINT
                })

            doc.save(out_path, **args)
            doc.close()

            end = os.path.getsize(out_path) / (1024 * 1024)
            diff = start - end
            saved = 0.0 if diff <= 0 else (diff / start) * 100

            print(f"\n{Fore.GREEN}✅ SUCCESSFUL!")
            print(f"{Fore.CYAN}📍 Path ➜ {Fore.YELLOW}{out_path}")
            print(f"{Fore.RED}Before ➜ {start:.2f} MB")
            print(f"{Fore.GREEN}After  ➜ {end:.2f} MB")
            print(f"{Fore.YELLOW}Saved  ➜ {saved:.1f}%")

            log_run(
                f"[{datetime.now()}]\n"
                f"Input  : {path}\n"
                f"Output : {out_path}\n"
                f"Pages  : {total}\n"
                f"Saved  : {saved:.1f}%\n"
                f"{'-'*40}\n"
            )

            open_folder(out_path)

        except Exception as e:
            print(f"{Fore.RED}❌ Error ➜ {e}")

        if input(f"\n{Fore.YELLOW}Do another one? (y/n) ➜ {Fore.CYAN}").lower() != 'y':
            break

if __name__ == "__main__":
    main()
