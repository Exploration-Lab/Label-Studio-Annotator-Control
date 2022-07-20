# Label-Studio-Annotator-Control

## What is Label Studio?
When we are working in NLP related projects where labeling of data is needed to feed the models, we need the help of annotation to label most of the data. For annotation tasks we have various tools in the market and the choice for users depends upon what sort of thing they want to label. We went with a multifunction open-source, data-labeling software named Label-Studio.

### Please Check our [BLOG](https://exploration-lab.github.io/Label-Studio-Annotator-Control/) for more details regarding the PROJECT. If you face any issues, contact the contributors
BLOG Link: [https://exploration-lab.github.io/Label-Studio-Annotator-Control/](https://exploration-lab.github.io/Label-Studio-Annotator-Control/)

## Installation Procedure

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
git clone https://github.com/Exploration-Lab/Label-Studio-Annotator-Control/.git
cd label-studio-multimodal-annotation
# Install all package dependencies
pip install -e .
# Run database migrations
python label_studio/manage.py migrate
# Start the server in development mode at http://localhost:8080
python label_studio/manage.py runserver
```

#### Apply frontend changes(only for developers)

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

### Import button removed 
<img width="1424" alt="Screenshot 2022-07-19 at 2 30 40 PM" src="https://user-images.githubusercontent.com/82379532/179711348-ed2dc666-ac19-48b0-8b14-361fd6e37b1a.png">

### Delete annotation button removed 
<img width="861" alt="Screenshot 2022-07-19 at 2 31 40 PM" src="https://user-images.githubusercontent.com/82379532/179711552-17976993-e838-4e49-92ec-e5b91d423624.png">
