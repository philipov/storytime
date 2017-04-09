@setlocal
@ECHO off

set REPO=%1

pushd %REPO%
echo REPO %REPO%.init =] %ADDRESS_GIT%/%REPO%.git

git init
git remote add origin %ADDRESS_GIT%/%REPO%.git
echo.

popd
endlocal
