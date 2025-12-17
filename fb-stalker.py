import time
import random
import os
import sys
from datetime import datetime

# ANSI Color codes
class Colors:
    RESET = '\033[0m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    
    # Colors
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    GRAY = '\033[90m'
    
    # Bright colors
    BRED = '\033[91m'
    BGREEN = '\033[92m'
    BYELLOW = '\033[93m'
    BBLUE = '\033[94m'
    BMAGENTA = '\033[95m'
    BCYAN = '\033[96m'

# Custom names list
CUSTOM_NAMES = [
    "Serena鉱.",
    "Yumie Ijin",
    "Acyxi Zyi",
    "Kyomiu Sato",
    "Zyie Vizano",
    "Shia",
    "lı Nokiah",
    "Sume Ayase",
    "Apii Moch",
    "Stayc Lee",
    "Sienna Solará",
    "cazie夜.",
    "Yzhrie イ",
    "Nerrie Anne S. Vasquez",
    "Shia",
    "Kaizen夏.",
    "雨愛する",
    "Zeysha",
    "Kiro lı",
    "Sereiaか.",
    "Satoshi聡",
    "Ren Asamiya",
    "Macaroni Lata",
    "Florea",
    "Ina",
    "Azhra Luvrscwt",
    "Ira II",
    "Nami お",
    "Naiza Moncada",
    "Artemitsui",
    "Fritz Daniel Manggay"
]

