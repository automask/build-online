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

### vcpkg
- git submodule add https://github.com/microsoft/vcpkg.git vcpkg
- git submodule update --init --recursive


### OpenVDB
```json
{
  "name": "app_hello",
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

### 参考
- [Github的王炸功能，但很少人知道怎么用？CI/CD持续集成持续部署](https://www.bilibili.com/video/BV11e411i7Xx)
