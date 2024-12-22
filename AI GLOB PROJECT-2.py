#INTERNET SPEED TESTER TOOL USING PYTHON PROGRAMMING


import speedtest

def test_internet_speed():
    print("Testing internet speed... Please wait.")
    
    # Create a Speedtest object
    st = speedtest.Speedtest()
    
    # Get the best server
    st.get_best_server()
    
    # Test download speed
    download_speed = st.download() / 1_000_000  # Convert to Mbps
    
    # Test upload speed
    upload_speed = st.upload() / 1_000_000  # Convert to Mbps
    
    # Test ping
    ping = st.results.ping
    
    print("\n--- Internet Speed Test Results ---")
    print(f"Download Speed: {download_speed:.2f} Mbps")
    print(f"Upload Speed: {upload_speed:.2f} Mbps")
    print(f"Ping: {ping:.2f} ms")

# Run the tool
test_internet_speed()