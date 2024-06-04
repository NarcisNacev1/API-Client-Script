## API Client Script

This script interfaces with the public "Game of Thrones" API to fetch and display data, specifically extracting and printing the names from the retrieved dataset.

### Key Learnings

- **Script Development:** 
  - **Libraries Used:**
    - `requests`: For sending HTTP requests.
    - `argparse`: For handling command-line arguments.
    - `json`: For parsing JSON data.
  - **Argument Handling:** 
    - The script accepts various command-line arguments, including the API URL and optional tokens, enhancing flexibility and functionality.
  - **Version Control:** 
    - The script was committed to a Git repository using standard version control commands.

#### Git Workflow for Initial Upload:

```sh
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/USERNAME/REPOSITORY_NAME.git
git push -u origin main
```

#### Git Workflow for Updates:

```sh
git status
git add .
git commit -m "Updated the API client script to handle new API response format"
git pull origin main --rebase
git push origin main
```

By following these workflows, the script was successfully integrated into the repository, ensuring proper version management and collaboration.
