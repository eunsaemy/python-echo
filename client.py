import argparse
import socket


HOST = "192.168.0.153"
PORT = 8000


def tcp_echo_client(host, port):
    """
    Runs a TCP client.
    :param host: server IP address
    :param port: server port number
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # allows socket re-use
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        s.connect((host, port))

        while True:
            message = input("Please enter a message to echo:\n")
            s.sendall(bytes(message, "utf-8"))
            if message.lower() == "exit":
                break
            data = s.recv(1024)
            print(f"Received {data.decode()}")


def udp_echo_client(host, port):
    """
    Runs a UDP client.
    :param host: server IP address
    :param port: server port number
    """
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        # allows socket re-use
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        while True:
            message = input("Please enter a message to echo:\n")
            s.sendto(bytes(message, "utf-8"), (host, port))
            if message.lower() == "exit":
                break
            data, server = s.recvfrom(1024)
            print(f"Received {data.decode()}")


def main():
    parser = argparse.ArgumentParser(description="Distributed File System [Client]")
    parser.add_argument("-c", "--conn_type", help="connection type", required=True)

    args = parser.parse_args()

    if args.conn_type.lower() == "tcp":
        tcp_echo_client(HOST, PORT)
    elif args.conn_type.lower() == "udp":
        udp_echo_client(HOST, PORT)


if __name__ == "__main__":
    main()
