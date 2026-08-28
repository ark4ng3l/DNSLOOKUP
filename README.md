<div align="center">

# 🔍 Ark Ang3l DNSLOOKUP
### Advanced DNS Intelligence, Record Enumeration & Reconnaissance Suite

[![Python 3.8+](https://img.shields.io/badge/Python-3.8+-38bdf8?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![dnspython](https://img.shields.io/badge/DNS-dnspython-10b981?style=for-the-badge&logo=pypi&logoColor=white)](https://www.dnspython.org/)
[![License](https://img.shields.io/badge/License-MIT-f59e0b?style=for-the-badge)](LICENSE)

<br/>

[🌟 Features](#-key-features) •
[📊 Supported Records](#-supported-dns-records) •
[🚀 Installation](#-installation--usage) •
[📄 Output Sample](#-sample-output)

<br/>

```ascii
     _         _       _                   _____  _   _  _____ _                 _                 
    / \   _ __| | __  / \   _ __   __ _ 3 / / _ \| \ | |/ ____| |               | |                
   / _ \ | '__| |/ / / _ \ | '_ \ / _` | / / | | |  \| | (___ | |     ___   ___ | | ___   _ _ __   
  / ___ \| |  |   < / ___ \| | | | (_| |/ /| |_| | |\  |\___ \| |    / _ \ / _ \| |/ / | | | '_ \  
 /_/   \_\_|  |_|\_/_/   \_\_| |_|\__, /_/  \___/|_| \_|_____/|_____\___/ \___/|_|\_\__,_| .__/  
                                  |___/                                                  |_|      
                       CYBER RECONNAISSANCE TOOL // v2.0
```

</div>

---

## 🌟 Overview

**DNSLOOKUP** is a fast, terminal-based DNS enumeration and reconnaissance tool engineered for cybersecurity professionals, penetration testers, and network administrators.

It automatically queries **14 essential DNS record types**, calculates round-trip response latency in milliseconds, highlights results in formatted ANSI color tables, and automatically exports clean textual audit reports for documentation.

---

## ✨ Key Features

- ⚡ **14 DNS Record Types:** Comprehensive coverage from basic IPv4/IPv6 to security policies (SPF, CAA, DNSKEY, DS).
- ⏱ **Latency Profiling:** Measures DNS resolution query latency in milliseconds per record type.
- 🌐 **Custom Nameserver Selection:** Query specific DNS resolvers (e.g. `8.8.8.8`, `1.1.1.1`, or target private nameservers) to bypass caching or test split-horizon DNS.
- 🎨 **Rich ANSI Color Tables:** Color-coded status outputs powered by `PrettyTable` and `colorama`.
- 📁 **Automated Audit Export:** Automatically saves formatted lookup results to text files (`<target>_dns_lookup.txt`).

---

## 📊 Supported DNS Records

| Record Type | Description | Security & OSINT Significance |
| :--- | :--- | :--- |
| **`A`** | IPv4 Address Record | Maps hostname to IP host / Web server |
| **`AAAA`** | IPv6 Address Record | IPv6 infrastructure and modern routing |
| **`CNAME`** | Canonical Name Record | Uncovers third-party services, CDNs, & subdomains |
| **`MX`** | Mail Exchange Record | Email routing hosts (Google Workspace, Office365, etc.) |
| **`NS`** | Name Server Record | Authoritative DNS infrastructure providers |
| **`SOA`** | Start of Authority | Zone admin email, serial numbers, and refresh timers |
| **`TXT`** | Text Record | Verification tokens, Google/MS validation strings |
| **`SPF`** | Sender Policy Framework | Permitted email sending servers & IP ranges |
| **`CAA`** | Certification Authority Auth | Authorized SSL/TLS Certificate Authorities |
| **`SRV`** | Service Locator Record | Discovers SIP, LDAP, XMPP, or Active Directory ports |
| **`DNSKEY`**| DNSSEC Public Key Record | DNSSEC zone signing and cryptographic integrity |
| **`DS`** | Delegation Signer | DNSSEC chain of trust validation |
| **`PTR`** | Pointer Record | Reverse DNS lookups |
| **`NAPTR`** | Naming Authority Pointer | DDDS application mapping rules |

---

## 🚀 Installation & Usage

### 1. Clone & Install Dependencies
```bash
git clone https://github.com/ark4ng3l/DNSLOOKUP.git
cd DNSLOOKUP
pip install dnspython prettytable colorama pyfiglet
```

### 2. Run DNSLOOKUP
```bash
python DNSLOOKUP_v2.py
```

### 3. Interactive Prompts
1. **Target URL:** Enter target domain (e.g., `example.com` or `https://github.com`).
2. **DNS Server:** Press `Enter` for system default, or enter custom DNS server (e.g., `1.1.1.1`).

---

## 📄 Sample Output

```text
Using DNS server: 1.1.1.1
+----------+-----------------------------------------------------------------------------+------------+
|   Type   |                                    Data                                     | Time (ms)  |
+----------+-----------------------------------------------------------------------------+------------+
| A        | IPv4 address record                                                         |            |
| -------- | --------------------------------------------------------------------------- | ---------- |
| A        | 140.82.121.4                                                                | 21.45      |
| -------- | --------------------------------------------------------------------------- | ---------- |
| MX       | Mail exchange record                                                        |            |
| -------- | --------------------------------------------------------------------------- | ---------- |
| MX       | 10 aspmx.l.google.com.                                                      | 18.20      |
+----------+-----------------------------------------------------------------------------+------------+
```

---

## 📜 License

Distributed under the **MIT License**. See [LICENSE](LICENSE) for details.

<div align="center">
<b>Ark Ang3l DNSLOOKUP</b> • Developed by <a href="https://github.com/ark4ng3l">@ark4ng3l</a>
</div>
