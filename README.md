# OpenCL GPU Test

This project verifies GPU compute on an AMD Radeon RX 6600 using
OpenCL through Mesa Rusticl and RadeonSI.

## Hardware

- GPU: AMD Radeon RX 6600 8 GB
- GPU architecture: RDNA2 / Navi 23
- Linux kernel: 7.0.0-34-generic
- OpenCL implementation: Mesa Rusticl
- GPU driver: RadeonSI

## Python Environment

The project uses a dedicated Python virtual environment:

```text
.venv/
```

Python dependencies are installed only inside this environment.

## Dependencies

- Python 3.14
- NumPy
- PyOpenCL

## What the Test Does

`opencl_test.py`:

1. Detects the OpenCL platform.
2. Selects an OpenCL GPU device.
3. Creates an OpenCL context and command queue.
4. Creates two arrays of 1024 floating-point values.
5. Executes an OpenCL kernel that adds the arrays on the GPU.
6. Copies the result back to Python.
7. Verifies the GPU result against NumPy.

## Running the Test

The canonical way to run the project is:

```bash
./run.sh
```

The runner explicitly exposes the RX 6600 to Rusticl through RadeonSI.

For direct execution, the equivalent command is:

```bash
RUSTICL_ENABLE=radeonsi python opencl_test.py
```

A successful run should report:

```text
Platform: rusticl
Device:   AMD Radeon RX 6600 (...)
OpenCL:   OpenCL 3.0
Result correct: True
```

## Reproducible Setup

The project declares its direct Python dependencies in `requirements.txt`.

To recreate the environment in a fresh virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

Then run:

```bash
./run.sh
```

The project has been validated successfully from a fresh temporary virtual environment using the same `requirements.txt` dependencies.

## Why `RUSTICL_ENABLE=radeonsi` Is Required

On this system, Mesa Rusticl does not automatically expose the RadeonSI
GPU as an OpenCL device.

Setting:

```bash
RUSTICL_ENABLE=radeonsi
```

enables the RadeonSI backend for Rusticl for that command.

The variable is intentionally applied per command rather than being added
globally to the user shell environment.

## ROCm / HIP Note

This project uses OpenCL rather than ROCm/HIP.

The AMD Radeon RX 6600 (`gfx1032`) is not an officially supported target
in the current AMD ROCm/HIP compute support matrix being used for this
project.

Therefore, ROCm/HIP was not installed merely to force support for this GPU.

## Project Status

OpenCL GPU execution has been verified successfully on the AMD Radeon RX 6600.

The Git working tree should remain clean after running the test.
