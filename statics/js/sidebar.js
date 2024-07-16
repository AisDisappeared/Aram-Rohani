    // sidebar will closed when click on out of sidebar
    // document.addEventListener('DOMContentLoaded', function() {
    //     const sidebarToggle = document.querySelector('[data-drawer-toggle="sidebar-multi-level-sidebar"]');
    //     const sidebar = document.getElementById('sidebar-multi-level-sidebar');

    //     sidebarToggle.addEventListener('click', function() {
    //         sidebar.classList.toggle('-translate-x-full');
    //     });

    //     document.addEventListener('click', function(event) {
    //         if (!sidebar.contains(event.target) && !sidebarToggle.contains(event.target)) {
    //             sidebar.classList.add('-translate-x-full');
    //         }
    //     });
    // });

       // sidebar will closed when we move the mouse out of the sidebar
        document.addEventListener('DOMContentLoaded', function() {
        const sidebarToggle = document.querySelector('[data-drawer-toggle="sidebar-multi-level-sidebar"]');
        const sidebar = document.getElementById('sidebar-multi-level-sidebar');

        sidebarToggle.addEventListener('click', function() {
            sidebar.classList.toggle('-translate-x-full');
        });

        sidebar.addEventListener('mouseleave', function() {
            sidebar.classList.add('-translate-x-full');
        });
    });