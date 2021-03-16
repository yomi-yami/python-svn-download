@ echo off

cd /d %~dp0

rem 9から最新までを取得
rem svn.exe チェックアウト 8:HEAD upload_files

rem 9の変更分を取得
rem svn.exe チェックアウト 8:9 upload_files
rem svn.exe チェックアウト 9 upload_files

svn.exe チェックアウト 8 2.2.000.000

svn.exe チェックアウト 9 2.3.000.000

pause