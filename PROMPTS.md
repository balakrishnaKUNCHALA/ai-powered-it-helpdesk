# AI-Powered IT Helpdesk Automation System — Prompt Documentation

## Prompt 1: Project Planning
Build a beginner-friendly IT Helpdesk web application using Python and Streamlit. The application should allow users to report IT issues, manage support tickets, and receive troubleshooting guidance.

## Prompt 2: Ticket Management
Create a ticket management system that records ticket IDs, user names, issue categories, priorities, descriptions, statuses, and creation timestamps.

## Prompt 3: Issue Categories and Priority
Allow users to classify tickets into categories such as Network, Hardware, Software, Login/Access, and General Support. Provide Low, Medium, and High priority options.

## Prompt 4: AI Troubleshooting
Integrate the Google Gemini API to generate clear, relevant, beginner-friendly troubleshooting steps based on the user's issue description and selected category. Keep recommendations safe and suggest contacting IT support when necessary.

## Prompt 5: Ticket Dashboard
Display ticket information in a Streamlit dashboard. Allow ticket statuses to be updated and provide an option to download ticket records as a CSV file.

## Prompt 6: Error Handling and API Security
Load the Gemini API key from an environment variable using a `.env` file. Do not hardcode API keys or commit secret files to GitHub. Handle API errors and missing credentials gracefully.

## Tools Used
- Python
- Streamlit
- Google Gemini API
- Pandas
- python-dotenv
- Visual Studio Code
- GitHub

## Implementation Status
The application has been tested locally. Ticket creation, dashboard display, ticket status updates, CSV export, and AI-generated troubleshooting suggestions have been tested.

## Future Enhancements
- Database storage for persistent ticket records
- User authentication and role-based access
- Email notifications for ticket updates
- Cloud deployment
- Automated testing and improved error handling
