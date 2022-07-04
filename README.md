<img src="https://raw.githubusercontent.com/heartexlabs/label-studio/master/images/ls_github_header.png"/>


## What is Label Studio?

Label Studio is an open source data labeling tool. It lets you label data types like audio, text, images, videos, and time series with a simple and straightforward UI and export to various model formats. It can be used to prepare raw data or improve existing training data to get more accurate ML models.

## What is this Modified-Label Studio?

Label-Studio for Data Annotations have been modified. Here It can be used with multi users with safe control over the data. No user can delete labels, predictions or make changes in setting.


### Install locally with pip

```bash
# Requires >=Python3.6, <3.9
pip install label-studio

# Start the server at http://localhost:8080
label-studio
```

### Install for local development

You can run the latest Label Studio version locally without installing the package with pip. 

```bash
git clone https://github.com/Prajit-Sengupta/Modified-Label-Studio.git
cd label-studio
git checkout 3e28c167765c5a4030fbd309955d4eb64baf1841
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
- Safe Enviroment for multi-users to work on an enviroment
- Have removed the Danger Zone, Cloud Storage & WebHooks Pages from Settings, so that no user/annotator can delete or make modifications in the whole project
- Removed 3 Actions of Tasks: Delete Tasks, Delete Task Annotations, Delete Task Predcitions
- All deletion actions have been removed.

### Settings Page Modified.
![image](https://user-images.githubusercontent.com/71543838/175102704-331ef22e-ddae-485e-94c7-79395ae58f4d.png)

### Tasks Toggle Modified
![image](https://user-images.githubusercontent.com/71543838/175102817-9104a625-09ee-4cd5-ac60-d796479587e9.png)
