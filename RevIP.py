import socket
import requests
import csv
import xml.etree.ElementTree as ET
from termcolor import colored
from pyfiglet import Figlet
import time
from colorama import init, Fore

# Initialize colorama
init()

# Constants
WAIT_TIME = 3600  # Example wait time in seconds (1 hour)
MAX_ATTEMPTS = 5

# Function to get the IP address from a domain name
def get_ip_from_domain(domain):
    try:
        ip = socket.gethostbyname(domain)
        return ip
    except socket.gaierror:
        return None

# Function to perform a reverse IP lookup using an external API
def reverse_ip_lookup(ip):
    url = f"https://api.hackertarget.com/reverseiplookup/?q={ip}"
    attempt = 0
    while attempt < MAX_ATTEMPTS:
        try:
            response = requests.get(url)
            response.raise_for_status()
            if "API count exceeded" in response.text:
                print(Fore.RED + "API count exceeded. Please wait and try again later." + Fore.RESET)
                wait_time = WAIT_TIME
                while wait_time > 0:
                    minutes, seconds = divmod(wait_time, 60)
                    print(Fore.YELLOW + f"Retrying in {minutes}m {seconds}s..." + Fore.RESET, end='\r')
                    time.sleep(1)
                    wait_time -= 1
                print()
                attempt += 1
            else:
                sites = response.text.strip().split('\n')
                return [site.strip() for site in sites if site.strip()]
        except requests.RequestException as e:
            print(Fore.RED + f"Error performing RevIP : {e}" + Fore.RESET)
            return []
    print(Fore.RED + "Maximum attempts reached. Please try again later." + Fore.RESET)
    return []

# Function to save the list of websites to a TXT file
def save_to_txt(sites, domain):
    filename = f"sites_list_{domain.replace('.', '_')}.txt"
    with open(filename, 'w') as file:
        file.write(f"{Figlet(font='big').renderText('Mohamed Fouad')}\n")
        file.write("Welcome to the Reverse IP Lookup (RevIP) Tool!\n")
        file.write(f"Processing domain: {domain}\n")
        file.write(f"IP address for the domain: {get_ip_from_domain(domain)}\n")
        file.write("Websites hosted on the same server:\n")
        for site in sites:
            file.write(f"{site}\n")
    print(Fore.GREEN + f"Results have been saved to '{filename}'" + Fore.RESET)

# Function to save the list of websites to a CSV file
def save_to_csv(sites, domain):
    filename = f"sites_list_{domain.replace('.', '_')}.csv"
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([Figlet(font='big').renderText('Mohamed Fouad')])
        writer.writerow(["Welcome to the Reverse IP Lookup (RevIP) Tool!"])
        writer.writerow([f"Processing domain: {domain}"])
        writer.writerow([f"IP address for the domain: {get_ip_from_domain(domain)}"])
        writer.writerow(["Websites hosted on the same server:"])
        for site in sites:
            writer.writerow([site])
    print(Fore.GREEN + f"Results have been saved to '{filename}'" + Fore.RESET)

# Function to save the list of websites to an XML file
def save_to_xml(sites, domain):
    filename = f"sites_list_{domain.replace('.', '_')}.xml"
    root = ET.Element("ReverseIPLookup")
    header = ET.SubElement(root, "Header")
    ET.SubElement(header, "Programmer").text = "Mohamed Fouad"
    ET.SubElement(header, "WelcomeMessage").text = "Welcome to the Reverse IP Lookup (RevIP) Tool!"
    ET.SubElement(header, "ProcessingDomain").text = f"Processing domain: {domain}"
    ET.SubElement(header, "IPAddress").text = f"IP address for the domain: {get_ip_from_domain(domain)}"
    sites_element = ET.SubElement(root, "Sites")
    for site in sites:
        ET.SubElement(sites_element, "Site").text = site
    tree = ET.ElementTree(root)
    tree.write(filename, encoding='utf-8', xml_declaration=True)
    print(Fore.GREEN + f"Results have been saved to '{filename}'" + Fore.RESET)

