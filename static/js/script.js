// when clicking on search in mobile sidenav, it compacts the mobile side nav
function hideMobileNavBar() {
        mobileNavBar = document.getElementById("mobile-sidenav");
        mobileNavBar.classList.remove("show");
}

// Toggles visibility for image info sidebar
function hideInfoSidebar() {
    sidebar = document.getElementById("image-info-and-purchase");
    sidebar.classList.toggle("d-none");
}

// Function from Bootstrap that enables tooltips
$(function () {
  $('[data-toggle="tooltip"]').tooltip()
})