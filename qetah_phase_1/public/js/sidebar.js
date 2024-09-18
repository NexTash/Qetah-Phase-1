// document.addEventListener('DOMContentLoaded', function() {
//     // Get the current URL path
//     var currentPath = window.location.pathname.replace(/\/$/, '') || '/';

//     // Get all sidebar links
//     document.querySelectorAll('.sidebar-auth a').forEach(function(link) {
//         var href = link.getAttribute('href').replace(/\/$/, '') || '/';

//         // Debugging outputs
//         //console.log('Current Path:', currentPath);
//         //console.log('Href:', href);

//         // Check if the href matches the current path
//         if (currentPath === href) {
//             link.querySelector('.auth-media').classList.add('sidebar-active');
//         }
//     });
// });



// sidebar js
document.addEventListener("DOMContentLoaded", () => {
  function toggleSidebar() {
    const sidebar = document.getElementById("sidebar");
    sidebar.classList.toggle("open");
    sidebar.style.display = sidebar.classList.contains("open")
      ? "block"
      : "none"; // Use display none/block based on the toggle state
  }

  function closeSidebarOnClickOutside(event) {
    const sidebar = document.getElementById("sidebar");
    const toggleButton = document.getElementById("toggleButton");

    if (
      !sidebar.contains(event.target) &&
      !toggleButton.contains(event.target)
    ) {
      sidebar.classList.remove("open");
      sidebar.style.display = "none"; // Ensure sidebar closes when clicking outside
    }
 }

  function updateSidebarBehavior() {
    const toggleButton = document.getElementById("toggleButton");
    const sidebar = document.getElementById("sidebar");
    const mediaQuery = window.matchMedia("(max-width: 1024px)");

    if (mediaQuery.matches) {
      // On small screens, initialize sidebar as hidden and wait for toggle
      sidebar.style.display = "none"; // Set to none when screen is resized to 1024px or less
      toggleButton.addEventListener("click", handleSidebarToggle);
      document.addEventListener("click", closeSidebarOnClickOutside);
    } else {
      // On larger screens, ensure the sidebar is always visible
      toggleButton.removeEventListener("click", handleSidebarToggle);
      document.removeEventListener("click", closeSidebarOnClickOutside);
      sidebar.style.display = "block"; // Ensure the sidebar is visible on larger screens
      sidebar.classList.remove("open"); // Reset the sidebar to non-toggled state
    }
  }

  function handleSidebarToggle(event) {
    event.stopPropagation();
    toggleSidebar(
      sidebar.style.display = "block",
    ); // Toggle sidebar visibility on button click
  }

  updateSidebarBehavior();
  window.addEventListener("resize", updateSidebarBehavior); // Handle resizing
 });

