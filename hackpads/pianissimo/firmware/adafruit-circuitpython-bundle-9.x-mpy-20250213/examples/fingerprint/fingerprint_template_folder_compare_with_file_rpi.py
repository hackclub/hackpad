# SPDX-FileCopyrightText: 2024 itsFDavid
# SPDX-License-Identifier: MIT
"""
`fingerprint_template_folder_compare_with_file.py`
====================================================

This is an example program to demo storing fingerprint templates in a folder. It also allows
comparing a newly obtained print with one stored in the folder in the previous step. This is helpful
when fingerprint templates are stored centrally (not on sensor's flash memory) and shared
between multiple sensors.

* Author(s): itsFDavid

Implementation Notes
--------------------
This program was used on other fingerprint sensors,
and everything worked as expected, including testing with Raspberry Pi Zero 2W.

To run the program:
1. Connect the fingerprint sensor to your Raspberry Pi.
2. Install required libraries.
3. Execute the script using Python.
"""

import os
import time

import serial
from PIL import Image
import adafruit_fingerprint

# If using with a computer such as Linux/RaspberryPi, Mac, Windows with USB/serial converter:
# uart = serial.Serial("COM6", baudrate=57600, timeout=1)

# If using with Linux/Raspberry Pi and hardware UART:
uart = serial.Serial("/dev/ttyUSB0", baudrate=57600, timeout=1)

finger = adafruit_fingerprint.Adafruit_Fingerprint(uart)

# Folder where fingerprint templates are stored
FINGERPRINT_FOLDER = "fingerprint/"


