## Problem Statement

Given the following files:

- `app-debug.apk`: An Android application artifact to be tested.
- `app-debug-androidTest.apk`: A test application artifact that contains tests for the application above.
- `AllTests.txt`: A List of fully-qualified instrumented test methods to execute.
- Create a script/binary that executes the given test suite on Firebase Test Lab

## Deliverables

- An executable (script or binary) that
  - executes the given test set on [Firebase Test Lab](https://firebase.google.com/docs/test-lab) (device: `NexusLowRes`, api: `28`);
- Test results 
- Instruction to execute the script/binary
- Isues encountered and solutions
- learnings and improvements

## Pre-requisite :

- You should have `Firebase account` and created a `test lab project` [one time set up]
  - [ instruction to follow [ https://firebase.google.com/docs/test-lab/android/get-started ] 
- `google cloud SDK` is installed and set up gcloud cli tool [ one time set up]
- Authenticate your account to access firebase projects from gcloud cli utility
  - For more details please follow instructions [ https://firebase.google.com/docs/test-lab/android/command-line ]
- Python is required to run the script [ https://www.python.org/downloads/ ]
- Make sure to map/set your project correctly before executing the script
  - use "`gcloud config get project`" command to see the current mapped project
  - use "`gcloud config set project <project_name>`" to set the project you want to run the test

## Solution

- Clone the given repo or download the apk files to local system
- Run "`python run_tests.py`" with 3 arguments
  - usage : `python run_tests.py --apkfile <apk_file_path> --apktestsuite <test_apk_file_path>  --bucketname <bucketname>`
  -  help : `python run_tests.py -h or run_tests.py --help`
- you will see test run status in the console , it takes around 8-10 minutes to complete the run
- Once completed click on the bucket link provided in console to check the complete test results

## Isues encountered and solutions

1. ERROR: `(gcloud.firebase.test.android.run) [~/mobile-devx-code-exercise/app-debug.apk] not found or not accessible`
    
    - Problem : input apkfile or apktest file not fount
    - Solution : check the exact path for apk file and/or testsuite apk file. make sure to pass the correct path as argument 

2. ERROR: `(gcloud.firebase.test.android.run) Permission denied while creating bucket. Is billing enabled for project`
   
    - Problem : gcloude cli / service account doesn't have the permissions to create a bucket or we can't create own bucket for non billed projects
    - Solution : 
       - Tried many workarounds . Gave editor access to services accounts , attached new roles to service accounts
        still did not work.
       - later found from [official documentation](https://cloud.google.com/sdk/gcloud/reference/firebase/test/android/run#--results-bucket) that bucket must be owned by a billing-enabled project, and that using a non-default bucket will result in billing charges for the storage used. So for my project billing is not enabled so Permission denied while creating bucket.
    - use the default bucket provided by Firebase Test Lab to upload the test results. 

## Learning from this project

 - Thanks for providing me opportunity to learn and explore firebase test lab. First time i used the test lab and it was nice experience
 - Eventhough i am more comfortable in bash scripting , i tried to create a script using python as that is best tool to interact with cloud or working with API's. Learnt more about python doing this exercise. going forward I decide to do more of python scripting than bash
 - Faced many issues and errors while creating/testing the script and able to resolve the issues encounterd 
 - Learnt a bit of using Google Cloud and gcloud Cli tool
 - I worked on server side code most of the time , but this apk testing let me to explore some opportunites to android and ios apps.

## Improvements and future goals
 - Gain more hand-on experience on python and go programming
 - Pass “Kubernetes Certified Administrator” certification
 - Pass “AWS Certified DevOps Engineer” certification
 - Upgrade my skills on more of cloud services Ex : EKS , AWS , Terraform , ELB , cloud watch , Azure etc
 - Gain more knowledge on Networking concepts