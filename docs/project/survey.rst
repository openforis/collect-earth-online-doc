
   A. **Survey Questions**

This is where you design the questions that your data collectors/photo
interpreters will answer for each of your survey plots. Each question
creates a column of data. This raw data facilitates calculating key
metrics and indicators and contributes to fulfilling your project goals.

**Survey Cards** are the basic unit of organization. Each survey card
creates a page of questions on the Data Collection interface. The basic
workflow is: Create new top-level question (new survey card) 🡪 populate
answers 🡪 create any child questions & answers 🡪 move to next top-level
question (new survey card) & repeat until all questions have been asked.

For the **Survey Question** tab, the left panel allows you to enter
questions while the right panel provides a preview of how these
questions will appear to your data collectors.\ |image6|

We will now go into more detail about how to add a question and answers,
the types of questions that can be asked and when these questions might
be useful.

1. How to add questions and answers

i. CEO provides a straightforward way to ask **multiple-choice**
   questions. As the most common question type used, we will use it for
   this example. In CEO, these questions are called “button—text”
   questions as in data collection they display as a button with text.

Questions of this type are useful for land use and land cover surveys,
or anywhere where you want the user to choose between a limited set of
mutually exclusive options. |image7|

ii.  To start, type your first question into the **Question Text** box.
     Since it is your first question, you cannot assign a **Parent
     Question** or **Parent Answers** for the question.

iii. Try to keep the question text below 45 characters so the whole
     question will be displayed during data collection.

iv.  Click [+\ **Add Survey Question**] to create your first **Survey
     Card**.

v.   You can now add Answers to your question. Answers have two parts: a
     color and a text box.

a) Click on the **[blue rectangle]** to bring up the **Color Selector.**
      You can move the color selector dot, use the eyedropper tool, or
      type in RGB values (0-255). Click off of the color selector when
      you are done. The color you choose will be associated with the
      answer. When a data collector selects that answer, any sample
      points assigned that answer would also be assigned that color to
      display on the map.

b) You can type your answer into the **Text Box**. Try to type answers
   with around 15 characters or less so that the full name is displayed
   during data collection.

c) You can also use the **[Bulk Add]** button to add multiple color and
   answer pairs.

vi.   Click the green [+] symbol to add the answer.

vii.  Continue adding answers until all the answers to your survey
      question have been added.

viii. Now that you have a top-level, or parent, question with answers,
      you can edit and delete questions and answers, and add child
      questions and child questions that appear only when specific
      answers are chosen.

2. You can delete or edit your questions and answers after you create
   them.

i.   To delete a question or a specific answer, click on the
     **Trashcan** icon next to the question or answer you would like to
     delete.

ii.  To edit a question or an answer, first type your edits into the
     box, then click the **Save** icon next to the edited question or
     answer.

iii. 

iv.  Parent & child questions, particularly child questions that have
     parent answers, are useful when you have broad categories and then
     want to refine the answer within that category.\ |image8|

3. You can ask follow-up questions based on a user’s response to further
   refine information about the plot. For example, if a user categorizes
   a plot as forest, you can follow up by asking them if it is deciduous
   or coniferous forest.

i.   To create a child question, next to **Parent Question** select the
     question you want using the drop-down menu.

ii.  You can then assign one or more **Parent Answers** through the
     dropdown menu. Hold down the ctrl button to select multiple
     answers. When one of the parent answers is chosen, the child
     question will appear.

iii. If you want to have the child question appear regardless of the
     answer, select all of the answers for **Parent Answer**.

iv.  Once you have finished adding child questions with their answers,
     you can create a second survey card by setting the **Parent
     Question** field to **None**.

v.   You can delete a question by clicking the **Trashcan** icon.
     Deleting a parent question with children will delete the children
     questions as well.

.. image:: media/image5.png
   :width: 0.30208in
   :height: 0.30208in

And here is how a survey card with parent/child questions appears on the
data collection page initially:

And after selecting “Answer #1”:

