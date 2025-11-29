import requests
from datetime import datetime

# Fetch data from CISA's Known Exploited Vulnerabilities catalog
print("Fetching vulnerabilities from CISA KEV catalog...")

url = "https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json"
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    vulnerabilities = data['vulnerabilities']
    
    print(f"\nTotal vulnerabilities in catalog: {len(vulnerabilities)}")
    print("\n" + "="*80)
    print("TOP 5 MOST RECENT VULNERABILITIES")
    print("="*80 + "\n")
    
    # Show the first 5 vulnerabilities
    for i, vuln in enumerate(vulnerabilities[:5], 1):
        print(f"{i}. {vuln['cveID']} - {vuln['vulnerabilityName']}")
        print(f"   Vendor: {vuln['vendorProject']}")
        print(f"   Product: {vuln['product']}")
        print(f"   Date Added: {vuln['dateAdded']}")
        print(f"   Short Description: {vuln['shortDescription'][:100]}...")
        print()
else:
    print(f"Error: Could not fetch data (Status code: {response.status_code})")