# Function to save the list of websites to an HTML file
def save_to_html(sites, domain):
    filename = f"sites_list_{domain.replace('.', '_')}.html"
    with open(filename, 'w') as file:
        file.write(f"<!DOCTYPE html>\n<html>\n<head>\n<title>Reverse IP Lookup(RevIP)!</title>\n<style>body {{ font-family: Arial, sans-serif; }}</style>\n</head>\n<body>\n")
        file.write(f"<h1 style='font-family: monospace;'>{Figlet(font='big').renderText('Mohamed Fouad')}</h1>\n")
        file.write(f"<h2>Welcome to the Reverse IP Lookup Tool!</h2>\n")
        file.write(f"<p>Processing domain: {domain}</p>\n")
        file.write(f"<p>IP address for the domain: {get_ip_from_domain(domain)}</p>\n")
        file.write("<h3>Websites hosted on the same server:</h3>\n<ul>\n")
        for site in sites:
            file.write(f"<li>{site}</li>\n")
        file.write("</ul>\n</body>\n</html>")
    print(Fore.GREEN + f"Results have been saved to '{filename}'" + Fore.RESET)

# Function to generate a colorful welcome message
def welcome_message():
    f = Figlet(font='slant')
    welcome_text = f.renderText("      RevIP   ")
    print(Fore.CYAN + welcome_text + Fore.RESET)
    print(Fore.RED + "    Free Palestine   " + Fore.RESET)
    print(Fore.CYAN + "Programmer by: Mohamed Fouad" + Fore.RESET)
    print(Fore.BLUE + "Welcome to the Reverse IP Lookup Tool!(RevIP)" + Fore.RESET)
    print(Fore.LIGHTGREEN_EX + "Enter the domains you want to search, and we will retrieve the websites hosted on the same server." + Fore.RESET)
    print()

# Function to handle file saving
def handle_file_saving(sites, domain):
    file_options = {
        '1': ('txt', save_to_txt),
        '2': ('csv', save_to_csv),
        '3': ('xml', save_to_xml),
        '4': ('html', save_to_html)
    }

    print(Fore.BLUE + "Select the file formats to save the results:" + Fore.RESET)
    print(Fore.CYAN + "1. TXT" + Fore.RESET)
    print(Fore.CYAN + "2. CSV" + Fore.RESET)
    print(Fore.CYAN + "3. XML" + Fore.RESET)
    print(Fore.CYAN + "4. HTML" + Fore.RESET)
    print(Fore.RED + "5. Exit without saving" + Fore.RESET)

    selections = input(Fore.BLUE + "Enter the numbers (comma-separated) for the file formats you want (maximum 3 formats): " + Fore.RESET).split(',')
    selections = [selection.strip() for selection in selections if selection.strip()]

    if '5' in selections:
        print(Fore.RED + "Exiting without saving results." + Fore.RESET)
        return

    if len(selections) > 3:
        print(Fore.RED + "You can only select up to 3 formats. Please try again." + Fore.RESET)
        return

    for selection in selections:
        if selection in file_options:
            file_type, save_function = file_options[selection]
            save_function(sites, domain)
        else:
            print(Fore.RED + f"Invalid selection: {selection}" + Fore.RESET)

# Main function that ties everything together
def main():
    welcome_message()

    domains = input(Fore.BLUE + "Enter the domains (comma-separated): " + Fore.RESET).split(',')
    domains = [domain.strip() for domain in domains if domain.strip()]  # Filter out empty domains

    if not domains:
        print(Fore.RED + "No valid domains provided." + Fore.RESET)
        return

    for domain in domains:
        print(Fore.CYAN + f"\nProcessing domain: {domain}" + Fore.RESET)
        ip = get_ip_from_domain(domain)

        if ip:
            print(Fore.CYAN + f"IP address for the domain: {ip}" + Fore.RESET)
            sites = reverse_ip_lookup(ip)

            if sites:
                print(Fore.GREEN + "Websites hosted on the same server:" + Fore.RESET)
                for site in sites:
                    print(Fore.YELLOW + site + Fore.RESET)

                handle_file_saving(sites, domain)
            else:
                print(Fore.RED + "No shared websites found or information could not be retrieved." + Fore.RESET)
        else:
            print(Fore.RED + "Failed to find the IP for the provided domain." + Fore.RESET)

if __name__ == "__main__":
    main()
