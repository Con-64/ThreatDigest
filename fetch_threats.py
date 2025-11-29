import requests
from datetime import datetime

def fetch_vulnerabilities():
    """Fetch vulnerabilities from CISA KEV catalog"""
    print("Fetching vulnerabilities from CISA KEV catalog...")
    
    url = "https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return data['vulnerabilities']
    else:
        print(f"Error: Could not fetch data (Status code: {response.status_code})")
        return None

def format_digest(vulnerabilities, count=5):
    """Format vulnerabilities into a markdown string"""
    # Create the header with today's date
    today = datetime.now().strftime("%Y-%m-%d")
    
    output = f"# Threat Intelligence Digest - {today}\n\n"
    output += f"**Total vulnerabilities in CISA KEV catalog:** {len(vulnerabilities)}\n\n"
    output += "---\n\n"
    output += "## Top Recent Vulnerabilities\n\n"
    
    # Format each vulnerability
    for i, vuln in enumerate(vulnerabilities[:count], 1):
        output += f"### {i}. {vuln['cveID']}\n\n"
        output += f"**Vulnerability:** {vuln['vulnerabilityName']}\n\n"
        output += f"**Vendor:** {vuln['vendorProject']}\n\n"
        output += f"**Product:** {vuln['product']}\n\n"
        output += f"**Date Added:** {vuln['dateAdded']}\n\n"
        output += f"**Description:** {vuln['shortDescription']}\n\n"
        
        if 'requiredAction' in vuln:
            output += f"**Required Action:** {vuln['requiredAction']}\n\n"
        
        output += "---\n\n"
    
    return output

def save_digest(content, filename):
    """Save the digest to a file"""
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✓ Digest saved to: {filename}")
        return True
    except Exception as e:
        print(f"✗ Error saving file: {e}")
        return False

# Main execution
if __name__ == "__main__":
    # Fetch the data
    vulnerabilities = fetch_vulnerabilities()
    
    if vulnerabilities:
        # Format it as markdown
        digest_content = format_digest(vulnerabilities)
        
        # Generate filename with today's date
        today = datetime.now().strftime("%Y-%m-%d")
        filename = f"digest_{today}.md"
        
        # Save to file
        save_digest(digest_content, filename)
        
        # Also print summary to terminal
        print(f"\nProcessed {len(vulnerabilities)} total vulnerabilities")
        print(f"Formatted top 5 into digest")