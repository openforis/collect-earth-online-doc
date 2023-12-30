Advanced plot analysis
======================

Multiple time periods
---------------------

For analyses comparing two or more time periods, you may need to toggle between imagery from different dates.

1. You may need to click **[Update Imagery]** when toggling between different imagery sources.
2. Your institution should have set up the project with two labeled imagery options for the time periods of interest.
3. Click the **drop-down menu** under **IMAGERY OPTIONS** and select the earlier of the two time periods.
4. Then, repeat this for the later of the two time periods.
5. Some imagery options allow you to enter imagery start and end dates.

.. thumbnail:: ../_images/collect10.png
   :title: Start and end dates for imagery.
   :group: collect-advanced
   :align: center

6. Some imagery options also allow you to choose a feature profile for the imagery. This is essentially a filter that the imagery provider puts on their data. For example, the Cloud Cover Profile filters out imagery with too much cloud cover.

.. thumbnail:: ../_images/collect11.png
   :title: Different profiles available.
   :group: collect-advanced
   :align: center

7. For the Planet Daily data, you will see a list of checkboxes pop up just to the left of the **Imagery Options**. You can use these checkboxes to refine the dates of the map data you want to see displayed. Planet Daily imagery is received as a stack of images. CEO displays the imagery and the checkboxes in the same order that Planet Daily provides this imagery stack. That is, the top date is also the top layer in the imagery stack. If you turn the top image off by unchecking the box, you will see the next date’s image is now on top. It is like looking through a stack of photographs, removing the top one reveals the photo underneath.

.. thumbnail:: ../_images/collect12.png
   :title: Planet Daily data selection.
   :group: collect-advanced
   :align: center

8. If your project uses SecureWatch Imagery, you will be able to select a range of dates (under **Select Range**) or specific dates (under **Select Dates**). Your institution will have set a default range of dates when the project was created. The list of **Available Dates** will automatically    populate with the available dates for the sample plot you are looking at. When you answer a question, the date or range of dates will be recorded. Please refer to any specific instructions your institution has given you regarding which imagery options to use for SecureWatch.

.. thumbnail:: ../_images/collect13.png
   :title: SecureWatch imagery options.
   :group: collect-advanced
   :align: center

9.   Make sure you also refer to the second tab, where the Geo-Dash information is presented. The time series information that is presented in the Geo-Dash window is also helpful in determining if change has occurred on the landscape.
10.  If both images look the same, no change occurred, so we select all points and label them as no change or stable.
11.  If there has been change, select the appropriate change option.
12.  Repeat for all Sample Value categories.

.. seasonality: 

Seasonality
-----------

Seasonality issues can occur when different land uses appear different between seasons. For example, a grassland might be bright green in spring but look brown in the summer. If you saw just the brown imagery, you might think the brown is dirt and incorrectly classify the grassland as barren dirt.

1.   To avoid this issue, try switching between different imagery that is available to you. Look to see if there is imagery available from different seasons to help with your decision.
2.   You can also look at the Geo-Dash page for the plot to see if there is any NDVI or other additional information that could help you.
3.   You can also click on **Download Plot KML** to download a .kml file to view in Google Earth. Google Earth has multiple current and historic imagery sources that can help you identify a plot.

Adjusting the zooom level
-------------------------

Zooming in and out to gather contextual clues from the landscape is important for multiple land use and land cover types. For example:

1.   Water in larger waterbodies often appears black or dark until you zoom out.
2.   Tree plantations may look like forests until you zoom out and see the regular pattern of planted trees.

Flag a plot
-----------

You can click **[Flag Plot]** if the imagery is insufficient (missing, low resolution, etc.) to accurately label the plot attributes. It will automatically reload the next plot for your project.

1.   **Flag Plot** will delete any attributes that have been assigned to the points/plots.
2.   Using **Navigate Through** set to **My Analyzed Plots** you can return to the flagged plot and try to answer the questions again. The **flag plot** button will be disabled because the plot has already been flagged and you cannot flag it again.
3.   Your responses will be recorded, and the plot will be unflagged if you click **Save**.
4.   Plots can either be flagged or saved by a user, but not both.

Difficult plots
---------------

Sometimes plots are hard to interpret, even with good imagery! These plots can only be reliably and accurately classified by having knowledge of local agricultural systems, local vegetation types, and landscape patterns.

1.   Try making use of the surroundings of the plot to glean as much information as you can before making a best guess.
2.   If different users identify the plot differently, it will be flagged internally as a difficult plot.
3.   If you do not feel comfortable interpreting the plot, you should click **[Flag Plot]**.

Skip a plot
-----------

At any time, you can skip a plot for later analysis by clicking the **[Next Plot Arrow]** in the **Plot Navigation** tab. Alternatively, click on **[Previous Plot Arrow]** to revisit the previous plot

Project information
-------------------

If you click on the project name, it will show the number and percent of plots completed, the number and percent of plots flagged as bad, and the total number of plots. An accuracy score based on the project’s training data will also be available soon.

.. thumbnail:: ../_images/collect14.png
   :title: Clicking on the project name shows project information.
   :group: collect-advanced
   :align: center
