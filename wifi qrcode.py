import wifi_qrcode_generator as qr

im = qr.wifi_qrcode('Some_SSID', False, 'WPA', 'secret_pass')

im.show()