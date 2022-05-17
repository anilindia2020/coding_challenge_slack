# This script initiates the test suite execution in the Firebase test lab and stores result in the user given bucket
#
# pre-requisite :
# 1. You should have created Firebase account and created a test lab project [one time set up]
# instruction to follow [ https://firebase.google.com/docs/test-lab/android/get-started ]
# 2. Make sure google cloud SDK is installed which contains gcloud cli tool [ one time set up]
# for more details pls follow [ https://firebase.google.com/docs/test-lab/android/command-line ]
# 3. Make sure to map/set your project correctly before executing the script 
# use "gcloud config get project" to see the current mapped project
# use "gcloud config set project <project_name>"
#
# Run "python run_tests.py" with 3 arguments
#  - usage : `python run_tests.py --apkfile <apk_file_path> --apktestsuite <test_apk_file_path>  --bucketname <bucketname>`
#  -  help : `python run_tests.py -h or run_tests.py --help`
#############################################################################################################################

#import the required packages
import os
import argparse
#parsing the arguments entered from user
parser = argparse.ArgumentParser()
parser.add_argument('--apkfile', type=str, required=True , help='apk file path')
parser.add_argument('--apktestsuite', type=str, required=True , help='apk test suite file path')
parser.add_argument('--bucketname', type=str, required=True , help='your gcloud bucket name')
args = parser.parse_args()
# setting up the apkfile path , test suite apk path and bucketid
apk_file_path= args.apkfile
testsuite_apk_file_path= args.apktestsuite
bucket_name= args.bucketname

#command to execute the test case remotely via cli
cmd = f"gcloud firebase test android run --results-bucket=gs://{bucket_name} --results-dir=test_result --type instrumentation --app {apk_file_path} --test {testsuite_apk_file_path} --device model=NexusLowRes,version=28"

#making sure from user before executing the tests
user_input = input(f'\n Ready for test suite execution ? Please confirm : yes/no \n')

if  user_input.upper() == "YES":
    try:
        os.system(cmd)
    except Exception as run_error:
        print (run_error)
else:
    print('Exiting...')
    exit()