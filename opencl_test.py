import numpy as np
import pyopencl as cl


KERNEL = """
__kernel void add(
    __global const float *a,
    __global const float *b,
    __global float *c
)
{
    int i = get_global_id(0);
    c[i] = a[i] + b[i];
}
"""

def main():
    platforms = cl.get_platforms()
    platform = platforms[0]

    devices = platform.get_devices(device_type=cl.device_type.GPU)
    if not devices:
        raise RuntimeError("No OpenCL GPU device found.")

    device = devices[0]

    print(f"Platform: {platform.name}")
    print(f"Device:   {device.name}")
    print(f"OpenCL:   {platform.version}")

    context = cl.Context([device])
    queue = cl.CommandQueue(context)

    a = np.arange(1024, dtype=np.float32)
    b = np.full(1024, 2.0, dtype=np.float32)
    result = np.empty_like(a)

    memory_flags = cl.mem_flags

    a_buffer = cl.Buffer(
        context,
        memory_flags.READ_ONLY | memory_flags.COPY_HOST_PTR,
        hostbuf=a,
    )

    b_buffer = cl.Buffer(
        context,
        memory_flags.READ_ONLY | memory_flags.COPY_HOST_PTR,
        hostbuf=b,
    )

    result_buffer = cl.Buffer(
        context,
        memory_flags.WRITE_ONLY,
        result.nbytes,
    )

    program = cl.Program(context, KERNEL).build()

    program.add(
        queue,
        (1024, ),
        None,
        a_buffer,
        b_buffer,
        result_buffer,
    )

    cl.enqueue_copy(queue, result, result_buffer).wait()

    correct = np.allclose(result, a + b)

    print(f"Result correct: {correct}")
    print(f"First 5 results: {result[:5]}")
    print(f"Last 5 results:  {result[-5:]}")

    if not correct:
        raise RuntimeError("OpenCL computation produced an incorrect result.")

if __name__ == "__main__":
    main()
