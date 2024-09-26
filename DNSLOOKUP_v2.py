import dns.resolver
import pyfiglet
from prettytable import PrettyTable
import time
import re  # برای کار با الگوهای منظم
import colorama  # برای رنگ‌آمیزی متن
from colorama import Fore

# Initialize colorama
colorama.init()

# Display Banner
github = 'https://github.com/ark4ng3l/DNSLOOKUP'
banner = pyfiglet.figlet_format("Ark Ang3l NSLooKup", font="digital")
print(Fore.RED + banner + Fore.RESET)
print(Fore.CYAN + github + Fore.RESET)

# Get target URL from user
target_url = input(Fore.GREEN + 'Please input your target URL: ' + Fore.RESET)

# Ensure proper URL format (strip protocol if exists, and remove 'www.')
if target_url.startswith(('http://', 'https://', 'www.')):
    target_url = target_url.replace('http://', '').replace('https://', '').replace('www.', '', 1)

# Get DNS server from user
dns_server = input(Fore.GREEN + 'Please input your DNS server (leave blank for default): ' + Fore.RESET)

# Set the DNS server if provided
if dns_server:
    resolver = dns.resolver.Resolver(configure=False)
    resolver.nameservers = [dns_server]
else:
    resolver = dns.resolver.Resolver()

# Define record types to query and their descriptions
record_info = {
    "A": "IPv4 address record",
    "AAAA": "IPv6 address record",
    "CNAME": "Canonical name record (alias)",
    "MX": "Mail exchange record",
    "NS": "Name server record",
    "SOA": "Start of authority record",
    "TXT": "Text record",
    "PTR": "Pointer record",
    "CAA": "Certification authority authorization",
    "SRV": "Service locator",
    "NAPTR": "Naming Authority Pointer",
    "DS": "Delegation signer",
    "DNSKEY": "DNS key record",
    "SPF": "Sender Policy Framework"
}

# Create a PrettyTable object for DNS records (overall table)
table = PrettyTable()
table.field_names = ["Type", "Data", "Time (ms)"]

# Store output for file writing
output_lines = []

# Print the DNS server information
dns_info = f"Using DNS server: {dns_server if dns_server else 'Default DNS server'}"
print(Fore.YELLOW + dns_info + Fore.RESET)
output_lines.append(dns_info)  # Save without color for output file
output_lines.append("")  # Empty line for separation

# Perform DNS lookup for each record type
for record_type in record_info.keys():
    # Add description in Data column
    table.add_row([Fore.CYAN + record_type + Fore.RESET, Fore.YELLOW + record_info[record_type] + Fore.RESET, ""])

    # Add a separator line for description
    table.add_row(["-" * 8, "-" * 75, "-" * 11])  # Row of dashes for separation after description

    start_time = time.time()  # Start timing the request
    try:
        answers = resolver.resolve(target_url, record_type)
        response_time = (time.time() - start_time) * 1000  # Convert to milliseconds

        # Add answers to the table
        for rdata in answers:
            table.add_row([Fore.CYAN + record_type + Fore.RESET, Fore.GREEN + str(rdata) + Fore.RESET, f"{response_time:.2f}"])
        
    except dns.resolver.NoAnswer:
        # If no records found, display 'No records found'
        table.add_row([Fore.CYAN + record_type + Fore.RESET, Fore.RED + "No records found" + Fore.RESET, ""])
    except dns.resolver.NXDOMAIN:
        print(Fore.RED + f"Domain {target_url} does not exist" + Fore.RESET)
        break
    except dns.resolver.Timeout:
        print(Fore.YELLOW + f"Timeout occurred while querying {record_type} records for {target_url}" + Fore.RESET)
    except dns.resolver.NoNameservers:
        print(Fore.YELLOW + f"No name servers found for {target_url}" + Fore.RESET)
    except Exception as e:
        print(Fore.RED + f"An error occurred: {str(e)}" + Fore.RESET)

    # Add a separator line after the records for the current DNS type
    table.add_row(["-" * 8, "-" * 75, "-" * 11])  # Row of dashes for separation after the data

# Prepare output lines for the text file
output_lines.append("+" + "-" * 8 + "+" + "-" * 75 + "+" + "-" * 11 + "+")
output_lines.append("|  Type  |                                   Data                                    | Time (ms) |")
output_lines.append("+" + "-" * 8 + "+" + "-" * 75 + "+" + "-" * 11 + "+")

# Add table rows to output_lines without colors
for row in table._rows:  # Access rows using _rows
    output_lines.append("|  " + str(row[0]).ljust(6) + "  |  " + str(row[1]).ljust(75) + "  |  " + str(row[2]).rjust(10) + "  |")

output_lines.append("+" + "-" * 8 + "+" + "-" * 75 + "+" + "-" * 11 + "+")

# Create a valid filename from the target URL (removing invalid characters)
valid_filename = re.sub(r'[^a-zA-Z0-9_.-]', '_', target_url) + '_dns_lookup.txt'

# Print the overall table with color-coded text
print(str(table))
