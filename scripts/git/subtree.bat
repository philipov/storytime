@setlocal
@ECHO off

set REPO=%1

echo REPO %REPO%.subtree =] %ADDRESS_GIT%/%REPO%.git
git clone %ADDRESS_GIT%/%REPO%.git
echo.

popd
endlocal
