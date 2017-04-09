@setlocal
@ECHO off

set FILE=%1
set REPO=%2

pushd %REPO%
echo REPO %REPO%.rm %FILE%

git rm --cached %FILE%

popd
endlocal

