@setlocal
@ECHO off

echo REPO init =] %ADDRESS_GIT%/%REPO%.git

git init
git remote add origin %ADDRESS_GIT%/storytime.git
echo.

popd
endlocal
