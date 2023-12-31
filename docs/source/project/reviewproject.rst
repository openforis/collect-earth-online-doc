
Reviewing Projects
==================

In the Project Wizard
---------------------

Once the project set up is complete, click on **[Review]** in the bottom right-hand corner.

You will now see an overview of your project details.

Scroll through to check that everything is correct. If everything is correct, click **[Create Project]**. You will need to accept CEO’s terms and conditions.

If you notice a mistake, click **[Continue Editing]** to fix it.

After you click **[Create Project]**, a pop-up window will ask ‘Do you REALLY want to create this project?’ Click **[OK]**.

.. thumbnail:: ../_images/project52.png
    :title: Creating a project pop up
    :align: center
    :width: 90%

After you create the project, you will be taken to the Project Information interface. 

Project Information interface
-----------------------------

If you are navigating back to the **Project Information** (not visiting right after project creation), you can reach this page by finding your Institution on the **Home** page left panel. Click the **[Edit]** icon next to the project name to get to the **Project Information/Review Project** page.

The Project Information Interface has two components: **Project Details** on the left and **Project Management** on the right.

Project Details
^^^^^^^^^^^^^^^

The **Project Detail** pane includes an overview of your project, including sample collection design, imagery selection, the AOI boundary, and survey questions. 

- The **Collection Design** will now show the location of a subset of your plots (a maximum number can be displayed). 
- The **Plot Design** and **Sample Design** sections will show a summary of the choices you made or the .csv and .shp files you uploaded. 
- **Survey Questions** shows all the **Survey Cards** you created, along with the corresponding **Component Type, Answers, and Rules.**

Project Management
^^^^^^^^^^^^^^^^^^

The **Project Management** pane includes project publication information and important links to manage your project. 

**Publication status**

The publication status includes the **Date Created**, **Date Published**, and **Date Closed** for your project. If your project is not published yet, the **Date Published** will not be present. There is also text describing your project status:

- Draft Mode projects: This project is in draft mode. Admins can review, edit, and test collecting the project. Publish the project in order for users to begin collection. Any data collected in a Draft Mode project will not be retained.
- Published projects: This project is published. Users can begin collecting. Limited changes to the project details can be made. Close the project to prevent anymore updates.
- Closed projects: This project is closed. The project is closed to all changes. Reopen the project for additional collection.

.. tip:: 
      
      We suggest testing your project **extensively** while in draft mode. Check that you are asking all of your desired questions, rules are correct, and you have the desired plot and sample design.

      When you are completely happy with your project, that is the best time to publish it.

**Modify Project Details**

Next, examine the important links for your project:

- **Publish Project**: Clicking on this will publish your project and allow users to collect data. Note that if a project is not “Published” *only the admins of the institution can see it, not the members*.
- **Close Project**: If you have a published project, you can close it and stop data collection by clicking this button.
- **Edit Project**: This button will take you back to the project creation wizard (see :doc:`create`).

  - When your project is in DRAFT MODE, you can change all aspects of your project.
  - When your project is PUBLISHED, you can change the **Project Name, Description, and Privacy Level**.

- **Delete Project**: This will permanently delete your project.

.. tip:: 
      
      If you accidentally publish a faulty project, you can use it as the template for a revised project and not lose all your work.

**External Links**

- **Configure Geo-Dash:** Clicking on **[Configure Geo-Dash]** will open the Geo-Dash configuration interface. For more detail, please see :doc:`geodash`.
- **Collect:** This will take you to your project data collection interface so you can start collecting data right away.
- **Project Dashboard:** If you click on **[Project Dashboard]** you will see an overview of the AOI, along including the number of members, contributors, total plots, flagged plots, analyzed plots, unanalyzed plots, and the date the project was created, published and closed. Admins do not count towards the project’s member count.

.. thumbnail:: ../_images/projinfo1.png
    :title: The project dashboard.
    :align: center
    :width: 90%

**Export Data:**

There are three data download options, **Download Plot Data**, **Download Sample Data**, and **Download SHP**.

.. note:: 
      
      Data downloaded from CEO will be in WGS84 EPSG:4326 format.

**Download Plot Data** downloads your data with all samples summarized by plot. It is downloaded in .csv, which can be opened in programs like Microsoft Excel or imported into data analysis software. Downloaded columns will be: 
  
- **PLOT_ID:** the CEO-assigned unique sample plot number or the user provided Plot ID (for .csv and .shp files).
- **CENTER_LON** and **CENTER_LAT** are the geographic coordinates of the center of your sample plots.
- **SIZE_M** and **SHAPE** describe the size in meters and the shape (circle or square) of the sample plot.
- **SAMPLE_POINTS** indicates the number of samples in each plot.
- **EMAIL** is the user id (email address) of the person that classified the plot.
- **FLAGGED**: This will be FALSE for plots where data was collected and for plots where data has not been collected yet. It will be TRUE when a user has flagged the quality of the background map as not good enough to analyze the samples (e.g. due to clouds or poor image resolution).

  - Plots can either be flagged or saved by a user, but not both.
  - If a user flags the plot, then goes back and enters data and saves the plot, the plot will not be flagged.

