
Plot Design—Quality Control Options
===================================

.. **add csv column stuff**

We have implemented automated quality assurance and quality control (QAQC) tools for projects created in CEO.

User Assignment
---------------

You can assign members of your institution to a specified proportion of the plots using the user assignment feature.

There are three options: **Equal assignments**, **Percentage of plots**, and **File**. The **File** option is only available if you are using a csv or shp file to specify your plot boundaries. It will be greyed out when using CEO's built in options.

- **No assignments**: User assignments are not enabled by default. 
- **Equal assignments**: Splits the total number of plots evenly between users.
- **Percentage of plots**: Allows for uneven splits. For example, one user can be assigned 50% of the total plots while two other users can each be assigned 25% of the total plots. Total percentages must add up to 100%.
- **File**: Allows the administrator to specify which user should collect data on each plot. When creating your file, you can add a column called 'user'. This column should contain the email address for the user you would like to review the plot.

.. thumbnail:: ../_images/project24v2.png
    :title: User assignment options
    :align: center
    :width: 50%

Quality Modes
-------------

You can also implement quality control measures using one of the **Quality Modes**. This allows multiple users to collect data for the same plot for QA/QC purposes.

- **None**: Quality control is not enabled by default.
- **Overlap**: A certain percentage of each users’ plots are reviewed by the other users.

.. thumbnail:: ../_images/project25.png
    :title: The Overlap option.
    :align: center
    :width: 40%

- **Subject Matter Expert Verification (SME Verification**): A percentage of each users’ plots are reviewed by one or more SMEs. For example, the SME might be someone with deep knowledge of the local landscape, or a project administrator.

.. thumbnail:: ../_images/project26.png
    :title: The SME Verification option.
    :align: center
    :width: 40%

- **File**: Allows the administrator to manually specify additional user(s) to collect data on each plot. When creating your file, you can add a column called 'reviewers.' This column should contain the emails of users that will also be collecting data for the plot. This column accepts more than one email separated by a semi-colon (;). 

   .. note:: 
        
       The 'users' column can be used without the 'reviewers' column, but not the other way around. If the 'reviewers' column is not present in the file, then the QAQC will not automatically be set, allowing the project administrator to use the drop-down options. 

       Once a CSV containing these two new columns is uploaded, the project admin will not be able to change either the User Assignments nor the QAQC, as they will be locked. In order to unlock them, the project admin can remove these columns and reupload the file, or change the plot design method by selecting another type in the **Spatial Distribution** dropdown menu.



.. note::
    When Quality Control is enabled, the project can no longer support User Drawn samples.

When you implement Quality Control, you will be able to use the QAQC Administrator Review Mode. See :doc:`/project/reviewdata` for more information.

You will also be able to use the QAQC Dashboard. See :doc:`/project/qaqcdashboard` for more information.

