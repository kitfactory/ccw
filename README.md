# Speech Recognition Automation Software 🎤🚀

This is a free, easy-to-use continuous voice input software designed for seamless integration with Cursor, Cline, and Windsurf. Whether you are controlling a user interface or automating text input, this tool provides a smooth experience using voice commands.

## Features 🔥✨
- **Voice Recognition Integration**  
  The application is built with a robust speech recognition engine and uses it with all necessary permissions obtained.
- **Automated UI Interactions**  
  Uses `pyautogui` to automatically move the mouse to a set cursor position, perform clicks, and paste recognized text.
- **Flexible Configuration**  
  All essential settings (window position, cursor position, and keyword trigger) are managed via a `.ccw` file located in your home directory.
- **Free to Use**  
  Enjoy the power of continuous voice input without any cost!

## Technologies 🛠️
- **pywebview**: For displaying a WebView-based interface.
- **pyautogui**: For automating mouse and keyboard operations.
- **pyperclip**: For clipboard functionalities.
- **PyYAML**: For managing configuration files.
- **Python**: The primary programming language.

## Getting Started 🚀
1. Install the required libraries:
    ```sh
    pip install pywebview pyautogui pyperclip pyyaml
    ```
2. **Configuration File (.ccw)**:  
   Create or update the `.ccw` file in your home directory with the following sections. **All sections must be preserved for proper operation.**
   
   - **Window Configuration**:  
     Specifies the initial window position of the WebView.
     ```yaml
     window:
         x: 1500   # X position (initial window X-coordinate)
         y: 10     # Y position (initial window Y-coordinate)
     ```
     
   - **Cursor Configuration**:  
     Specifies the cursor position used for automated mouse movement, click, and paste actions.
     ```yaml
     cursor:
         x: 1877   # Cursor X position
         y: 932    # Cursor Y position
     ```
     
   - **Keyword Configuration**:  
     Specifies the trigger keyword used in the recognized speech message.  
     If the recognized message contains this trigger (e.g., "Enter"), the trigger is removed from the text, the remaining text is pasted, and an Enter key is simulated.
     ```yaml
     keyword:
         trigger: "Enter"  # Trigger keyword for processing the recognized text
     ```

3. Launch the application and enjoy seamless voice command control!

## Permissions 📜
This software uses voice recognition technology and all necessary permissions have been obtained for its operation.

---

Have fun using this awesome tool! 😄🎉✨


# ICON
https://www.flaticon.com/free-icon/mic_4787623?related_id=4787614&origin=search