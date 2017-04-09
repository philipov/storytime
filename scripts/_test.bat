@setlocal
@echo OFF

set COMMAND=pytest %PATH_CORE_TESTS%\%*

echo COMMAND    %COMMAND%

%COMMAND%
endlocal
