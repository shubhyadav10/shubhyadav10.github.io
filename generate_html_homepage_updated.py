
import os

def generate_html_homepage():
    # Get the base directory and set project-specific folders
    base_dir = os.path.dirname(os.path.abspath(__file__))

    
    # Define paths relative to the project directory
    meets_dir = os.path.join(base_dir, "meets")
    
    # Helper function to generate table rows from files in a directory
    # def generate_rows(directory):
    #     rows = []
    #     for file in sorted(os.listdir(directory)):
    #         if file.endswith(".html"):
    #             file_path = os.path.join(directory, file)
    #             relative_path = os.path.relpath(file_path, base_dir)
    #             rows.append(f'<tr><td><a href="{relative_path}">{file}</a></td></tr>')
    #     return "\n".join(rows)
    
    def generate_rows(directory):
        rows = []
        for file in sorted(os.listdir(directory)):
            if file.endswith(".html"):
                file_path = os.path.join(directory, file)
                relative_path = os.path.relpath(file_path, base_dir)
                
                # Normalize file name by removing underscores and ".html" extension
                display_name = file.replace("_", " ").replace(".html", "")
                
                rows.append(f'<tr><td><a href="{relative_path}">{display_name}</a></td></tr>')
        return "\n".join(rows)
    
    # Generate rows for each section
    meet_rows = generate_rows(meets_dir)
    # HTML template
    html_template = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ann Arbor Skyline Meets</title>
    <link rel="stylesheet" href="../css/reset.css">
    <link rel="stylesheet" href="../css/style.css">
</head>
<body>
    <a href = "#main">Skip to Main Content</a>
    <nav>
     <ul>
        <li><a href="../index.html">Home Page</a></li>
        <li><a href="#summary">Summary</a></li>
        <li><a href="#team-results">Team Results</a></li>
        <li><a href="#individual-results">Individual Results</a></li>
        <li><a href="#gallery">Gallery</a></li>
     </ul>
   </nav>
    <header id="hdr" > 
    <!-- FAB Button with SVG Search Icon -->
    <button class="fab">
    <img src="../gallery_images/236072/search.png" alt="Search Icon" class="fab-icon">
</button>
    </svg>
    </button>

    <h1>Athletics Homepage</h1>
    </header>
    <main id = "main">
    <h2>Meets</h2>
    <table>
        <tr><th>Meet Rows</th></tr>
        {meet_rows}
    </table>
<footer>  
<button id="mode-toggle" onclick="toggleMode()">Switch to Dark Mode</button>
</footer>

"""

    html_template += ''' <script>
        document.addEventListener('DOMContentLoaded', () => {
            const savedMode = localStorage.getItem('mode');
            const body = document.body;
            const toggleButton = document.getElementById('mode-toggle');
    
            // Check for saved preference in localStorage
            if (savedMode) {
                if (savedMode === 'dark-mode') {
                    body.classList.add('dark-mode');
                    toggleButton.textContent = 'Switch to Light Mode';
                } else {
                    body.classList.add('light-mode');
                    toggleButton.textContent = 'Switch to Dark Mode';
                }
            } else {
                // Use system preference if no saved preference
                if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
                    body.classList.add('dark-mode');
                    toggleButton.textContent = 'Switch to Light Mode';
                } else {
                    body.classList.add('light-mode');
                    toggleButton.textContent = 'Switch to Dark Mode';
                }
            }
        });
    
        function toggleMode() {
            const body = document.body;
            const toggleButton = document.getElementById('mode-toggle');
    
            if (body.classList.contains('light-mode')) {
                body.classList.remove('light-mode');
                body.classList.add('dark-mode');
                toggleButton.textContent = 'Switch to Light Mode';
                localStorage.setItem('mode', 'dark-mode');
            } else {
                body.classList.remove('dark-mode');
                body.classList.add('light-mode');
                toggleButton.textContent = 'Switch to Dark Mode';
                localStorage.setItem('mode', 'light-mode');
            }
        }
    </script>'''

    html_template += '''
    </body>
    </html>'''

    
    # Write the HTML template to a file
    output_file_path = os.path.join(base_dir, "index.html")
    with open(output_file_path, "w") as file:
        file.write(html_template)
    
    print(f"HTML homepage generated at: {output_file_path}")

# Run the function to generate the homepage
if __name__ == "__main__":
    generate_html_homepage()
