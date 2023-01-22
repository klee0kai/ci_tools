import os

os.environ["GITHUB_API_URL"] = "https://api.github.com"
os.environ["GITHUB_STEP_SUMMARY"] = "summary.md"
os.environ["GITHUB_ENV"] = "env.fl"
os.environ["GITHUB_REPOSITORY"] = ""

# secret data, should be override
os.environ["SECRETS_GH_API_TOKEN"] = ""

