import psutil
from dataclasses import dataclass

@dataclass
class SystemStats:
  cpu_percent: float
  ram_percent: float
  ram_used_mb: int
  ram_total_mb: int

def get_system_stats() -> SystemStats:
  cpu = psutil.cpu_percent(interval=0.4)
  mem = psutil.virtual_memory()
  return SystemStats(
  cpu_percent=cpu,
  ram_percent=mem.percent,
  ram_used_mb=int(mem.used / (1024**2)).
  ram_total_mb=int(mem.total / (1024**2)),
  )
