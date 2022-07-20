# Label-Studio-Annotator-Control

Github Link: [https://github.com/Exploration-Lab/Label-Studio-Annotator-Control.git](https://github.com/Exploration-Lab/Label-Studio-Annotator-Control.git
)

**Contents:**
1. Use-case
2. What Is Label-Studio?
3. Issues Faced
4. Our Solution 
5. How to use it. (Install,run, deploy)
6. Managing your project
7. Conclusion (Resource & our feedback)
8. Contributors

### 1. Our Use Case
Natural language processing (NLP) is a subfield of AI and linguistics which enables computers to understand, interpret and manipulate human language. 
Today, humans are needed in the data annotation/labeling process in order to identify and classify information. Without these labels, a machine learning algorithm will have a difficult time predicting attributes that enable understanding of spoken or written language. When it comes to annotation, machines can’t function without humans-in-the-loop.

Types of annotations in a natural language processing data set
- Utterance
- Intent 
- Entity

These are very complex and thus need a multipurpose annotation tool which can create a label dataset having all the annotations. Label Studio is one such tool for annotation which is open sourced. We have modified the tool for our convenience to easily deal with the annotations without any fear of loss of data or mishandling of data. We have modified the tool such that multiple annotators can use it  with safe control over the projects. We hope that you also benefited by the modifications which we have done to make it easy to annotate pictures, videos, text etc.


### 2. What is Label Studio?
When we are working in NLP related projects where labeling of data is needed to feed the models, we need the help of annotation to label most of the data. For annotation tasks we have various tools in the market and the choice for users depends upon what sort of thing they want to label. We went with a multifunction open-source, data-labeling software named Label-Studio.
It lets us label data types like audio, text, images, videos, and time series with an extremely simple UI and export to various model formats. It can be used to prepare dataset and testing data-sets to get more accurate ML models. 

It is quite easy to import data(in .csv, .json, .tsv, .mp4 formats) and preview it for annotation. Also data like videos needs a context of the scene for understanding. Such functionalities are also present in this software, making it very convenient for the annotators. Also we can provide annotating options within some other annotating options, to the annotators. This makes annotation easier for them. For example in the below image, we can import an image sample (from a dataset), and annotate (label) it, whether it's :”Airbus” or ”Boeing”. This way we can label data, to build a dataset for the model.

### 3. Issues Faced
We planned to collect annotated data through crowdsourcing. Label Studio provides us with a very simple interface for uploading data, annotating it, and finally exporting annotated data in a format of our choice. But the open-sourced (community) version of label studio has its issues while being used as a crowdsourcing tool. Some of those issues are:

- The annotators could erase and delete the annotations, tasks and predictions which would lead to loss of data. 
- The annotators have the power to delete and create projects which contain labeled as well as unlabelled data.
- The annotators could change the settings which included a danger zone of deleting the data and changing the sync storage which can interfere with our dataset.
- The annotators could import their own project which would be chaotic and confusing.



### 4. Our Solution
We have made many apt changes to the code-base for the label-studio to be used by annotators (people who want to volunteer to label different sorts of data for a particular project) from all around the world. The annotators can get in any of the Projects available in the [software’s] dashboard. From there itself they can annotate any dataset they prefer to, but cannot make any changes to the originality of the project (dataset/training set).

To make this into action we have to use 2 portals. One is the admin portal which has all the functionality of Label-Studio & the other for public use(for the annotators.) Both are connected to the same database.

These are the following changes we made in Label-Studio(For Public use) to release it to the public for annotation of the huge data:
- Safe Environment for multi-users to work.
- Have the functionality of the Settings button, so that no user/annotator can delete or make modifications in any way possible to the whole project
- Removed 3 Actions of Tasks: Delete Tasks, Delete Task Annotations, Delete Task 
- Predictions. This wouldn't allow any user to delete/modify any of the particular sample in the project
Before


After


All deletion actions have been removed, which safeguard the project owners from loosing their data.

Before


After


Have removed the Import and Create functionality, so that no user can add new data to the existing dataset, which might destroy the sole purpose of the project.

CREATE functionality:
Before

After


IMPORT functionality:
Before


After




**NOTE:** Have removed the Synced Storage functionality. So that no user/annotator can sync the data to some different project, which might lead to a mess in the existing project.
Have made some changes in the UI, for users to preview the data like videos, along with context videos in an easy & simple manner.

#### 5. How to Use It?(Installation)
To use this software we need to download the original label-studio code for the admin to create & manage his/her project. While for the public annotators, they need to install from the github repo [software_name]
**Install Label-Studio(admin)**
```
# Requires >=Python3.6, <3.9
pip install label-studio
# Start the server at http://localhost:8080
label-studio
```


**Install [Software] - Public Annotators**
```
git clone https://github.com/Exploration-Lab/label-studio-multimodal-annotation.git
cd label-studio
# Install all package dependencies
pip install -e .
# Run database migrations
python label_studio/manage.py migrate
# Start the server in development mode at http://localhost:8080(Port Default)
python label_studio/manage.py runserver
```

Note: The Database of both of the versions (Label-Studio & [Software] ) will be connceted by default. (For eg the path to the dataset will be the same for both of the versions.) Here you dont’t need to make any changes.



### 6. Managing your project 
You can manage the changes in the final project by making a new label studio environment with pip such that both the environments are in sync. You can create the projects here, select the type of labelling setup that you require and import the json for syncing the database to the tool.
Make changes in the xml and you are good to go for annotators to annotate. 
OR
You can also make a super user using the command python manage.py makesuperuser which inbuilt feature of the backend which can help you monitor the tasks.
Note: You can refer out [Tutorial Video](https://drive.google.com/file/d/1sHGTmhcXgCzvOp9iUgVa6D8rOwb__7i9/view?usp=drivesdk)

### 7. Conclusion
We feel this [Software], can make the job of millions of students/researchers job of annotating or labeling data of their dataset fast & in a secured way. They can open-source their project to volunteers (who will be the annotators), to labe their huge-datset, which would have consumed lot of time, if they would have done on their own. 
This way the process of labelling of data becomes quite fast as well as transparent.  
You can simple follow the above steps for easy and Bingo! You are good to go with your labelling of your data via other people. 

**Note:** If you face any sort of bugs or any issue you can contact the contributors



### Contributors:

This Project was made by:

1.**Prajit Sengupta** (Thapar Institute of Engineering & Technology) (Email Id).

2.**Dishay Mehta** (Indian Institute of Technology Kanpur) (Email Id).

3.**Tejas R** (Indian Institute of Technology Kanpur) (Email Id).

Under the mentorship of **Prof Ashutosh Modi** (Indian Institute of Technology , CSED)






