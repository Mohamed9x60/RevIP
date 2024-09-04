# Reverse IP Lookup Tool (RevIP)

**Programmed by: Mohamed Fouad**

## Introduction

RevIP is a Python-based tool that allows users to perform reverse IP lookups. By entering a domain name, the tool retrieves the associated IP address and displays all other websites hosted on the same server. Results can be saved in various formats, including TXT, CSV, XML, and HTML.

## Features

- **Reverse IP Lookup**: Retrieves a list of websites hosted on the same server as the entered domain.
- **Multiple Save Options**: Save results in TXT, CSV, XML, or HTML formats.
- **User-Friendly Interface**: A colorful command-line interface for easy navigation.
- **Error Handling**: Manages errors such as invalid domains or API limits with clear messages.

## Requirements

The tool requires the following Python libraries:

- `requests`
- `termcolor`
- `pyfiglet`
- `colorama`

You can install the required libraries using:

```
pip install -r requirements.txt
```

## Usage

### 1. Clone the repository:

```
git clone https://github.com/Mohamed9x60/RevIP.git
```

### 2. Navigate to the project directory:

```
cd RevIP
```

### 3. Install the required libraries:

```
pip install -r requirements.txt
```

### 4. Run the tool:

```
python3 RevIP.py
```

### 5. Enter the domain names you want to check (comma-separated) and follow the on-screen instructions to save the results in your preferred format.

## Example Usage

```
Enter the domains (comma-separated): example.com, anotherdomain.com

Processing domain: example.com
IP address for the domain: 93.184.216.34
Websites hosted on the same server:
- example.com
- anotherexample.com

Select the file formats to save the results:
1. TXT
2. CSV
3. XML
4. HTML
5. Exit without saving
```

## Tool Features

- **Versatile Options**: RevIP provides you with the ability to choose and save results in multiple formats to suit your needs.
- **Speed and Efficiency**: Results are obtained quickly and organized, saving you time in gathering information.
- **Interactive Design**: The tool offers an interactive and easy-to-use experience through a command-line interface.
- **Integration with Web Services**: RevIP relies on trusted web services to retrieve data, with the flexibility to handle service limitations gracefully.
