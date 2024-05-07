import requests

def download_file(url, filename):
    response = requests.get(url)
# This sends a GET request to the URL

# Check if the request was successful (status code 200)
if response.status.code == 200:
    with open(filename, 'wb') as f:
        f.write(response.content)
    print(f"File '{filename}' downloaded successfully.")
else: 
    print(f"Failed to download the file form the {url}. Status Code: {response.status_code}")

def main();
# URL of the Dell Command Update .exe file
url = "https://www.dell.com/support/home/en-us/drivers/driversdetails?driverid=8dgg4"

#filename to save the downloaded file
filename = "Dell-Command-Update-Application_8DGG4_WIN_4.4.0_A00.EXE"

#Download file
download_file(url, filename)

if __name__ == "__main__ ": 
    main()


 





