# AI Replace — minimal Calibre plugin

This is a minimal example Calibre plugin that adds a single menu item called "AI Replace" to Calibre's Tools menu. When clicked it displays a simple message box.

Files:
- `action.py` — The `InterfaceAction` implementation that creates the menu item.
- `__init__.py` — Exports the action class and contains minimal metadata.

How to package and install

1. Zip the plugin folder (create a plugin archive Calibre can load):

```bash
cd /path/to/repo
zip -r ai_replace_plugin.zip ai_replace_plugin
```

2. In Calibre: Preferences → Plugins → Load plugin from file → select `ai_replace_plugin.zip`.

3. Restart Calibre if needed. The menu item will appear under the `Tools` menu as "AI Replace".

Notes
- This example assumes your Calibre has PyQt5 available (standard for Calibre).
- You can change the displayed text or connect the action to more complex logic by editing `action.py`.
