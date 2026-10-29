# AI-Powered IT Helpdesk Automation System

## Overview
A web-based IT helpdesk application built with Python and Streamlit. Users can report technical issues, receive AI-generated troubleshooting suggestions using Google's Gemini API, and track support tickets.

## Features
- IT issue reporting and ticket creation
- Issue category and priority selection
- Gemini AI-powered troubleshooting suggestions
- Helpdesk dashboard with ticket statistics
- Ticket status management
- CSV export of support tickets

## Technologies Used
- Python
- Streamlit
- Google Gemini API (`google-genai`)
- Pandas
- python-dotenv
- GitHub
- Streamlit Community Cloud

## Live Demo
https://ai-powered-it-appdesk-steqvuc3yaiv6fvacqf5sx.streamlit.app/

## Run Locally
1. Clone this repository.
2. Install the dependencies:

   `python -m pip install -r requirements.txt`

3. Create a `.env` file in the project directory and add your Gemini API key:

   `GEMINI_API_KEY=your_api_key_here`

4. Start the application:

   `python -m streamlit run app.py`

## Security
Keep your Gemini API key private. Do not commit `.env` files or API keys to GitHub.

## Project Status
Deployed prototype tested with ticket creation, AI troubleshooting, ticket status updates, dashboard statistics, and CSV export.

## Future Improvements
- Persistent database storage
- User authentication and role-based access
- Enhanced ticket assignment and reporting
