Survey Rules
============

Survey rules help ensure users collect logical and correct answers. If you do not want to add any rules, you can just click **[Next]**.

Rule Types
----------

You can select one of multiple different rule types, depending on your needs and the types of questions you have included in your Survey.

.. thumbnail:: ../_images/project47.png
    :title: The Rule Type drop down menu
    :align: center
    :width: 90%

**Text Regex Match**: This rule applies only to **Input—text** questions & their answers. It allows you to verify if the entered value fits, using regular expressions.

.. tip:: 
      Unless you have a specific reason to use the **Input—text** question type, consider using **Button—text** or **Radiobutton—text** instead. These options are easier for users and will always provide exact text.

This rule uses the JavaScript RegExp function, documentation for writing a regular expression can be found here: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions.

**Numeric Range:** This rule applies to **Input—number** questions & their answers. With this rule, you can verify that the numeric input falls within a predefined range.

For example, if you are asking about the proportion of points in the plot that contain trees, you could constrain the answers between 0 and 1.

**Sum of Answers:** This rule applies to any **number** type questions & their answers. You select multiple questions (2 or more) and specify what the questions should sum to.

For example, this is helpful if you have multiple questions asking about percent of land cover, where the sum should be 100%.

**Matching sums:** This rule applies to any **number** type questions & their answers. With this rule, you specify two sets of multiple questions (2 or more) that should have equal sums.

**Incompatible answers:** This rule can apply to any type of question. It allows the user to define incompatible sets of answers.

For example, if the answer to one question is land cover = “Water”, the answer to another question could not be land use = “Industrial”.

**Multiple incompatable answers:** This rule limits what answers can be chosen based on the answers for multiple other questions.

For example, if you answer "landcover start = forest" and "change event = deforestation", then "landcover end" CANNOT equal "forest".

Rule Preview
------------

You can preview how the rules will look for users in the **Question Preview** pane by mousing over and clicking on the **[Rule]** icon (clipboard).

.. thumbnail:: ../_images/project48.png
    :title: Preview how rules will look for users
    :align: center
    :width: 90%

Clicking on the **[Rule]** icon will show a list of rules.

.. thumbnail:: ../_images/project49.png
    :title: A list of rules
    :align: center
    :width: 50%

Navigating back to the Survey Questions tab will also show when questions have Rules associated with them. Mousing over the **[Rule]** icon will display the rule text.

.. thumbnail:: ../_images/project50.png
    :title: Rules on the survey card setup
    :align: center
    :width: 90%

Data collectors will be able to view any rules you implement by mousing over the **[Rule]** icon.

.. thumbnail:: ../_images/project51.png
    :title: The view for data collectors
    :align: center
    :width: 50%

They will see an error if they try to enter an answer that conflicts with the rules.
