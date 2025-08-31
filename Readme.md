## Github Acton

### Build
- cmake -B build -G Ninja -DCMAKE_BUILD_TYPE=Release
- cmake --build build --config Release

### Push
- git tag v1.0.0
- git push origin v1.0.0
- git push origin master
- add
    - git add -A . 
    - git commit -m "message"

### 触发条件
```yml
# 当 push tag为 v1.xx时候
on:
  push:
    tags:
      - "v*"

# 手动触发
on: workflow_dispatch 
```

### 参考
- [Github的王炸功能，但很少人知道怎么用？CI/CD持续集成持续部署](https://www.bilibili.com/video/BV11e411i7Xx)

## Build C++

### vcpkg
- git submodule add https://github.com/microsoft/vcpkg.git vcpkg
- git submodule update --init --recursive
- vcpkg.json|manifest mode
  - 只能使用配置json来安装
  - 直接vcpkg install 直接安装vcpkg.json的依赖文件
```yml
name: Windows CI with vcpkg

on:
  push:
    tags: ["v*"]          # 也可以改成 push / pull_request

env:
  # 让 vcpkg 把编译好的二进制缓存到 GitHub Actions Cache，二次构建秒过
  VCPKG_BINARY_SOURCES: "clear;x-gha,readwrite"

jobs:
  build:
    runs-on: windows-latest

    steps:
    - uses: actions/checkout@v4
      with:
        submodules: recursive     # 拉取 vcpkg 子模块

    - name: Setup MSVC
      uses: ilammy/msvc-dev-cmd@v1

    # 官方 action：自动装缓存、自动 bootstrap vcpkg
    - name: Restore vcpkg & install ports
      uses: lukka/run-vcpkg@v11
      with:
        vcpkgJsonGlob: 'vcpkg.json'   # 指定 manifest 文件
        # 其余参数全默认即可

    - name: Configure CMake
      run: >
        cmake -B build -G Ninja
        -DCMAKE_BUILD_TYPE=Release
        -DCMAKE_TOOLCHAIN_FILE=${{ github.workspace }}/vcpkg/scripts/buildsystems/vcpkg.cmake

    - name: Build
      run: cmake --build build --config Release

    - name: Upload artifact
      uses: actions/upload-artifact@v4
      with:
        name: demo-win64
        path: build/Release/demo.exe
```

### tbb
- vcpkg install tbb:x64-windows | 默认安装动态库
- vcpkg install tbb:x64-windows-static

### OpenVDB
```json
{
  "name": "app_vdb",
  "version": "1.0.0",
  "dependencies": [
    "zlib",
    "libpng",
    "openexr",
    "tbb",
    "gtest",
    "cppunit",
    "blosc",
    "glfw3",
    "glew",
    "python3",
    "jemalloc",
    "boost-iostreams",
    "boost-interprocess",
    "boost-algorithm",
    "nanobind"
  ]
}
```