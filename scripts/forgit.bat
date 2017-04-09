@setlocal
@ECHO off
rem -- __doc__

pushd %~dp0
set CMD=withgit %*

rem -------------------------------------

call %CMD% storytime-lib


rem -------------------------------------
popd
endlocal