- **FLAGGED_REASON**: A user provided reason for flagging the plot.
- **CONFIDENCE**: Collected user confidence.
- **COLLECTION_TIME**: date and time the user collected the plot data. Time in UTC.
- **ANALYSIS_DURATION**: Amount of time, in seconds, the user spent analyzing the plot.
- **COMMON_SECUREWATCH_DATE**: Most common SecureWatch date used.
- **TOTAL_SECUREWATCH_DATE**: Number of SecureWatch dates used.
- If you used a .csv or .shp file for plot design, any additional data columns you uploaded will be preserved in the .csv download. They will be preceded by PL_(column name). 
- All the following columns will have information about each of the survey questions broken down by answer. They are labeled **QUESTION TEXT:ANSWER TEXT**. For example, LULC:Built Surface would indicate that “LULC” was the question and “Built Surface” was the answer. 

  - In the plot summary download, these are quantified as percent (max 100) of the sample points in the plot that were assigned that answer.
  - For example, suppose you have four sample points within your plot and two answers (e.g. land cover class) to choose from. If one sample point is assigned to one answer and the other three points to the second answer, the data when downloaded will say ‘25’ for the first answer and ‘75’ for the second answer. 
  - For proactive sampling, percentages are based on sample count, *NOT AREA*.
  
**Download Sample Data** downloads your raw data, with information for each sample point within each plot as its own row. If you would like your plot data analyzed differently, the Download Sample Data option is a better fit.Downloaded in .csv, which can be opened in programs like Microsoft Excel or imported into data analysis software.

Downloaded .csv data from Download Sample Data will have the following columns:

- **PLOT_ID**: the CEO-assigned unique sample plot number or the user provided Plot ID (for .csv and .shp files).
- **SAMPLE_ID**: the CEO-assigned unique sample point number or the user provided Sample ID (for .csv and .shp files).
- **LON** and **LAT** are the geographic coordinates of the center of your sample points.
- **EMAIL:** is the user id (email address) of the person that classified the plot.
- **FLAGGED**: This will be FALSE for plots where data was collected and for plots where data has not been collected yet. It will be TRUE when a user has flagged the quality of the background map as not good enough to analyze the samples (e.g. due to clouds or poor image resolution).
- **COLLECTION_TIME**: The date and time when the user classified the plot. *Time zone is UTC.*
- **ANALYSIS_DURATION**: Time in seconds that the user took to analyze the plot.
- **IMAGERY_TITLE**: Name of the Imagery layer that the user had selected while analyzing the plot.
- **IMAGERY_ATTRIBUTIONS**: Any attribution for the imagery used.

.. note::

   If multiple imagery sources were used, only the name of the last imagery layer used will be recorded. There is no way to know all the layers used by the user, e.g. if you want to check that two years of imagery were used.

- If you used a .csv or .shp file for sample plot design, any additional data columns you uploaded will be preserved in the .csv download. They will be preceded by PL_(column name).
- If you used a .csv or .shp file for sample point design, any additional data columns you uploaded will be preserved in the .csv download. They will be preceded by SMPL_(column name).
- All the following columns will have information about each of the survey questions. They will be labeled **QUESTION TEXT**, where question text is the literal text of the question.

  .. note::
      
      Note that imagery dates are not available as many of the imagery sources are composite. *This means that* *each map tile is stitched together from imagery acquired on multiple dates. There is not a single date for an imagery tile*.

- If you are using SecureWatch imagery, you will have four additional columns:

  - **IMAGERYDATESECUREWATCH** will have a value for any samples which were classified while a specific date was selected from the imagery date dropdown.
  - **IMAGERYSTARTDATESECUREWATCH**, **IMAGERYENDDATESECUREWATCH**, and **FEATUREPROFILESECUREWATCH** will have values for any samples which were classified while a date range and feature profile were selected.

.. note:: 
      
      Note that imagery properties are associated with samples (not plots) because users are free to change these properties while classifying samples. Thus, any given plot may have some of its samples classified with one map image and other samples classified with a different map image.

**Download Shape File** downloads a zip file with two folders: plot-shape-file and sample-shape-file. Each file contains a corresponding shapefile, consisting of .shp, ..cpg, .dbf, .prj, and .shx files. Column (feature) information includes:

- PROJECTID: The project ID number from CEO.
- PLOTID: The PLOTID number from CEO.
- SAMPLEID: For the sample-shape-file only, the SAMPLEID number.

Using this information, you can join the shapefile with the plot or sample .csv information using a desktop GIS application such as QGIS or ArcGIS. You could also use a web-based application such as Google Earth Engine.
