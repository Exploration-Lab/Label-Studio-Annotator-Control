# Label-Studio-Annotator-Control

## What is Label Studio?
When we are working in NLP related projects where labelled data is needed to feed the models, we need the help of annotations to label most of the data. For annotation tasks we have various tools in the market and the choice for users depends upon what sort of thing they want to label. We went with a multifunction open-source, data-labeling software named Label-Studio.

### Please check our [BLOG](https://exploration-lab.github.io/Label-Studio-Annotator-Control/) for more details regarding the PROJECT. If you face any issues, contact the contributors
BLOG Link: [https://exploration-lab.github.io/Label-Studio-Annotator-Control/](https://exploration-lab.github.io/Label-Studio-Annotator-Control/)\
Also we have a [Tutorial Video](https://drive.google.com/file/d/1sHGTmhcXgCzvOp9iUgVa6D8rOwb__7i9/view?usp=drivesdk) for better understanding of this software.

### Contributors:
This Project was made by:

1.**Prajit Sengupta** (Thapar Institute of Engineering & Technology) ([Email me](mailto:ratulsengupta8@gmail.com)).

2.**Dishay Mehta** (Indian Institute of Technology Kanpur) ([Email me](mailto:dishaym20@iitk.ac.in)).

3.**Tejas R** (Indian Institute of Technology Kanpur) ([Email me](mailto:tejasr20@iitk.ac.in)).

Under the mentorship of <a href="https://ashutosh-modi.github.io/"> Dr. Ashutosh Modi </a> (Indian Institute of Technology Kanpur)

## Installation Procedure
To use this software we need to download the original label-studio code for the admin to create & manage the project. For the public annotators, they need to install from the github repository Label-Studio-Annotator-Control.

**Install Label-Studio(admin)**
```
# Requires >=Python3.6, <3.9
pip install label-studio
# Start the server at http://localhost:8080
label-studio
```

**Install [Software] - Public Annotators**
```
git clone https://github.com/Exploration-Lab/Label-Studio-Annotator-Control.git
cd label-studio
# Install all package dependencies
pip install -e .
# Run database migrations
python label_studio/manage.py migrate
# Start the server in development mode at http://localhost:8080 (Default Port)
python label_studio/manage.py runserver
```

## What you get from Modified-Label Studio(Label-Studio-Annotator-Control)
- Annotation Now made Easy!
- Safe environment for multi-users to work on an enviroment
- Edited settings button with no functionality, so that no user/annotator can delete or make modifications in the whole project, nor can import/create a new project.
- Annotate without fear of data loss since all deletion actions have been removed- 3 Actions of Tasks: Delete Tasks, Delete Task Annotations, Delete Task Predictions
- And MANY MORE! Do Check out the [BLOG](https://exploration-lab.github.io/Label-Studio-Annotator-Control/)

#### DO star the repository if you liked our open source contribution. Hope you are benefited by it :innocent:
