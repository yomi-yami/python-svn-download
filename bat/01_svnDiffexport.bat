@ echo off

cd /d %~dp0

rem 9����ŐV�܂ł��擾
rem svn.exe �`�F�b�N�A�E�g 8:HEAD upload_files

rem 9�̕ύX�����擾
rem svn.exe �`�F�b�N�A�E�g 8:9 upload_files
rem svn.exe �`�F�b�N�A�E�g 9 upload_files

svn.exe �`�F�b�N�A�E�g 8 2.2.000.000

svn.exe �`�F�b�N�A�E�g 9 2.3.000.000

pause