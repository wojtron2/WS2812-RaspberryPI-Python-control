import time
import board
import neopixel

# Konfiguracja taśmy LED
LED_COUNT = 4         # Liczba diod LED
LED_PIN = board.D18   # Pin sterujący (GPIO18)
LED_BRIGHTNESS = 0.2  # Jasność (0.0 - 1.0)
ORDER = neopixel.GRB  # Kolejność kolorów

# Inicjalizacja taśmy LED
pixels = neopixel.NeoPixel(LED_PIN, LED_COUNT, brightness=LED_BRIGHTNESS, auto_write=False, pixel_order=ORDER)

def kolor_czerwony():
    pixels.fill((255, 0, 0))  # Czerwony kolor
    pixels.show()

def kolor_zielony():
    pixels.fill((0, 255, 0))  # Zielony kolor
    pixels.show()

def kolor_niebieski():
    pixels.fill((0, 0, 255))  # Niebieski kolor
    pixels.show()

def efekt_pulsowania():
    for i in range(0, 256, 5):  
        pixels.fill((i, 0, 0))  
        pixels.show()
        time.sleep(0.02)
    for i in range(255, -1, -5):  
        pixels.fill((i, 0, 0))  
        pixels.show()
        time.sleep(0.02)

try:
    while True:
        kolor_czerwony()
        time.sleep(1)
        kolor_zielony()
        time.sleep(1)
        kolor_niebieski()
        time.sleep(1)
        efekt_pulsowania()
except KeyboardInterrupt:
    pixels.fill((0, 0, 0))  # Wyłączenie LED przy zamknięciu programu
    pixels.show()