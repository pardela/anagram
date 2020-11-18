from setuptools import setup, find_packages

setup(
    name='anagram',
    extras_require=dict(tests=['pytest']),
    packages=find_packages(where='src'),
    package_dir={"": "src"},
)

# Steps for a new project
# create project from welcome screen (or File menu)
# create setup.py file at the project level with the above code (name of the project will change!)
# create subfolder src/name of the project under project root
# create source code under that subfolder - in this case we have anagram.py
# in the terminal run "pip install -e .[tests]" to create dependencies from extras_required
# go to settings Preferences and
# under Python integrated tools menu option and choose pytest in the Testing - Default test runner
# create subfolder tests under project root
# create test code under that subfolder
# Use VCS menu to share project in GitHub
# Use vertical Commit menu to Commit and Push code
# You can do both at the same time, see drop down options in commit button