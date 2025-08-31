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

### 参考
- [Github的王炸功能，但很少人知道怎么用？CI/CD持续集成持续部署](https://www.bilibili.com/video/BV11e411i7Xx)