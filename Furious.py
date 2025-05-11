import socket
import socks

def send_http_request(host_ip, host_port, request):
    # Use socks.socksocket for creating the socket
    socket.socket = socks.socksocket
    
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            # Set a timeout of 10 seconds
            s.settimeout(10)
            # Connect to the target host and port
            s.connect((host_ip, host_port))
            # Convert the hexadecimal request to bytes
            request_bytes = bytes.fromhex(request)
            # Send the request
            s.sendall(request_bytes)
            print("HTTP request sent:")
            print(request_bytes)
            
            # Receive the response
            response = b""
            while True:
                data = s.recv(4096)
                if not data:
                    break
                response += data
            
            # Decode the response to a string
            return response.decode('utf-8', errors='replace')
    
    except Exception as e:
        print("An error occurred:", e)
        return None

if __name__ == "__main__":
    # Replace with the target IP address
    host = '192.168.1.100'  # Example IP address
    host_port = 80           # HTTP port
    # Example HTTP GET request in hexadecimal
    # This represents: "GET / HTTP/1.1\r\nHost: 192.168.1.100:80\r\n\r\n"
    request = "474554202f20485454502f312e310d0a486f7374203a203139392e392e392e393020484b0d0a0d0a"
    
    response = send_http_request(host, host_port, request)
    if response:
        print("\nHTTP response received:")
        print(response)








