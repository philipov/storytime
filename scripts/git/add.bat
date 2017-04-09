@setlocal
@ECHO off

set TARGET=%1
set REPO=%2

pushd %REPO%
echo REPO %REPO%.add %TARGET%

git add %TARGET%
echo.

popd
endlocal
