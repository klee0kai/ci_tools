import os

os.environ["GITHUB_API_URL"] = "https://api.github.com"
os.environ["GITHUB_STEP_SUMMARY"] = "summary.md"
os.environ["GITHUB_ENV"] = "env.fl"

# secret data, should be override
os.environ["GITHUB_API_TOKEN"] = ""
os.environ["GITHUB_REPOSITORY"] = ""

