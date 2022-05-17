# Instructions

Mobile Developer Experience projects at Slack often involve developing solutions that integrate with remote 3rd party systems. The following exercise is based on real-world challenges that our team has had to tackle. Have fun with it and feel free to reach out with any questions!

## Given

The following files:

- `app-debug.apk`: An Android application artifact to be tested.
- `app-debug-androidTest.apk`: A test application artifact that contains tests for the application above.
- `AllTests.txt`: A List of fully-qualified instrumented test methods to execute.

## Create

- [A free account on Firebase Test Lab](https://firebase.google.com/docs/test-lab).
  - This free account will give you 15 free test runs per day.
- An executable (script or binary) that...
  - executes the given test set on [Firebase Test Lab](https://firebase.google.com/docs/test-lab) (device: `NexusLowRes`, api: `28`);
  - places the results (JUnit XML file(s)) in a top-level `test_result` directory.
- Along with your solution, please provide instructions for how to execute it (preferably a shell command).
- Feel free to use a language of your choice. We’ve found Python to be well-suited for such work and use it ourselves; however, you are welcome to work with a language that you are comfortable with and believe to be a good fit for the task.

## Submit

- Please create a `dev` branch within this repo. In your `dev` branch, work on your solution by committing with the frequency and with the type of commit messages you would write on a typical project.
- Creating a `SOLUTION.md` that gives an overview of the project and instructions on how to execute your solution is strongly encouraged.
- Once you finish, create a Pull Request against the `main` branch of this repo. We will review it as soon as possible.
- We'll execute your solution against our own Firebase account with your instructions from the repo you provide.

## What we’re looking for

- At the minimum, your solution should execute and run correctly.
- Your code should be clean, easy to follow (well-documented or self-describing). Work on this project as if you were collaborating with others and planned on maintaining it with a team in the future.
- Bonus points (aka, things that would differentiate your solution in a positive way).
- We don’t expect you to include all these items below in your implementation, but you should think about them and either leave comments where you see potential areas for improvements and/or be ready to talk about it in follow up conversations:
  - user-friendly console output
  - unit tests
  - error handling
  - extra debug information that would help developers investigate test failures
  - efficiency & scalability
  - extensibility

## Resources

Here are some resources that may be helpful in getting started:

- [Firebase Test Lab for Android](https://firebase.google.com/docs/test-lab/android/get-started)
- [Installing Google Cloud SDK](https://cloud.google.com/sdk/install)
- [Google Cloud Storage](https://cloud.google.com/storage/docs/apis)
- [Cloud testing APIs for Python](https://developers.google.com/resources/api-libraries/documentation/testing/v1/python/latest/index.html)
