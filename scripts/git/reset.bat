@setlocal
@ECHO off

set REPO=%1

pushd %REPO%
echo REPO %REPO%.reset

git reset
echo.

popd
endlocal
