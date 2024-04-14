import requests

# Function to shorten a URL using a third-party service
def shorten_url(long_url):
    try:
        # Define the URL of the third-party URL shortening service (e.g., Bitly)
        service_url = "https://api-ssl.bitly.com/v4/shorten"

        # Set your Bitly API access token here
        api_token = "YOUR_BITLY_API_TOKEN"

        # Define headers with the API access token
        headers = {
            "Authorization": f"Bearer {api_token}",
            "Content-Type": "application/json"
        }

        # Define the payload with the long URL
        payload = {
            "long_url": long_url
        }

        # Send a POST request to the Bitly API to shorten the URL
        response = requests.post(service_url, headers=headers, json=payload)

        # Check if the request was successful
        if response.status_code == 200:
            short_url = response.json()["link"]
            return short_url
        else:
            print("URL shortening failed. Please check your input or API configuration.")
            return None

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None

if __name__ == "__main__":
    print("Welcome to URLShortener - Your Fast Link Shortening Tool!")

    while True:
        print("\nMenu:")
        print("1. Shorten URL")
        print("2. Quit")

        choice = input("Enter your choice (1/2): ").strip()

        if choice == '1':
            long_url = input("Enter the long URL to shorten: ").strip()
            short_url = shorten_url(long_url)
            if short_url:
                print(f"Shortened URL: {short_url}")
        elif choice == '2':
            break
        else:
            print("Invalid choice. Please select a valid option.")
