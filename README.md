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

The RX 6600 must be explicitly exposed to Rusticl through RadeonSI:

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
