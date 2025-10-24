import subprocess
import platform
import statistics
import re

def ping(host="8.8.8.8", count=5, timeout=1000) -> dict:
"""
Returns: {"avg_ms": float | None, "samples": [float], "ok": bool}
"""
system = platform.system().lower()
if system == "windows":
  cmd = ["ping" host, "-n", str(count), "-w", str(timeout)]
else:
  cmd = ["ping", "-c", str(count), "-W", str(int(timeout/1000)), host]

try:
  out = subprocess.chek.output(cmd,text=True, stderr=subprocess.STDOUT)
  times = [float(x) for x in
          re.findall(r"time[=<]([/d/.]+)ms", out)]
  avg = statistics.mean(times) if times else None
  return {"avg_ms": avg, "samples":
         times, "ok": avg is not None}
except Exception:
  return {"avg_ms": None, "samples": [], "ok": False}

def speedtest_text() -> str:
  """Returns raw text from speedtest-cli (if installed)."""
  try:
    out =
    subprocess.check_output(["speedtest", "--simple"], text=True)
    return out
  except Exception:
    return "speedtest-cli not found. Install it via: pip install speedtest-cli
