import requests

def download_file(url, filename):
    response = requests.get(url)
    # This sends a GET request to the URL

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        with open(filename, 'wb') as f:
            f.write(response.content)
        print(f"File '{filename}' downloaded successfully.")
    else: 
        print(f"Failed to download the file from {url}. Status Code: {response.status_code}")

def main():
    # URL of the Dell Command Update .exe file
    url = "https://www.dell.com/support/home/en-us/drivers/driversdetails?driverid=6gmr6"

    # Filename to save the downloaded file
    filename = "Dell-Command-Update-Windows-Universal-Application_6GMR6_WIN_4.8.0_A00_01.EXE"

    # Download file
    download_file(url, filename)

if __name__ == "__main__":
    main()
