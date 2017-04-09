@setlocal
@pushd %~dp0
@ECHO off

set PATH_THIS=%~dp0
set PATH_CORE_SCRIPTS=platform\scripts

set ENV_NAME=%1
set GIT_HOST=

rem git clone %GIT_HOS%/omd-env-%ENV_NAME%
rem python env\%ENV_NAME%\setup.py install

@popd
@endlocal
