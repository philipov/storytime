@setlocal
@ECHO off

set REPO=%1

pushd %REPO%
echo REPO %REPO% remove .git directory

rmdir /S/Q .git
echo.

popd
endlocal
