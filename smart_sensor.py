import time
import board
from digitalio import DigitalInOut, Direction
from PIL import Image, ImageDraw, ImageFont
from adafruit_rgb_display import st7789
import adafruit_hdc302x
import datetime
import os

# Font size
FONTSIZE = 30


# Initialize HDC302x sensor
try:
    i2c = board.I2C()
    hdc = adafruit_hdc302x.HDC302x(i2c)
except ValueError as e:
    print(f"ValueError: {e}")
    exit(1)
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    exit(1)

# Create the display
cs_pin = DigitalInOut(board.CE0)
dc_pin = DigitalInOut(board.D25)
reset_pin = DigitalInOut(board.D24)
BAUDRATE = 24000000

spi = board.SPI()
disp = st7789.ST7789(
    spi,
    height=240,
    y_offset=80,
    rotation=180,
    cs=cs_pin,
    dc=dc_pin,
    rst=reset_pin,
    baudrate=BAUDRATE,
)


# Turn on the Backlight
backlight = DigitalInOut(board.D26)
backlight.switch_to_output()
backlight.value = True

# Create blank image for drawing.
width = disp.width
height = disp.height
image = Image.new("RGB", (width, height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Clear display.
draw.rectangle((0, 0, width, height), outline=0, fill=(32, 32, 32))
disp.image(image)

# Load fonts
large_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 40)
medium_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 30)
small_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 20)

# Check WiFi status
def get_wifi_status():
    wifi_status = os.popen("iwgetid -r").read().strip()
    if wifi_status:
    	return "WiFi On"
    else:
        return "WiFi Off"


while True:
    # Read temperature and humidity from the sensor
    try:
        temp_celcius = hdc.temperature
        humidity = hdc.relative_humidity
        temp_fahrenheit = (temp_celcius * 9/5) + 32
    except ValueError as ve:
        print(f"ValueError while reading sensor data: {ve}")
        temp_celcius = None
        humidity = None
        temp_fahrenheit = None
    except IOError as ioe:
        print(f"IOError while accessing the sensor: {ioe}")
        temp_celcius = None
        humidity = None
        temp_fahrenheit = None
    except Exception as e:
        print(f"Unexpected error occurred: {e}")
        temp_celcius = None
        humidity = None
        temp_fahrenheit = None

    # Get current time
    current_time = datetime.datetime.now().strftime("%I:%M %p")

    # Get WiFi status
    wifi_status = get_wifi_status()

    # Draw black background
    draw.rectangle((0, 0, width, height), outline=0, fill=(32, 32, 32))

    # Display temperature and humidity
    if temp_celcius is not None and humidity is not None:
        draw.text((10, 10), f"T: {temp_celcius:.1f}C", font=large_font, fill=(255, 69, 0))
        draw.text((10, 60), f"F: {temp_fahrenheit:.1f}F", font=large_font, fill=(255, 69, 0))
        draw.text((10, 110), f"H: {humidity:.1f}%", font=large_font, fill=(30, 144, 255))
    else:
        draw.text((10, 60), "Sensor Error", font=large_font, fill=(255, 0, 0))

    # Display WiFi status
    wifi_color = (0, 255, 0) if wifi_status else (255, 0, 0)  # Green for On, Red for Off
    draw.text((10, 180), wifi_status, font=small_font, fill=wifi_color)

    #  Display Time
    draw.text((width - 100, 180), current_time, font=small_font, fill=(255, 255, 255))

    # Separator line
    draw.line((0, 170, width, 170), fill=(255, 255, 255), width=2)

    # Display the image
    disp.image(image)

    time.sleep(1)
