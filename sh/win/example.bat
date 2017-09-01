@setlocal
@ECHO off
rem ---------------------------------

set THIS_PATH=%~dp0
set PROJECT_PATH=%THIS_PATH%..\..
set PROJECT_NAME=storytime

set PYTHONPATH=%PROJECT_PATH%;%PYTHONPATH%
@pushd %PATH_PROJECT%


rem ---------------------------------
where python

set CMD=python -m %PROJECT_NAME% run examples.alicebob 10
echo "CMD" %CMD%
%CMD%

rem ---------------------------------
@popd
@endlocal
