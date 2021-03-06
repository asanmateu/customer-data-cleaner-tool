# CD Customer List Cleaner (version: 1.0.0)

The purpose of this script is to speed up the process of cleaning manual customer data templates.

The script features a range of functions with different functionality that clean each of the template columns.

**Pre-dockerised version:** This package runs with a conda environment to benefit from conda's dependency management functionality.


## 1. Version 1.0.0 

### 1.1. What this version does ✅

1. Cleans every filed of the customer list data except the Discount related fields. **Please review this beforehand**.

2. Includes address codes validation process, however, for it to work data needs to be in a decent status, including address types, and either customer codes or customer names that are unique for the connection.

2. Returns a **results.xlsx** file with 3 new columns **RESULT, ALERT, ERROR**.

    * **RESULT**: Indicates whether the row is clean, values have been set to default, or denied.
    * **ALERT**: Alerts contain recommendations and require taking note as this may include payment methods defaulted to none since these were not setup or price type defaulted to the first in the designer's order settings.
    * **ERROR**: Fields that need to be fixed compulsory for analysts to process them.

4. These flags will make obvious if values have been removed to default or where the key errors are.


### 1.2. What this version does NOT DO ⚠️ 

1. Clean discount fields.

2. **Bad data must be spot intuitively (unfortunately).**

3. Check intention of bad data (i.e. multiple rows for a same retailer without customer code when brand only wanted multiple buyers).

4. Validate additional buyers. Analyst must concatenate them and drop them there. Additional emails will just be added to existing ones.


##  3. Installation 🛠 

1. Request your credential to access **prod_ro** to management.


2. Make sure you have installed conda: https://docs.anaconda.com/anaconda/install/mac-os/.


3. Open Anaconda Navigator and open **jupyter-lab > terminal** window. Then, run this command on the command line:
```
# This is to make conda environments work on 'zsh' -> MAC OSX's terminal system.

$ conda init zsh
```

4. Create a new conda environment using environment export found in the tool's conda directory:
```
# If this doesn't work try -f path/to/cdcleaner-conda-env.yml

$ conda env create -f cdcleaner-conda-env.yml
```

5. Activate conda environment from your **personal terminal** (it will go back to **base** environment every time you reset terminal session). Check it works:

```
$ conda activate cd-cleaner-conda-env
```
  
This step is done everytime so that you can run the script on the tool's environment. By default, terminal starts session on 'base' environment.


6. Make sure pip has installed the tool's python modules:
```
# Include the dot

$ pip install .
```


## 4. Instructions 🛁

1. Start by checking and fixing Discount fields.


2. Additional buyers should be placed manually as **add_buyer_email1;add_buyer_email2;...**. Also initial additional emails into the additional emails columns. The script will add to additional emails those extra emails in the emails field. No need to touch these,


3. Deposit customer list data into the template found in **files/input** directory. **DO NOT CHANGE ITS NAME NOR COLUMN NAMES**.


3. Open terminal and **activate** environment:
```
$ conda activate cd-cleaner-conda-env
```

4. Navigate to tool directory and run **pipeline.py**:
```
$ cd ~/desktop/joor-cd-cleaner

$ python3 pipeline.py
```
 
5. Let the script run, if there is no error, once it is finished it will direct you to check the files/output directory where the results file will be placed.


6. For best practices, delete this file or take it out of the output folder to avoid confusing next time you use the tool.Otherwise, make sure you check the last time it was updated in case the tool threw an error and you were collecting an old results file.


7. If you have many additional emails then use emails2query template and script to put them automatically into query format. Copy and paste into query template and drop the push request.



## 5. Updating CD Cleaner Tool 📡

1. Download the repository's zip file and remove the old one.

2. Open terminal in the tool's conda environment and run:

```
# Include the dot

$ pip install .
```

3. You should be able to use the script as usual. Check on the **version** section 1 to see what has changed.


**Alternatively**, if you are familiar with version control:

1. Link the tool package to this remote repository and pull the new version.


2. Run:
```
# This installs all the updated internal modules into environment level

$ pip install .
```


