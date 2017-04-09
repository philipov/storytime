@setlocal
@ECHO off

set REPO=%1

pushd %REPO%
echo REPO %REPO%.push

git push -u origin master
echo.

popd
endlocal
