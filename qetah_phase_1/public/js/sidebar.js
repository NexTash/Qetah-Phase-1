document.addEventListener('DOMContentLoaded', function() {
    // Get the current URL path
    var currentPath = window.location.pathname.replace(/\/$/, '') || '/';

    // Get all sidebar links
    document.querySelectorAll('.sidebar-auth a').forEach(function(link) {
        var href = link.getAttribute('href').replace(/\/$/, '') || '/';

        // Debugging outputs
        //console.log('Current Path:', currentPath);
        //console.log('Href:', href);

        // Check if the href matches the current path
        if (currentPath === href) {
            link.querySelector('.auth-media').classList.add('sidebar-active');
        }
    });
});





