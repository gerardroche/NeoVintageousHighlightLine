# NeoVintageous Highlight Line Management

Achieve a seamless writing and editing experience with NeoVintageous Highlight Line Management. This Sublime Text plugin ensures that the highlight line gracefully deactivates when you enter Insert mode or Visual mode, allowing you to focus on your content without distraction. This refined functionality is made possible by [NeoVintageous](https://github.com/NeoVintageous/NeoVintageous), a robust Vim emulator plugin designed specifically for Sublime Text.

## Installation

### Method 1: Using Package Control

1. Open Sublime Text.
2. Press `Ctrl+Shift+P` (Windows/Linux) or `Cmd+Shift+P` (macOS) to open the Command Palette.
3. Type "Package Control: Install Package" and press `Enter`.
4. In the input field, type "NeoVintageousHighlightLine" and select it from the list of available packages.

### Method 2: Manual Installation

1. Visit the [NeoVintageousHighlightLine GitHub repository](https://github.com/gerardroche/NeoVintageousHighlightLine).
2. Click on the "Code" button and select "Download ZIP."
3. Extract the downloaded ZIP file.
4. Open Sublime Text and go to `Preferences -> Browse Packages...` to open the Packages folder.
5. Copy the "NeoVintageousHighlightLine" folder from the extracted ZIP and paste it into the Packages folder.

### Method 3: Manual Git Repository Installation

1. Open a terminal or command prompt.
2. Navigate to the Sublime Text Packages directory:
    - On Windows: `%APPDATA%\Sublime Text\Packages`
    - On macOS: `~/Library/Application Support/Sublime Text/Packages`
    - On Linux: `~/.config/sublime-text/Packages`
3. Clone the plugin repository directly into the Packages directory using Git:
   ```
   git clone https://github.com/gerardroche/NeoVintageousHighlightLine.git NeoVintageousHighlightLine
   ```

## Unleash the Power of Highlighted Lines

Take control of your editing environment with these convenient commands:

| Command                   | Alias             | Description
| :-------------------------| :-----------------| :----------
| `yoc`                     | `coc`             | Toggle the highlight line using the Unimpaired plugin.

## License

Released under the [GPL-3.0-or-later License](LICENSE).
