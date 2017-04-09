@setlocal
@ECHO off

set TARGET=%1

echo REPO %REPO%.add %TARGET%
git add %TARGET%
echo.

popd
endlocal
