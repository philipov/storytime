@setlocal
@echo OFF


set PYTHONPATH=%PATH_SCRIPTS%..
set PYTHONHOME=C:\Anaconda3
set PATH=%PATH_SCRIPTS%;%PYTHONHOME%\Scripts;%PYTHONHOME%;%PATH%

set PATH_SCRIPTS=%~dp0
call %PATH_SCRIPTS%lib\_git.cmd
call %PATH_SCRIPTS%lib\_splitargs.cmd %*
pushd %PATH_SCRIPTS%..
call %PATH_SCRIPTS%lib\_announce.cmd

rem ToDo: pushd should be part of a script

%*

endlocal
