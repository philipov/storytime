@setlocal
@ECHO off

set MSG=%1

echo git commit -m %MSG%
git commit -m %MSG%
echo.

popd
endlocal
