import argparse
import socket


HOST = "192.168.0.153"
PORT = 8000


def tcp_echo_server(host, port):
    """
    Runs a TCP server.
    :param host: server IP address
    :param port: server port number
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # allows socket re-use
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        s.bind((host, port))
        s.listen()
        print("Server listening...")
        conn, addr = s.accept()

        with conn:
            while True:
                data = conn.recv(1024)
                if not data or data.decode().lower() == "exit":
                    break
                print(f"Received {data.decode()}")
                conn.sendall(data)


def udp_echo_server(host, port):
    """
    Runs a UDP server.
    :param host: server IP address
    :param port: server port number
    """
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        # allows socket re-use
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        s.bind((host, port))
        print("Server listening...")

        while True:
            data, addr = s.recvfrom(1024)
            if not data or data.decode().lower() == "exit":
                break
            print(f"Received {data.decode()}")
            s.sendto(data, addr)


def main():
    parser = argparse.ArgumentParser(description="Distributed File System [Server]")
    parser.add_argument("-c", "--conn_type", help="connection type", required=True)

    args = parser.parse_args()

    if args.conn_type.lower() == "tcp":
        tcp_echo_server(HOST, PORT)
    elif args.conn_type.lower() == "udp":
        udp_echo_server(HOST, PORT)


if __name__ == "__main__":
    main()
