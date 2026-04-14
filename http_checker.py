import requests
import time

# Function: Classify HTTP status code into categories
# Returns:
#   Success (2xx), Redirection (3xx), Client Error (4xx), Server Error (5xx)
def get_status_category(status_code):
    if 200 <= status_code < 300:
        return "Success"
    elif 300 <= status_code < 400:
        return "Redirection"
    elif 400 <= status_code < 500:
        return "Client Error"
    elif 500 <= status_code < 600:
        return "Server Error"
    else:
        return "Unknown"

# Infinite loop to allow continuous checks
while True:
    # Get user input
    url = input("Enter URL (or type 'exit' to quit): ")

    # Exit condition
    if url.lower() == "exit":
        break

    # Add https:// if missing (input cleaning)
    if not url.startswith("http://") and not url.startswith("https://"):
        url = "https://" + url

    try:
        # Start timer (measure response time)
        start = time.time()

        # Send HTTP request
        response = requests.get(url)

        # End timer
        end = time.time()

        # Calculate response time
        response_time = end - start

        # Get status category (Success, Client Error, etc.)
        category = get_status_category(response.status_code)

        print("\n" + "=" * 40)
        print("--- HTTP Check ---")
        print("URL:", url)
        print(f"Status: {response.status_code} {response.reason} ({category})")
        print(f"Response time: {response_time:.3f} seconds")

        # Print response headers (server info, content type, etc.)
        print("\nHeaders:")
        for key, value in response.headers.items():
            print(f"  {key}: {value}")

        print("\n" + "-" * 40 + "\n")

    # Handle connection errors (invalid domain, no DNS, etc.)
    except requests.exceptions.ConnectionError:
        print("\n--- HTTP Check ---")
        print("URL:", url)
        print("Status: ERROR")
        print("Reason: Could not connect (invalid domain or network issue)\n")

    # Handle invalid URL format
    except requests.exceptions.MissingSchema:
        print("\n--- HTTP Check ---")
        print("URL:", url)
        print("Status: ERROR")
        print("Reason: Invalid URL format\n")

    # Catch any other request-related errors
    except requests.exceptions.RequestException as e:
        print("\n--- HTTP Check ---")
        print("URL:", url)
        print("Status: ERROR")
        print("Reason:", e, "\n")