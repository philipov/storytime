@setlocal
@ECHO off
rem -- execute command using this script's path as the working directory
rem -- call utilities to prepare omd environment, as a dev environment
rem -- use below environment variables to override default configuration

set OMD_VERSION=
set PATH_DATA=
set PATH_LOGS=

@pushd %~dp0

call lib\_git.cmd
call lib\_setenv_dev.cmd %~dp0
call lib\_splitargs.cmd %*
call lib\_announce.cmd

%*

@ECHO on
@endlocal
