import time
import argparse
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions

# Set HTML IDs for the TTS website
Sites = {
    "ttsmp3": {
        "url": "https://ttsmp3.com/ai",  # The URL of the TTS site
        "textbox": {
            "by": "id",  # Type of locator (id)
            "value": "voicetext",  # The ID of the input field for the text
            "set_to": ""  # Text will be dynamically set during script execution
        },
        "button": {
            "by": "id",  # Type of locator (id)
            "value": "vorlesenbutton"  # The ID of the button to start the speech
        },
        "speed": {
            "by": "id",  # Type of locator (id)
            "value": "speed",  # The ID for the speed input field
            "set_to": 0  # Default speed value
        }
    }
}

# Set up Chrome browser options for headless mode and performance optimizations
chrome_options = ChromeOptions()
chrome_options.add_argument("--headless")  # Run in headless mode (no UI)
chrome_options.add_argument("--no-sandbox")  # Disable sandboxing (security feature)
chrome_options.add_argument("--disable-gpu")  # Disable GPU hardware acceleration
chrome_options.add_argument("--disable-usb-discovery")  # Disable USB discovery
chrome_options.add_argument("--disable-webgl")  # Disable WebGL
chrome_options.add_argument("--disable-software-rasterizer")  # Disable software rasterizer
chrome_options.add_argument("log-level=3")  # Suppress most logs (info, warning, error)

# Set up Edge browser options (similar to Chrome options)
edge_options = EdgeOptions()
edge_options.add_argument("--headless")
edge_options.add_argument("--no-sandbox")
edge_options.add_argument("--disable-gpu")
edge_options.add_argument("--disable-usb-discovery")
edge_options.add_argument("--disable-webgl")
edge_options.add_argument("--disable-software-rasterizer")
edge_options.add_argument("log-level=3")


def parse_arguments():
    """
    Function to parse command-line arguments.
    It includes text to speak, speed, site choice, and browser choice.

    Returns:
        argparse.Namespace: Parsed arguments object containing the user inputs.
    """

    def validate_speed(value):
        """
        Validates that the speed is within the acceptable range (0.5 to 2.0).

        Args:
            value (str): The speed value provided from the command line.

        Returns:
            float: Validated speed value.

        Raises:
            argparse.ArgumentTypeError: If the speed is outside the valid range.
        """
        try:
            value = float(value)
            if 0.5 <= value <= 2.0:
                return value
            else:
                raise argparse.ArgumentTypeError("Speed must be between 0.5 and 2.0")
        except ValueError:
            raise argparse.ArgumentTypeError("Speed must be a float between 0.5 and 2.0")

    # Initialize argument parser
    parser = argparse.ArgumentParser(description="A script to read text aloud using a specified TTS site.")

    # Argument for the text to be spoken
    parser.add_argument('--text', '-t', type=str, help="Text to be spoken", required=True)

    # Argument for setting the speed of speech
    parser.add_argument("--speed", "-spd", type=validate_speed, default=0.85,
                        help="Set the TTS reading speed. Overrides the default speed.")

    # Argument to select the TTS site (e.g., ttsmp3)
    parser.add_argument('--site', '-s', type=str, choices=Sites.keys(), default='ttsmp3',
                        help="Choose the TTS site (default: ttsmp3)")

    # Option to list available TTS sites
    parser.add_argument('--list-sites', '-l', action='store_true', help="List available TTS sites")

    # Argument for the wake word to prepend to the text
    parser.add_argument('--wake-word', '-w', type=str, default="Alexa, ",
                        help="Wake word to prepend to text (default: 'Alexa')")

    # Argument to select the browser (chrome, edge, safari)
    parser.add_argument('--browser', '-b', type=str, choices=['chrome', 'edge', 'safari'], default='chrome',
                        help="Choose the browser to use (default: chrome)")

    return parser.parse_args()


def TTS_ttsmp3(driver, site: dict):
    """
    This function automates the process of visiting the TTS site,
    entering text, setting the speed, and triggering speech output.

    Args:
        d (webdriver.Chrome): Selenium WebDriver instance (either Chrome or Edge).
        site (dict): Dictionary containing site-specific elements and values.
    """
    # Navigate to the specified TTS site
    driver.get(site["url"])

    # Find the textbox element and enter the text to be spoken
    textbox = driver.find_element(site["textbox"]["by"], site["textbox"]["value"])
    textbox.send_keys(site["textbox"]["set_to"])

    # Set the speech speed using JavaScript (because it's a range input)
    speed_input = driver.find_element(site["speed"]["by"], site["speed"]["value"])
    driver.execute_script("arguments[0].value = arguments[1]; arguments[0].dispatchEvent(new Event('input'));",
                     speed_input, site["speed"]["set_to"])

    # Click the 'Read' button to trigger the speech output
    read_button = driver.find_element(site["button"]["by"], site["button"]["value"])
    read_button.click()

    # Wait for the site to finish reading the text
    while True:
        if read_button.get_attribute("value") == "Read":
            break
        else:
            time.sleep(1)

    # Close the browser after reading the text
    driver.close()


if __name__ == '__main__':
    """
    Main execution block. Parses command-line arguments, sets up the browser,
    and executes the TTS functionality on the selected site.
    """
    # Parse command-line arguments
    args = parse_arguments()

    if args.list_sites:
        # List all available TTS sites if the user requested it
        print("Available sites:")
        for site in Sites:
            print(f"- {site}")
        exit(0)

    # Ensure that the text starts with the wake word, if not, prepend it
    if not (args.text.lower().startswith(args.wake_word.lower()) or args.text.lower().startswith(
            args.wake_word.strip(", ").lower())):
        args.text = f"{args.wake_word}, {args.text}"

    # Set the chosen site for TTS processing
    chosen_site = args.site

    # Start the appropriate WebDriver based on the selected browser
    if args.browser == "chrome":
        driver = webdriver.Chrome(options=chrome_options)
    elif args.browser == "edge":
        driver = webdriver.Edge(options=edge_options)
    elif args.browser == "safari":
        driver = webdriver.Safari()

    # Execute TTS functionality on the specified site (ttsmp3)
    if chosen_site == "ttsmp3":
        Sites["ttsmp3"]["textbox"]["set_to"] = args.text
        Sites["ttsmp3"]["speed"]["set_to"] = args.speed
        TTS_ttsmp3(driver, Sites["ttsmp3"])