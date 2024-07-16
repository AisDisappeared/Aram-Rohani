    document.addEventListener('DOMContentLoaded', function() {
        const sidebarToggle = document.querySelector('[data-drawer-toggle="sidebar-multi-level-sidebar"]');
        const sidebar = document.getElementById('sidebar-multi-level-sidebar');

        sidebarToggle.addEventListener('click', function() {
            sidebar.classList.toggle('-translate-x-full');
        });

        document.addEventListener('click', function(event) {
            if (!sidebar.contains(event.target) && !sidebarToggle.contains(event.target)) {
                sidebar.classList.add('-translate-x-full');
            }
        });
    });