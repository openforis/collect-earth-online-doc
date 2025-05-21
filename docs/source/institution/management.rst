Institution management
======================

Institution information
-----------------------

If you are an Administrator for an Institution, you can make changes to your Institution's information after the Institution is created.

1. If you want to make changes, start by navigating to your Institution’s info page (See :doc:`create`).
2. You can make changes to the Institution page by clicking **[Edit]** at the top of the page.
3. You can also delete your Institution by clicking **[Delete]**. 
   
   .. warning::
    
     This action is **PERMANENT**, and your Institution cannot be recovered afterwards. **ALL PROJECTS ASSOCIATED WITH THE INSTITUTION WILL ALSO BE DELETED.**

Key Institution components
--------------------------

More importantly, you can also manage three aspects of your Institution that allow data collection through CEO. These include the **Imagery** available, the data collection **Projects**, and the **Users** associated with the Institution. This information is displayed in three panels on your **Institution’s** info page.

1. The **Imagery** tab lists all available imagery and WMS Feeds. You can add new imagery feeds here as well. See :doc:`imagery`.
2. The **Projects** panel lists your Institution's projects, identifies projects as public or private, and allows you to create new projects. This is discussed in :doc:`../project/create`.
3. The **Users** panel lists your Institution's members and allows them to be updated. This is discussed below.

Institution user (member) management
------------------------------------

As an Administrator, you can add a Collect Earth Online member to the Institution by typing the user's email address into the box and clicking the **[Add User]** button. If you are successful, a pop-up window will notify you that the user has been given the role "Member," and the user's email address will appear in the list of users.

   .. tip::
   
      Only email addresses that have already created a CEO account can be added to the Institution.
   
There are two roles for users in an Institution: **Admin** and **Member**. The Administrator role allows the user to edit any of the Institution's projects, add and delete imagery, and manage the Institution's Users. The Member role allows the user to collect data in the Institution's projects.

As an Administrator, you can change the role of any user using the drop-down menu and buttons to the right of their email address.

1. Click on the drop-down menu to the right of their email address. 
2. Select **Admin** or **Member**.
3. Click the **[Update]** button to save your changes. CEO will ask you to confirm your changes. Click **[OK]** to confirm.
4. You can also remove users from the Institution by clicking on the **[Remove]** button. If you do this, the user will no longer be able to access any of the Institution's projects.  

You can approve or reject pending affiliation requests as well.

1. If a user has requested to join your Institution, you will see their email address in the list of users with a status of "**Pending**." 
2. You can approve this request by clicking the drop-down menu next to their email address and selecting **Admin** or **Member** buttons next to their email address. If you select **Admin**, the user will be given Administrator privileges for the Institution. If you select **Member**, the user will be given member privileges.
3. You can deny this request by clicking the **[Remove]** button. This will remove the user from the list of pending requests. 

   .. note::
   
      If you are an Administrator for an Institution, you can also remove other Administrators from the Institution. However, you cannot remove yourself from the Institution. If you want to remove yourself from the Institution, you will need to ask another Administrator to do this for you.

   .. note::
      
      To restrict the Administrator capabilities of a user to only one of the Institution's projects, you can create a new Institution specifically for that project. Add the user as an Administrator for the new Institution.


Other Administrator privileges
------------------------------

1. As an Administrator, you can review and modify the answers for all plots, including plots labeled by other CEO users. Members of an Institution can only review and modify answers for plots they themselves have labeled. To access this feature, use **Review** toggle for the **Navigate Through** dropdown menu on the **Collection Page**. See :doc:`../project/reviewdata` for more information.
2. As an Administrator you can review Draft Mode projects that you or other Administrators have created. This is discussed further in :doc:`../project/create`.
3. As an Administrator, you can download collected data from Institution projects. See :doc:`../project/reviewproject`.
