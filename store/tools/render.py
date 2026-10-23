"""Renders an HTML file to a PNG with headless Edge/Chrome (no extra dependencies)."""
import subprocess
import sys
import tempfile
from pathlib import Path

BROWSERS = [
    r'C:\Program Files\Google\Chrome\Application\chrome.exe',
    r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe',
]


def render(html_file, out_png, width, height):
    exe = next(b for b in BROWSERS if Path(b).exists())
    out = Path(out_png)
    out.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory() as profile:
        cmd = [
            exe, '--headless=new', '--disable-gpu', '--no-sandbox', '--hide-scrollbars',
            f'--user-data-dir={profile}', '--force-device-scale-factor=1',
            '--default-background-color=FFFFFFFF',
            f'--window-size={width},{height}', f'--screenshot={out}',
            Path(html_file).resolve().as_uri(),
        ]
        subprocess.run(cmd, check=True, capture_output=True, timeout=120)
    return out


if __name__ == '__main__':
    render(sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4]))
