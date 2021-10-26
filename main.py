#!/usr/bin/env python3

import argparse
import datetime
import typing
from flask import Flask
import requests
import threading
import time
from typing import Callable

app = Flask(__name__)

output = []
output_lock = threading.Lock()
@app.route("/")
def hello_html():
    output_lock.acquire()
    s = '<br>'.join(output)
    output_lock.release()

    return f"<h4>{s}</h4>"

def is_connected() -> bool:
    """
    Checks if host is connected
    :return: True is connected, False otherwise
    """
    try:
        response = requests.get('http://example.com', timeout=1)

        if response.status_code == requests.codes.OK:
            return True
        else:
            return False
    except:
        return False


def monitor_connectivity(handler: Callable[[str], None]):
    """
     Continuously monitor connectivity
    """
    previous_state: bool = is_connected()
    disconnected_time = time.time()
    cycles = 0
    while True:
        time.sleep(1)
        new_state = is_connected()
        if new_state != previous_state or cycles % 600 == 0:
            disconnected_len_str = ''
            if new_state == False:
                disconnected_time = time.time()
            else: # new_state = True
                disconnected_len = time.time() - disconnected_time
                if disconnected_len < 2:
                    disconnected_len_str = '<2s'
                elif disconnected_len < 5:
                    disconnected_len_str = '<5s'
                elif disconnected_len < 10:
                    disconnected_len_str = '<10s'
                elif disconnected_len < 30:
                    disconnected_len_str = '<30s'
                elif disconnected_len < 60:
                    disconnected_len_str = '<1m'
                elif disconnected_len < 120:
                    disconnected_len_str = '<2m'
                elif disconnected_len < 240:
                    disconnected_len_str = '<4m'
                elif disconnected_len < 480:
                    disconnected_len_str = '<8m'
                elif disconnected_len < 960:
                    disconnected_len_str = '<15m'
                elif disconnected_len < 1920:
                    disconnected_len_str = '<30m'
                elif disconnected_len < 3840:
                    disconnected_len_str = '<1h'
                elif disconnected_len < 7680:
                    disconnected_len_str = '<2.1h'
                elif disconnected_len < 15360:
                    disconnected_len_str = '<4.2h'
                elif disconnected_len < 30720:
                    disconnected_len_str = '<8.5h'
                else:
                    disconnected_len_str = '>30s'
            msg = f'{datetime.datetime.now()}  {"connected" if new_state else "no connected "} {disconnected_len_str}'
            handler(msg)

        cycles += 1
        previous_state = new_state

def web_handler(msg: str):
    global output
    
    output_lock.acquire()
    output.append(msg)
    output_lock.release()

def cli_handler(msg: str):
    print(msg)

def parse_args():
    parser = argparse.ArgumentParser(description='Monitor internet connectivity')
    parser.add_argument('format', type=str, choices=['web', 'cli'])
    parser.add_argument('--port', '-p', type=int, help='the seerver port for web option', required=False)

    return parser.parse_args()

def main():   
    print("hello world")    
    #monitor_connectivity()
    args = parse_args()
    if args.format == 'web':
        monitoring_thread = threading.Thread(target=monitor_connectivity, args=(web_handler,))
        monitoring_thread.start()
        app.run(host='0.0.0.0', port=args.port)
        monitoring_thread.join()
    else:
        monitor_connectivity(cli_handler)
        
if __name__ == "__main__":
    main()
