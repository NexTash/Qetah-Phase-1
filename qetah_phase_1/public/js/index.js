document.addEventListener('DOMContentLoaded', () => {
  // const toggleButton = document.getElementById('toggleButton');
  // const sidebar = document.getElementById('sidebar');
  
  // // Function to toggle the sidebar
  // function toggleSidebar() {
  //   sidebar.classList.toggle('translate-x-0');
  //   sidebar.classList.toggle('-translate-x-full');
  // }

  // // Event listener for the toggle button
  // toggleButton.addEventListener('click', (event) => {
  //   event.stopPropagation();
  //   toggleSidebar();
  // });

  // // Close sidebar when clicking outside
  // document.addEventListener('click', (event) => {
  //   if (!sidebar.contains(event.target) && !toggleButton.contains(event.target)) {
  //     sidebar.classList.add('-translate-x-full');
  //     sidebar.classList.remove('translate-x-0');
  //   }
  // });
});

// Ripple Effect
// function createRipple(event) {
//   const button = event.target;
//   const ripple = document.createElement("span");
//   ripple.classList.add("ripple-effect");

//   const rippleX = event.offsetX;
//   const rippleY = event.offsetY;
//   const rippleDiameter = Math.sqrt(
//     button.offsetWidth * button.offsetWidth +
//     button.offsetHeight * button.offsetHeight
//   );

//   ripple.style.top = `${rippleY - rippleDiameter / 2}px`;
//   ripple.style.left = `${rippleX - rippleDiameter / 2}px`;
//   ripple.style.width = `${rippleDiameter}px`;
//   ripple.style.height = `${rippleDiameter}px`;

//   button.appendChild(ripple);

//   setTimeout(() => {
//     ripple.remove();
//   }, 500);
// }

// document.addEventListener('DOMContentLoaded', () => {
//   document.querySelectorAll('.btn.ripple').forEach(button => {
//     button.addEventListener('click', function (e) {
//       // Remove any existing ripple effect
//       const existingRipple = this.querySelector('.ripple-effect');
//       if (existingRipple) {
//         existingRipple.remove();
//       }

//       createRipple(e); // Reuse createRipple function
//     });
//   });
// });