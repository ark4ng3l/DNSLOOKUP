import colorama
import dns.resolver
import pyfiglet
from prettytable import PrettyTable

# Display Banner
github = 'https://github.com/ark4ng3l/DNSLOOKUP'
banner = pyfiglet.figlet_format("Ark Ang3l NSLooKup", font="digital")
print((colorama.Fore.RED + banner + colorama.Fore.RESET))
print((colorama.Fore.CYAN + github + colorama.Fore.RESET))

# Get target URL from user
target_url = input(colorama.Fore.GREEN + 'please input your target url: ' + colorama.Fore.RESET)

# Ensure proper URL format (strip protocol if exists, and remove 'www.')
if target_url.startswith(('http://', 'https://', 'www.')):
    target_url = target_url.replace('http://', '').replace('https://', '').replace('www.', '', 1)

# Define record types to query
record_types = ["A", "AAAA", "CNAME", "MX", "NS", "SOA", "TXT", "PTR"]

# Initialize DNS resolver
resolver = dns.resolver.Resolver()

# Create a PrettyTable object for DNS records (overall table)
table = PrettyTable()
table.field_names = [f"{colorama.Fore.CYAN}Record Type{colorama.Fore.RESET}", f"{colorama.Fore.YELLOW}Record Data{colorama.Fore.RESET}"]

# Perform DNS lookup for each record type
for record_type in record_types:
    # Add a section header for each record type
    table.add_row([f"{colorama.Fore.GREEN + record_type + colorama.Fore.RESET} Records", ""])
    table.add_row(["-" * 30, "-" * 30])  # Add separator row

    try:
        answers = resolver.resolve(target_url, record_type)

        # Add answers to the table
        for rdata in answers:
            table.add_row([f"{colorama.Fore.CYAN + record_type + colorama.Fore.RESET}", f"{colorama.Fore.YELLOW + str(rdata) + colorama.Fore.RESET}"])

    except dns.resolver.NoAnswer:
        # If no records found, display 'No records found'
        table.add_row([f"{colorama.Fore.CYAN + record_type + colorama.Fore.RESET}", f"{colorama.Fore.RED}No records found{colorama.Fore.RESET}"])

    except dns.resolver.NXDOMAIN:
        print(colorama.Fore.RED + f"Domain {target_url} does not exist" + colorama.Fore.RESET)
        break

    except dns.resolver.Timeout:
        print(colorama.Fore.RED + f"Timeout occurred while querying {record_type} records for {target_url}" + colorama.Fore.RESET)

    except dns.resolver.NoNameservers:
        print(colorama.Fore.RED + f"No name servers found for {target_url}" + colorama.Fore.RESET)

    except Exception as e:
        print(colorama.Fore.RED + f"An error occurred: {str(e)}" + colorama.Fore.RESET)

    # Add an empty row after each record type section for spacing
    table.add_row(["", ""])

# Print the overall table
print(table)
