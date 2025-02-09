"""
Module for launching Speech Recognition sample using pywebview.
pywebviewを利用して、音声認識サンプル (speech.html) を表示するモジュールです。

This module creates a window with pywebview and loads the local HTML file 'speech.html'.
本モジュールはpywebviewを利用し、ローカルHTMLファイル'speech.html'をロードするウィンドウを作成します.
"""

import os
import logging
import webview

# Configure logging and display information messages.
# ログ出力の設定: 情報メッセージを出力します。
logging.basicConfig(level=logging.DEBUG, format='[%(asctime)s] %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def update_yaml_config(config_file, new_position):
    """
    Update the .ccw file with the new window position along with keeping the existing cursor and keyword information.
    新しいウィンドウ位置で .ccw ファイルを更新し、既存のcursorとkeywordの情報も保持します。
    
    If the cursor information is missing, it will be set to {"x": 1880, "y": 932}.
    もしcursorの値が存在しなければ、{"x": 1880, "y": 932} で保存します。
    
    If the keyword trigger is missing, it will be set to {"trigger": "エンター"}.
    もしkeywordのtriggerが存在しなければ、{"trigger": "エンター"} で保存します。
    
    Input:
      config_file - Path to the configuration file.
                    設定ファイルへのパス。
      new_position - Tuple (x, y) indicating the new window position.
                     新しいウィンドウ位置 (x, y) のタプル。
    Output:
      None
      なし
    """
    try:
        import yaml  # PyYAML required // PyYAML を使用します。
        # Load the existing configuration file // 既存の設定ファイルを読み込みます。
        with open(config_file, "r", encoding="utf-8") as f:
            config_data = yaml.safe_load(f)
        if not isinstance(config_data, dict):
            config_data = {}
        # Retrieve existing cursor information or set default if missing
        # 既存のcursor情報を取得し、なければデフォルト値を設定します。
        cursor_val = config_data.get("cursor", {})
        if not isinstance(cursor_val, dict) or "x" not in cursor_val or "y" not in cursor_val:
            cursor_val = {"x": 1880, "y": 932}
        # Retrieve existing keyword information or set default if missing
        # 既存のkeyword情報を取得し、なければデフォルト値を設定します。
        keyword_val = config_data.get("keyword", {})
        if not isinstance(keyword_val, dict) or "trigger" not in keyword_val:
            keyword_val = {"trigger": "エンター"}
        # Update the window position while preserving existing cursor and keyword information.
        # ウィンドウ位置を更新し、既存のcursorとkeywordの情報を保持します。
        config_data["window"] = {"x": new_position[0], "y": new_position[1]}
        config_data["cursor"] = cursor_val
        config_data["keyword"] = keyword_val
        with open(config_file, "w", encoding="utf-8") as f:
            yaml.dump(config_data, f, allow_unicode=True)
        message = f"Updated config file with window: {new_position}, cursor: {cursor_val}, keyword: {keyword_val}"
        print(message)  # Display updated information on screen // 画面に更新情報を表示します。
        logger.info(message)
    except Exception as e:
        logger.warning("Failed to update config: %s", e)

class SpeechAPI:
    """
    API class exposed to JavaScript.
    JavaScriptから呼び出されるAPIクラスです。
    
    Methods:
      log_result(transcript): Processes the recognized speech message by moving the cursor, performing click,
                              and pasting the message based on configuration and trigger detection.
                              認識された音声メッセージを処理し、カーソル移動、クリック、設定に基づくtrigger検出後の貼り付けを行います。
    """
    def log_result(self, transcript: str):
        """
        Process and log the recognized transcript along with performing automated cursor movement and text pasting.
        認識されたtranscriptを処理し、カーソル移動およびテキスト貼り付けの自動処理を行い、ログ出力します。
        
        1. Move the mouse cursor to the position specified in the .ccw file's cursor section and click.
           .ccwファイルのcursorに指定された位置にカーソルを移動しクリックします。
        2. If the transcript contains the keyword trigger defined in the .ccw file, remove the trigger text, then paste the remaining text to the screen and simulate an Enter key press.
           transcriptに.ccwファイルで定義されたkeywordのtriggerが含まれている場合、triggerを除去し、残りのテキストを画面に貼り付け、Enterキーをシミュレートします。
        3. Otherwise, paste the transcript text as is.
           それ以外の場合は、そのままtranscriptを画面に貼り付けます。
        
        Input:
          transcript - Recognized text from the speech service.
                       音声認識サービスからの認識結果。
        Output:
          A confirmation string indicating processing completion.
          処理完了を示す確認用の文字列を返します。
        """
        import os  # For file path operations // ファイルパス操作用
        import yaml  # For reading the configuration file // 設定ファイル読み込み用
        import pyautogui  # For automating mouse and keyboard actions // マウスとキーボード操作の自動化用
        
        # Load configuration from .ccw file in home directory // ホームディレクトリの.ccwファイルから設定を読み込みます。
        home_dir = os.path.expanduser("~")
        config_file = os.path.join(home_dir, ".ccw")
        try:
            with open(config_file, "r", encoding="utf-8") as f:
                config_data = yaml.safe_load(f)
            if not isinstance(config_data, dict):
                config_data = {}
        except Exception as e:
            config_data = {}
        
        # Retrieve cursor position from configuration, default to {"x":1880, "y":932} if missing
        # 設定からcursor位置を取得し、存在しなければデフォルト{"x":1880, "y":932}を使用します。
        cursor_val = config_data.get("cursor", {})
        if not (isinstance(cursor_val, dict) and "x" in cursor_val and "y" in cursor_val):
            cursor_val = {"x": 1880, "y": 932}
        
        # Retrieve keyword trigger from configuration, default to {"trigger": "エンター"} if missing
        # 設定からkeywordのtriggerを取得し、存在しなければデフォルト{"trigger": "エンター"}を使用します。
        keyword_val = config_data.get("keyword", {})
        if not (isinstance(keyword_val, dict) and "trigger" in keyword_val):
            keyword_val = {"trigger": "エンター"}
        trigger = keyword_val.get("trigger", "エンター")
        
        # Step 1: Move the mouse cursor to the configured cursor position and perform a click.
        # ステップ1: 設定されたcursor位置にカーソルを移動し、クリックを実行します。
        pyautogui.moveTo(cursor_val["x"], cursor_val["y"])
        pyautogui.click()
        
        # Step 2 & 3: Process the transcript based on whether it contains the trigger keyword.
        # ステップ2 & 3: transcriptがtriggerキーワードを含むか否かに基づき処理します。
        if trigger in transcript:
            # Remove trigger from transcript if present.
            # triggerが存在する場合、transcriptからtrigger文字列を除去します。
            text_to_paste = transcript.replace(trigger, "")
            try:
                import pyperclip  # For clipboard operations // クリップボード操作用
                pyperclip.copy(text_to_paste)
                pyautogui.hotkey('ctrl', 'v')
            except ImportError:
                pyautogui.write(text_to_paste)
            # Simulate pressing the Enter key after pasting.
            # 貼り付け後にEnterキーをシミュレートします。
            pyautogui.press('enter')
            triggered = True
        else:
            try:
                import pyperclip
                pyperclip.copy(transcript)
                pyautogui.hotkey('ctrl', 'v')
            except ImportError:
                pyautogui.write(transcript)
            triggered = False
        
        if triggered:
            final_message = f"Processed transcript: {transcript} (Cursor moved to {cursor_val} and processed with trigger '{trigger}')"
        else:
            final_message = f"Processed transcript: {transcript} (Cursor moved to {cursor_val} without trigger)"
        
        print(final_message)  # Display the final processed message // 最終的な処理済みメッセージを出力します。
        logger.info(final_message)
        return "Processed and pasted the result."
    

def main():
    """
    Main function to launch the Speech Recognition sample.
    ホームディレクトリ内の YAML 設定ファイル (.ccw) を読み込み、ウィンドウ位置設定に従いウィンドウを生成、
    ウィンドウ移動時に .ccw を更新し、音声認識サンプルを起動するメイン関数です。
    """
    logger.info("Starting Speech Recognition Sample using pywebview. // pywebviewを使用して音声認識サンプルを起動します。")
    
    # Load YAML configuration from the home directory (.ccw) // ホームディレクトリの .ccw ファイルから設定を読み込みます。
    try:
        import yaml  # PyYAML required // PyYAML を使用します。
        home_dir = os.path.expanduser("~")
        config_file = os.path.join(home_dir, ".ccw")
        with open(config_file, "r", encoding="utf-8") as f:
            config_data = yaml.safe_load(f)
        window_val = config_data.get("window", {})
        cursor_val = config_data.get("cursor", {})
        keyword_val = config_data.get("keyword", {})
        logger.info("Loaded config from %s", config_file)
        logger.info("Config values: window: %s, cursor: %s, keyword: %s", window_val, cursor_val, keyword_val)
        print(f"Config values - window: {window_val}, cursor: {cursor_val}, keyword: {keyword_val}")
    except Exception as e:
        logger.warning("Failed to load config: %s", e)
        window_val = {}
        cursor_val = {}
        keyword_val = {}
    
    # Retrieve window position from configuration // YAMLの設定値からウィンドウ位置 (x, y) を取得します。
    try:
        wx = int(window_val.get("x", 0))
        wy = int(window_val.get("y", 0))
    except Exception as e:
        wx = 0
        wy = 0
        logger.warning("Invalid window configuration, using default position (0,0): %s", e)
    
    # Determine the current directory and HTML/ICO file paths // 現在のディレクトリと HTML/ICO ファイルのパスを決定します。
    current_dir = os.path.dirname(os.path.abspath(__file__))
    html_file = os.path.join(current_dir, "speech.html")
    # Set application icon using mic.ico located in the same directory as speech.py
    # アプリのアイコンとして、speech.py と同じディレクトリ内の mic.ico を使用します。
    icon_file = os.path.join(current_dir, "mic.ico")
    logger.info("Loading HTML file at: %s", html_file)
    
    api = SpeechAPI()
    
    # Create a window with the positioning from the YAML configuration and custom icon.
    # YAML設定に従うウィンドウ位置および、カスタムアイコンを指定してウィンドウを作成します。
    window = webview.create_window(
        "Speech Recognition Sample",
        html_file,
        js_api=api,
        width=250,
        height=120,
        x=wx,       # X-position from YAML config // YAML設定のX座標
        y=wy,       # Y-position from YAML config // YAML設定のY座標
        resizable=False,
        on_top=True,
        # icon=icon_file  # Set the window icon // ウィンドウアイコンを設定します。
    )
    
    # Register the moved event callback using pywebview's events.
    # pywebviewの events を利用して、ウィンドウ移動イベントのコールバックを登録します。
    def on_window_moved(x, y):
        message = f"Window moved to: ({x}, {y})"
        print(message)  # Display the new window position on the console // 新しいウィンドウ位置をコンソールに出力します。
        logger.info(message)  # Log the new window position // 新しいウィンドウ位置をログに記録します。
        update_yaml_config(config_file, (x, y))  # Update the YAML config file with new position // .ccwファイルを新しい位置で更新します。
    
    window.events.moved += on_window_moved
    
    # Move the mouse pointer to (1500,700) at app startup // アプリ起動時にマウス位置を(1500,700)に移動します。
    try:
        import pyautogui  # For moving the mouse // マウス移動用
        pyautogui.moveTo(1500, 700)
    except ImportError:
        logger.warning("pyautogui is not installed, skipping mouse repositioning. // pyautoguiがインストールされていないため、マウスの再配置をスキップします。")
    
    webview.start(debug=False)
    logger.info("pywebview event loop has started. // pywebviewのイベントループが開始されました。")

if __name__ == '__main__':
    main() 