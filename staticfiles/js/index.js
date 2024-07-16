document.addEventListener('DOMContentLoaded', function () {
    const bellIcon = document.getElementById('notificationBell');
    if (bellIcon) {
        const unreadCount = parseInt(bellIcon.getAttribute('data-unread-count')) || 0;

        if (unreadCount > 0) {
            const unreadBadge = document.getElementById('unreadCount');
            unreadBadge.textContent = unreadCount;
            unreadBadge.style.display = 'inline-block';

            bellIcon.classList.add('text-danger');
        }
    }
});
