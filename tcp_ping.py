#!/usr/bin/env python3
"""Simple TCP-based ping utility.

Measures round-trip time for establishing a TCP connection to a server,
which can be used when ICMP ping is blocked. The tool mimics the familiar
output of the ``ping`` command but uses TCP SYN packets instead of ICMP.
"""
import argparse
import socket
import time
from typing import List, Optional

def tcp_ping(host: str, port: int, count: int = 4, timeout: float = 2.0) -> List[Optional[float]]:
    """Perform ``count`` TCP connection attempts and measure latency.

    Returns a list of latencies in milliseconds. ``None`` indicates a failed
    connection attempt.
    """
    results: List[Optional[float]] = []
    for _ in range(count):
        start = time.perf_counter()
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(timeout)
            try:
                sock.connect((host, port))
            except OSError:
                results.append(None)
            else:
                elapsed_ms = (time.perf_counter() - start) * 1000
                results.append(elapsed_ms)
        time.sleep(1)
    return results

def main() -> None:
    parser = argparse.ArgumentParser(description="TCP ping - measure latency using TCP packets")
    parser.add_argument("host", help="Target host to ping")
    parser.add_argument("port", type=int, help="Target TCP port")
    parser.add_argument("-c", "--count", type=int, default=4, help="Number of packets (default: 4)")
    parser.add_argument("-t", "--timeout", type=float, default=2.0, help="Connection timeout in seconds")
    args = parser.parse_args()

    latencies = tcp_ping(args.host, args.port, args.count, args.timeout)

    success = [lat for lat in latencies if lat is not None]
    for i, latency in enumerate(latencies, 1):
        if latency is None:
            print(f"tcp_seq={i} connection failed")
        else:
            print(f"tcp_seq={i} time={latency:.2f} ms")

    if success:
        avg = sum(success) / len(success)
        print(f"average={avg:.2f} ms")
    else:
        print("all attempts failed")

if __name__ == "__main__":
    main()
