A. **Survey Rules**

Survey rules help ensure users collect logical and correct answers. If
you do not want to add any rules, you can just click **Next**.

**Rule Types** include:

-  | **Text Regex Match**: This rule applies only to **Input—text**
        questions & their answers. It allows you to verify if the
        entered value fits, using regular expressions.
      | However, unless you have a specific reason to use the
        **Input—text** question type, consider using **Button—text** or
        **Radiobutton—text** instead. These options are easier for users
        and will always provide exact text.
      | This rule uses the JavaScript RegExp function, documentation for
        writing a regular expression can be found here:
        https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions.

-  **Numeric Range:** This rule applies to **Input—number** questions &
      their answers. With this rule, you can verify that the numeric
      input falls within a predefined range.

For example, if you are asking about the proportion of points in the
plot that contain trees, you could constrain the answers between 0 and
1.\ |image12|

-  **Sum of Answers:** This rule applies to any **number** type
      questions & their answers. You select multiple questions (2 or
      more) and specify what the questions should sum to.

For example, this is helpful if you have multiple questions asking about
percent of land cover, where the sum should be 100%.\ |image13|

-  **Matching sums:** This rule applies to any **number** type questions
      & their answers. With this rule, you specify two sets of multiple
      questions (2 or more) that should have equal sums.

-  **Incompatible answers:** This rule can apply to any type of
      question. It allows the user to define incompatible sets of
      answers.

For example, if the answer to one question is land cover = “Water”, the
answer to another question could not be land use =
“Industrial”.\ |image14|

You can preview how the rules will look for users in the Question
Preview pane by mousing over and clicking on the **Rule** icon
(clipboard).

Clicking on the **Rule** icon will show a list of rules.

Navigating back to the Survey Questions tab will also show when
questions have Rules associated with them. Mousing over the Rule will
display the rule text.

.. image:: media/image5.png
   :width: 0.30208in
   :height: 0.30208in

Data collectors will be able to view any rules you implement by mousing
over the rules icon.

They will see an error if they try to enter an answer that conflicts
with the rules:
