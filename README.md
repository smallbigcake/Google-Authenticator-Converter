# Google-Authenticator-Converter
Convert Google Authenticator export format to plain text format.

When export OTP from Google Authenticator app, we will get one or more QR code. These QR code is in its OTP Auth Migration format.

OTP Auth Migration URL is like:

`otpauth-migration://offline?data=ChoKCpJGgiRoGgaSpKgSBkRlbW8gMSABKAEwAgoeCg6SSum4zwsy2zrOmgzRNhIGRGVtbyAyIAEoATACCiQKFJJKgqBJkm6BtK6zgKukqDNimSZJEgZEZW1vIDMgASgBMAIKKAoJsWxH8MtqsI%2FGEg1EZW1vIDQ6dXNlciA0GgZEZW1vIDQgASgBMAIKJwoIYdOEEddNURcSDURlbW8gNTp1c2VyIDUaBkRlbW8gNSABKAEwAhABGAEgACj4s4nu%2B%2F%2F%2F%2F%2F8B
`

What this repo do is to convert these URL to plain OTP Auth URL format.

Plain OTP Auth URL is like:

`otpauth://totp/Demo 4:Demo 4:user 4?secret=WFWEP4GLNKYI7RQ=&issuer=Demo 4&algorithm=SHA1&digits=6
`

## Dependency

`Python 3.12` with `opencv-python` and `protobuf`

```Bash
pip install opencv-python protobuf
```

## Usage

```Bash
python src/qrcode.py src/demo.jpg
```

