document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('.collapsible-toggle').forEach(button => {
        button.addEventListener('click', function () {
            this.classList.toggle('active');
            const content = this.nextElementSibling;
            if (content.style.display === "block") {
                content.style.display = "none";
                this.textContent = "Show Details";
            } else {
                content.style.display = "block";
                this.textContent = "Hide Details";
            }
        });
    });
});
