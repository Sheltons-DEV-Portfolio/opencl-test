import os
import subprocess
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SCRIPT = PROJECT_ROOT / "opencl_test.py"


def test_opencl_gpu_execution():
    environment = os.environ.copy()
    environment["RUSTICL_ENABLE"] = "radeonsi"

    result = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=PROJECT_ROOT,
        env=environment,
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode == 0, result.stderr
    assert "Platform: rusticl" in result.stdout
    assert "Device:   AMD Radeon RX 6600" in result.stdout
    assert "Result correct: True" in result.stdout
