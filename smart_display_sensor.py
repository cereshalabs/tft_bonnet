import time
import board
from digitalio import DigitalInOut, Direction
from PIL import Image, ImageDraw, ImageFont
from adafruit_rgb_display import st7789
import adafruit_hdc302x

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

# Input pins:
button_A = DigitalInOut(board.D5)
button_A.direction = Direction.INPUT

button_B = DigitalInOut(board.D6)
button_B.direction = Direction.INPUT

button_L = DigitalInOut(board.D27)
button_L.direction = Direction.INPUT

button_R = DigitalInOut(board.D23)
button_R.direction = Direction.INPUT

button_U = DigitalInOut(board.D17)
button_U.direction = Direction.INPUT

button_D = DigitalInOut(board.D22)
button_D.direction = Direction.INPUT

button_C = DigitalInOut(board.D4)
button_C.direction = Direction.INPUT

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
draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
disp.image(image)

# Load font
fnt = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 30)

while True:
    # Read temperature and humidity from the sensor
    try:
        temperature = hdc.temperature
        humidity = hdc.relative_humidity
    except Exception as e:
        print(f"Error reading sensor data: {e}")
        temperature = None
        humidity = None

    # Draw black background
    draw.rectangle((0, 0, width, height), outline=0, fill=0)

    # Display temperature and humidity
    if temperature is not None and humidity is not None:
        draw.text((10, 60), f"Temp: {temperature:.2f} C", font=fnt, fill=(255, 255, 255))
        draw.text((10, 120), f"Humi: {humidity:.2f} %", font=fnt, fill=(255, 255, 255))
    else:
        draw.text((10, 90), "Sensor Error", font=fnt, fill=(255, 0, 0))

    # Display button state (for debugging if needed)
    # Example: Display button U state
    if not button_U.value:
        print("Up button pressed")

    # Display the image
    disp.image(image)

    time.sleep(1)

