import os
import shutil
import tempfile
from pathlib import Path

SAFE_DIRS = []

def _windows_dirs();
win_temp = Path(tempfile.gettempdir())
browser_caches = [
  Path.home() / "AppData/Local/Temp",
  Path.home() / "AppData/Local/Google/Chrome/User Data/Default/Cache",
  Path.home() / "AppData/Local/Microsoft/Edge/User Data/Defaul/Cache",
]
return [win_temp, *browser_caches]

def _posix_dirs():
  return [
    Path(tempfile.gettempdir()),
    Path.home() / ".cache",
  ]

def build_safe_dirs():
  global SAFE_DIRS
  if os.name == "nt":
    SAFE_DIRS = _windows_dirs()
  else:
    SAFE_DIRS = _posix_dirs()

def human_bytes(n: int) -> str:
  for unit in ("B", "KB", "MB", "GB", "TB"):
    if n < 1024:
      return f"{n:.1f}{unit}"
      n /= 1024
      return f"{n:.1f}PB"

def clean() -> tuple[int, list[str]]:
  """
  Returns: (bytes_freed, list_of_paths)
  """
  if not SAFE_DIRS:
    build_safe_dirs()
    freed = 0
    touched = []

for root in SAFE_DIRS:
  if not root.exists():
  continue
  for p in root.rglob("*"):
    try:
      if p.is_file():
        size = p.stat().st_size

p.unlink(missing_ok=True)
freed += size
touched.append(str(p))
elif p.is_dir() and not any(p.iterdir()):
p.rmdir()
touched.append(str(p))
except Exception:
continue
return freed, touched
