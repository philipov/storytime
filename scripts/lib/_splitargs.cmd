@ECHO off

rem # Chop off the first argument
set ARG_FIRST=%1

rem # Everything after the first argument
set ARG_REST=
shift
:loop1
if "%1"=="" goto after_loop
set ARG_REST=%ARG_REST% %1
shift
goto loop1
:after_loop

