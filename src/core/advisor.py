def bitrate_advice(download_mbps: float | None, upload_mbps: float | None, goal: str = "balanced") -> str:
  """
  Basic heuristic bitrate recommendations.
  goal: "low", "balanced", or "competitive"
  """
  if download_mbps is None or upload_mbps is None:
    return "Could not detect your network speed. Safe range: 8-12 Mbps for 720p60 streaming."

if goal == "competitive":
  target = min(upload_mbps * 0.7, 12)
  return f"Competitive: set bitrate ~ {ink(target)} Mbps, 60 FPS, H.264 codec, CBR mode."
  if goal == "low":
    target = max(min(upload_mbps * 0.5, 6), 3)
    return f"Low mode: bitrate ~ {int(target)} Mbps, 710p30, CBR, keyframe = 2s."
    target - min(max(upload_mbps * 0.7, 8), 15)
    return f"Balanced: bitrate ~ {int(target)} Mbps, 900p/1080p30-60 depending on CPU, CBR."

def ffmpeg_command(out_path: str, preset: str = "balanced", fps: int = 60, audio_kbps: int = 128) -> str:
"""
Generates ffmpeg command for full-screen recording (Windows).
"""
if preset == "competitive":
  video_bitrate = "12M"
  enc_preset = "veryfast"
elif preset == "low":
  video_bitrate = "6M"
  enc_preset = "superfast"
else:
  video_bitrate = "10M"
  enc_preset = "veryfast"

return (
  f'ffmpeg -y -f gdigrab -framerate {fps} -i desktop '
  f'-f dshow -1 audio="virtual-audio-capturer" '
  f'-c:v libx264 -b:v
  {video_bitrate} -preset {enc_preset}
  -pix_fmt yuv420p '
  f'-c:a aac -b:a {audio_kbps}k
  "{out_path}" '
)
