@echo off
setlocal EnableDelayedExpansion

echo.
echo CMD            %ARG_FIRST%%ARG_REST%
call :createSub
call :echo "PWD            "
cd
echo.
echo SCRIPT_DIR     %PATH_SCRIPTS%
echo PYTHON         %PYTHONHOME%
echo PYTHONPATH     %PYTHONPATH%
echo GIT            %PATH_GIT%
echo PATH           %PATH%
echo.

echo ########################################################################
echo.
exit /b

:echo
> txt.tmp (echo(%~1!sub!)
copy txt.tmp /a txt2.tmp /b > nul
type txt2.tmp
del txt.tmp txt2.tmp
exit /b

:createSub
copy nul sub.tmp /a > nul
for /F %%a in (sub.tmp) DO (
   set "sub=%%a"
)
del sub.tmp
exit /b
