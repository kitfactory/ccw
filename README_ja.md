# CCW (Counter Clock Wise) 🎤🚀

CCWは **Cursor, Cline, Windsurf** の頭文字を取った名称であり、このソフトウェアは無料で音声入力を連続的に行い、テキスト入力の自動化やユーザーインターフェース操作を支援するツールです。

## 概要 🔍
- **ソフトウェア名称:** CCW (Counter Clock Wise)  
  *CCWはCursor、Cline、Windsurfを意味します。*
- **操作概要:**  
  - **起動方法:** コマンドラインで `ccw` コマンドを実行して起動します。
  - **WebView起動:** WebViewウィンドウが起動され、音声認識のためにSpeech APIが有効化されます。
  - **連続音声入力:** 画面上部で連続的に音声入力が行われます。
  - **テキスト入力支援:** 認識されたテキストは、設定ファイルに指定された場所に自動的に貼り付けられます。
  - **トリガーワードによる改行:** 音声入力に指定のトリガーワード（例：「エンター」）が含まれている場合、その文字列を削除し、改行（Enterキーのシミュレーション）を実行します。

## 特徴 🔥✨
- **音声認識の統合**  
  本ソフトウェアは堅牢な音声認識エンジンを使用しており、必要な許可を取得した上で利用可能です。  
  *The application is built with a robust speech recognition engine and uses it with all necessary permissions obtained.*
- **UI操作の自動化**  
  `pyautogui` により、カーソル移動、クリック、テキスト貼り付けの操作が自動的に実行されます。  
  *Uses pyautogui to automatically move the mouse, click at a configured position, and paste recognized text.*
- **柔軟な設定管理**  
  ホームディレクトリに配置する `.ccw` ファイルにより、ウィンドウ位置、カーソル位置、そしてキーワード（trigger）を管理します。**すべての項目は正常な動作のために維持する必要があります。**  
  *Essential settings (window position, cursor position, and keyword trigger) are managed via a .ccw file located in your home directory. All sections must be preserved for proper operation.*
- **無料で利用可能**  
  無料で音声認識を用いた連続入力の機能をお楽しみいただけます！  
  *Enjoy the power of continuous voice input without any cost!*

## 使用技術 🛠️
- **pywebview:** WebViewベースのインターフェース表示  
  *For displaying a WebView-based interface.*
- **pyautogui:** マウス・キーボード操作の自動化  
  *For automating mouse and keyboard operations.*
- **pyperclip:** クリップボード操作  
  *For clipboard functionalities.*
- **PyYAML:** 設定ファイルの管理  
  *For managing configuration files.*
- **Python:** 主な開発言語  
  *The primary programming language.*

## 始め方 🚀
1. 必要なライブラリをインストールします:
    ```sh
    pip install ccw
    ```
2. **設定ファイル (.ccw):**  
   ホームディレクトリにある `.ccw` ファイルを以下のセクションで作成または更新してください。**すべてのセクションは正常な動作のために維持する必要があります。**  
   *Create or update the .ccw file in your home directory with the following sections. All sections must be preserved for proper operation.*
   
   - **ウィンドウ設定:**  
     WebView の初期位置を指定します。  
     *Specifies the initial window position of the WebView.*
     ```yaml
     window:
         x: 1500   # ウィンドウのX座標 (初期位置) // Initial window X-coordinate
         y: 10     # ウィンドウのY座標 (初期位置) // Initial window Y-coordinate
     ```
     
   - **カーソル設定:**  
     自動クリックや貼り付け動作で使用するカーソルの位置を指定します。  
     *Specifies the cursor position used for automated mouse movement, click, and paste actions.*
     ```yaml
     cursor:
         x: 1877   # カーソルのX座標 // Cursor X position
         y: 932    # カーソルのY座標 // Cursor Y position
     ```
     
   - **キーワード設定:**  
     認識された音声メッセージ中で使用するトリガーキーワード（例：「エンター」）を指定します。  
     このキーワードが含まれている場合、該当部分が削除され、残りのテキストが貼り付けられた後、Enterキーがシミュレーションされます。  
     *Specifies the trigger keyword used in the recognized speech message. If the recognized message contains this trigger (e.g., "エンター"), the trigger is removed, the remaining text is pasted, and an Enter key is simulated.*
     ```yaml
     keyword:
         trigger: "エンター"  # 認識メッセージ処理用トリガー // Trigger keyword for processing the recognized text
     ```

3. アプリケーションを起動し、音声コマンドによるシームレスな操作をお楽しみください！  
   *Launch the application and enjoy seamless voice command control!*

## 許可について 📜
本ソフトウェアは音声認識技術を利用しており、必要な許可を取得してその機能を実装しています。  
*This software uses voice recognition technology and all necessary permissions have been obtained for its operation.*

---

この素晴らしいツールをぜひご利用ください！ 😄🎉✨  
*Have fun using this awesome tool!*

# ICON
https://www.flaticon.com/free-icon/mic_4787623?related_id=4787614&origin=search 