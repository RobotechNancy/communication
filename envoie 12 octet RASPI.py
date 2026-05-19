import serial
import time

ser = serial.Serial(
    port='/dev/serial0',
    baudrate=9600,
    bytesize=serial.EIGHTBITS,
    parity=serial.PARITY_EVEN,
    stopbits=serial.STOPBITS_TWO,
    timeout=1
)

valeurs = [10, 20, 30, 40, 50, 60, 70, 80]

try:
    while True:
        # Construction : Header (2) + Data (8) + Footer (2) = 12 octets
        header = [0xAA, 0x55]
        footer = [0x0D, 0x0A] # Tes 2 octets de STOP de trame
        #aa 55 0a 14 1e 28 32 3c 46 50 0d 0a
        paquet = bytes(header + valeurs + footer)
        
        ser.write(paquet)
        print(f"Trame complète envoyée (12 octets) : {paquet.hex(' ')}")
        
        time.sleep(1)

except KeyboardInterrupt:
    ser.close()