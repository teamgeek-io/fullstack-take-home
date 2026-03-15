# Full-Stack Take-Home Assignment: Task Tracker

Thank you for taking the time to complete this assignment.

The goal of this exercise is to understand how you approach building a small full-stack feature end-to-end. We are interested in:

- Code quality
- UI quality
- Project structure
- Development workflow
- Communication and documentation
- Engineering judgement

This assignment should take **approximately 4–6 hours**.

Please do not spend significantly longer than this.

---

# Scenario

Build a small **Task Tracker** application using:

- **React frontend**
- **Python Django backend**

The application should allow a user to manage a list of tasks.

Users should be able to:

- View tasks
- Create a task
- Update a task
- Mark a task as complete or incomplete
- Filter tasks by status

Each task should include at minimum:

- **title**
- **description**
- **status** (`todo`, `in_progress`, `done`)
- **created date**

---

# Technical Requirements

## Backend

Use **Python with Django**.

The backend should:

- Store tasks in a database
- Expose API endpoints for the frontend
- Include basic validation
- Have clear project setup instructions

Minimum endpoints expected:

```
GET /tasks
POST /tasks
PATCH /tasks/:id
```

You may structure the backend however you prefer.

---

## Frontend

Use **React** and **Tailwind CSS**.

The frontend should include:

- A page displaying the list of tasks
- A form for creating tasks
- The ability to edit tasks
- The ability to change task status
- Filtering by status
- Loading, empty, and error states

The UI should be **clean, usable, and thoughtfully structured**.

We are interested in how you:

- Structure components
- Design interactions
- Organise UI code
- Use Tailwind effectively

---

# Dependency Usage

You may install any additional libraries or dependencies that you feel improve the implementation.

Examples might include:

- Form libraries
- State management tools
- API utilities
- Validation libraries
- Testing frameworks
- UI helper libraries

Please include a short section in `NOTES.md` describing:

- Which additional dependencies you installed
- Why you chose them
- Any alternatives you considered (if relevant)

We are interested in understanding your reasoning.

Good engineering judgement often means:

- Using a dependency where it adds value
- Avoiding unnecessary dependencies for simple problems

---

# Git Usage

Please submit your work as a **Git repository**.

We would like to see a **clear commit history** showing how you approached the work.

Guidelines:

- Commit as you normally would during development
- Use meaningful commit messages
- Avoid submitting the entire assignment as a single commit

Your commit history helps us understand:

- How you structure changes
- How you approach development incrementally
- How you communicate changes in a team setting

---

# Handling Edge Cases

Consider how your application behaves when:

- There are **no tasks**
- The **API request fails**
- A **user submits invalid data**
- A request **takes longer than expected**

You do not need complex solutions, but the application should behave sensibly.

---

# Optional Enhancements

These are **not required**, but are good places to demonstrate stronger engineering judgement:

- Reusable UI components
- Typed frontend code
- Thoughtful state management
- Tests
- Improved validation
- Pagination or sorting
- Accessibility considerations
- Optimistic UI updates
- Containerisation
- Improved developer experience

You do not need to implement many of these. One or two well-chosen improvements is enough.

---

# AI Usage

You are allowed to use AI tools while completing this assignment.

However, you must include a file called:

This should briefly describe:

- Which AI tools you used
- What parts of the assignment they were used for
- Example prompts or types of prompts
- What you modified or rejected from AI output

We are not evaluating whether you used AI.  
We are evaluating **how you use it**.

---

# Refactoring Requirement

After completing the feature, choose **one part of your implementation** and refactor it to improve it.

In `NOTES.md`, briefly explain:

- What the original implementation looked like
- What you improved
- Why you changed it

Examples might include:

- Extracting reusable components
- Improving API structure
- Reducing duplicated code
- Improving validation
- Simplifying state management

---

# Design Question

In `NOTES.md`, include a short answer to the following question:

**If this task tracker needed to support thousands of users and large numbers of tasks per user, what changes would you make to the architecture?**

You might consider topics such as:

- Database indexing
- Pagination
- API design
- Caching
- Background jobs
- Frontend performance

A few thoughtful paragraphs are sufficient.

---

# Required Documentation

## README.md

Your README should include:

- Setup instructions
- How to run the frontend
- How to run the backend
- Any environment variables required

We should be able to run the project locally.

---

## NOTES.md

Please include:

### 1. Your approach

Briefly describe:

- How you structured the backend
- How you structured the frontend
- Any notable design decisions

### 2. Refactoring explanation

Describe the improvement you made.

### 3. Scaling discussion

Answer the design question above.

### 4. Dependency choices

Explain any additional dependencies you added and why.

### 5. What you would add next

Provide a short list of improvements you would make with more time.

---

# Submission

Please submit a repository containing:

- Frontend
- Backend
- README.md
- NOTES.md
- AI_USAGE.md

---

# What We Will Evaluate

We will primarily look at:

- Code clarity
- UI quality
- DRY and reusable code
- Project structure
- Correctness
- Documentation
- Dependency choices
- Git usage
- Ability to explain decisions
- Engineering judgement
