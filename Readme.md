### Build
- cmake -B build -G Ninja -DCMAKE_BUILD_TYPE=Release
- cmake --build build --config Release

### Push
- git tag v1.0.0
- git push origin v1.0.0