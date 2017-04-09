@setlocal
@echo OFF

set COMMAND=pytest tests\%*

echo COMMAND    %COMMAND%

%COMMAND%
endlocal
