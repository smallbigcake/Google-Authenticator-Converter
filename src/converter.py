import base64
from urllib.parse import unquote

from otpauth_migration_pb2 import Payload
from mapping import OTP_TYPE, OTP_ALGORITHM, OTP_DIGIT, OTP_TYPE_HOTP


class Converter(object):

    def __init__(self):
        self.payload = Payload()

    def to_plain(self):
        pass

    def from_migration_string(self, migration_string):

        data = unquote(migration_string.split('data=')[1])

        self.payload.ParseFromString(base64.b64decode(data))

    def to_plain_string(self):

        otp_str_list = []
        for otp_item in self.payload.otp_parameters:

            otp_type = OTP_TYPE[otp_item.type]
            issuer = otp_item.issuer
            name = otp_item.name
            label = f'{issuer}:{name}'
            secret = base64.b32encode(otp_item.secret).decode()
            otp_algorithm = OTP_ALGORITHM[otp_item.algorithm]
            digits = OTP_DIGIT[otp_item.digits]
            counter = otp_item.counter

            otp_url = f'otpauth://{otp_type}/{label}?secret={secret}&issuer={otp_item.issuer}&algorithm={otp_algorithm}&digits={digits}'
            if otp_type == OTP_TYPE_HOTP:
                otp_url += f'&counter={counter}'

            # print(otp_url)
            otp_str_list.append(otp_url)
        return otp_str_list

        # print(otp_str_list)
