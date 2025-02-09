# WebView & 音声認識 アプリケーション仕様書  
# WebView & Speech Recognition Application Specification

## 1. 概要 (Overview)  
本アプリケーションは、音声認識サンプルを提供するために、pywebview を利用し WebView ウィンドウを表示します。  
ユーザーが WebView 内のボタン操作を行うと、JavaScript から Python API が呼び出され、認識された音声メッセージに対して以下の自動化処理を実施します。  

This application provides a speech recognition sample using a pywebview-based window.  
When a button in the WebView is clicked, a JavaScript call invokes a Python API to process the recognized speech message through a series of automated steps.

- **音声認識メッセージ処理**:  
  - `.ccw` ファイルから設定情報（ウィンドウ位置、カーソル位置、キーワード trigger）を読み込み、  
  - `pyautogui` によって指定されたカーソル位置までマウスを移動・クリック、  
  - 認識メッセージに設定された trigger キーワード（例: 「エンター」）が含まれている場合、当該文字列を除去した上で画面にペーストし、Enter キーをシミュレート、  
  - 含まれていない場合はそのまま貼り付けを実施します。

The recognized speech message is processed as follows:
- Load configuration settings (window position, cursor position, keyword trigger) from the `.ccw` file.
- Use `pyautogui` to move the mouse to the configured cursor position and perform a click.
- If the recognized message contains the configured trigger keyword (e.g., "エンター"), remove the trigger text, paste the remaining text, and simulate an Enter key press.
- Otherwise, paste the recognized message as is.

また、WebView ウィンドウの移動が発生した場合は、移動後のウィンドウ位置が `.ccw` ファイルに更新され、既存のカーソルおよびキーワード設定が保持されます。  
In addition, if the WebView window is moved, its new position is updated in the `.ccw` file while preserving the existing cursor and keyword configurations.

---

## 2. 機能仕様 (Functional Specification)  

### 2.1 WebView ウィンドウ / WebView Window  
- **表示**: ウィンドウは常に最前面に表示 (on_top=True)  
  (Displayed as a topmost window.)
- **ファイル読み込み**: ローカルの `speech.html` をロード  
  (Loads the local file `speech.html`.)
- **API連携**: WebView 内のボタンから JavaScript 経由で Python API を呼び出す  
  (Invoked via a button in the WebView page that calls the Python API through JavaScript.)

### 2.2 音声認識メッセージの自動処理 / Automated Speech Recognition Message Processing  
- **設定ファイル**: ユーザーのホームディレクトリに配置される `.ccw` ファイルから、以下の情報を取得  
  - `window`: ウィンドウの初期位置  
  - `cursor`: クリックおよび貼り付けの操作位置  
  - `keyword`: 認識メッセージ内のトリガー文字列（例：エンター）  
- **処理手順**:
  1. **カーソル移動とクリック**:  
     `pyautogui` を用い、`.ccw` の `cursor` に指定された位置へ移動しクリック  
     (Move the mouse to the cursor position specified in the `.ccw` file and click.)
  2. **テキスト処理と入力**:  
     - 認識メッセージにキーワード trigger が含まれている場合、当該文字列を削除し、残りのテキストをクリップボード経由または直接貼り付け、続いて Enter キーをシミュレート  
     - キーワードが含まれていなければ、そのまま貼り付け  
     (If the recognized message contains the trigger keyword, remove it, paste the remaining text, and then simulate pressing Enter. Otherwise, paste the text as is.)
  3. **ログ出力**:  
     各処理の結果はログに記録される  
     (All processing results are logged.)

### 2.3 ウィンドウ位置の更新 (Window Position Update)  
- WebView ウィンドウが移動した場合、新しい位置が `.ccw` ファイルの `window` として更新され、`cursor` と `keyword` の情報は保持  
  (When the WebView window is moved, the new position is saved in the `.ccw` file while preserving the cursor and keyword information.)

---

## 3. 使用技術 (Technologies)  
- **pywebview**: WebView ウィンドウの表示  
- **pyautogui**: マウス操作・クリック、キーボード入力の自動化  
- **pyperclip**: クリップボード操作（貼り付け対応）  
- **PyYAML**: `.ccw` 設定ファイルの読み書き  
- **Logging**: システム情報のログ出力

---

## 4. インストール手順 (Installation Steps)  
1. 必要なライブラリのインストール:
    ```sh
    pip install pywebview pyautogui pyperclip pyyaml
    ```
2. プロジェクト内に `speech.html` を配置  
   (Place `speech.html` in the project directory.)
3. ユーザーのホームディレクトリに `.ccw` 設定ファイルを作成・配置  
   (Create and place the `.ccw` configuration file in the user's home directory.)

### `.ccw` ファイルの例 / Example `.ccw` File  
```yaml
# Window configuration // ウィンドウの設定
window:
    x: 1500   # X position // X座標
    y: 10     # Y position // Y座標

# Cursor configuration // カーソルの設定
cursor:
    x: 1877   # Cursor X position // カーソルのX座標
    y: 932    # Cursor Y position // カーソルのY座標

# Keyword configuration // キーワードの設定
keyword:
    trigger: "エンター"  # Activation keyword // 起動キーワード
```

---

## 5. 動作フロー (Operation Flow)  
1. アプリ起動時、WebView ウィンドウが最前面 (on_top=True) で表示され、`speech.html` がロードされる。  
   (At startup, the WebView window is displayed on top and `speech.html` is loaded.)
2. WebView 内のボタンがクリックされると、JavaScript により Python API が呼び出され、認識メッセージが送信される。  
   (When the button in the WebView is clicked, the Python API is called with the recognized speech message.)
3. API は `.ccw` ファイルから各種設定を読み込み、以下の処理を実施する：  
   - カーソル位置まで移動しクリック  
   - 認識メッセージ内に trigger が含まれる場合はその文字列を除去し、テキストの貼り付けと Enter キーをシミュレート  
   - 含まれない場合はそのままテキストを貼り付ける  
4. ウィンドウ移動が検知された場合、移動先の位置が `.ccw` ファイルへ更新される。  
   (If the window is moved, the new window position is updated in the `.ccw` file.)

---

## 6. 拡張機能（今後の改善点） (Future Improvements)  
- 高度な音声認識エンジンの統合  
- GUI による設定ファイル編集機能の追加  
- 自動フォーカス回復やその他ウィンドウ管理機能の拡充  
- 認識メッセージに対する文字列処理の精度向上

---

## 7. 注意点 (Cautions)  
- `pyautogui` およびキーボード・マウス操作は OS や環境依存のため、位置調整が必要な場合があります。  
- `.ccw` 設定ファイルの形式に準拠した正しい設定が求められます。  
- 認識結果のテキスト加工時、余分なスペースや不要な文字が付加される可能性があるため注意が必要です。

