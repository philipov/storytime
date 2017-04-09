@setlocal
@ECHO off
set REPO=%1
pushd ../../%REPO%

git pull

popd
endlocal
