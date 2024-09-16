function sidebarState() {
  return {
    isStatic: false,
    isHovered: false,
    toggleSidebar() {
      this.isStatic = !this.isStatic;
    },
    expandSidebar() {
      this.isHovered = true;
    },
    collapseSidebar() {
      this.isHovered = false;
    },
  };
}
// main js

function toggleMenu() {
  const mobileMenu = document.getElementById("mobileMenu");
  mobileMenu.classList.toggle("show");
}
document
  .querySelector(".navbar-toggler")
  .addEventListener("click", (e) => {
    e.stopPropagation();
    toggleMenu();
  });
function closeMenuOnClickOutside(event) {
  const mobileMenu = document.getElementById("mobileMenu");
  const menuButton = document.querySelector(".navbar-toggler");
  if (
    !mobileMenu.contains(event.target) &&
    !menuButton.contains(event.target)
  ) {
    mobileMenu.classList.remove("show");
  }
}
document.addEventListener("click", closeMenuOnClickOutside);

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
    toggleSidebar(); // Toggle sidebar visibility on button click
  }

  updateSidebarBehavior();
  window.addEventListener("resize", updateSidebarBehavior); // Handle resizing
});

// Sidebar content JS (for toggling sidebar content area)
document.addEventListener("DOMContentLoaded", function () {
  const toggler = document.querySelector(".sidebar-toggler");
  const sidebar = document.getElementById("sidebar");
  const contentArea = document.querySelector(".content-area");

  toggler.addEventListener("click", function (event) {
    event.stopPropagation();
    contentArea.classList.toggle("sidebar-area-content");
  });

  document.addEventListener("click", function (event) {
    if (!sidebar.contains(event.target) && !toggler.contains(event.target)) {
      contentArea.classList.remove("sidebar-area-content");
    }
  });
});

// sideebar content js
document.addEventListener("DOMContentLoaded", function () {
  const toggler = document.querySelector(".sidebar-toggler");
  const sidebar = document.getElementById("sidebar");
  const contentArea = document.querySelector(".content-area");

  toggler.addEventListener("click", function (event) {
    event.stopPropagation();
    contentArea.classList.toggle("sidebar-area-content");
  });

  document.addEventListener("click", function (event) {
    if (
      !sidebar.contains(event.target) &&
      !toggler.contains(event.target)
    ) {
      contentArea.classList.remove("sidebar-area-content");
    }
  });
});
// ripple
function createRipple(event) {
  const button = event.target;
  const ripple = document.createElement("span");
  ripple.classList.add("ripple-effect");

  const rippleX = event.offsetX;
  const rippleY = event.offsetY;
  const rippleDiameter = Math.sqrt(
    button.offsetWidth * button.offsetWidth +
    button.offsetHeight * button.offsetHeight
  );

  ripple.style.top = `${rippleY - rippleDiameter / 2}px`;
  ripple.style.left = `${rippleX - rippleDiameter / 2}px`;
  ripple.style.width = `${rippleDiameter}px`;
  ripple.style.height = `${rippleDiameter}px`;

  button.appendChild(ripple);

  setTimeout(() => {
    ripple.remove();
  }, 500);
}

window.Alpine = {
  createRipple: createRipple,
};
document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('.btn.ripple').forEach(button => {
    button.addEventListener('click', function (e) {
      // Remove any existing ripple effect
      const existingRipple = this.querySelector('.ripple-effect');
      if (existingRipple) {
        existingRipple.remove();
      }

      const rect = button.getBoundingClientRect();
      const ripple = document.createElement('span');
      ripple.classList.add('ripple-effect');
      const size = Math.max(rect.width, rect.height);
      const x = e.clientX - rect.left - size / 2;
      const y = e.clientY - rect.top - size / 2;

      ripple.style.width = ripple.style.height = `${size}px`;
      ripple.style.left = `${x}px`;
      ripple.style.top = `${y}px`;

      this.appendChild(ripple);

      ripple.addEventListener('animationend', () => {
        ripple.remove();
      });
    });
  });
});



// Add to Cart button functionality
document.getElementById('addToCartBtn')?.addEventListener('click', function () {
  var badge = document.getElementById('cartBadge');
  var currentValue = parseInt(badge.textContent, 10);
  badge.textContent = currentValue + 1;
});

// Handle counter increments
// document.querySelectorAll('.counter-increment').forEach(button => {
//   button.addEventListener('click', function () {
//     var counter = this.previousElementSibling;
//     var value = parseInt(counter.value, 10);
//     counter.value = value + 1;

//     // Update cart badge count
//     updateCartBadge(1);
//   });
// });



