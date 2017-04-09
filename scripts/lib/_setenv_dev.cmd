rem --- Configure Environment -- v0.3

rem   Define the path structure of your project and dependency stack here
rem   Dependencies may have additional environment variables to configure
rem   Set the following before calling _setenv to pass arguments:
rem      OMD_VERSION             - one tick version
rem      PATH_DATA               - database storage root
rem      PATH_LOGS               - log storage root
rem   Otherwise, default values are used.


rem ####################################################

rem ####################################################
rem - Scripts -

set PATH_PACKAGE_ROOT=%1
set PATH_PACKAGE_ROOT=%PATH_PACKAGE_ROOT:~0,-1%

rem - Install Directory is 2 folders above the script path
call :setPATH_ROOT %PATH_PACKAGE_ROOT%..
call :setPATH_ROOT %PATH_ROOT%..

rem remove final slash

rem #############################
rem - Data Storage -



rem ####################################################

rem ####################################################
rem - Python Configuration -


set PATH_PYTHON=C:\Python34

set PYTHONHOME=%PATH_PYTHON_BASE%

rem - Locations of Python Packages -
rem set PYTHONPATH=%PYTHONPATH%;%PATH_TESTS%
set PYTHONPATH=%PYTHONPATH%;%PATH_PYTHON%\Lib
rem set PYTHONPATH=%PYTHONPATH%;%PATH_PYTHON%\Lib\site-packages


rem ####################################################

set PATH_GIT=C:\Program Files\Git\cmd

rem ####################################################
rem - Construct Executables Paths -

set Path=%PATH_OMD_BIN%
set Path=%Path%;%PATH_PYTHON%

rem ####################################################
goto :eof


rem - Call macro to set PATH_ROOT, the installation directory -
rem   passing %dir%.. as the first parameter indicates 2 directories above dir
rem   dir should have a final slash. The last character is deleted
:setPATH_ROOT
set PATH_ROOT=%~dp1
set PATH_ROOT=%PATH_ROOT:~0,-1%

goto :eof

rem ToDo: call macro to set value only if not existing
rem ToDo: call macro for if-then-else
