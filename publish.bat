cls
@echo off

if "%1" == "" ( 
    echo Git publish script version 1
    echo Usage : publish.bat [comments without quotes]
    goto :end
)

git add *
git commit -a -m "%*"
git push origin master

:end
echo Done

