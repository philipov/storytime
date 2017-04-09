@setlocal
@ECHO off
rem -- execute file located in omdwin\core\scripts\git,
rem -- using omdwin's parent as the working directory

pushd %~dp0
call lib\_git.cmd

pushd ..\..\..
%~dp0git\%*

popd
popd
endlocal
