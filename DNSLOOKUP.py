import colorama
import  dns.resolver 
import pyfiglet

github = 'https://github.com/ark4ng3l/DNSLOOKUP'
banner = pyfiglet.figlet_format("Ark Ang3l NSLooKup", font="digital")
print((colorama.Fore.RED + banner + colorama.Fore.RESET))
print((colorama.Fore.CYAN + github + colorama.Fore.RESET))
target_url = input(colorama.Fore.GREEN + 'please input your target url: ' +colorama.Fore.RESET)

record_types = ["A", "AAAA", "CNAME", "MX", "NS", "SOA", "TXT", "PTR"]
resolver = dns.resolver.Resolver()


for record_type in record_types:
    # Perform DNS lookup for the specified domain and record type
    try:
        answers = resolver.resolve(target_url, record_type)
    except dns.resolver.NoAnswer:
        continue
    # Print the answers
    print(f"{colorama.Fore.CYAN+record_type} {colorama.Fore.GREEN}records for {colorama.Fore.RED+target_url}:"+colorama.Fore.RESET)
    for rdata in answers:
        print(colorama.Fore.YELLOW+f" {rdata}"+colorama.Fore.RESET)
