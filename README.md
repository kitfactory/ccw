# CCW (Counter Clock Wise) 🎤🚀

CCW stands for **Cursor, Cline, and Windsurf**. This free continuous voice input software enables seamless automation of text input and UI control through speech commands.

## Overview 🔍
- **Software Name:** CCW (Counter Clock Wise)  
  *CCW is named after Cursor, Cline, and Windsurf.*
- **Operation Summary:**  
  - **Launch Method:** Start the application by running the `ccw` command from the command line.
  - **WebView Launch:** A WebView window is launched and the Speech API is activated for voice recognition.
  - **Continuous Voice Input:** Voice is continuously captured from the screen top.
  - **Text Input Support:** Recognized text is automatically pasted into a location specified in the configuration file.
  - **Trigger-Based Newline:** When a specified trigger keyword (e.g., "エンター") is detected in the voice input, it is removed and a newline (Enter key simulation) is performed to aid in text editing.

## Features 🔥✨
- **Voice Recognition Integration**  
  Utilizes a robust speech recognition engine with all required permissions.
- **Automated UI Interactions**  
  Automates mouse movement, clicking, and text pasting using `pyautogui`.
- **Flexible Configuration**  
  Essential settings such as window position, cursor position, and trigger keyword are managed via a `.ccw` configuration file located in your home directory.
- **Command Line Launch**  
  Simply run the `ccw` command to start the application.
- **Optimized for Editors**  
  Designed to support continuous voice input at the top of the screen, pasting text into an editor and inserting newlines using a trigger keyword.
- **Free to Use**  
  Enjoy advanced voice input automation at no cost!

## Technologies 🛠️
- **pywebview:** Used to display a WebView-based interface.
- **pyautogui:** Automates mouse and keyboard operations.
- **pyperclip:** Handles clipboard operations.
- **PyYAML:** Manages configuration files.
- **Python:** The core programming language.

## Getting Started 🚀

### Installation
This library is distributed on PyPI under the name `ccw`.  
To install, run:
```sh
pip install ccw
```
Alternatively, install from source:
```sh
python -m pip install .
```

Ensure that a configuration file named `.ccw` is located in your home directory with the following sections:

- **Window Configuration:**  
  Specifies the initial window position.
  ```yaml
  window:
      x: 1500   # Initial window X-coordinate
      y: 10     # Initial window Y-coordinate
  ```

- **Cursor Configuration:**  
  Specifies the cursor position for automated text pasting.
  ```yaml
  cursor:
      x: 1877   # Cursor X position
      y: 932    # Cursor Y position
  ```

- **Keyword Configuration:**  
  Defines the trigger keyword – if this keyword (e.g., "エンター") is detected in the voice input, it is removed and a newline is inserted.
  ```yaml
  keyword:
      trigger: "エンター"  # Trigger keyword for newline insertion
  ```

### Running the Application
After installation and configuration, start the application by running:
```sh
ccw
```
This command launches the WebView window and activates the Speech API for continuous voice recognition and text input automation.

## Permissions 📜
This software uses voice recognition technology and has obtained all necessary permissions for operation.

---

Enjoy CCW and revolutionize your text input experience! 😄🎉✨

# ICON
https://www.flaticon.com/free-icon/mic_4787623?related_id=4787614&origin=search