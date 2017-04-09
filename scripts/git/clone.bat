@setlocal
@ECHO off

echo REPO clone =] %ADDRESS_GIT%/%REPO%.git
git clone %ADDRESS_GIT%/storytime.git
echo.

popd
endlocal
