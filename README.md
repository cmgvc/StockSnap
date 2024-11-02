# Stock Snap

Stock snap is a web application that aggregates financial data from various sources, allowing users to visualize and track stock performance over time. Users can search for specific stocks, view key metrics, and compare multiple stocks simultaneously.

## Features
- **User Authentication:** Secure sign-up and login to personalize the experience.
- **Stock Search:** Search for individual stocks using their ticker symbols.
- **Multiple Stock Comparison:** Select multiple stocks to view their performance side-by-side.
- **Data Visualization:** Interactive charts and graphs for a better understanding of market trends.
- **Real-time Updates:** Automatically update data from various financial APIs.

## Technologies Used

- **Frontend:** React.js, HTML, CSS
- **Backend:** Flask (Python)
- **APIs:** Integration with financial data APIs for stock prices and metrics

## Installation
1. Clone the repository:
```bash
git clone https://github.com/yourusername/financial-dashboard.git
```
2. Navigate to project directory 
```bash
cd StockSnap
```
3. Set up the backend:
    - Create a virtual environment:
    ```bash
    python3 -m venv venv
    ```
    - Activate the virtual environment:
    ```bash
    source venv/bin/activate 
    ```
    - Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```
4. Start the backend server:
```bash
python app.py
```
5. For the frontend:
    - Navigate to the frontend directory (if separate):
    ```bash
    cd frontend
    ```
    - Install the required packages:
    ```bash
    npm install
    ```
    - Start the React application:
    ```bash
    npm start
    ```