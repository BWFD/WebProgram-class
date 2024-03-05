import sys 
import network

def WiFi_connect(ssid_c, password_c) :
    wlan = network.WLAN(network,STA_IF)
    wlan.active(True)
    
    if wlan.isconnected() :
        print("ESP32 is connected!")
    print("Searching WiFi")
    ssid_all = wlan.scan()
    
    for ssid in ssid_all : 
        if ssid_c == bytes.decode(ssid[0]) :
            print("find ESP32")
            break
        else :
            print("Cant find ESP32")
            sys.exit(-1)
            return 0
    try :
        wlan.connect(ssid_c,password)
        print("connecting")
        delay(2500)
        while not wlan.isconnected() :
            pass
    except :
        print("ERROR")
        sys.exit(-1)
    return wlan

if __name__ == "__main__" :
    wlan = WiFi_connect("ESP32_Master","3B017126")
