@setlocal
@ECHO off

set REPO=%1

pushd %REPO%
echo REPO %REPO%.pull

git pull

popd
endlocal
