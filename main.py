from stream_server import Stream_Server

def main():
    server = Stream_Server("")
    print("hello")

    while True:

        server.handle_stream_requests()

if __name__ == "__main__":
    main()