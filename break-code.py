import base64


hex_string = "48 34 73 49 47 41 73 4f 73 47 51 41 2f 30 31 54 61 32 64 56 4d 6c 5a 31 57 6b 4e 43 61 47 4e 49 51 6e 4e 68 56 30 35 6f 5a 45 64 73 64 6d 4a 70 51 6a 42 68 53 45 70 32 5a 46 64 6b 62 30 6c 48 4f 54 46 6a 61 55 49 7a 57 6c 64 4b 65 6d 46 59 55 6d 78 44 61 6b 31 77 53 55 56 57 64 46 6c 58 62 48 4e 4a 52 33 52 6f 59 32 35 4b 63 46 70 59 53 6d 78 4d 56 30 70 73 59 32 31 34 63 47 4a 72 51 6d 70 68 52 31 5a 71 59 58 70 4a 4d 45 78 74 55 6d 78 4a 53 47 52 77 5a 45 64 6e 5a 32 52 48 56 6a 52 6b 52 47 39 6e 53 57 78 4f 62 46 6b 7a 53 6d 78 6b 51 30 4a 56 57 6c 68 6f 4d 45 39 70 51 57 38 30 62 30 4e 70 4e 47 39 44 4c 7a 52 76 51 32 6c 4c 55 30 6b 39 41 45 74 6c 5a 58 41 67 52 32 39 70 62 6d 63 73 49 48 6c 76 64 53 64 79 5a 53 42 68 62 47 31 76 63 33 51 67 64 47 68 6c 63 6d 55 41 42 59 42 42 43 51 41 67 46 45 4f 72 4c 4a 45 74 48 73 36 4c 41 31 33 39 77 32 65 6c 50 6e 65 72 30 51 65 5a 78 77 41 78 79 34 78 4a 45 77 41 41 41 41 3d 3d"
hex_string = hex_string.replace(" ", "")

byte_sequence = bytes.fromhex(hex_string)
print(byte_sequence)
decoded_message = base64.b64decode(byte_sequence).decode('utf-8', errors='ignore')
print(decoded_message)

base64_string = "MSkgU2VuZCBhcHBsaWNhdGlvbiB0aHJvdWdoIG91ciB3ZWJzaXRlCjMpIEVtYWlsIGthcnJpZXJlLWJlcmxpbkBjaGVjazI0LmRlIHdpdGggdGV4dDogIlNlY3JldCBUZXh0OiAo4oCi4oC/4oCiKSI="

# Decode the Base64 string
decoded_step2 = base64.b64decode(base64_string).decode('utf-8')
decoded_step2