def clear_screen():
    """Clear terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def slow_print(text, delay=0.03, color=''):
    """Print text with typing effect"""
    for char in text:
        print(f"{color}{char}{Colors.RESET}", end='', flush=True)
        time.sleep(delay)
    print()

def progress_bar(duration, text, color=Colors.CYAN):
    """Display a progress bar"""
    bar_length = 30
    for i in range(bar_length + 1):
        percent = int((i / bar_length) * 100)
        filled = '#' * i
        empty = ' ' * (bar_length - i)
        print(f'\r{color}[{filled}{empty}] {percent}%{Colors.RESET}', end='', flush=True)
        time.sleep(duration / bar_length)
    print()

def generate_random_name():
    """Generate random name from custom list"""
    return random.choice(CUSTOM_NAMES)

def generate_session_id():
    """Generate fake session ID"""
    return f"{random.randint(1000, 9999)}-{random.randint(100000, 999999)}-{random.randint(10, 99)}"

def generate_fb_id():
    """Generate fake Facebook ID"""
    return f"100{random.randint(10000000000, 99999999999)}"

def print_banner():
    """Print tool banner"""
    banner = f"""
{Colors.BRED}{Colors.BOLD}
           STALKER DETECTOR
{Colors.RESET}{Colors.BCYAN}
            Mysteriousq
{Colors.RESET}
"""
    print(banner)

def login_screen():
    """Display login screen"""
    clear_screen()
    print_banner()
    
    print(f"{Colors.BCYAN}═══════════════════════════════════════════════════════════════{Colors.RESET}")
    print(f"{Colors.BGREEN}              FACEBOOK ACCOUNT AUTHENTICATION{Colors.RESET}")
    print(f"{Colors.BCYAN}═══════════════════════════════════════════════════════════════{Colors.RESET}\n")
    
    # Email/Mobile input
    print(f"{Colors.BYELLOW}[?]{Colors.RESET} Mobile number or email:")
    email = input(f"{Colors.WHITE}>>> {Colors.RESET}").strip()
    
    if not email:
        print(f"\n{Colors.BRED}[!] Error: Email/Mobile required{Colors.RESET}\n")
        return None, None
    
    # Password input
    print(f"{Colors.BYELLOW}[?]{Colors.RESET} Password:")
    password = input(f"{Colors.WHITE}>>> {Colors.RESET}").strip()
    
    if not password:
        print(f"\n{Colors.BRED}[!] Error: Password required{Colors.RESET}\n")
        return None, None
    
    return email, password

def authenticate(email, password):
    """Simulate authentication process"""
    print()
    print(f"{Colors.BCYAN}[*] Authenticating with Facebook servers...{Colors.RESET}")
    time.sleep(1)
    
    auth_steps = [
        "Validating credentials",
        "Establishing secure connection",
        "Verifying account status",
        "Loading profile data",
        "Authorization complete"
    ]
    
    for step in auth_steps:
        print(f"{Colors.GRAY}[*] {step}...{Colors.RESET}")
        time.sleep(random.uniform(0.5, 1.0))
    
    # Fixed user data
    user_name = "Siegfried Samá 🥐🥐🥐"
    user_id = generate_fb_id()
    
    print(f"\n{Colors.BGREEN}[✓] Login successful!{Colors.RESET}\n")
    time.sleep(1)
    
    return user_name, user_id

def display_logged_user(name, user_id):
    """Display logged in user info"""
    print(f"{Colors.BCYAN}Login: {Colors.RESET}{Colors.BGREEN}{name}{Colors.RESET}")
    print(f"{Colors.BCYAN}ID: {Colors.RESET}{Colors.GRAY}{user_id}{Colors.RESET}\n")

def print_system_info():
    """Print system information"""
    session_id = generate_session_id()
    print(f"{Colors.GRAY}[*] Session ID: {session_id}{Colors.RESET}")
    print(f"{Colors.GRAY}[*] Encryption: AES-256-GCM{Colors.RESET}")
    print(f"{Colors.GRAY}[*] API Version: v4.2.1{Colors.RESET}\n")

def loading_phase():
    """Display loading sequence"""
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"{Colors.GRAY}Scan initiated at {now}{Colors.RESET}\n")
    
    loading_steps = [
        ("Initializing core modules", Colors.CYAN),
        ("Establishing secure connection to META servers", Colors.BBLUE),
        ("Authenticating with Graph API v18.0", Colors.BLUE),
        ("Injecting trace packets into social graph", Colors.GREEN),
        ("Enumerating profile interaction vectors", Colors.YELLOW),
        ("Decrypting engagement metadata cache", Colors.MAGENTA),
        ("Analyzing behavioral pattern signatures", Colors.CYAN),
        ("Cross-referencing with temporal databases", Colors.BGREEN),
        ("Compiling stalker fingerprint matrix", Colors.BYELLOW),
        ("Finalizing threat assessment report", Colors.BMAGENTA),
    ]
    
    for step, color in loading_steps:
        print(f"{color}{step}:{Colors.RESET} ", end='')
        progress_bar(random.uniform(0.8, 1.5), step, color)
        time.sleep(random.uniform(0.1, 0.3))
    
    print(f"\n{Colors.BGREEN}{Colors.BOLD}[✓] Scan complete - Profile analysis successful{Colors.RESET}\n")
    time.sleep(0.5)

def generate_stalkers():
    """Generate list of fake stalkers"""
    num_stalkers = random.randint(25, 40)
    stalkers = []
    
    for i in range(num_stalkers):
        name = generate_random_name()
        
        # Determine view count based on position
        if i < 3:
            views = random.randint(5, 7)
        elif i < 8:
            views = random.randint(3, 5)
        elif i < 15:
            views = random.randint(2, 3)
        else:
            views = 1
        
        # Random status: Friend, Non Follower, or Unknown
        rand = random.random()
        if rand < 0.4:
            status = "Friend"
        elif rand < 0.7:
            status = "Non Follower"
        else:
            status = "Unknown"
        
        # Generate last seen
        hours = random.randint(1, 72)
        if hours < 24:
            last_seen = f"{hours}h ago"
        else:
            days = hours // 24
            last_seen = f"{days}d ago"
        
        stalkers.append({
            'name': name,
            'views': views,
            'status': status,
            'last_seen': last_seen
        })
    
    return stalkers

def display_statistics(stalkers):
    """Display overall statistics"""
    total_views = sum(s['views'] for s in stalkers)
    friends = sum(1 for s in stalkers if s['status'] == 'Friend')
    non_followers = sum(1 for s in stalkers if s['status'] == 'Non Follower')
    unknown = sum(1 for s in stalkers if s['status'] == 'Unknown')
    high_freq = sum(1 for s in stalkers if s['views'] >= 4)
    
    print(f"{Colors.BCYAN}{Colors.BOLD}═══════════════════════════════════════════════════════════════{Colors.RESET}")
    print(f"{Colors.BGREEN}                    THREAT ASSESSMENT SUMMARY{Colors.RESET}")
    print(f"{Colors.BCYAN}═══════════════════════════════════════════════════════════════{Colors.RESET}\n")
    
    print(f"{Colors.YELLOW}[•] Total Profile Visitors:{Colors.RESET} {Colors.BOLD}{len(stalkers)}{Colors.RESET}")
    print(f"{Colors.YELLOW}[•] Total View Count:{Colors.RESET} {Colors.BOLD}{total_views}{Colors.RESET}")
    print(f"{Colors.BGREEN}[•] Friends:{Colors.RESET} {friends}")
    print(f"{Colors.BRED}[•] Non-Followers:{Colors.RESET} {non_followers}")
    print(f"{Colors.GRAY}[•] Unknown Entities:{Colors.RESET} {unknown}")
    print(f"{Colors.BRED}[•] High-Frequency Stalkers (4+ views):{Colors.RESET} {Colors.BOLD}{high_freq}{Colors.RESET}\n")

def display_results(stalkers):
    """Display stalker results"""
    display_statistics(stalkers)
    
    print(f"{Colors.BCYAN}{Colors.BOLD}═══════════════════════════════════════════════════════════════{Colors.RESET}")
    print(f"{Colors.BMAGENTA}                    DETAILED VISITOR LOG{Colors.RESET}")
    print(f"{Colors.BCYAN}═══════════════════════════════════════════════════════════════{Colors.RESET}\n")
    
    print(f"{Colors.BCYAN}{'No.':<4} {'Name':<30} {'Status':<18} {'Views':<8} {'Last Seen'}{Colors.RESET}")
    print(f"{Colors.GRAY}{'-' * 75}{Colors.RESET}")
    
    for i, stalker in enumerate(stalkers, 1):
        name = stalker['name']
        views = stalker['views']
        status = stalker['status']
        last_seen = stalker['last_seen']
        
        # Color code based on views
        if views >= 5:
            view_color = Colors.BRED
            view_icon = "⚠"
        elif views >= 3:
            view_color = Colors.BYELLOW
            view_icon = "!"
        elif views >= 2:
            view_color = Colors.YELLOW
            view_icon = "•"
        else:
            view_color = Colors.GRAY
            view_icon = "·"
        
        # Status color
        if status == "Friend":
            status_color = Colors.BGREEN
            status_display = f"{status_color}(Friend){Colors.RESET}"
        elif status == "Non Follower":
            status_color = Colors.BRED
            status_display = f"{status_color}(Non Follower){Colors.RESET}"
        else:
            status_color = Colors.GRAY
            status_display = f"{status_color}(Unknown){Colors.RESET}"
        
        # Format output with proper alignment
        print(f"{Colors.WHITE}{i:<4d} {name:<30} {status_display:<28} "
              f"{view_color}{view_icon} {views}x{Colors.RESET}     "
              f"{Colors.GRAY}{last_seen}{Colors.RESET}")
        time.sleep(0.05)
    
    print(f"\n{Colors.BCYAN}═══════════════════════════════════════════════════════════════{Colors.RESET}\n")
    print(f"{Colors.GRAY}[i] Threat Level Key:{Colors.RESET}")
    print(f"    {Colors.BRED}⚠ 5+ views{Colors.RESET} - High risk stalker behavior")
    print(f"    {Colors.BYELLOW}! 3-4 views{Colors.RESET} - Elevated interest")
    print(f"    {Colors.YELLOW}• 2 views{Colors.RESET} - Moderate engagement")
    print(f"    {Colors.GRAY}· 1 view{Colors.RESET} - Normal activity\n")
    
    print(f"{Colors.GRAY}[i] Note: Data aggregated from Facebook Graph API trace logs{Colors.RESET}")
    print(f"{Colors.GRAY}[i] Timestamp range: Last 7 days | Confidence: 94.7%{Colors.RESET}\n")
    
    print(f"{Colors.BYELLOW}[?] Type 'scan' to run again or 'exit' to quit{Colors.RESET}")

def main():
    """Main function"""
    # Login screen
    email, password = login_screen()
    
    if not email or not password:
        return
    
    # Authenticate
    user_name, user_id = authenticate(email, password)
    
    # Clear and show main screen
    clear_screen()
    print_banner()
    
    # Display logged user
    display_logged_user(user_name, user_id)
    
    # System info
    print_system_info()
    
    # Loading phase
    loading_phase()
    
    # Generate and display results
    stalkers = generate_stalkers()
    display_results(stalkers)
    
    # Ask to scan again
    while True:
        choice = input(f"{Colors.BCYAN}>>> {Colors.RESET}").strip().lower()
        
        if choice == 'scan':
            clear_screen()
            print_banner()
            display_logged_user(user_name, user_id)
            print_system_info()
            loading_phase()
            stalkers = generate_stalkers()
            display_results(stalkers)
        elif choice == 'exit':
            print(f"\n{Colors.BGREEN}[✓] Session terminated. Data purged from cache.{Colors.RESET}")
            print(f"{Colors.GRAY}[*] Secure exit protocol completed{Colors.RESET}\n")
            break
        else:
            print(f"{Colors.BRED}[!] Invalid command. Use 'scan' or 'exit'{Colors.RESET}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{Colors.BYELLOW}[!] Emergency shutdown initiated{Colors.RESET}")
        print(f"{Colors.GRAY}[*] Cleaning traces... Done{Colors.RESET}\n")
        sys.exit(0)
    except Exception as e:
        print(f"\n{Colors.BRED}[!] Critical error: {str(e)}{Colors.RESET}\n")
        sys.exit(1)
