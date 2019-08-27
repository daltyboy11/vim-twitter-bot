#!/bin/bash - 
#===============================================================================
#
#          FILE: upload.sh
# 
#         USAGE: ./upload.sh 
# 
#   DESCRIPTION: Uploads a new revision of the vim-twitter-bot lambda function to
#                aws lambda
# 
#       OPTIONS: ---
#  REQUIREMENTS: ---
#          BUGS: ---
#         NOTES: ---
#        AUTHOR: Dalton Sweeney
#  ORGANIZATION:
#       CREATED: 23/08/2019 21:54
#      REVISION: 1.0 
#===============================================================================

set -o nounset                              # Treat unset variables as an error

TARGET_DIR="./package"
PYTHON_CFG="/Users/daltyboy11/.pydistutils.cfg"
REQUIREMENTS="requirements.txt"
ZIP_NAME="function.zip"
FUNCTION_NAME="function.py"

rm $ZIP_NAME
rm -r $TARGET_DIR

### Install dependencies to ./package
echo [install] > $PYTHON_CFG
echo prefix= >> $PYTHON_CFG

pip3 install --target $TARGET_DIR python-twitter

rm $PYTHON_CFG

### zip archive and dependencies
cd $TARGET_DIR
zip -r9 ${OLDPWD}/$ZIP_NAME .

### add function to archive
cd ${OLDPWD}
zip -g $ZIP_NAME $FUNCTION_NAME

### upload to aws
aws lambda update-function-code --function-name twitter_bot_action --zip-file fileb://$ZIP_NAME
