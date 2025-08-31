import sys, os, subprocess

paks = ["openvdb", "tbb"]


def main2():
    print(">>> args", *sys.argv[1:])

    if len(sys.argv) > 1:
        root = sys.argv[1]
        exe = os.path.abspath(f"{root}/vcpkg.exe")
        if os.path.exists(exe):
            print(f">>> find {exe} ...")
            for p in paks:
                subprocess.run([exe, "install", p], shell=False)
        else:
            raise RuntimeError(f">>> vcpkg.exe not find...")
    else:
        raise RuntimeError(">>> args error...")


def main():
    print(">>> args", *sys.argv[1:])

    if len(sys.argv) > 1:
        root = sys.argv[1]
        files = os.listdir(root)
        for f in files:
            print(f)
    else:
        raise RuntimeError(">>> args error...")


main()
