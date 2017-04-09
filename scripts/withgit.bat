@setlocal
@ECHO off
rem -- execute file located in omdwin\core\scripts\git,
rem -- using omdwin's parent as the working directory

call %~dp0lib\_git.cmd
echo abc
set PATH=%~dp0git;%PATH%
echo def
pushd %~dp0..

%*

popd
endlocal
