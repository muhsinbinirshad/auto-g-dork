import requests
import urllib.parse

# ANSI escape sequences for color formatting
GREEN = "\033[32m"
RESET = "\033[0m"

# Function to perform the Google search and print results
def search_dorks(domain, dork_list):
    for dork in dork_list:
        query = f"site:{domain} {dork}"
        encoded_query = urllib.parse.quote(query)
        url = f"https://www.google.com/search?q={encoded_query}"

        # Send the request to Google and get the response
        response = requests.get(url)
        html_content = response.text

        # Check if the response contains search results or just "0 results"
        if "About 0 results" not in html_content:
            result_count = html_content.count('class="g"')
            # Print the dork line in green color
            print(GREEN + query + " result = " + str(result_count) + RESET)

# Main code
if __name__ == "__main__":
    # Ask the user for the path of the dork list
    dork_list_path = input("Enter the path of the dork list file: ")

    # Read the dork list from the file
    with open(dork_list_path, "r") as file:
        dorks = [line.strip() for line in file.readlines()]

    # Ask the user for the domain and dork type
    domain = input("Enter the domain: ")
    dork_type = input("Enter the dork type (1: Single domain, 2: Wildcard domain): ")

    if dork_type == "1":
        domain_dorks = [f"site:{domain} {dork.split(' ', 1)[-1]}" for dork in dorks]

        search_dorks(domain, domain_dorks)
    elif dork_type == "2":
        wildcard_domain_dorks = [f"site:.*{domain} {dork.split(' ', 1)[-1]}" for dork in dorks]
        search_dorks(f".*{domain}", wildcard_domain_dorks)
    else:
        print("Invalid dork type. Exiting...")
        exit(1)
