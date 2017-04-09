@setlocal
@ECHO off

set REPO=%1

pushd %REPO%
echo REPO %REPO%.status

git status
echo.

popd
endlocal
