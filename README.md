## Running the Project

To run the project, follow these steps:

1. Clone the repository:

    ```bash
    git clone 'https://github.com/{username}/EQ-Insight.git'
    ```
    
    ```bash
    cd 'EQ-Insight'
    ```

2. Set up a Python environment and install dependencies:

    ```bash
    cd api 
    python -m venv venv
    venv\Scripts\activate
    ```
    
    ```bash
    pip install -r requirements.txt
    ```

3. Run the Flask app:

    ```bash
    cd .. (to go back to the root directory)
    npm install
    yarn start-api
    ```

3. Open a web browser and navigate to `http://127.0.0.1:5000/` to interact with the app.

For the React frontend:

4. Start the React development server:

    ```bash
    yarn start
    ```

5. The React app will be running on `http://localhost:3000/` by default.

