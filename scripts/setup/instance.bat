@setlocal
@ECHO off
set REPO=%1
pushd %REPO%
echo %REPO%
git init
echo.

popd
endlocal
