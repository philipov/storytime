@setlocal
@ECHO off

set MSG=%1
set REPO=%2

pushd %REPO%
echo REPO %REPO%.commit %MSG%

git commit -m %MSG%
echo.

popd
endlocal
