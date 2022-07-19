<img src="https://raw.githubusercontent.com/heartexlabs/label-studio/master/images/ls_github_header.png"/>


## What is Label Studio?

Label Studio is an open source data labeling tool. It lets you label data types like audio, text, images, videos, and time series with a simple and straightforward UI and export to various model formats. It can be used to prepare raw data or improve existing training data to get more accurate ML models.

## What is this Modified-Label Studio?

Label-Studio for Data Annotations have been modified. Here It can be used with multi users with safe control over the data. No user can delete labels, predictions or make changes in setting.


### Install unmodified label-studio locally with pip
Activate virtual environment and pip install inside it. 

```bash
# Requires >=Python3.6, <3.9
pip install label-studio==1.4

# Start the server at http://localhost:8080
label-studio
```

### Install for local development

Steps to install the modified version with danger buttons disabled: 
Activate virtual environment and clone the repo inside it. 
```bash
git clone https://github.com/Prajit-Sengupta/Modified-Label-Studio.git
cd label-studio-multimodal-annotation
# Install all package dependencies
pip install -e .
# Run database migrations
python label_studio/manage.py migrate
# Start the server in development mode at http://localhost:8080
python label_studio/manage.py runserver
```

#### Apply frontend changes

The frontend part of Label Studio app lies in the `frontend/` folder and written in React JSX. In case you've made some changes there, the following commands should be run before building / starting the instance:

```
cd label_studio/frontend/
npm ci
npx webpack
cd ../..
python label_studio/manage.py collectstatic --no-input
```


## What you get from Modified- Label Studio
- Safe environment for multi-users to work on an enviroment
- Edited settings button with no functionality, so that no user/annotator can delete or make modifications in the whole project
- Annotate without fear of data loss since all deletion actions have been removed- 3 Actions of Tasks: Delete Tasks, Delete Task Annotations, Delete Task Predictions


### Settings Page made empty.
<img width="1406" alt="Screenshot 2022-07-19 at 2 28 40 PM" src="https://user-images.githubusercontent.com/82379532/179710953-7c63f860-8d7a-4449-84cf-80889654f6ab.png">

### Tasks Toggle Modified
![image](https://user-images.githubusercontent.com/71543838/175102817-9104a625-09ee-4cd5-ac60-d796479587e9.png)