And after selecting “Answer #2”:

The child question with no parent answer will appear when either answer
is selected. The child question with “Answer #2” as the parent answer
only appears when “Answer #2” is selected.

You can also see that these questions were too long, and the user cannot
read the whole question. Try to keep your question below 45 characters.

You can create extensive lists of land cover classification options for
data collection using this approach.

4. Manipulating the survey cards.

i.  You can collapse a survey card by clicking the [-] symbol in the
    upper left.

ii. You can change the order of the Survey Cards by clicking the blue up
    & down arrows in the top right.

5. Here are the other types of questions that can be asked and when
   these questions might be useful:

i.  Now we will explore the other **Component Type** options.

ii. These **Component Types** include combinations of four question
    types and three data types.

..

   The four question types are:

-  **Button**: This creates clickable buttons, allowing users to select
      one out of many answers for each sample point.

-  **Input:** Allows users to enter answers in the box provided. The
      answer text provided by the project creator becomes the default
      answer.

-  **Radiobutton:** This creates radio buttons, allowing users to select
      one out of many answers for each sample point.

-  **Dropdown:** Allows users to select from a list of answers.

..

   The three data types allowed are:

-  **Boolean:** Use this when you have two options for a question
      (yes/no).

-  **Text:** Use this when you have multiple options which are text
      strings. They may include letters, numbers, or symbols.

-  **Number:** Use this when you have multiple options that are numbers,
      which do not contain letters or symbols.

iii. For the Input type only, you can choose whether to require an
     answer during data collection.

a) Leave this box unchecked if you don’t want users to always collect
   the information. This is useful for adding optional details about a
   plot.

b) Be sure to check the box if you need the question to be answered.

Following are examples of how each question type listed under
**Component** Type appears in the **Data Collection** screen, and notes
on when each type might be useful.

**Button—text:**

**Button—number:**

**Button—text** and **Button—number** are useful when you want the user
to classify each sample point as one of many different options.
Different sample points can be assigned different answers. These are a
great option for land use and land cover questions. |image9|

Try to use answer names with 15 characters or less so that the full name
is displayed during analysis.

The **Button—number** option, coupled with numeric answers, allows you
to implement numeric-only rules that will not work on **Button—text**
elements.

**Input—number:**

.. image:: media/image5.png
   :width: 0.30208in
   :height: 0.30208in

Users can input integers, decimals, negative and positive numbers, and
the letter “e” for scientific notation. Decimals must use “.” and not
“,”. What the survey creator types in the “Answer” field will become the
default text in the input box. Note the user must click “Save” to input
the answer.

**Input—text:**

.. image:: media/image5.png
   :width: 0.30208in
   :height: 0.30208in

Users can input any character. What the survey creator types in the
“Answer” field will become the default text in the input box.

**Input—number** and **Input—text** are useful when you want the user to
provide custom input for each plot. For example, you might ask local
participants to identify agricultural crops. Answers can be long (500+
characters).\ |image10|

**Radiobutton—boolean:**

**Radiobutton—text:**

**Radiobutton—number:**

Radiobuttons are functionally much the same as Buttons, but with a
different aesthetic and the added Boolean option. You can choose
different answers for each sample point. Try to use names with around 15
characters or less so that the full name is displayed during analysis.

**Radiobuttons** are useful when you want your users to choose one
answer for each of your sample points from multiple options. They work
well for land use and land cover questions. The Boolean option also
works well for areas you want to classify as yes/no, e.g. Forested or
Not Forested.\ |image11|

**Dropdown—boolean:**

**Dropdown—text:**

**Dropdown—number:**

The **Dropdown** questions function similarly to the **Button** and
**Radiobutton** options, but with the dropdown menu aesthetic instead of
the button aesthetic. As with the other options, you can assign each
sample point a different answer, though it is more difficult from a user
perspective. This option may encourage assigning only one answer to all
the sample points. Overall, choose the option that will be easiest for
your users to understand.
