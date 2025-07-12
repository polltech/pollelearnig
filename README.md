# PolleLearning

A simple static website to display Udemy courses from a `courses.json` file.

## How to Use

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    ```
2.  **Navigate to the project directory:**
    ```bash
    cd <project-directory>
    ```
3.  **Open `index.html` in your web browser:**
    You can do this by double-clicking the `index.html` file in your file explorer, or by right-clicking and selecting "Open with" your preferred browser.

    Alternatively, you can start a local web server to serve the files. This is recommended to avoid any potential issues with `fetch`ing the `courses.json` file due to browser security policies (CORS).

    **Using Python's built-in HTTP server:**
    ```bash
    # For Python 3
    python -m http.server
    ```
    Then, open your browser and go to `http://localhost:8000`.

## Features

*   **Course Listing:** Displays a grid of courses from the `courses.json` file.
*   **Search:** Live search to filter courses by title or description.
*   **Responsive:** The layout is responsive and works on both desktop and mobile devices.

## File Structure

*   `index.html`: The main HTML file that contains the structure, styling, and JavaScript for the website.
*   `courses.json`: A JSON file that contains the course data. You can replace this file with your own data.
