@echo off
set /p commitMessage=Enter commit message: 
git add .
git commit -m "%commitMessage%"
git push origin main
echo Commit Complete...
Echo Exiting script...
timeout 5 >nul
exit