# Enroll and verification functions
def get_num(max_num):
    """Prompts the user to enter a valid template number within the available range."""
    while True:
        try:
            num = int(input(f"Enter a template number (0-{max_num}): "))
            if 0 <= num <= max_num:
                return num
            print(f"Please enter a number between 0 and {max_num}.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def get_fingerprint():
    """Get an image from the fingerprint sensor for search, process for a match."""
    print("Waiting for finger...")
    while finger.get_image() != adafruit_fingerprint.OK:
        pass
    print("Processing image...")
    if finger.image_2_tz(1) != adafruit_fingerprint.OK:
        print("Error processing image.")
        return False
    print("Searching for matches...")
    return finger.finger_search() == adafruit_fingerprint.OK


def enroll_finger(location):
    """Enroll a fingerprint and store it in the specified location."""
    for fingerimg in range(1, 3):
        action = "Place finger on sensor" if fingerimg == 1 else "Same finger again"
        print(action, end="")
        while True:
            if finger.get_image() == adafruit_fingerprint.OK:
                print("Image captured")
                break
            print(".", end="")
        print("Processing image...", end="")
        if finger.image_2_tz(fingerimg) != adafruit_fingerprint.OK:
            print("Error processing image.")
            return False
        if fingerimg == 1:
            print("Remove finger")
            time.sleep(1)
            while finger.get_image() != adafruit_fingerprint.NOFINGER:
                pass
    print("Creating model...", end="")
    if finger.create_model() != adafruit_fingerprint.OK:
        print("Error creating model.")
        return False
    print(f"Storing model in location #{location}...", end="")
    if finger.store_model(location) != adafruit_fingerprint.OK:
        print("Error storing model.")
        return False
    print("Model stored.")
    return True


def save_fingerprint_image(filename):
    """Capture a fingerprint and save the image to a file."""
    print("Waiting for finger...")
    while finger.get_image() != adafruit_fingerprint.OK:
        pass
    img = Image.new("L", (256, 288), "white")
    pixeldata = img.load()
    mask = 0b00001111
    result = finger.get_fpdata(sensorbuffer="image")
    coor_x, coor_y = 0, 0
    for i, value in enumerate(result):
        if i % 100 == 0:
            print("", end="")
        pixeldata[coor_x, coor_y] = (int(value) >> 4) * 17
        coor_x += 1
        pixeldata[coor_x, coor_y] = (int(value) & mask) * 17
        if coor_x == 255:
            coor_x = 0
            coor_y += 1
        else:
            coor_x += 1
    img.save(filename)
    print(f"\nImage saved to {filename}")
    return True


def enroll_save_to_file():
    """Capture a fingerprint, create a model, and save it to a file."""
    for fingerimg in range(1, 3):
        action = "Place finger on sensor" if fingerimg == 1 else "Same finger again"
        print(action, end="")
        while True:
            if finger.get_image() == adafruit_fingerprint.OK:
                print("Image captured")
                break
            print(".", end="")
        print("Processing image...", end="")
        if finger.image_2_tz(fingerimg) != adafruit_fingerprint.OK:
            print("Error processing image.")
            return False
        if fingerimg == 1:
            print("Remove finger")
            while finger.get_image() != adafruit_fingerprint.NOFINGER:
                pass
    print("Creating model...", end="")
    if finger.create_model() != adafruit_fingerprint.OK:
        print("Error creating model.")
        return False
    print("Storing template...")
    data = finger.get_fpdata("char", 1)
    filename = os.path.join(FINGERPRINT_FOLDER, f"template_{int(time.time())}.dat")
    with open(filename, "wb") as file:
        file.write(bytearray(data))
    print(f"Template saved to {filename}")
    return True


def fingerprint_check_folder():
    """Compare a fingerprint with all files in the fingerprint folder."""
    print("Waiting for fingerprint...")
    while finger.get_image() != adafruit_fingerprint.OK:
        pass
    print("Processing image...")
    if finger.image_2_tz(1) != adafruit_fingerprint.OK:
        print("Error processing image.")
        return False
    print("Searching for matches in the template folder...", end="")
    found_match = False
    matched_filename = None
    for filename in os.listdir(FINGERPRINT_FOLDER):
        if filename.endswith(".dat"):
            file_path = os.path.join(FINGERPRINT_FOLDER, filename)
            with open(file_path, "rb") as file:
                data = file.read()
            finger.send_fpdata(list(data), "char", 2)
            if finger.compare_templates() == adafruit_fingerprint.OK:
                matched_filename = filename
                found_match = True
                break
    if found_match:
        print(f"Fingerprint matches the template in the file {matched_filename}!")
    else:
        print("No match found.")
    return found_match


def main():
    """Main function to run the fingerprint enrollment and verification program.
    This function provides a menu for the user to enroll fingerprints, search for
    fingerprints, delete templates, save fingerprint images, and reset the fingerprint library.
    It interacts with the user via the console and performs the necessary actions based on
    user input.
    """
    while True:
        print("----------------")
        if finger.read_templates() != adafruit_fingerprint.OK:
            raise RuntimeError("Could not read templates.")
        print("Stored fingerprint templates: ", finger.templates)

        if finger.count_templates() != adafruit_fingerprint.OK:
            raise RuntimeError("Could not count templates.")
        print("Number of templates found: ", finger.template_count)

        if finger.read_sysparam() != adafruit_fingerprint.OK:
            raise RuntimeError("Could not retrieve system parameters.")
        print("Template library size: ", finger.library_size)
        print("Options:")
        print("e) Enroll fingerprint")
        print("f) Search fingerprint")
        print("d) Delete fingerprint")
        print("s) Save fingerprint image")
        print("cf) Compare template with file")
        print("esf) Enroll and save to file")
        print("r) Reset library")
        print("q) Exit")
        print("----------------")
        user_choice = input("> ")
        match user_choice.lower():
            case "e":
                enroll_finger(get_num(finger.library_size))
            case "f":
                print_fingerprint()
            case "d":
                delete_fingerprint()
            case "s":
                save_fingerprint_image(f"fingerprint_{int(time.time())}.png")
            case "cf":
                fingerprint_check_folder()
            case "esf":
                enroll_save_to_file()
            case "r":
                reset_library()
            case "q":
                exit_program()
            case _:
                print("Invalid option.")


def print_fingerprint():
    """Prints the fingerprint detection result."""
    if get_fingerprint():
        output_finger_detected = f"Fingerprint detected with ID #{finger.finger_id}"
        output_finger_confidence = f"Confidence: {finger.confidence}"
        print(output_finger_detected)
        print(output_finger_confidence)
    else:
        print("Fingerprint not found.")


def delete_fingerprint():
    """Deletes a fingerprint model based on user input."""
    if finger.delete_model(get_num(finger.library_size)) == adafruit_fingerprint.OK:
        print("Deleted successfully!")
    else:
        print("Failed to delete.")


def reset_library():
    """Resets the fingerprint library."""
    if finger.empty_library() == adafruit_fingerprint.OK:
        print("Library reset.")
    else:
        print("Failed to reset library.")


def exit_program():
    """Exits the program."""
    print("Exiting...")
    raise SystemExit


if __name__ == "__main__":
    main()
